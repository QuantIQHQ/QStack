# 🧠 QStack AI Context Examples

## 📋 Sample `.qstack-context.md` Files

### Example 1: Traditional Fullstack Project

```markdown
# 🚀 MyTodoApp - QStack Project Context

> **AI-Readable Project Documentation** - Everything an AI needs to understand this project

## 📋 Project Metadata
- **Project Name**: `MyTodoApp`
- **Type**: `fullstack`
- **Database**: `postgres`
- **Generated**: `2024-01-15T10:30:00Z`
- **QStack Version**: `0.1.0`

## 🏗️ Architecture Overview
```
MyTodoApp/
├── frontend/              # React + Vite + Tailwind CSS 4.0
│   ├── src/
│   │   ├── App.jsx        # Main application component
│   │   ├── components/    # Reusable UI components
│   │   └── main.jsx       # Application entry point
│   ├── package.json       # Frontend dependencies
│   └── Dockerfile         # Frontend container config
├── backend/               # Django + REST Framework
│   ├── mytodoapp_project/ # Django project settings
│   ├── todos/             # Main Django app
│   │   ├── models.py      # Database models
│   │   ├── views.py       # API endpoints
│   │   └── serializers.py # Data serialization
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Backend container config
├── docker-compose.yml     # Multi-container orchestration
├── README.md              # Human-readable documentation
├── defineprojectscope.md  # AI-friendly project scope
└── .qstack-context.md     # THIS FILE - AI project context
```

## 🔧 Tech Stack Encoding
**Frontend Framework**: React 18.2+ with modern hooks pattern
**Build Tool**: Vite 4+ for fast HMR and building
**Styling**: Tailwind CSS 4.0 with utility-first approach
**Package Manager**: npm (check package.json for exact versions)

**Backend Framework**: Django 4.2+ with REST Framework
**Database**: Postgres 15+
**API Style**: RESTful API with DRF serializers
**Authentication**: Django's built-in auth system

**Containerization**: Docker + docker-compose
**Development Ports**: 
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- Database: localhost:5432

## 📊 Database Schema Quick Reference
```python
# Primary Models (check backend/mytodoapp/models.py for full definitions)
Todo:
  - title: CharField(max_length=200)
  - description: TextField 
  - is_completed: BooleanField
  - created_at: DateTimeField
  - updated_at: DateTimeField
```

## 🎨 Frontend Component Architecture
```jsx
// Component Hierarchy (check frontend/src/components/)
App.jsx                    // Root application component
├── TodoList.jsx          // Main todo display component
├── TodoItem.jsx          // Individual todo item
├── TodoForm.jsx          // Add/edit todo form
└── Layout/               // Common layout components
    ├── Header.jsx
    └── Footer.jsx
```

## 🛠️ Development Commands

### Quick Start
```bash
cd MyTodoApp
qstack up --build          # Start all services with build
```

### QStack Commands
```bash
qstack up                  # Start development environment
qstack down                # Stop all services
qstack logs                # View application logs
qstack status              # Check feature implementation status
```

## 🤖 AI Assistant Instructions

When working on this MyTodoApp project:

1. **Always Reference This File**: Check `.qstack-context.md` first for project understanding
2. **Follow QStack Patterns**: Use established conventions from similar QStack projects
3. **Use Predefined Commands**: Stick to the commands listed above
4. **Update Context**: When adding features, update this file accordingly

### Code Patterns to Follow
**React Components**:
- Functional components with hooks
- Props destructuring in function parameters
- Tailwind for all styling

**Django Models**:
- Include `created_at` and `updated_at` fields
- Use descriptive `verbose_name` in Meta class
- Implement `__str__` method for admin display
```

---

### Example 2: AI-Generated Social Media App

```markdown
# 🚀 social_media_app_with_posts_and_likes - QStack Project Context

> **AI-Readable Project Documentation** - Everything an AI needs to understand this project

## 📋 Project Metadata
- **Project Name**: `social_media_app_with_posts_and_likes`
- **Type**: `fullstack`
- **Database**: `postgres`
- **Generated**: `2024-01-15T14:22:33Z`
- **QStack Version**: `0.1.0`
- **AI Generated**: ✅ Claude-powered
- **Original Description**: "a social media app with posts and likes"

## 🤖 AI-Detected Features

### User Management
**Description**: User registration, authentication, and profile management
**Models**: User, UserProfile
**Components**: LoginForm, SignupForm, ProfileCard
**API Endpoints**: /api/auth/, /api/profile/

### Post System
**Description**: Create, read, update, delete posts with rich content
**Models**: Post, PostImage
**Components**: PostList, PostCard, CreatePost
**API Endpoints**: /api/posts/, /api/posts/{id}/

### Like System
**Description**: Like and unlike posts with real-time counts
**Models**: Like
**Components**: LikeButton, LikeCount
**API Endpoints**: /api/posts/{id}/like/

## 📊 Database Schema Quick Reference
```python
# AI-Generated Models (check backend/social_media_app_with_posts_and_likes/models.py)
User:
  - username: CharField(max_length=150, unique=True)
  - email: EmailField(unique=True)
  - first_name: CharField(max_length=30)
  - last_name: CharField(max_length=30)
  - is_active: BooleanField(default=True)
  - created_at: DateTimeField(auto_now_add=True)
  - updated_at: DateTimeField(auto_now=True)

Post:
  - title: CharField(max_length=200)
  - description: TextField(blank=True)
  - is_completed: BooleanField(default=False)
  - due_date: DateTimeField(null=True, blank=True)
  - created_at: DateTimeField(auto_now_add=True)
  - updated_at: DateTimeField(auto_now=True)

