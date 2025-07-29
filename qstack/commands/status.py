"""Status command to show project progress."""

import os
import click
from colorama import Fore, Style
from ..core.status_parser import StatusParser

@click.command()
@click.option('--path', '-p', default='.', help='Path to project directory')
def status(path):
    """Show project status and progress tracking."""
    
    if not os.path.exists(path):
        click.echo(f"{Fore.RED}❌ Directory '{path}' does not exist{Style.RESET_ALL}")
        return
        
    scope_file = os.path.join(path, 'defineprojectscope.md')
    
    if not os.path.exists(scope_file):
        click.echo(f"{Fore.YELLOW}⚠️  No defineprojectscope.md found. This might not be a QStack project.{Style.RESET_ALL}")
        return
    
    try:
        parser = StatusParser(scope_file)
        progress = parser.get_progress()
        
        click.echo(f"{Fore.CYAN}📊 Project Status{Style.RESET_ALL}")
        click.echo(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        total_features = len(progress['features'])
        completed = sum(1 for f in progress['features'] if f['completed'])
        
        click.echo(f"Progress: {completed}/{total_features} features completed")
        
        if total_features > 0:
            percentage = completed/total_features*100
            click.echo(f"Completion: {Fore.GREEN}{percentage:.1f}%{Style.RESET_ALL}\n")
        else:
            click.echo(f"Completion: {Fore.YELLOW}No tracked features{Style.RESET_ALL}\n")
        
        for feature in progress['features']:
            status_icon = "✅" if feature['completed'] else "⏳"
            color = Fore.GREEN if feature['completed'] else Fore.YELLOW
            click.echo(f"{status_icon} {color}{feature['name']}{Style.RESET_ALL}")
            if feature['description']:
                click.echo(f"   {feature['description']}")
        
        if progress['next_steps']:
            click.echo(f"\n{Fore.CYAN}🎯 Next Steps:{Style.RESET_ALL}")
            for step in progress['next_steps']:
                click.echo(f"  • {step}")
                
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error reading project status: {str(e)}{Style.RESET_ALL}")