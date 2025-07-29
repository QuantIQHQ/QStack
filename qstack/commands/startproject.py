"""Start project command."""

import os
import click
from colorama import Fore, Style
from ..core.generator import ProjectGenerator

@click.command()
@click.argument('project_name')
@click.option('--template', '-t', default='fullstack', 
              help='Project template (fullstack, frontend-only, api-only)')
@click.option('--database', '-d', default='postgres',
              type=click.Choice(['postgres', 'sqlite', 'mysql']),
              help='Database type (default: postgres)')
@click.option('--force', '-f', is_flag=True,
              help='Overwrite existing directory')
def startproject(project_name, template, database, force):
    """Create a new fullstack project.
    
    PROJECT_NAME: Name of the project to create
    """
    if not project_name.replace('_', '').replace('-', '').isalnum():
        click.echo(f"{Fore.RED}❌ Project name must contain only letters, numbers, hyphens, and underscores{Style.RESET_ALL}")
        return
    
    # Check if directory exists
    if os.path.exists(project_name) and not force:
        click.echo(f"{Fore.RED}❌ Directory '{project_name}' already exists. Use --force to overwrite.{Style.RESET_ALL}")
        return
    
    click.echo(f"{Fore.GREEN}🚀 Creating {template} project: {project_name}{Style.RESET_ALL}")
    click.echo(f"{Fore.CYAN}📊 Database: {database}{Style.RESET_ALL}")
    
    try:
        generator = ProjectGenerator(project_name, template, database)
        generator.generate()
        
        click.echo(f"\n{Fore.GREEN}✅ Project '{project_name}' created successfully!{Style.RESET_ALL}")
        click.echo(f"\n{Fore.CYAN}Next steps:{Style.RESET_ALL}")
        click.echo(f"  cd {project_name}")
        click.echo(f"  qstack up --build")
        click.echo(f"  Open http://localhost:5173 🎉")
        
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error creating project: {str(e)}{Style.RESET_ALL}")
        raise click.Abort()