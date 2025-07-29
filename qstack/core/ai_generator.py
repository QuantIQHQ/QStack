"""AI-powered project generator that creates custom projects based on Claude analysis."""

import os
import json
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader
from .ai_integration import AIProjectAnalysis, ProjectFeature
from .generator import ProjectGenerator


class AIProjectGenerator(ProjectGenerator):
    """Extended project generator with AI-powered customization."""
    
    def __init__(self, project_name: str, ai_analysis: AIProjectAnalysis):
        # Use analysis results for configuration
        super().__init__(
            project_name=project_name,
            template_type=ai_analysis.template_type,
            database=ai_analysis.database_type
        )
        self.ai_analysis = ai_analysis
        self.custom_models = self._extract_models()
        self.custom_components = self._extract_components()
        self.additional_packages = ai_analysis.additional_packages
    
    def generate(self):
        """Generate AI-customized project."""
        # Call parent generation first
        super().generate()
        
        # Then apply AI customizations
        self._generate_custom_models()
        self._generate_custom_components()
        self._update_package_dependencies()
        self._generate_ai_documentation()
        self._update_urls_and_views()
    
    def _generate_ai_context(self, project_path, context):
        """Override parent method to include AI-specific context."""
        from datetime import datetime
        
        # Enhance context with AI-specific data
        ai_context = context.copy()
        ai_context.update({
            'generation_timestamp': datetime.now().isoformat(),
            'qstack_version': '0.1.0',
            'ai_generated': True,
            'original_description': getattr(self.ai_analysis, 'original_description', None),
            'ai_analysis': self.ai_analysis,
            'custom_models': self.custom_models,
            'custom_components': self.custom_components
        })
        
        # Generate main QStack context file with AI data
        self._render_template('qstack-context.md.j2', project_path / '.qstack-context.md', ai_context)
        
        # Generate enhanced Cursor IDE context file
        self._generate_cursor_context(project_path, ai_context)
    
    def _extract_models(self) -> Dict[str, Dict]:
        """Extract Django models from AI analysis."""
        models = {}
        
        for feature in self.ai_analysis.features:
            for model_name in feature.models:
                models[model_name] = {
                    'feature': feature.name,
                    'fields': self._generate_model_fields(model_name, feature),
                    'description': f"Model for {feature.description}"
                }
        
        return models
    
    def _extract_components(self) -> Dict[str, Dict]:
        """Extract React components from AI analysis."""
        components = {}
        
        for feature in self.ai_analysis.features:
            for component_name in feature.components:
                components[component_name] = {
                    'feature': feature.name,
                    'description': f"Component for {feature.description}",
                    'props': self._generate_component_props(component_name, feature)
                }
        
        return components
    
    def _generate_model_fields(self, model_name: str, feature: ProjectFeature) -> Dict[str, str]:
        """Generate Django model fields based on model name and feature."""
        common_fields = {
            'created_at': 'models.DateTimeField(auto_now_add=True)',
            'updated_at': 'models.DateTimeField(auto_now=True)'
        }
        
        # Smart field generation based on model name
        fields = common_fields.copy()
        
        if 'User' in model_name:
            fields.update({
                'username': 'models.CharField(max_length=150, unique=True)',
                'email': 'models.EmailField(unique=True)',
                'first_name': 'models.CharField(max_length=30)',
                'last_name': 'models.CharField(max_length=30)',
                'is_active': 'models.BooleanField(default=True)'
            })
        
        elif 'Todo' in model_name or 'Task' in model_name:
            fields.update({
                'title': 'models.CharField(max_length=200)',
                'description': 'models.TextField(blank=True)',
                'is_completed': 'models.BooleanField(default=False)',
                'due_date': 'models.DateTimeField(null=True, blank=True)',
                'priority': 'models.CharField(max_length=10, choices=[(\"low\", \"Low\"), (\"medium\", \"Medium\"), (\"high\", \"High\")], default=\"medium\")'
            })
        
        elif 'Category' in model_name:
            fields.update({
                'name': 'models.CharField(max_length=100)',
                'color': 'models.CharField(max_length=7, default=\"#007bff\")',
                'description': 'models.TextField(blank=True)'
            })
        
        elif 'Profile' in model_name:
            fields.update({
                'user': 'models.OneToOneField(User, on_delete=models.CASCADE)',
                'bio': 'models.TextField(max_length=500, blank=True)',
                'avatar': 'models.ImageField(upload_to=\"avatars/\", blank=True)',
                'phone': 'models.CharField(max_length=20, blank=True)'
            })
        
        else:
            # Generic fields for unknown models
            fields.update({
                'name': 'models.CharField(max_length=100)',
                'description': 'models.TextField(blank=True)'
            })
        
        return fields
    
    def _generate_component_props(self, component_name: str, feature: ProjectFeature) -> Dict[str, str]:
        """Generate React component props based on component name."""
        props = {}
        
        if 'List' in component_name:
            props = {
                'items': 'array',
                'onItemClick': 'function',
                'loading': 'boolean'
            }
        elif 'Form' in component_name:
            props = {
                'onSubmit': 'function',
                'initialValues': 'object',
                'loading': 'boolean'
            }
        elif 'Item' in component_name:
            props = {
                'item': 'object',
                'onEdit': 'function',
                'onDelete': 'function'
            }
        
        return props
    
    def _generate_custom_models(self):
        """Generate custom Django models based on AI analysis."""
        if not self.custom_models:
            return
        
        # Create custom models.py
        models_content = self._create_models_file()
        project_name_snake = self.project_name.replace('-', '_')
        models_path = os.path.join(self.project_name, 'backend', f'{project_name_snake}', 'models.py')
        
        with open(models_path, 'w') as f:
            f.write(models_content)
    
    def _create_models_file(self) -> str:
        """Create the models.py file content."""
        content = '''"""Custom models generated by QStack AI."""

from django.db import models
from django.contrib.auth.models import User


'''
        
        for model_name, model_data in self.custom_models.items():
            content += f'class {model_name}(models.Model):\n'
            content += f'    """Model for {model_data["description"]}."""\n'
            
            for field_name, field_definition in model_data['fields'].items():
                content += f'    {field_name} = {field_definition}\n'
            
            content += f'\n    class Meta:\n'
            content += f'        verbose_name = "{model_name}"\n'
            content += f'        verbose_name_plural = "{model_name}s"\n'
            content += f'        ordering = ["-created_at"]\n\n'
            content += f'    def __str__(self):\n'
            
            # Smart __str__ method
            if 'name' in model_data['fields']:
                content += f'        return self.name\n'
            elif 'title' in model_data['fields']:
                content += f'        return self.title\n'
            elif 'username' in model_data['fields']:
                content += f'        return self.username\n'
            else:
                content += f'        return f"{model_name} {{self.id}}"\n'
            
            content += '\n\n'
        
        return content
    
    def _generate_custom_components(self):
        """Generate custom React components based on AI analysis."""
        if not self.custom_components:
            return
        
        components_dir = os.path.join(self.project_name, 'frontend', 'src', 'components')
        
        for component_name, component_data in self.custom_components.items():
            component_content = self._create_component_file(component_name, component_data)
            component_path = os.path.join(components_dir, f'{component_name}.jsx')
            
            with open(component_path, 'w') as f:
                f.write(component_content)
    
    def _create_component_file(self, component_name: str, component_data: Dict) -> str:
        """Create React component file content."""
        props_str = ', '.join(component_data.get('props', {}).keys())
        
        content = f'''import React from 'react';

/**
 * {component_name} - {component_data['description']}
 * Generated by QStack AI
 */
const {component_name} = ({{ {props_str} }}) => {{
    return (
        <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-xl font-semibold mb-4">{component_name}</h2>
            <p className="text-gray-600">
                {component_data['description']}
            </p>
            {{/* TODO: Implement {component_name} functionality */}}
        </div>
    );
}};

export default {component_name};
'''
        return content
    
    def _update_package_dependencies(self):
        """Update package.json with additional AI-suggested packages."""
        if not self.additional_packages:
            return
        
        package_json_path = os.path.join(self.project_name, 'frontend', 'package.json')
        
        try:
            with open(package_json_path, 'r') as f:
                package_data = json.load(f)
            
            # Add AI-suggested packages
            for package in self.additional_packages:
                if package not in package_data.get('dependencies', {}):
                    # You'd normally look up the latest version
                    package_data.setdefault('dependencies', {})[package] = 'latest'
            
            with open(package_json_path, 'w') as f:
                json.dump(package_data, f, indent=2)
                
        except (json.JSONDecodeError, FileNotFoundError):
            pass  # Skip if package.json is invalid or missing
    
    def _generate_ai_documentation(self):
        """Generate AI-specific documentation."""
        ai_doc_content = f"""# AI-Generated Project: {self.project_name}

## Project Description
{self.ai_analysis.description}

## AI-Detected Features

"""
        
        for feature in self.ai_analysis.features:
            ai_doc_content += f"""### {feature.name.replace('_', ' ').title()}
**Description:** {feature.description}

**Models:** {', '.join(feature.models) if feature.models else 'None'}

**Components:** {', '.join(feature.components) if feature.components else 'None'}

**API Endpoints:** {', '.join(feature.api_endpoints) if feature.api_endpoints else 'None'}

**Dependencies:** {', '.join(feature.dependencies) if feature.dependencies else 'None'}

---

"""
        
        ai_doc_content += f"""
## Implementation Notes

This project was generated using QStack AI with Claude analysis. The structure and features were automatically detected from your natural language description.

### Next Steps
1. Review the generated models in `backend/{self.project_name.replace('-', '_')}/models.py`
2. Check the React components in `frontend/src/components/`
3. Run migrations: `docker-compose exec backend python manage.py makemigrations`
4. Run migrations: `docker-compose exec backend python manage.py migrate`
5. Customize the generated code as needed

### AI Analysis Results
- **Template Type:** {self.ai_analysis.template_type}
- **Database:** {self.ai_analysis.database_type}
- **Additional Packages:** {', '.join(self.ai_analysis.additional_packages) if self.ai_analysis.additional_packages else 'None'}

Generated with ❤️ by QStack AI - Powered by Claude
"""
        
        ai_doc_path = os.path.join(self.project_name, 'AI_ANALYSIS.md')
        with open(ai_doc_path, 'w') as f:
            f.write(ai_doc_content)
    
    def _update_urls_and_views(self):
        """Generate basic API views and URLs for detected features."""
        # This would generate Django REST framework views and URLs
        # For now, just create a placeholder
        pass