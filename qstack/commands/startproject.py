"""Start project command."""

import os
import click
from colorama import Fore, Style
from ..core.generator import ProjectGenerator
from ..core.ai_integration import create_ai_analyzer
from ..core.ai_generator import AIProjectGenerator

@click.command()
@click.argument('project_name_or_description')
@click.option('--template', '-t', default='fullstack', 
              help='Project template (fullstack, frontend-only, api-only)')
@click.option('--database', '-d', default='postgres',
              type=click.Choice(['postgres', 'sqlite', 'mysql']),
              help='Database type (default: postgres)')
@click.option('--force', '-f', is_flag=True,
              help='Overwrite existing directory')
@click.option('--ai', is_flag=True,
              help='Use AI to analyze project requirements from natural language description')
def startproject(project_name_or_description, template, database, force, ai):
    """Create a new fullstack project.
    
    PROJECT_NAME_OR_DESCRIPTION: Project name, or with --ai flag, a natural language description
    
    Examples:
      qstack startproject myapp
      qstack startproject "a todo app with user auth and categories" --ai
    """
    
    if ai:
        # AI-powered project generation
        click.echo(f"{Fore.MAGENTA}🤖 AI Mode: Analyzing your project requirements...{Style.RESET_ALL}")
        
        # Initialize Claude analyzer
        analyzer = create_ai_analyzer()
        if not analyzer:
            click.echo(f"{Fore.RED}❌ Claude API key not found. Set ANTHROPIC_API_KEY environment variable.{Style.RESET_ALL}")
            click.echo(f"{Fore.YELLOW}💡 Get your API key from: https://console.anthropic.com/{Style.RESET_ALL}")
            return
        
        try:
            # Analyze the description
            click.echo(f"{Fore.CYAN}🔍 Claude is analyzing: \"{project_name_or_description}\"{Style.RESET_ALL}")
            analysis = analyzer.analyze_project_requirements(project_name_or_description)
            
            # Use AI-suggested project name
            project_name = analysis.project_name
            
            # Check if directory exists
            if os.path.exists(project_name) and not force:
                click.echo(f"{Fore.RED}❌ Directory '{project_name}' already exists. Use --force to overwrite.{Style.RESET_ALL}")
                return
            
            # Display analysis results
            click.echo(f"\n{Fore.GREEN}✅ AI Analysis Complete!{Style.RESET_ALL}")
            click.echo(f"{Fore.CYAN}📝 Project: {project_name}{Style.RESET_ALL}")
            click.echo(f"{Fore.CYAN}📊 Database: {analysis.database_type}{Style.RESET_ALL}")
            click.echo(f"{Fore.CYAN}🏗️  Template: {analysis.template_type}{Style.RESET_ALL}")
            
            if analysis.features:
                click.echo(f"\n{Fore.YELLOW}🎯 Detected Features:{Style.RESET_ALL}")
                for feature in analysis.features:
                    click.echo(f"  • {feature.name.replace('_', ' ').title()}: {feature.description}")
            
            if analysis.additional_packages:
                click.echo(f"\n{Fore.BLUE}📦 Additional Packages: {', '.join(analysis.additional_packages)}{Style.RESET_ALL}")
            
            # Generate AI-powered project
            click.echo(f"\n{Fore.MAGENTA}🤖 Generating AI-customized project...{Style.RESET_ALL}")
            generator = AIProjectGenerator(project_name, analysis)
            generator.generate()
            
            click.echo(f"\n{Fore.GREEN}✅ AI-powered project '{project_name}' created successfully!{Style.RESET_ALL}")
            click.echo(f"\n{Fore.CYAN}🤖 AI Features:{Style.RESET_ALL}")
            click.echo(f"  • Custom models generated based on your requirements")
            click.echo(f"  • React components tailored to your features")
            click.echo(f"  • AI analysis documentation in AI_ANALYSIS.md")
            
        except Exception as e:
            click.echo(f"{Fore.RED}❌ AI analysis failed: {str(e)}{Style.RESET_ALL}")
            click.echo(f"{Fore.YELLOW}💡 Falling back to standard project generation...{Style.RESET_ALL}")
            # Fallback to standard generation
            ai = False
    
    if not ai:
        # Standard project generation
        project_name = project_name_or_description
        
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
            
        except Exception as e:
            click.echo(f"{Fore.RED}❌ Error creating project: {str(e)}{Style.RESET_ALL}")
            raise click.Abort()
    
    # Common next steps
    click.echo(f"\n{Fore.CYAN}Next steps:{Style.RESET_ALL}")
    click.echo(f"  cd {project_name}")
    click.echo(f"  qstack up --build")
    click.echo(f"  Open http://localhost:5173 🎉")
    
    if ai:
        click.echo(f"\n{Fore.MAGENTA}🤖 AI Tips:{Style.RESET_ALL}")
        click.echo(f"  • Check AI_ANALYSIS.md for detailed feature breakdown")
        click.echo(f"  • Review generated models in backend/{project_name}/models.py")
        click.echo(f"  • Customize generated components in frontend/src/components/")
        click.echo(f"  • Run migrations after reviewing models")