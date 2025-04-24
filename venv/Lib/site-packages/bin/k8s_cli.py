#!/usr/bin/env python3

import argparse
from rich.console import Console
from rich import print
from modules.cluster import connect_to_cluster
from modules.helm import install_helm
from modules.keda import install_keda
from modules.deployment import create_deployment
from modules.hpa import create_hpa
from modules.health import get_health_status

console = Console()

def main():
    parser = argparse.ArgumentParser(description="🚀 Automate Kubernetes Operations with Style")
    parser.add_argument("--action", choices=[
        "connect", "install-helm", "install-keda",
        "create-deployment", "create-hpa", "get-health-status"
    ], required=True, help="Action to perform")

    parser.add_argument("--image", help="Docker image for deployment")
    parser.add_argument("--cpu-limit", help="CPU limit for deployment")
    parser.add_argument("--mem-limit", help="Memory limit for deployment")
    parser.add_argument("--ports", nargs="+", help="Ports to expose")
    parser.add_argument("--deployment-id", help="Deployment ID to check health status or create HPA")

    args = parser.parse_args()

    try:
        if args.action == "connect":
            with console.status("[bold cyan]🔗 Connecting to cluster...[/bold cyan]", spinner="dots"):
                connect_to_cluster()
                console.print(":white_check_mark: [bold green]Connected to cluster successfully![/bold green]")

        elif args.action == "install-helm":
            with console.status("[bold cyan]📦 Installing Helm...[/bold cyan]", spinner="dots"):
                install_helm()
                console.print(":white_check_mark: [bold green]Helm installed successfully![/bold green]")

        elif args.action == "install-keda":
            with console.status("[bold cyan]⚙️ Installing KEDA...[/bold cyan]", spinner="dots"):
                install_keda()
                console.print(":white_check_mark: [bold green]KEDA installed successfully![/bold green]")

        elif args.action == "create-deployment":
            if args.image and args.cpu_limit and args.mem_limit and args.ports:
                create_deployment(args.image, args.cpu_limit, args.mem_limit, args.ports)
            else:
                console.print("[bold red]❌ Missing required parameters for deployment creation.[/bold red]")

        elif args.action == "create-hpa":
            if args.deployment_id:
                create_hpa(args.deployment_id)
            else:
                console.print("[bold red]❌ Deployment ID required for HPA creation.[/bold red]")

        elif args.action == "get-health-status":
            if args.deployment_id:
                get_health_status(args.deployment_id)
            else:
                console.print("[bold red]❌ Deployment ID required to get health status.[/bold red]")

    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
