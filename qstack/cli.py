"""QStack CLI interface."""

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
"""
    click.echo(banner)

@click.group()
@click.version_option(version="0.1.0")
@click.option('--no-banner', is_flag=True, help='Skip the banner display')
def main(no_banner):
    """QStack - Modern fullstack project generator by QuantIQ for vibecoders.
    
    Create production-ready fullstack applications with React, Django, 
    Docker, and AI-friendly documentation in seconds.
    """
    if not no_banner:
        print_banner()

# Import new commands
from .commands.up import up
from .commands.down import down
from .commands.logs import logs

# Register commands
main.add_command(startproject)
main.add_command(status) 
main.add_command(build)
main.add_command(up)
main.add_command(down)
main.add_command(logs)

if __name__ == "__main__":
    main()