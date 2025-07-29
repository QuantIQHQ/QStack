# QStack AI Context System Design

## 🎯 Vision
Create a comprehensive AI-readable knowledge base that makes QStack projects instantly understandable to any AI tool (Cursor, Claude, ChatGPT, etc.)

## 📋 Core Components

### 1. `.qstack-context.md` - Master Context File
Located in project root, this file contains EVERYTHING an AI needs to understand the project:

```markdown
# 🚀 QStack Project Context

## Project Metadata
- **Name**: MyTodoApp
- **Type**: fullstack
- **Database**: postgres
- **Generated**: 2024-01-15T10:30:00Z
- **QStack Version**: 0.1.0
- **AI Generated**: true

## 🏗️ Architecture Overview
```
MyTodoApp/
├── frontend/          # React + Vite + Tailwind
├── backend/           # Django + REST API
├── docker-compose.yml # Container orchestration
└── .qstack-context.md # THIS FILE
```

## 🔧 Tech Stack Encoding
**Frontend**: React 18 + Vite 4 + Tailwind CSS 4.0
**Backend**: Django 4.2 + DRF + PostgreSQL
**DevOps**: Docker + docker-compose
**AI Tools**: Claude-generated models & components

## 📊 Database Schema
```python
# Auto-extracted from models.py
User -> (username, email, password)
Todo -> (title, description, completed, user_id, category_id)
Category -> (name, color, user_id)
```

## 🎨 Component Map
```jsx
// Auto-extracted from src/components/
├── TodoList.jsx       # Main todo display
├── TodoForm.jsx       # Add/edit todos
├── CategoryFilter.jsx # Filter by category
└── UserProfile.jsx    # User settings
```

## 🛠️ Available Commands
- `qstack up --build`     # Start development
- `qstack logs --follow`  # View logs
- `qstack status`         # Check features
- `docker exec -it backend python manage.py shell` # Django shell

## 🤖 AI Assistant Instructions
When working on this project:
1. Always check this context file first
2. Use the predefined commands above
3. Follow the established patterns
4. Update this file when adding features
```

### 2. Project Structure Encoding Format

**Hierarchical Structure with Metadata**:
```yaml
# .qstack-structure.yml
project:
  name: "MyTodoApp"
  type: "fullstack"
  
structure:
  frontend:
    type: "react-vite"
    entry: "src/main.jsx"
    components:
      - TodoList: "Main todo display component"
      - TodoForm: "Add/edit form component"
    styling: "tailwind"
    
  backend:
    type: "django"
    apps:
      - todos: "Main todo functionality"
      - users: "User authentication"
    models:
      - User: ["username", "email", "password"]
      - Todo: ["title", "description", "completed"]
    
  infrastructure:
    containerization: "docker-compose"
    database: "postgresql"
    ports:
      frontend: 5173
      backend: 8000
```

### 3. AI Command Patterns

**Predefined AI-friendly commands**:
```bash
# In project root, AI can use:
qstack ai-context           # Show full context
qstack ai-help              # AI-specific help
qstack ai-structure         # Show structure encoding
qstack ai-add-feature "user auth"  # AI-guided feature addition
```

### 4. Cursor IDE Integration

**`.cursor-context`** file for Cursor IDE:
```markdown
# Cursor AI Context for MyTodoApp

## Quick Start
This is a QStack-generated fullstack app. Key files:
- `frontend/src/App.jsx` - Main React app
- `backend/todos/models.py` - Django models
- `docker-compose.yml` - Run with `qstack up`

## Development Workflow
1. `qstack up --build` to start
2. Frontend: http://localhost:5173
3. Backend API: http://localhost:8000/api/

## Code Patterns
- React components use Tailwind CSS
- Django views use DRF serializers
- All models include created_at/updated_at
```

### 5. Context Generator Integration

**Update `generator.py`** to create context files:
```python
def generate_ai_context(self):
    """Generate comprehensive AI context files."""
    context_data = {
        'project_metadata': self.get_project_metadata(),
        'tech_stack': self.get_tech_stack(),
        'structure': self.analyze_structure(),
        'commands': self.get_available_commands(),
        'patterns': self.extract_code_patterns()
    }
    
    # Generate .qstack-context.md
    self.render_template('qstack-context.md.j2', 
                        '.qstack-context.md', context_data)
    
    # Generate .cursor-context 
    self.render_template('cursor-context.md.j2',
                        '.cursor-context', context_data)
```

## 🚀 Implementation Strategy

### Phase 1: Core Context System
1. Create `.qstack-context.md` template
2. Add context generation to ProjectGenerator
3. Include structure encoding format

### Phase 2: AI Integration
1. Add predefined AI commands
2. Create Cursor IDE integration
3. Add context update mechanisms

### Phase 3: Advanced Features
1. Dynamic context updates
2. AI-guided feature additions
3. Cross-project context sharing

## 🎯 Benefits
- **Instant AI Understanding**: Any AI tool can immediately grasp the project
- **Consistent Development**: Standardized patterns across all QStack projects
- **Better Collaboration**: Team members and AI tools work from same context
- **Faster Development**: No need to explain project structure repeatedly

## 🔄 Auto-Update System
Context files automatically update when:
- New models are added
- Components are created
- Dependencies change
- Project structure evolves

This makes QStack projects "AI-native" by default!