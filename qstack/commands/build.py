"""Build command for production deployment."""

import os
import click
from colorama import Fore, Style

@click.command()
@click.option('--clean', '-c', is_flag=True, help='Clean development files')
@click.option('--path', '-p', default='.', help='Path to project directory')
def build(clean, path):
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
    
    try:
        # Run docker build
        import subprocess
        
        click.echo("📦 Building Docker images...")
        result = subprocess.run(
            ['docker-compose', 'build', '--no-cache'],
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
        click.echo("  • Push to your git repository")
        click.echo("  • Deploy to your hosting platform")
        click.echo("  • Update environment variables")
        
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Build error: {str(e)}{Style.RESET_ALL}")