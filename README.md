# Kubernetes Automation CLI

## Overview

This CLI script automates the process of connecting to a Kubernetes cluster, installing Helm and KEDA, creating deployments with autoscaling, and retrieving health status for deployments.

## Prerequisites

- Python 3.x
- kubectl
- Helm
- KEDA

## Installation

1. Clone the repository.
2. Install cli:
    ```bash
    cd k8s-cli
    pip install .
    ```

## Usage

### Connect to Cluster
```bash
k8s-cli --action connect
```

### Install Helm
```bash
k8s-cli --action install-helm
```

### Install KEDA
```bash
k8s-cli --action install-keda
```
### Create Deployment
```bash
k8s-cli --action create-deployment --image <image_name> --cpu-limit <cpu_limit> --mem-limit <mem_limit> --ports <port1> <port2>
```
### Create HPA
```bash
k8s-cli --action create-hpa --deployment-id <deployment_name>
```
### Get Health Status
```bash
k8s-cli --action get-health-status --deployment-id <deployment_name>
```