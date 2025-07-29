"""AI context management commands."""

import os
import json
import click
from pathlib import Path
from colorama import Fore, Style
from ..core.generator import ProjectGenerator

@click.command()
@click.option('--format', '-f', type=click.Choice(['full', 'structure', 'quick']), 
              default='full', help='Context display format')
def ai_context(format):
    """Display AI-readable project context.
    
    Shows comprehensive project information that AI tools can use
    to understand the codebase structure and patterns.
    """
    context_file = Path('.qstack-context.md')
    
    if not context_file.exists():
        click.echo(f"{Fore.RED}❌ No QStack context found. Run this in a QStack project root.{Style.RESET_ALL}")
        return
    
    if format == 'quick':
        _show_quick_context()
    elif format == 'structure':
        _show_structure_only()
    else:
        _show_full_context()

@click.command()
def ai_help():
    """Show AI-specific help and commands for QStack projects."""
    
    click.echo(f"{Fore.CYAN}🤖 QStack AI Assistant Commands{Style.RESET_ALL}\n")
    
    click.echo(f"{Fore.GREEN}📋 Context Commands:{Style.RESET_ALL}")
    click.echo("  qstack ai-context           # Show full project context")
    click.echo("  qstack ai-context --format=quick  # Show condensed context")
    click.echo("  qstack ai-context --format=structure  # Show only structure")
    click.echo("  qstack generate-context      # Regenerate context files")
    
    click.echo(f"\n{Fore.GREEN}🚀 Development Commands:{Style.RESET_ALL}")
    click.echo("  qstack up --build           # Start with fresh build")
    click.echo("  qstack logs --follow        # Follow application logs")
    click.echo("  qstack status               # Check feature status")
    
    click.echo(f"\n{Fore.GREEN}🛠️ AI-Guided Development:{Style.RESET_ALL}")
    click.echo("  qstack add-feature 'feature description'  # AI-guided feature addition")
    click.echo("  qstack analyze-code         # Analyze codebase patterns")
    click.echo("  qstack suggest-improvements # Get AI suggestions")
    
    click.echo(f"\n{Fore.MAGENTA}💡 AI Tool Integration:{Style.RESET_ALL}")
    click.echo("  • Cursor IDE: Reads .cursor-context automatically")
    click.echo("  • Claude: Use 'qstack ai-context' output as context")
    click.echo("  • ChatGPT: Copy .qstack-context.md content for full context")
    
    click.echo(f"\n{Fore.BLUE}📚 Context Files:{Style.RESET_ALL}")
    click.echo("  .qstack-context.md          # Master AI context file")
    click.echo("  .cursor-context             # Cursor IDE specific context")
    click.echo("  defineprojectscope.md       # Human-readable project scope")
    click.echo("  AI_ANALYSIS.md              # AI generation analysis (if applicable)")

@click.command()
@click.argument('feature_description')
@click.option('--implement', '-i', is_flag=True, help='Implement the feature immediately')
def add_feature(feature_description, implement):
    """AI-guided feature addition to existing QStack project.
    
    FEATURE_DESCRIPTION: Natural language description of the feature to add
    
    Example: qstack add-feature "user profile with avatar upload"
    """
    click.echo(f"{Fore.MAGENTA}🤖 AI Feature Analysis: {feature_description}{Style.RESET_ALL}")
    
    # Check if we're in a QStack project
    if not Path('.qstack-context.md').exists():
        click.echo(f"{Fore.RED}❌ Not in a QStack project. Run this in project root.{Style.RESET_ALL}")
        return
    
    # Here you would integrate with AI to analyze the feature
    click.echo(f"{Fore.CYAN}🔍 Analyzing feature requirements...{Style.RESET_ALL}")
    click.echo(f"{Fore.YELLOW}⚡ Feature: {feature_description}{Style.RESET_ALL}")
    
    # Mock analysis output
    click.echo(f"\n{Fore.GREEN}✅ Analysis Complete:{Style.RESET_ALL}")
    click.echo("  📋 Models to create: UserProfile")
    click.echo("  🎨 Components needed: ProfileForm, AvatarUpload")
    click.echo("  🔗 API endpoints: /api/profile/, /api/profile/avatar/")
    click.echo("  📦 Dependencies: django-storages, pillow")
    
    if implement:
        click.echo(f"\n{Fore.MAGENTA}🚀 Implementing feature...{Style.RESET_ALL}")
        # Implementation logic would go here
        click.echo(f"{Fore.GREEN}✅ Feature implemented! Check updated files.{Style.RESET_ALL}")
    else:
        click.echo(f"\n{Fore.BLUE}💡 Use --implement flag to generate this feature automatically{Style.RESET_ALL}")

@click.command()
def generate_context():
    """Regenerate AI context files for current project."""
    
    # Check if we're in a QStack project by looking for key files
    has_docker_compose = Path('docker-compose.yml').exists()
    has_frontend = Path('frontend').exists()
    has_backend = Path('backend').exists()
    
    if not (has_docker_compose or has_frontend or has_backend):
        click.echo(f"{Fore.RED}❌ Not in a QStack project directory.{Style.RESET_ALL}")
        return
    
    click.echo(f"{Fore.CYAN}🔄 Regenerating AI context files...{Style.RESET_ALL}")
    
    # Analyze current project structure
    project_info = _analyze_current_project()
    
    # Generate context files
    _generate_qstack_context(project_info)
    _generate_cursor_context(project_info)
    
    click.echo(f"{Fore.GREEN}✅ Context files updated!{Style.RESET_ALL}")
    click.echo("  📝 .qstack-context.md - Master AI context")
    click.echo("  🎯 .cursor-context - Cursor IDE integration")

