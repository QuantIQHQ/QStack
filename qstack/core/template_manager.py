"""Template management functionality."""

import os
from pathlib import Path

class TemplateManager:
    """Manages project templates."""
    
    def __init__(self):
        self.templates_dir = Path(__file__).parent.parent / 'templates'
    
    def get_available_templates(self):
        """Get list of available templates."""
        templates = []
        if self.templates_dir.exists():
            for item in self.templates_dir.iterdir():
                if item.is_dir():
                    templates.append(item.name)
        return templates
    
    def template_exists(self, template_name):
        """Check if template exists."""
        return (self.templates_dir / template_name).exists()
    
    def get_template_config(self, template_name):
        """Get template configuration."""
        config_file = self.templates_dir / template_name / 'template.json'
        if config_file.exists():
            import json
            with open(config_file) as f:
                return json.load(f)
        return {}