# QuantiqTodo

A modern fullstack todo application built with QStack by QuantIQ, featuring React, Vite, Tailwind CSS 4.0, Django, and Docker.

## 🚀 Quick Start

1. **Prerequisites**
   - Docker and Docker Compose
   - Git (optional)

2. **Run the Application**
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000/api/todos/
   - Database: localhost:5432
   

## 🛠 Development

### Frontend (React + Vite + Tailwind CSS 4.0)
- Located in `frontend/` directory
- Hot module replacement enabled
- Tailwind CSS 4.0 with modern utility classes
- Proxy API calls to backend

### Backend (Django + REST Framework)
- Located in `backend/` directory
- Django REST Framework for API
- PostgreSQL database
- CORS enabled for frontend

### Database
- **PostgreSQL 15**
- Database: `quantiq_todo_db`
- User: `quantiq_todo_user`
- Access via: `docker-compose exec db psql -U quantiq_todo_user -d quantiq_todo_db`


## 📝 Common Commands

### Development
```bash
# Start all services
docker-compose up

# Rebuild and start
docker-compose up --build

# Run backend migrations
docker-compose exec backend python manage.py migrate

# Create Django superuser
docker-compose exec backend python manage.py createsuperuser

# Install new frontend dependencies
docker-compose exec frontend npm install <package-name>

# View logs
docker-compose logs frontend
docker-compose logs backend
```

### Production
```bash
# Build for production
qstack build --clean

# Generate environment file
cp .env.example .env
# Edit .env with production values
```

## 🎯 Features

- ✅ Todo CRUD operations
- ✅ Responsive design with Tailwind CSS 4.0
- ✅ Real-time updates
- ✅ Docker containerization
- ✅ Database integration
- ✅ REST API
- ✅ Development hot-reload

## 🔧 Customization

### Adding New Features
1. Update `defineprojectscope.md` with feature description
2. Use AI tools (Cursor, ChatGPT) to generate code
3. Test the feature
4. Update the status in `defineprojectscope.md`

### Changing Database
To switch databases, update `docker-compose.yml` and `backend/quantiq_todo_project/settings.py`.


### Environment Variables
Copy `.env.example` to `.env` and customize:
- `DEBUG`: Development/Production mode
- `DJANGO_SECRET_KEY`: Django secret key
- `DB_*`: Database connection settings


## 📚 Documentation

- **Project Scope**: See `defineprojectscope.md` for features and progress
- **API Documentation**: Visit http://localhost:8000/api/ for interactive API docs
- **Frontend Components**: Located in `frontend/src/components/`

## 🚀 Deployment

### Using Docker
1. Build production images
2. Set environment variables
3. Deploy to your hosting platform (DigitalOcean, AWS, etc.)

### Environment Setup
- Set `DEBUG=False` in production
- Configure `ALLOWED_HOSTS`
- Use secure `DJANGO_SECRET_KEY`
- Configure production database credentials


## 🤖 AI-Friendly Development

This project is optimized for AI-assisted development:

- **English-first documentation** in `defineprojectscope.md`
- **Clear project structure** for easy AI navigation
- **Modern stack** that AI tools understand well
- **Simple conventions** for consistent code generation

Use tools like Cursor, ChatGPT, or Claude to:
- Generate new features
- Debug issues
- Add tests
- Optimize performance

---

*Generated with ❤️ by QStack - Powered by QuantIQ Devs*

## 🏢 About QuantIQ
QuantIQ builds developer tools that make fullstack development faster and more enjoyable. QStack is our flagship tool for vibecoders who want to ship fast with AI assistance.

**Tech Stack Credits:**
- ⚛️ **React** - A JavaScript library for building user interfaces
- ⚡ **Vite** - Next generation frontend tooling  
- 🎨 **Tailwind CSS** - A utility-first CSS framework
- 🐍 **Django** - The web framework for perfectionists with deadlines
- 🐳 **Docker** - Containerization platform