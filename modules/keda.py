import subprocess

def install_keda():
    """Install KEDA on the Kubernetes cluster using Helm in the 'keda' namespace."""
    try:
        subprocess.run(
            ["helm", "repo", "add", "kedacore", "https://kedacore.github.io/charts"],
            check=True,
            capture_output=True,
            text=True
        )

        # Check if KEDA is already installed
        result = subprocess.run(
            ["helm", "list", "-n", "keda"],
            capture_output=True,
            text=True
        )
        if "keda" in result.stdout:
            return "KEDA is already installed in namespace 'keda'. Skipping installation."

        subprocess.run(
            ["helm", "install", "keda", "kedacore/keda", "--namespace", "keda", "--create-namespace"],
            check=True,
            capture_output=True,
            text=True
        )

        return "KEDA installed successfully in namespace 'keda'."
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error installing KEDA: {e.stderr if e.stderr else str(e)}")
