# Project Description

## Problem Statement

Service Function Chain (SFC) placement is a critical challenge in edge-cloud environments. Traditional placement approaches rely on current resource availability and often ignore network topology, leading to increased latency, poor resource utilization, and frequent VNF migrations.

This project proposes a topology-aware SFC placement framework that integrates machine learning and optimization techniques to proactively identify optimal deployment locations.

---

## Objectives

* Predict future node resource utilization.
* Learn topology-aware node representations.
* Minimize placement cost and latency.
* Improve resource utilization.
* Enhance Quality of Service (QoS).

---

## Methodology

### 1. Resource Monitoring

Prometheus continuously collects:

* CPU utilization
* Memory utilization
* RTT
* Bandwidth

from Kubernetes worker nodes.

### 2. LSTM-Based Prediction

Historical resource traces are used to train an LSTM model that predicts future resource states for each worker node.

### 3. Topology Learning

The Kubernetes cluster is modeled as a graph. A lightweight custom GNN performs neighborhood aggregation to generate topology-aware node scores.

### 4. Placement Optimization

Predicted resources and topology scores are combined into a topology-aware cost function. An ILP optimizer selects the optimal placement node.

When a single node cannot accommodate the complete SFC, an Assignment-based placement strategy is used.

### 5. Deployment

The selected placement configuration is deployed on Kubernetes using containerized VNFs.

---

## Evaluation Metrics

* Latency
* Throughput
* CPU Utilization
* Memory Utilization
* Jitter
* Placement Cost

---

## Traffic Scenarios

* Low Traffic
* Medium Traffic
* High Traffic

The proposed framework is compared against EdgeDQN under all scenarios.
