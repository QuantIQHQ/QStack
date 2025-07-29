"""Build command for production deployment."""

import os
import subprocess
import click
from colorama import Fore, Style
from ..core.utils import detect_docker_compose

@click.command()
@click.option('--clean', '-c', is_flag=True, help='Clean development files')
@click.option('--path', '-p', default='.', help='Path to project directory')
@click.option('--no-cache', is_flag=True, help='Build without using cache')
def build(clean, path, no_cache):
    """Build project for production deployment."""
    
    if not os.path.exists(path):
        click.echo(f"{Fore.RED}❌ Directory '{path}' does not exist{Style.RESET_ALL}")
        return
    
    click.echo(f"{Fore.CYAN}🏗️  Building project for production...{Style.RESET_ALL}")
    
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
        click.echo(f"📦 Building Docker images using {compose_cmd}...")
        
        # Build command based on detected compose version
        if compose_cmd == 'docker compose':
            cmd = ['docker', 'compose', 'build']
        else:
            cmd = ['docker-compose', 'build']
            
        if no_cache:
            cmd.append('--no-cache')
        
        result = subprocess.run(
            cmd,
            cwd=path,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            click.echo(f"{Fore.RED}❌ Build failed:{Style.RESET_ALL}")
            click.echo(result.stderr)
            return
        
        click.echo(f"{Fore.GREEN}✅ Build completed successfully!{Style.RESET_ALL}")
        
        if clean:
            click.echo("🧹 Cleaning development files...")
            # Remove development markdown files
            dev_files = [
                'defineprojectscope.md',
                'gpt_help_in_the_idea.md', 
                'grok_help_in_the_idea.md',
                'my_raw_thought.md'
            ]
            
            for file in dev_files:
                file_path = os.path.join(path, file)
                if os.path.exists(file_path):
                    os.remove(file_path)
                    click.echo(f"  Removed {file}")
        
        click.echo(f"\n{Fore.CYAN}🚀 Ready for deployment!{Style.RESET_ALL}")
        click.echo("Next steps:")
        click.echo("  • qstack up (to run the application)")
        click.echo("  • Push to your git repository")
        click.echo("  • Deploy to your hosting platform")
        click.echo("  • Update environment variables")
        
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Build error: {str(e)}{Style.RESET_ALL}")