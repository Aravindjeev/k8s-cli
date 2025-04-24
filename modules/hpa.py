import subprocess
from rich.console import Console

console = Console()

def create_hpa(deployment_name, metric="cpu", target_value=50, namespace="default"):
    """Create a Horizontal Pod Autoscaler for the given deployment using kubectl with rich output."""
    with console.status(f"[bold cyan]⠦ Creating HPA for deployment '{deployment_name}'...[/bold cyan]", spinner="dots"):
        try:
            subprocess.run([
                "kubectl", "autoscale", "deployment", deployment_name,
                "--cpu-percent", str(target_value), "--min", "1", "--max", "10",
                "--namespace", namespace
            ], check=True, stderr=subprocess.PIPE)
            console.print(f":white_check_mark: [bold green]HPA created for '{deployment_name}' with {metric} metric (Target: {target_value}%).[/bold green]")
        except subprocess.CalledProcessError as e:
            error_output = e.stderr.decode('utf-8') if e.stderr else str(e)
            console.print(f"[bold red]❌ Error creating HPA for '{deployment_name}':[/bold red] {error_output}")
