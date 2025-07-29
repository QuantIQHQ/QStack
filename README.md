# 🚀 QStack - Fullstack Generator by QuantIQ

**QStack** is a modern CLI tool by QuantIQ that generates production-ready fullstack applications in seconds. Perfect for vibecoders who want to build fast with AI assistance!

## ✨ What Makes QStack Special

- **🤖 AI-Powered**: Generate projects from natural language with Claude Pro integration
- **🎯 Vibe-first**: Designed for AI-assisted development with English-readable documentation
- **⚡ Modern Stack**: React + Vite + Tailwind CSS 4.0 + Django + Docker
- **🎨 Beautiful CLI**: Stunning ASCII banner and Metasploit-inspired interface
- **🐳 Docker Smart**: Auto-detects `docker compose` vs `docker-compose` for compatibility
- **🚀 QStack Commands**: Clean command structure - `qstack up`, `qstack build`, `qstack logs`
- **📊 Database Smart**: PostgreSQL by default, MySQL or SQLite options available
- **📝 AI-Friendly Docs**: Auto-generated `defineprojectscope.md` for seamless AI context
- **🔐 Security First**: Auto-generated Django secret keys for each project

## 🚀 Quick Start

### Installation
```bash
# Clone and install
git clone <your-repo>
cd QStack
python3 -m venv qstack-venv
source qstack-venv/bin/activate
pip install -e .
```

### Create Your First Project

**Traditional Way:**
```bash
qstack startproject mytodo
cd mytodo
qstack up --build
# Open http://localhost:5173 🎉
```

**🤖 AI-Powered Way:**
```bash
# Just describe what you want in natural language!
qstack startproject "a todo app with user auth, categories, and due dates" --ai

cd todo_app_with_user_auth_categories_and_due_dates
qstack up --build
# Open http://localhost:5173 🎉
```

