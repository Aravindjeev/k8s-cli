import subprocess
import yaml
from rich import print
from rich.console import Console

console = Console()

def create_deployment(image, cpu_limit, mem_limit, ports, namespace="default"):
    """Create a Kubernetes deployment with the provided image and resource limits using rich UI."""
    
    # Ensure ports are integers
    try:
        port_list = [int(port) for port in ports]
    except ValueError:
        raise Exception("[bold red]❌ Error:[/bold red] All ports must be integers.")

    deployment_yaml = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "my-app", "namespace": namespace},
        "spec": {
            "replicas": 1,
            "selector": {
                "matchLabels": {"app": "my-app"}
            },
            "template": {
                "metadata": {"labels": {"app": "my-app"}},
                "spec": {
                    "containers": [{
                        "name": "my-app",
                        "image": image,
                        "resources": {
                            "requests": {
                                "cpu": cpu_limit,
                                "memory": mem_limit
                            },
                            "limits": {
                                "cpu": cpu_limit,
                                "memory": mem_limit
                            }
                        },
                        "ports": [{"containerPort": port} for port in port_list]
                    }]
                }
            }
        }
    }

    with open("deployment.yaml", "w") as f:
        yaml.dump(deployment_yaml, f, sort_keys=False)

    with console.status("[bold cyan]⠦ Creating deployment...[/bold cyan]", spinner="dots"):
        try:
            subprocess.run(["kubectl", "apply", "-f", "deployment.yaml"], check=True, stderr=subprocess.PIPE)
            console.print(f":white_check_mark: [bold green]Deployment created successfully with image {image}[/bold green]")
        except subprocess.CalledProcessError as e:
            error_output = e.stderr.decode('utf-8') if e.stderr else str(e)
            console.print(f"[bold red]❌ Error creating deployment:[/bold red] {error_output}")
