import pandas as pd
import numpy as np
import pulp

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


CSV_PATH = "cluster_metrics.csv"
SEQ_LEN = 5
EPOCHS = 1

ALPHA = 0.5
BETA = 0.3
GAMMA = 0.2
DELTA = 0.2   

EPS = 1e-6



def predict_nodes(csv_path):

    df = pd.read_csv(csv_path)
    df = df[['nodename','cpu','ram','rtt']].dropna()

    nodes = df['nodename'].unique()
    scaler = MinMaxScaler()

    preds = []

    for node in nodes:

        node_df = df[df['nodename']==node][['cpu','ram','rtt']].values

        if len(node_df) < SEQ_LEN + 1:
            continue

        scaled = scaler.fit_transform(node_df)

        X, y = [], []
        for i in range(len(scaled)-SEQ_LEN):
            X.append(scaled[i:i+SEQ_LEN])
            y.append(scaled[i+SEQ_LEN])

        X, y = np.array(X), np.array(y)

        model = Sequential([
            LSTM(32, input_shape=(SEQ_LEN,3)),
            Dense(3)
        ])

        model.compile(optimizer='adam', loss='mse')
        model.fit(X, y, epochs=EPOCHS, verbose=0)

        pred = model.predict(scaled[-SEQ_LEN:].reshape(1,SEQ_LEN,3), verbose=0)
        pred = scaler.inverse_transform(pred)[0]

        preds.append({
            'nodename': node,
            'cpu_pred': float(pred[0]),
            'ram_pred': float(pred[1]),
            'rtt_pred': abs(float(pred[2]))
        })

    pred_df = pd.DataFrame(preds)


    rtt = pred_df['rtt_pred']
    pred_df['rtt_norm'] = 100*(rtt - rtt.min())/(rtt.max()-rtt.min()+EPS)

    return pred_df



def apply_gnn(pred_df):

    features = pred_df[['cpu_pred','ram_pred','rtt_norm']].values

    n = len(features)

    adj = np.zeros((n,n))

    for i in range(n-1):
        adj[i][i+1] = 1
        adj[i+1][i] = 1

    emb = np.dot(adj, features)


    emb = emb / (np.max(emb)+EPS)

    pred_df['gnn_score'] = emb.mean(axis=1)

    return pred_df

def run_ilp(pred_df, vnf_req):

    nodes = pred_df['nodename'].tolist()
    vnfs = list(vnf_req.keys())

    prob = pulp.LpProblem("SFC_Placement", pulp.LpMinimize)

    x = pulp.LpVariable.dicts('x',(nodes,vnfs),0,1,cat='Binary')

    cost = {}

    rtt_ref = pred_df['rtt_pred'].max()+EPS

    for n in nodes:

        row = pred_df[pred_df['nodename']==n].iloc[0]

        cpu_free = 100-row['cpu_pred']
        ram_free = 100-row['ram_pred']

        for v in vnfs:

            cpu_r = vnf_req[v]['cpu']
            ram_r = vnf_req[v]['ram']

            cpu_ratio = cpu_r/(cpu_free+EPS)
            ram_ratio = ram_r/(ram_free+EPS)
            rtt_norm = row['rtt_pred']/rtt_ref
            gnn = row['gnn_score']

            cost[(n,v)] = (
                ALPHA*rtt_norm +
                BETA*cpu_ratio +
                GAMMA*ram_ratio +
                DELTA*gnn
            )

    
    prob += pulp.lpSum(cost[(n,v)]*x[n][v] for n in nodes for v in vnfs)

    # Each VNF assigned once
    for v in vnfs:
        prob += pulp.lpSum(x[n][v] for n in nodes) == 1

    # Capacity constraints
    for n in nodes:

        row = pred_df[pred_df['nodename']==n].iloc[0]
        cpu_free = 100-row['cpu_pred']
        ram_free = 100-row['ram_pred']

        prob += pulp.lpSum(vnf_req[v]['cpu']*x[n][v] for v in vnfs) <= cpu_free
        prob += pulp.lpSum(vnf_req[v]['ram']*x[n][v] for v in vnfs) <= ram_free

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    placement = {}

    for v in vnfs:
        for n in nodes:
            if x[n][v].value() == 1:
                placement[v] = n

    return placement


def run_pipeline():

    print("\n Running LSTM + GNN + ILP Pipeline...\n")

    pred_df = predict_nodes(CSV_PATH)

    pred_df = apply_gnn(pred_df)

    print("Predicted + GNN Features:\n")
    print(pred_df)

    vnf_req = {
        'firewall': {'cpu':20,'ram':25},
        'ids': {'cpu':15,'ram':20},
        'load_balancer': {'cpu':25,'ram':30}
    }

    placement = run_ilp(pred_df, vnf_req)

    print("\n FINAL SFC PLACEMENT:\n")

    for v,n in placement.items():
        print(f"{v}  →  {n}")


if __name__ == "__main__":
    run_pipeline()