> **Note**: AI mode requires Claude Pro API key. Set `ANTHROPIC_API_KEY` environment variable. [Get your key here](https://console.anthropic.com/)

## 🎨 CLI Experience

QStack features a beautiful, Metasploit-inspired CLI with stunning ASCII art:

```
 ██████╗ ███████╗████████╗ █████╗  ██████╗██╗  ██╗
██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
██║   ██║███████╗   ██║   ███████║██║     █████╔╝ 
██║▄▄ ██║╚════██║   ██║   ██╔══██║██║     ██╔═██╗ 
╚██████╔╝███████║   ██║   ██║  ██║╚██████╗██║  ██╗
 ╚══▀▀═╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                    (c) QuantIQ
    Modern Fullstack Generator for Vibecoders
```

**Smart Docker Detection**: Automatically detects whether your system uses `docker compose` (newer) or `docker-compose` (legacy) and adapts accordingly.

## 🛠 Commands

### `qstack startproject <name>` 

Create a new fullstack project with everything wired:
- **Frontend**: React + Vite + Tailwind CSS 4.0
- **Backend**: Django + REST Framework
- **Database**: PostgreSQL (default), MySQL/SQLite options
- **Docker**: Full containerization
- **Documentation**: AI-readable project scope

**Traditional Usage:**
```bash
qstack startproject myapp --database postgres
qstack startproject api-only --template api-only --database mysql
qstack startproject frontend-only --template frontend-only
```

**🤖 AI-Powered Usage:**
```bash
qstack startproject "a social media app with posts, likes, and comments" --ai
qstack startproject "an e-commerce store with products and shopping cart" --ai
qstack startproject "a project management tool with teams and tasks" --ai
```

**AI Features:**
- 🧠 Analyzes natural language requirements
- 🏗️ Generates custom Django models and React components  
- 📦 Suggests appropriate packages and dependencies
- 📋 Creates detailed AI analysis documentation
- 🎯 Smart database selection based on complexity

### `qstack up`
Start your QStack application (replaces docker-compose up):
```bash
qstack up --build          # Start with build
qstack up --detach         # Run in background
```

### `qstack down`
Stop your QStack application (replaces docker-compose down):
```bash
qstack down                # Stop application
qstack down --volumes      # Stop and remove volumes
```

### `qstack logs`
View application logs (replaces docker-compose logs):
```bash
qstack logs                # View all logs
qstack logs --follow       # Follow log output
qstack logs --service frontend  # View specific service logs
qstack logs --tail 100     # Show last 100 log lines
```

### `qstack build`
Prepare for production deployment:
```bash
qstack build --clean       # Build and clean dev files
qstack build --no-cache    # Build without cache
```

### `qstack status`
Track project progress with AI-readable status:
```bash
qstack status
# Shows:
# ✅ Todo List Display - Implemented
# ✅ Add New Todo - Implemented
# ⏳ User Authentication - Pending
```

## 🎯 Perfect For

### Vibecoders
- **English-first development** with `defineprojectscope.md`
- **AI tool integration** (Cursor, ChatGPT, Claude)
- **Modern stack** that AI understands
- **Instant prototyping** from ideas

### Indie Hackers
- **Speed to market** - working app in minutes
- **Production ready** with Docker
- **Deployment optimized** for modern platforms
- **Cost effective** with efficient resource usage

### Teams
- **Consistent architecture** across projects
- **Standardized patterns** for easy collaboration
- **Scalable foundation** for growing applications
- **AI-assisted development** workflows

## 🏗 Generated Project Structure

```
myproject/
├── frontend/              # React + Vite + Tailwind CSS 4.0
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
├── backend/               # Django + REST Framework
│   ├── myproject_project/
│   ├── todos/            # Sample app
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml    # Full stack orchestration
├── README.md            # Setup and usage guide
├── defineprojectscope.md # AI-readable project context
└── .env.example         # Environment configuration
```

## 🤖 AI-Assisted Development

QStack projects are optimized for AI tools:

### English-First Documentation
The `defineprojectscope.md` file uses simple English that AI tools can easily parse:

```markdown
## Next Steps
- Add user authentication
- Implement todo categories  
- Add due dates for todos

## Instructions for AI
Use simple English to describe new features.
Update status when implementing features.
```

### Modern Stack Recognition
AI tools work best with:
- ✅ React hooks and modern patterns
- ✅ Tailwind CSS utility classes
- ✅ Django REST Framework
- ✅ Docker containerization

### Consistent Patterns
- Clear file organization
- Predictable naming conventions
- Standard project structure
- Well-commented configuration

## 🔧 Customization

### Template Options
- `fullstack` (default): Frontend + Backend + Database
- `frontend-only`: React + Vite + Tailwind only
- `api-only`: Django + Database only

### Database Options
- `postgres` (default): PostgreSQL 15 - Production ready, full-featured
- `mysql`: MySQL 8 - Alternative relational database
- `sqlite`: Lightweight SQLite - Perfect for development and small apps

### Environment Variables
Copy `.env.example` to `.env` and customize:
```bash
DEBUG=True
DJANGO_SECRET_KEY=your-secret-key
DB_HOST=db
DB_NAME=myproject_db
```

## 🚀 Deployment Ready

Generated projects work out-of-the-box with:

- **DigitalOcean App Platform**
- **AWS ECS/Fargate**
- **Google Cloud Run**
- **Railway**
- **Render**
- **Vercel** (frontend)

## 📈 Roadmap

### Phase 1 (Current)
- ✅ Basic project generation
- ✅ Multiple database support
- ✅ AI-friendly documentation
- ✅ Docker containerization

### Phase 2 (Coming Soon)
- [ ] Template marketplace
- [ ] One-click deployment
- [ ] GitHub integration
- [ ] Custom templates

### Phase 3 (Future)
- [ ] AI-powered feature generation
- [ ] Real-time collaboration
- [ ] VSCode extension
- [ ] Web UI dashboard

## 🌟 Why QStack Will Trend

### The Vibe Economy is Here
- AI coding assistants are mainstream
- Developers need AI-readable projects
- Speed matters more than ever
- English-driven development is the future

### Technical Advantages
- Modern stack with latest tools
- Production-ready from day one
- Consistent, predictable patterns
- Extensible and customizable

### Market Timing
- Perfect intersection of AI + web development
- Addresses real pain points
- Built for the next generation of developers
- Scales from solo projects to teams

---

**QStack by QuantIQ - Built for vibecoders who love to ship fast** 🚀

## 🏢 About QuantIQ

QuantIQ is a developer tools startup focused on making fullstack development faster and more accessible. We believe in:

- **English-first development** - Code should be readable by humans and AI
- **Modern stack adoption** - Use the best tools available today
- **AI-assisted workflows** - Leverage AI to ship faster
- **Open source respect** - Give credit where credit is due

**Our Mission**: Empower the next generation of vibecoders to build and deploy applications at the speed of thought.

*Website: [QuantIQ.co.ke](https://quantiq.co.ke) (coming soon)*  
*Email: quants@quantiq.co.ke*  
*Twitter: [@QuantIQDevs](https://twitter.com/quantiqhq)*