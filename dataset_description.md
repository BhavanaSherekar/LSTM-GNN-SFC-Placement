# Dataset Description

## Overview

The dataset used in this project was collected from a Kubernetes-based edge-cloud testbed using Prometheus monitoring tools.

The dataset captures node-level resource utilization and network performance metrics required for training the LSTM prediction model and evaluating SFC placement decisions.

---

## Dataset File

```text
cluster_metrics.csv
```

---

## Data Collection

Metrics were periodically collected from Kubernetes worker nodes using Prometheus.

Sampling included:

* CPU utilization
* Memory utilization
* Round Trip Time (RTT)
* Network bandwidth

The collected measurements were aggregated and stored in CSV format.

---

## Dataset Attributes

| Attribute    | Description                |
| ------------ | -------------------------- |
| Timestamp    | Time of measurement        |
| Node ID      | Worker node identifier     |
| CPU Usage    | CPU utilization (%)        |
| Memory Usage | Memory utilization (%)     |
| RTT          | Round Trip Time (ms)       |
| Bandwidth    | Available bandwidth (Mbps) |

---

## Usage

The dataset is used for:

1. Training the LSTM resource prediction model.
2. Predicting future node resource availability.
3. Feasibility analysis during SFC placement.
4. Performance evaluation of the proposed framework.

---

## Reproducibility

The dataset included in this repository is sufficient to reproduce the resource prediction and placement experiments presented in the associated publication.
