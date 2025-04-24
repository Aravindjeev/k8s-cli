import subprocess
from rich import print
from rich.console import Console

console = Console()

def get_health_status(deployment_name, namespace="default"):
    """Get health status of a deployment with rich colored output."""
    try:
        with console.status(f"[bold cyan]⠦ Checking health of deployment [white]{deployment_name}[/white]...[/bold cyan]", spinner="dots"):
            result = subprocess.run(
                [
                    "kubectl", "get", "deployment", deployment_name,
                    "--namespace", namespace,
                    "-o", "jsonpath={.status.conditions[?(@.type=='Available')].status}"
                ],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            status = result.stdout.decode('utf-8').strip().strip("'\"")

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode('utf-8') if e.stderr else str(e)
        console.print(f"[bold red]❌ Error retrieving health status:[/bold red] {error_msg}")
        return

    # Print status result in a clean new line
    if status == "True":
        print(f"\n:white_check_mark: [bold green]Deployment '{deployment_name}' is Healthy[/bold green]")
    else:
        print(f"\n:x: [bold red]Deployment '{deployment_name}' is Not Healthy[/bold red]")
