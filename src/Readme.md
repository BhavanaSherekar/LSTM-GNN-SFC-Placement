# Source Code

This directory contains the implementation of the proposed framework.

## main_pipeline.py

Implements the complete placement workflow:

1. Resource Monitoring
2. LSTM-Based Resource Prediction
3. GNN-Based Topology Learning
4. Topology-Aware Cost Matrix Generation
5. ILP-Based Placement Optimization
6. Assignment-Based Fallback Placement
7. Service Function Chain Deployment

Input:
- cluster_metrics.csv

Output:
- Optimal VNF placement decisions
- Placement cost
- Resource utilization metrics
