"""Parse defineprojectscope.md for status tracking."""

import re
from pathlib import Path

class StatusParser:
    """Parse project scope markdown for progress tracking."""
    
    def __init__(self, scope_file_path):
        self.scope_file = Path(scope_file_path)
    
    def get_progress(self):
        """Parse the scope file and return progress data."""
        if not self.scope_file.exists():
            return {'features': [], 'next_steps': []}
        
        with open(self.scope_file, 'r') as f:
            content = f.read()
        
        features = self._parse_features(content)
        next_steps = self._parse_next_steps(content)
        
        return {
            'features': features,
            'next_steps': next_steps
        }
    
    def _parse_features(self, content):
        """Parse feature list from markdown."""
        features = []
        
        # Look for checkbox lists
        pattern = r'^[-*+]\s*\[([x\s])\]\s*(.+?)(?:\n\s*-\s*(.+?))?$'
        
        for match in re.finditer(pattern, content, re.MULTILINE):
            completed = match.group(1).lower() == 'x'
            name = match.group(2).strip()
            description = match.group(3).strip() if match.group(3) else ''
            
            features.append({
                'name': name,
                'description': description,
                'completed': completed
            })
        
        # Look for numbered features with status
        pattern = r'^\d+\.\s*\*\*(.+?)\*\*\s*\n\s*-\s*\*\*Description\*\*:\s*(.+?)\n\s*-\s*\*\*Status\*\*:\s*(.+?)(?:\s*[✓✗])?'
        
        for match in re.finditer(pattern, content, re.MULTILINE | re.DOTALL):
            name = match.group(1).strip()
            description = match.group(2).strip()
            status = match.group(3).strip()
            completed = 'implemented' in status.lower() or '✓' in status
            
            features.append({
                'name': name,
                'description': description,
                'completed': completed
            })
        
        # Look for ### headings with status on separate lines
        pattern = r'###\s*\d+\.\s*\*\*(.+?)\*\*.*?\n.*?-\s*\*\*Description\*\*:\s*(.+?)\n.*?-\s*\*\*Status\*\*:\s*(.+?)(?:\n|$)'
        
        for match in re.finditer(pattern, content, re.MULTILINE | re.DOTALL):
            name = match.group(1).strip()
            description = match.group(2).strip()
            status = match.group(3).strip()
            completed = 'implemented' in status.lower() or '✓' in status
            
            features.append({
                'name': name,
                'description': description,
                'completed': completed
            })
        
        return features
    
    def _parse_next_steps(self, content):
        """Parse next steps from markdown."""
        next_steps = []
        
        # Look for "Next Steps" section
        next_steps_match = re.search(r'##\s*Next Steps.*?\n(.*?)(?=\n##|\n#|$)', content, re.DOTALL | re.IGNORECASE)
        
        if next_steps_match:
            steps_content = next_steps_match.group(1)
            
            # Parse list items
            for match in re.finditer(r'^[-*+]\s*(.+?)$', steps_content, re.MULTILINE):
                step = match.group(1).strip()
                if step:
                    next_steps.append(step)
        
        return next_steps