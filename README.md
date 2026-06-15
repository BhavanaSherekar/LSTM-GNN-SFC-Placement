# Optimized Service Function Chain Placement in Edge–Cloud Infrastructures Using Machine Learning and Optimization

This repository contains the implementation and experimental artifacts for the research work:

**"Optimized Service Function Chain Placement in Edge–Cloud Infrastructures Using Machine Learning and Optimization"**

The proposed framework combines:

* LSTM-based resource prediction
* Graph Neural Network (GNN)-based topology learning
* Integer Linear Programming (ILP)-based optimization
* Kubernetes-based Service Function Chain (SFC) deployment

to achieve topology-aware and resource-efficient placement of Virtual Network Functions (VNFs) in edge-cloud environments.

---

## Project Overview

Service Function Chaining (SFC) enables network services such as firewalls, intrusion detection systems, and load balancers to be deployed in a predefined sequence. Efficient placement of these functions is challenging in edge environments due to:

* Limited computing resources
* Dynamic workload variations
* Network latency constraints
* Topological dependencies among edge nodes

The proposed framework addresses these challenges by predicting future resource availability using LSTM, learning topology-aware node importance using a lightweight GNN, and selecting optimal placement locations using ILP optimization.

---

## Architecture

The framework consists of the following components:

1. Resource Monitoring
2. LSTM-Based Resource Prediction
3. GNN-Based Topology Learning
4. Topology-Aware Cost Matrix Generation
5. ILP-Based Placement Optimization
6. Assignment-Based Fallback Placement
7. Kubernetes Deployment and Evaluation

---

## Experimental Environment

| Component            | Version             |
| -------------------- | ------------------- |
| Python               | 3.10                |
| Ubuntu               | 22.04 LTS           |
| Kubernetes           | v1.30.x             |
| Container Runtime    | containerd 1.7+     |
| Monitoring           | Prometheus          |
| Optimization Solver  | PuLP (CBC)          |
| Visualization        | Matplotlib, Seaborn |
| Graph Representation | NetworkX            |

---

## Dataset

The repository includes a custom dataset:

```text
dataset/cluster_metrics.csv
```

The dataset contains:

* CPU Utilization
* Memory Utilization
* RTT (Round Trip Time)

collected from Kubernetes worker nodes using Prometheus.

---

## Results

The framework is evaluated under:

* Low Traffic
* Medium Traffic
* High Traffic

Performance metrics include:

* Latency
* Throughput
* CPU Utilization
* Memory Utilization
* Jitter
* Placement Cost

The proposed framework consistently outperforms the EdgeDQN baseline across all traffic conditions.

---

## Repository Structure

```text
LSTM-GNN-SFC-Placement/
│
├── dataset/
├── docs/
├── results/
├── resource_prediction/
├── topology_learning/
├── optimization/
├── deployment/
├── requirements.txt
└── README.md
```

---

## Authors

* Bhavana Sherekar
* Kavya Uppin
* Ria Javalagi
* Vipin Sharma

---

