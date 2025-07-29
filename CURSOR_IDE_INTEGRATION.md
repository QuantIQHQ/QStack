# 🎯 Cursor IDE Integration Guide

## 🧠 How QStack + Cursor = Magic

QStack projects are designed to work seamlessly with Cursor IDE. Every generated project includes automatic AI context that makes development incredibly smooth.

## 🚀 Quick Start with Cursor

### 1. Generate a QStack Project
```bash
# Traditional project
qstack startproject myapp
cd myapp

# AI-powered project  
qstack startproject "a social media app with posts and likes" --ai
cd social_media_app_with_posts_and_likes
```

### 2. Open in Cursor
```bash
code .  # Or drag folder to Cursor
```

**That's it!** Cursor automatically reads the `.cursor-context` file and understands:
- Your entire project structure
- Tech stack (React, Django, Docker, etc.)
- Available commands and workflows
- Code patterns and conventions
- Database schema and models

## 📁 Auto-Generated Context Files

Every QStack project includes:

### `.cursor-context` - Cursor IDE Integration
```markdown
# Cursor AI Context for MyApp

## Quick Start
This is a QStack-generated fullstack application.

### Development Commands
- `qstack up --build` - Start development environment
- `qstack logs --follow` - View application logs
- `qstack status` - Check implementation status

### Key Files
- `frontend/src/App.jsx` - Main React application
- `backend/myapp_project/settings.py` - Django settings
- `backend/todos/models.py` - Database models
- `docker-compose.yml` - Container orchestration

### Architecture
- **Type**: fullstack
- **Database**: postgres
- **Generated**: 2024-01-15

### Code Patterns
- React: Functional components with hooks
- Styling: Tailwind CSS utility classes
- State: useState and useEffect hooks
- Django: Class-based views with DRF
- Models: Include created_at/updated_at fields
- API: RESTful endpoints with serializers

For full context, see .qstack-context.md
```

### `.qstack-context.md` - Master AI Context
Complete project documentation including:
- Project metadata and architecture
- Database schema with relationships
- All available commands
- Code patterns and best practices
- AI-specific development instructions

## 🎯 Cursor + QStack Workflow

### 1. Instant Project Understanding
```
Open project → Cursor reads .cursor-context → AI knows everything
```

### 2. Smart Code Completion
Cursor understands your:
- Django models and relationships
- React component patterns
- Tailwind CSS classes
- API endpoint structure
- Database queries

### 3. Context-Aware Suggestions
Ask Cursor:
- "Add a new Django model for user profiles"
- "Create a React component for displaying posts"
- "Add authentication to this API endpoint"
- "Generate a form component with Tailwind styling"

### 4. Project-Specific Commands
Cursor knows your available commands:
- `qstack up --build` - Start development
- `qstack logs --follow` - View logs
- `docker exec -it backend python manage.py shell` - Django shell

## 🔄 Dynamic Context Updates

When you modify your project:

```bash
# Regenerate context files
qstack generate-context

# Cursor automatically picks up changes
```

Context updates include:
- New models and components
- Modified database schema
- Additional dependencies
- Changed project structure

## 🛠️ Advanced Cursor Integration

### Custom Instructions
Add to your Cursor settings for enhanced QStack support:

```json
{
  "rules": [
    "Always check .qstack-context.md for project understanding",
    "Use QStack patterns for Django models (include created_at/updated_at)",
    "Follow Tailwind CSS utility-first approach for styling", 
    "Use functional React components with hooks",
    "Maintain QStack's consistent file organization"
  ]
}
```

### AI-Powered Feature Development
```bash
# In Cursor, ask:
"Based on the QStack context, add user authentication with email verification"

# Cursor understands:
# - Your Django project structure
# - Available models and serializers
# - React component patterns
# - Tailwind styling approach
# - Docker setup for testing
```

## 🎨 Example Development Session

### 1. Open QStack Project
```bash
qstack startproject "blog with comments" --ai
cd blog_with_comments
code .  # Opens in Cursor
```

### 2. Cursor Immediately Knows
- Project has Django backend with blog models
- React frontend with blog components
- PostgreSQL database
- Docker development environment
- All available commands and patterns

### 3. Ask Cursor to Add Features
```
"Add a comment system to the blog posts"
```

Cursor generates:
- Django Comment model with proper relationships
- Comment serializer and API endpoints
- React CommentList and CommentForm components
- Proper Tailwind styling
- Database migrations

### 4. Test Changes
```bash
qstack up --build  # Cursor knows this command
```

## 🚀 Benefits

### For Solo Developers
- **Zero context switching** - Cursor understands your project immediately
- **Consistent patterns** - Same approach across all QStack projects
- **Faster development** - AI knows your tech stack and conventions

### For Teams
- **Standardized workflow** - Everyone uses same patterns
- **Easy onboarding** - New team members get instant context
- **Consistent code quality** - AI follows established patterns

### For AI-Assisted Development
- **Native AI integration** - Projects designed for AI tools
- **Comprehensive context** - AI has all information needed
- **Predictable patterns** - AI suggestions are always relevant

## 🔧 Troubleshooting

### Context Not Loading?
```bash
# Regenerate context files
qstack generate-context

# Restart Cursor
# Context files are automatically detected
```

### Want More Detail?
```bash
# Show full project context
qstack ai-context

# Copy output to Cursor for enhanced understanding
```

### Missing Features?
```bash
# Get AI-specific help
qstack ai-help

# Add new features with AI guidance
qstack add-feature "feature description"
```

---

**QStack + Cursor = The Future of AI-Assisted Development** 🚀