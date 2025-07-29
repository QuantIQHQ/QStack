"""Up command to start the QStack application."""

import os
import subprocess
import click
from colorama import Fore, Style
from ..core.utils import detect_docker_compose

@click.command()
@click.option('--build', '-b', is_flag=True, help='Build images before starting')
@click.option('--detach', '-d', is_flag=True, help='Run in detached mode')
@click.option('--path', '-p', default='.', help='Path to project directory')
def up(build, detach, path):
    """Start the QStack application."""
    
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
        click.echo(f"{Fore.CYAN}🚀 Starting QStack application using {compose_cmd}...{Style.RESET_ALL}")
        
        # Build command based on detected compose version
        if compose_cmd == 'docker compose':
            cmd = ['docker', 'compose', 'up']
        else:
            cmd = ['docker-compose', 'up']
            
        if build:
            cmd.append('--build')
        if detach:
            cmd.append('-d')
        
        result = subprocess.run(cmd, cwd=path)
        
        if result.returncode == 0 and detach:
            click.echo(f"\n{Fore.GREEN}✅ QStack application started successfully!{Style.RESET_ALL}")
            click.echo(f"{Fore.CYAN}🌐 Frontend: http://localhost:5173{Style.RESET_ALL}")
            click.echo(f"{Fore.CYAN}🔧 Backend API: http://localhost:8000{Style.RESET_ALL}")
            click.echo(f"\n{Fore.YELLOW}💡 Use 'qstack logs' to view logs{Style.RESET_ALL}")
            click.echo(f"{Fore.YELLOW}💡 Use 'qstack down' to stop the application{Style.RESET_ALL}")
        
    except KeyboardInterrupt:
        click.echo(f"\n{Fore.YELLOW}⏹️  Stopping application...{Style.RESET_ALL}")
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error starting application: {str(e)}{Style.RESET_ALL}")