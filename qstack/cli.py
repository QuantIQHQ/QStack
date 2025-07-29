"""QStack CLI interface."""

import click
from colorama import init, Fore, Style
from .commands.startproject import startproject
from .commands.status import status
from .commands.build import build

# Initialize colorama for cross-platform colored output
init()

@click.group()
@click.version_option(version="0.1.0")
def main():
    """QStack - Modern fullstack project generator by QuantIQ for vibecoders.
    
    Create production-ready fullstack applications with React, Django, 
    Docker, and AI-friendly documentation in seconds.
    """
    click.echo(f"{Fore.CYAN}🚀 QStack - Powered by QuantIQ Devs{Style.RESET_ALL}")

# Register commands
main.add_command(startproject)
main.add_command(status) 
main.add_command(build)

if __name__ == "__main__":
    main()