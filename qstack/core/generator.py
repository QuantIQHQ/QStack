"""Project generator core functionality."""

import os
import shutil
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from .template_manager import TemplateManager
from .utils import generate_django_secret_key

class ProjectGenerator:
    """Main project generator class."""
    
    def __init__(self, project_name, template_type, database):
        self.project_name = project_name
        self.template_type = template_type
        self.database = database
        self.template_manager = TemplateManager()
        
        # Get templates directory
        self.templates_dir = Path(__file__).parent.parent / 'templates'
        
    def generate(self):
        """Generate the project structure."""
        
        # Create project directory
        project_path = Path(self.project_name)
        if project_path.exists():
            shutil.rmtree(project_path)
        project_path.mkdir()
        
        # Template context
        context = {
            'project_name': self.project_name,
            'project_name_snake': self.project_name.replace('-', '_'),
            'project_name_pascal': self._to_pascal_case(self.project_name),
            'database': self.database,
            'template_type': self.template_type,
            'django_secret_key': generate_django_secret_key(),
        }
        
        # Generate based on template type
        if self.template_type == 'fullstack':
            self._generate_fullstack(project_path, context)
        elif self.template_type == 'frontend-only':
            self._generate_frontend_only(project_path, context)
        elif self.template_type == 'api-only':
            self._generate_api_only(project_path, context)
    
    def _generate_fullstack(self, project_path, context):
        """Generate fullstack project with frontend + backend + docker."""
        
        # Create directory structure
        (project_path / 'frontend').mkdir()
        (project_path / 'backend').mkdir()
        
        # Generate frontend
        self._generate_react_frontend(project_path / 'frontend', context)
        
        # Generate backend
        self._generate_django_backend(project_path / 'backend', context)
        
        # Generate Docker files
        self._generate_docker_files(project_path, context)
        
        # Generate documentation
        self._generate_documentation(project_path, context)
        
        # Generate environment files
        self._generate_env_files(project_path, context)
    
    def _generate_frontend_only(self, project_path, context):
        """Generate frontend-only project."""
        self._generate_react_frontend(project_path, context)
        self._generate_documentation(project_path, context)
    
    def _generate_api_only(self, project_path, context):
        """Generate API-only project."""
        self._generate_django_backend(project_path, context)
        self._generate_docker_files(project_path, context)
        self._generate_documentation(project_path, context)
        self._generate_env_files(project_path, context)
    
    def _generate_react_frontend(self, frontend_path, context):
        """Generate React + Vite + Tailwind frontend."""
        self._copy_template('frontend', frontend_path, context)
    
    def _generate_django_backend(self, backend_path, context):
        """Generate Django backend."""
        self._copy_template('backend', backend_path, context)
    
    def _generate_docker_files(self, project_path, context):
        """Generate Docker configuration."""
        self._render_template('docker-compose.yml.j2', project_path / 'docker-compose.yml', context)
        self._render_template('.dockerignore.j2', project_path / '.dockerignore', context)
    
    def _generate_documentation(self, project_path, context):
        """Generate documentation files."""
        self._render_template('README.md.j2', project_path / 'README.md', context)
        self._render_template('defineprojectscope.md.j2', project_path / 'defineprojectscope.md', context)
    
    def _generate_env_files(self, project_path, context):
        """Generate environment files."""
        self._render_template('.env.example.j2', project_path / '.env.example', context)
        self._render_template('.gitignore.j2', project_path / '.gitignore', context)
    
    def _copy_template(self, template_name, dest_path, context):
        """Copy and render a template directory."""
        template_path = self.templates_dir / template_name
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template '{template_name}' not found")
        
        self._copy_and_render_directory(template_path, dest_path, context)
    
    def _copy_and_render_directory(self, src, dest, context):
        """Recursively copy and render directory templates."""
        dest.mkdir(exist_ok=True)
        
        for item in src.rglob('*'):
            if item.is_file():
                # Calculate relative path
                rel_path = item.relative_to(src)
                
                # Render dynamic directory names in path
                rel_path_str = str(rel_path)
                env = Environment()
                rel_path_template = env.from_string(rel_path_str)
                rendered_rel_path = rel_path_template.render(**context)
                
                dest_file = dest / rendered_rel_path
                
                # Create parent directories
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                
                # Render template if it's a .j2 file
                if item.suffix == '.j2':
                    dest_file = dest_file.with_suffix('')
                    self._render_template_file(item, dest_file, context)
                else:
                    # Copy file as-is
                    shutil.copy2(item, dest_file)
    
    def _render_template(self, template_name, dest_path, context):
        """Render a single template file."""
        env = Environment(loader=FileSystemLoader(self.templates_dir))
        template = env.get_template(template_name)
        content = template.render(**context)
        
        with open(dest_path, 'w') as f:
            f.write(content)
    
    def _render_template_file(self, template_path, dest_path, context):
        """Render a template file with Jinja2."""
        with open(template_path, 'r') as f:
            template_content = f.read()
        
        env = Environment()
        template = env.from_string(template_content)
        content = template.render(**context)
        
        with open(dest_path, 'w') as f:
            f.write(content)
    
    def _to_pascal_case(self, text):
        """Convert text to PascalCase."""
        return ''.join(word.capitalize() for word in text.replace('-', '_').split('_'))