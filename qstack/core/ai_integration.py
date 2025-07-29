"""AI integration module for Claude-powered project generation."""

import os
import json
import requests
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class ProjectFeature:
    """Represents a detected project feature."""
    name: str
    description: str
    models: List[str]
    components: List[str]
    dependencies: List[str]
    api_endpoints: List[str]


@dataclass
class AIProjectAnalysis:
    """Result of AI analysis of project requirements."""
    project_name: str
    description: str
    features: List[ProjectFeature]
    database_type: str
    template_type: str
    additional_packages: List[str]


class ClaudeAnalyzer:
    """Handles Claude API integration for project analysis."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        self.base_url = "https://api.anthropic.com/v1/messages"
        
        if not self.api_key:
            raise ValueError(
                "Claude API key not found. Set ANTHROPIC_API_KEY environment variable "
                "or pass api_key parameter."
            )
    
    def analyze_project_requirements(self, user_description: str) -> AIProjectAnalysis:
        """
        Analyze user's natural language project description using Claude.
        
        Args:
            user_description: Natural language description of the project
            
        Returns:
            AIProjectAnalysis with structured project requirements
        """
        prompt = self._create_analysis_prompt(user_description)
        
        try:
            response = self._call_claude_api(prompt)
            return self._parse_claude_response(response, user_description)
        except Exception as e:
            # Fallback to basic analysis if API fails
            return self._fallback_analysis(user_description)
    
    def _create_analysis_prompt(self, user_description: str) -> str:
        """Create a well-engineered prompt for Claude to analyze project requirements."""
        return f"""
You are QStack AI, an expert fullstack project analyzer. Analyze the following project description and return a structured JSON response.

PROJECT DESCRIPTION: "{user_description}"

Your task is to:
1. Extract key features and functionality
2. Determine appropriate database models
3. Identify required React components
4. Suggest API endpoints
5. Recommend additional packages

Return ONLY a valid JSON object with this exact structure:

{{
    "project_name": "suggested_project_name_snake_case",
    "description": "Clear 1-sentence description",
    "database_type": "postgres|mysql|sqlite",
    "template_type": "fullstack|frontend-only|api-only",
    "features": [
        {{
            "name": "feature_name",
            "description": "What this feature does",
            "models": ["ModelName1", "ModelName2"],
            "components": ["ComponentName1", "ComponentName2"],
            "dependencies": ["package1", "package2"],
            "api_endpoints": ["/api/endpoint1/", "/api/endpoint2/"]
        }}
    ],
    "additional_packages": ["extra-package1", "extra-package2"]
}}

FEATURE DETECTION RULES:
- "authentication/login/users" → User management feature
- "todo/task/project management" → Task management feature  
- "chat/messaging/real-time" → Chat/messaging feature
- "payment/billing/subscription" → Payment integration feature
- "upload/file/image" → File upload feature
- "dashboard/analytics/charts" → Data visualization feature
- "social/follow/like/share" → Social features
- "search/filter" → Search functionality
- "admin/management" → Admin panel feature

MODEL NAMING:
- Use PascalCase for model names
- Be specific: "TodoItem" not "Todo", "UserProfile" not "User"

COMPONENT NAMING:
- Use PascalCase for React components
- Be descriptive: "TodoList", "UserDashboard", "PaymentForm"

DATABASE SELECTION:
- Complex apps with relationships → postgres
- Simple apps → sqlite
- Specific MySQL needs → mysql

Be intelligent and creative. If the description is vague, make reasonable assumptions.
        """.strip()
    
    def _call_claude_api(self, prompt: str) -> str:
        """Make API call to Claude."""
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key,
            "anthropic-version": "2023-06-01"
        }
        
        data = {
            "model": "claude-3-sonnet-20240229",
            "max_tokens": 2000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        response = requests.post(self.base_url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        return result["content"][0]["text"]
    
    def _parse_claude_response(self, response: str, original_description: str) -> AIProjectAnalysis:
        """Parse Claude's JSON response into AIProjectAnalysis."""
        try:
            # Extract JSON from response (Claude might include extra text)
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            json_str = response[json_start:json_end]
            
            data = json.loads(json_str)
            
            # Convert to our data structure
            features = [
                ProjectFeature(
                    name=f["name"],
                    description=f["description"],
                    models=f.get("models", []),
                    components=f.get("components", []),
                    dependencies=f.get("dependencies", []),
                    api_endpoints=f.get("api_endpoints", [])
                )
                for f in data.get("features", [])
            ]
            
            return AIProjectAnalysis(
                project_name=data.get("project_name", "ai_generated_project"),
                description=data.get("description", original_description),
                features=features,
                database_type=data.get("database_type", "postgres"),
                template_type=data.get("template_type", "fullstack"),
                additional_packages=data.get("additional_packages", [])
            )
            
        except (json.JSONDecodeError, KeyError) as e:
            return self._fallback_analysis(original_description)
    
    def _fallback_analysis(self, user_description: str) -> AIProjectAnalysis:
        """Fallback analysis when API fails or response is invalid."""
        # Simple keyword-based analysis
        description_lower = user_description.lower()
        
        features = []
        additional_packages = []
        
        # Basic feature detection
        if any(word in description_lower for word in ['todo', 'task', 'project']):
            features.append(ProjectFeature(
                name="task_management",
                description="Task and todo management functionality",
                models=["TodoItem", "TodoCategory"],
                components=["TodoList", "TodoItem", "TodoForm"],
                dependencies=[],
                api_endpoints=["/api/todos/", "/api/categories/"]
            ))
        
        if any(word in description_lower for word in ['user', 'auth', 'login', 'account']):
            features.append(ProjectFeature(
                name="user_authentication",
                description="User registration and authentication",
                models=["User", "UserProfile"],
                components=["LoginForm", "RegisterForm", "UserProfile"],
                dependencies=["django-allauth"],
                api_endpoints=["/api/auth/", "/api/users/"]
            ))
        
        # Default feature if none detected
        if not features:
            features.append(ProjectFeature(
                name="basic_crud",
                description="Basic CRUD functionality",
                models=["Item"],
                components=["ItemList", "ItemForm"],
                dependencies=[],
                api_endpoints=["/api/items/"]
            ))
        
        return AIProjectAnalysis(
            project_name="ai_project",
            description=user_description,
            features=features,
            database_type="postgres",
            template_type="fullstack",
            additional_packages=additional_packages
        )


def create_ai_analyzer() -> Optional[ClaudeAnalyzer]:
    """Factory function to create Claude analyzer if API key is available."""
    try:
        return ClaudeAnalyzer()
    except ValueError:
        return None