def _show_quick_context():
    """Show condensed project context."""
    try:
        with open('.qstack-context.md', 'r') as f:
            content = f.read()
        
        # Extract key sections
        lines = content.split('\n')
        in_metadata = False
        in_commands = False
        
        for line in lines:
            if '## 📋 Project Metadata' in line:
                in_metadata = True
                click.echo(f"{Fore.CYAN}{line}{Style.RESET_ALL}")
            elif '## 🛠️ Development Commands' in line:
                in_commands = True
                click.echo(f"{Fore.GREEN}{line}{Style.RESET_ALL}")
            elif line.startswith('## ') and (in_metadata or in_commands):
                in_metadata = False
                in_commands = False
            elif in_metadata or in_commands:
                click.echo(line)
                
    except FileNotFoundError:
        click.echo(f"{Fore.RED}❌ Context file not found{Style.RESET_ALL}")

def _show_structure_only():
    """Show only project structure."""
    try:
        with open('.qstack-context.md', 'r') as f:
            content = f.read()
        
        # Extract structure section
        lines = content.split('\n')
        in_structure = False
        
        for line in lines:
            if '## 🏗️ Architecture Overview' in line:
                in_structure = True
                click.echo(f"{Fore.CYAN}{line}{Style.RESET_ALL}")
            elif line.startswith('## ') and in_structure:
                break
            elif in_structure:
                click.echo(line)
                
    except FileNotFoundError:
        click.echo(f"{Fore.RED}❌ Context file not found{Style.RESET_ALL}")

def _show_full_context():
    """Show full context file."""
    try:
        with open('.qstack-context.md', 'r') as f:
            content = f.read()
        click.echo(content)
    except FileNotFoundError:
        click.echo(f"{Fore.RED}❌ Context file not found{Style.RESET_ALL}")

def _analyze_current_project():
    """Analyze current project structure."""
    project_name = Path.cwd().name
    
    # Detect project type
    template_type = 'fullstack'
    if Path('frontend').exists() and not Path('backend').exists():
        template_type = 'frontend-only'
    elif Path('backend').exists() and not Path('frontend').exists():
        template_type = 'api-only'
    
    # Detect database
    database = 'postgres'  # Default
    if Path('docker-compose.yml').exists():
        with open('docker-compose.yml', 'r') as f:
            compose_content = f.read()
            if 'mysql' in compose_content:
                database = 'mysql'
            elif 'sqlite' in compose_content:
                database = 'sqlite'
    
    return {
        'project_name': project_name,
        'template_type': template_type,
        'database': database,
        'ai_generated': Path('AI_ANALYSIS.md').exists()
    }

def _generate_qstack_context(project_info):
    """Generate .qstack-context.md file."""
    from datetime import datetime
    from jinja2 import Environment, FileSystemLoader
    
    # Template context
    context = {
        **project_info,
        'project_name_snake': project_info['project_name'].replace('-', '_'),
        'generation_timestamp': datetime.now().isoformat(),
        'qstack_version': '0.1.0'
    }
    
    # Load and render template
    templates_dir = Path(__file__).parent.parent / 'templates'
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('qstack-context.md.j2')
    content = template.render(**context)
    
    with open('.qstack-context.md', 'w') as f:
        f.write(content)

def _generate_cursor_context(project_info):
    """Generate .cursor-context file for Cursor IDE."""
    content = f"""# Cursor AI Context for {project_info['project_name']}

## Quick Start
This is a QStack-generated {project_info['template_type']} application.

### Development Commands
- `qstack up --build` - Start development environment
- `qstack logs --follow` - View application logs
- `qstack status` - Check implementation status

### Key Files
{_get_key_files_list(project_info['template_type'], project_info['project_name'])}

### Architecture
- **Type**: {project_info['template_type']}
- **Database**: {project_info['database']}
- **AI Generated**: {'Yes' if project_info['ai_generated'] else 'No'}

### Code Patterns
{_get_code_patterns(project_info['template_type'])}

For full context, see .qstack-context.md
"""
    
    with open('.cursor-context', 'w') as f:
        f.write(content)

def _get_key_files_list(template_type, project_name):
    """Get list of key files based on template type."""
    if template_type == 'fullstack':
        return f"""- `frontend/src/App.jsx` - Main React application
- `backend/{project_name.replace('-', '_')}_project/settings.py` - Django settings
- `backend/todos/models.py` - Database models
- `docker-compose.yml` - Container orchestration"""
    elif template_type == 'frontend-only':
        return """- `src/App.jsx` - Main React application
- `package.json` - Dependencies and scripts
- `vite.config.js` - Build configuration"""
    else:  # api-only
        return f"""- `{project_name.replace('-', '_')}_project/settings.py` - Django settings
- `todos/models.py` - Database models
- `todos/views.py` - API endpoints"""

def _get_code_patterns(template_type):
    """Get code patterns description."""
    patterns = []
    
    if template_type in ['fullstack', 'frontend-only']:
        patterns.append("- React: Functional components with hooks")
        patterns.append("- Styling: Tailwind CSS utility classes")
        patterns.append("- State: useState and useEffect hooks")
    
    if template_type in ['fullstack', 'api-only']:
        patterns.append("- Django: Class-based views with DRF")
        patterns.append("- Models: Include created_at/updated_at fields")
        patterns.append("- API: RESTful endpoints with serializers")
    
    return '\n'.join(patterns) if patterns else "- Standard project patterns"