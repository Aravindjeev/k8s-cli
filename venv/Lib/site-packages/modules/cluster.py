import subprocess

def connect_to_cluster(kube_config_path=None):
    """Connect to Kubernetes cluster using kubectl."""
    command = ["kubectl", "cluster-info"]
    if kube_config_path:
        command.extend(["--kubeconfig", kube_config_path])
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error connecting to Kubernetes cluster: {e.stderr.decode('utf-8')}")
