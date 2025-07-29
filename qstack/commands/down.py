"""Down command to stop the QStack application."""

import os
import subprocess
import click
from colorama import Fore, Style
from ..core.utils import detect_docker_compose

@click.command()
@click.option('--volumes', '-v', is_flag=True, help='Remove volumes as well')
@click.option('--path', '-p', default='.', help='Path to project directory')
def down(volumes, path):
    """Stop the QStack application."""
    
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
        click.echo(f"{Fore.CYAN}⏹️  Stopping QStack application using {compose_cmd}...{Style.RESET_ALL}")
        
        # Build command based on detected compose version
        if compose_cmd == 'docker compose':
            cmd = ['docker', 'compose', 'down']
        else:
            cmd = ['docker-compose', 'down']
            
        if volumes:
            cmd.append('-v')
        
        result = subprocess.run(cmd, cwd=path)
        
        if result.returncode == 0:
            click.echo(f"{Fore.GREEN}✅ QStack application stopped successfully!{Style.RESET_ALL}")
        
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error stopping application: {str(e)}{Style.RESET_ALL}")