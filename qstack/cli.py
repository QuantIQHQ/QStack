"""QStack CLI interface."""

import sys
import click
from colorama import init, Fore, Style
from .commands.startproject import startproject
from .commands.status import status
from .commands.build import build

# Initialize colorama for cross-platform colored output
init()

def print_banner():
    """Print the beautiful QStack banner."""
    banner = f"""{Fore.CYAN}
 ██████╗ ███████╗████████╗ █████╗  ██████╗██╗  ██╗
██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
██║   ██║███████╗   ██║   ███████║██║     █████╔╝ 
██║▄▄ ██║╚════██║   ██║   ██╔══██║██║     ██╔═██╗ 
╚██████╔╝███████║   ██║   ██║  ██║╚██████╗██║  ██╗
 ╚══▀▀═╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{Style.RESET_ALL}{Fore.WHITE}                                    (c) QuantIQ{Style.RESET_ALL}
{Fore.MAGENTA}    Modern Fullstack Generator for Vibecoders{Style.RESET_ALL}
{Fore.BLUE}    🔗 https://github.com/QuantIQHQ/QStack{Style.RESET_ALL}
"""
    click.echo(banner)

class QStackGroup(click.Group):
    def get_help(self, ctx):
        """Override help to show banner first."""
        # Check if --no-banner was passed in command line arguments
        if '--no-banner' not in sys.argv:
            print_banner()
        return super().get_help(ctx)

@click.group(cls=QStackGroup)
@click.version_option(version="0.1.0")
@click.option('--no-banner', is_flag=True, help='Skip the banner display')
@click.pass_context
def main(ctx, no_banner):
    """QStack - Modern fullstack project generator by QuantIQ for vibecoders.
    
    Create production-ready fullstack applications with React, Django, 
    Docker, and AI-friendly documentation in seconds.
    """
    # Store no_banner in context for help display
    ctx.params['no_banner'] = no_banner
    
    # Show banner for normal command execution (not help)
    if ctx.invoked_subcommand is None and not no_banner:
        print_banner()

# Import new commands
from .commands.up import up
from .commands.down import down
from .commands.logs import logs
from .commands.ai_context import ai_context, ai_help, add_feature, generate_context

# Register commands
main.add_command(startproject)
main.add_command(status) 
main.add_command(build)
main.add_command(up)
main.add_command(down)
main.add_command(logs)

# Register AI context commands
main.add_command(ai_context, name='ai-context')
main.add_command(ai_help, name='ai-help')
main.add_command(add_feature, name='add-feature')
main.add_command(generate_context, name='generate-context')

if __name__ == "__main__":
    main()