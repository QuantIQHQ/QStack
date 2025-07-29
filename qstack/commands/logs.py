"""Logs command to view QStack application logs."""

import os
import subprocess
import click
from colorama import Fore, Style
from ..core.utils import detect_docker_compose

@click.command()
@click.option('--follow', '-f', is_flag=True, help='Follow log output')
@click.option('--tail', '-t', default=None, help='Number of lines to show from the end of the logs')
@click.option('--service', '-s', default=None, help='Show logs for specific service (frontend, backend, db)')
@click.option('--path', '-p', default='.', help='Path to project directory')
def logs(follow, tail, service, path):
    """View QStack application logs."""
    
    if not os.path.exists(path):
        click.echo(f"{Fore.RED}❌ Directory '{path}' does not exist{Style.RESET_ALL}")
        return
    
    # Check for docker-compose.yml
    docker_compose = os.path.join(path, 'docker-compose.yml')
    if not os.path.exists(docker_compose):
        click.echo(f"{Fore.RED}❌ No docker-compose.yml found. Not a QStack project?{Style.RESET_ALL}")
        return
    
    # Detect docker compose command
    compose_cmd, is_available = detect_docker_compose()
    if not is_available:
        click.echo(f"{Fore.RED}❌ Docker Compose not found. Please install Docker and Docker Compose.{Style.RESET_ALL}")
        return
    
    try:
        service_msg = f" for {service}" if service else ""
        click.echo(f"{Fore.CYAN}📋 Viewing logs{service_msg} using {compose_cmd}...{Style.RESET_ALL}")
        
        # Build command based on detected compose version
        if compose_cmd == 'docker compose':
            cmd = ['docker', 'compose', 'logs']
        else:
            cmd = ['docker-compose', 'logs']
            
        if follow:
            cmd.append('-f')
        if tail:
            cmd.extend(['--tail', tail])
        if service:
            cmd.append(service)
        
        subprocess.run(cmd, cwd=path)
        
    except KeyboardInterrupt:
        click.echo(f"\n{Fore.YELLOW}⏹️  Stopped viewing logs{Style.RESET_ALL}")
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error viewing logs: {str(e)}{Style.RESET_ALL}")