Like:
  - name: CharField(max_length=100)
  - description: TextField(blank=True)
  - created_at: DateTimeField(auto_now_add=True)
  - updated_at: DateTimeField(auto_now=True)
```

**Relationships**: 
- All models include `created_at` and `updated_at` timestamps
- Foreign keys follow Django naming: `model_id` or `model`
- Post belongs to User (author)
- Like connects User and Post (many-to-many through table)

## 🎨 Frontend Component Architecture
```jsx
// AI-Generated Components (check frontend/src/components/)
App.jsx                    // Root application component
├── PostList.jsx          // Main post display component
├── PostCard.jsx          // Individual post display
├── CreatePost.jsx        // Post creation form
├── LikeButton.jsx        // Like/unlike functionality
├── UserProfile.jsx       // User profile display
└── Layout/               // Common layout components
    ├── Header.jsx
    └── Footer.jsx
```

## 🤖 AI Features:
- Custom models generated based on your requirements
- React components tailored to your features
- AI analysis documentation in AI_ANALYSIS.md

## 🔄 Auto-Generated Files
**This project was AI-generated**. The following files contain AI-generated code:
- `AI_ANALYSIS.md` - Detailed AI analysis and feature breakdown
- `backend/social_media_app_with_posts_and_likes/models.py` - Custom Django models
- `frontend/src/components/PostList.jsx` - AI-generated component
- `frontend/src/components/CreatePost.jsx` - AI-generated component
- `frontend/src/components/LikeButton.jsx` - AI-generated component
```

---

### Example 3: Frontend-Only Project

```markdown
# 🚀 ReactDashboard - QStack Project Context

## 📋 Project Metadata
- **Project Name**: `ReactDashboard`
- **Type**: `frontend-only`
- **Generated**: `2024-01-15T16:45:12Z`
- **QStack Version**: `0.1.0`

## 🏗️ Architecture Overview
```
ReactDashboard/
├── src/
│   ├── App.jsx            # Main application component
│   ├── components/        # Reusable UI components
│   └── main.jsx           # Application entry point
├── package.json           # Dependencies and scripts
├── vite.config.js         # Vite configuration
├── README.md              # Human-readable documentation
├── defineprojectscope.md  # AI-friendly project scope
└── .qstack-context.md     # THIS FILE - AI project context
```

## 🔧 Tech Stack Encoding
**Frontend Framework**: React 18.2+ with modern hooks pattern
**Build Tool**: Vite 4+ for fast HMR and building
**Styling**: Tailwind CSS 4.0 with utility-first approach
**Package Manager**: npm

## 🛠️ Development Commands

### Quick Start
```bash
cd ReactDashboard
npm install                # Install dependencies
npm run dev                # Start development server
```

### Available Scripts
```bash
npm run dev                # Start dev server (http://localhost:5173)
npm run build             # Build for production
npm run preview           # Preview production build
```

## 🤖 AI Assistant Instructions

When working on this ReactDashboard project:

1. **Frontend-Only Focus**: This is a React-only project with no backend
2. **Vite Development**: Use `npm run dev` for development
3. **Tailwind Styling**: All components use Tailwind CSS utility classes
4. **Component Patterns**: Functional components with hooks only

### Code Patterns to Follow
**React Components**:
- Functional components with hooks
- Props destructuring in function parameters
- Tailwind for all styling
- JSX with semantic HTML elements

```jsx
const ComponentName = ({ prop1, prop2 }) => {
  const [state, setState] = useState(initialValue);
  
  return (
    <div className="p-4 bg-white rounded-lg shadow">
      {/* Component content */}
    </div>
  );
};
```
```

---

## 📱 Sample `.cursor-context` Files

### For Fullstack Project
```markdown
# Cursor AI Context for MyTodoApp

## Quick Start
This is a QStack-generated fullstack application.

### Development Commands
- `qstack up --build` - Start development environment
- `qstack logs --follow` - View application logs
- `qstack status` - Check implementation status

### Key Files
- `frontend/src/App.jsx` - Main React application
- `backend/mytodoapp_project/settings.py` - Django settings
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

### For Frontend-Only Project
```markdown
# Cursor AI Context for ReactDashboard

## Quick Start
This is a QStack-generated frontend-only application.

### Development Commands
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

### Key Files
- `src/App.jsx` - Main React application
- `package.json` - Dependencies and scripts
- `vite.config.js` - Build configuration

### Architecture
- **Type**: frontend-only
- **Generated**: 2024-01-15

### Code Patterns
- React: Functional components with hooks
- Styling: Tailwind CSS utility classes
- State: useState and useEffect hooks

For full context, see .qstack-context.md
```

---

## 🎯 Using Context in AI Tools

### With Cursor IDE
1. **Automatic**: Cursor reads `.cursor-context` automatically when you open the project
2. **Enhanced**: Copy `.qstack-context.md` content for deeper understanding

### With Claude/ChatGPT
```bash
# Get context to copy
qstack ai-context

# Or read file directly
cat .qstack-context.md
```

Then paste into your AI conversation for full project understanding.

### Context Commands
```bash
qstack ai-context                    # Show full context
qstack ai-context --format=quick    # Show condensed version
qstack ai-context --format=structure # Show only project structure
qstack generate-context             # Regenerate context files
```

---

**These examples show how QStack creates comprehensive, AI-readable documentation that makes any project instantly understandable to AI tools!** 🧠✨