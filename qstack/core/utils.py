"""Utility functions for QStack."""

import secrets
import string
import subprocess
from typing import Tuple

def generate_django_secret_key():
    """Generate a secure Django secret key."""
    chars = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    return ''.join(secrets.choice(chars) for _ in range(50))

def validate_project_name(name):
    """Validate project name follows naming conventions."""
    if not name.replace('_', '').replace('-', '').isalnum():
        return False, "Project name must contain only letters, numbers, hyphens, and underscores"
    
    if name.startswith('-') or name.startswith('_'):
        return False, "Project name cannot start with a hyphen or underscore"
    
    if len(name) < 2:
        return False, "Project name must be at least 2 characters long"
    
    return True, ""

def detect_docker_compose() -> Tuple[str, bool]:
    """Detect which docker compose command is available.
    
    Returns:
        Tuple of (command, is_available)
    """
    # Try docker compose (newer)
    try:
        result = subprocess.run(['docker', 'compose', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            return 'docker compose', True
    except FileNotFoundError:
        pass
    
    # Try docker-compose (legacy)
    try:
        result = subprocess.run(['docker-compose', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            return 'docker-compose', True
    except FileNotFoundError:
        pass
    
    return 'docker compose', False