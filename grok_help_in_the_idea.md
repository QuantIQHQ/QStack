QStack: Full-Stack Project Scaffold for Vibecoders
This is an MVP for qstack, a command-line tool to scaffold a full-stack project with React, Vite, Tailwind CSS 4.0, Django, Docker, and a configurable database. The tool generates a production-ready todo app with clear, AI-readable markdown files for vibecoders to prototype and deploy rapidly.
Project Overview
The qstack startproject {project_name} command creates a project with:

Frontend: React with Vite and Tailwind CSS 4.0 for modern, utility-first styling.
Backend: Django with Django REST Framework for a robust API.
Database: Configurable (PostgreSQL by default, with options for SQLite or MySQL).
Containerization: Docker and Docker Compose for consistent development and deployment.
Documentation: README.md for setup instructions and defineprojectscope.md for AI-assisted development and progress tracking.
Deployment: Ready for platforms like DigitalOcean or Render with GitHub Actions.

Project Structure
The generated project structure for qstack startproject todo is:
todo/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   └── TodoItem.jsx
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── Dockerfile
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
├── backend/
│   ├── todo/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── todo_project/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── manage.py
├── .env
├── .gitignore
├── docker-compose.yml
├── README.md
└── defineprojectscope.md

Setup Instructions
Run the following command to create a new project:
qstack startproject todo
cd todo

Prerequisites

Node.js (v20.19+)
Python (v3.10+)
Docker and Docker Compose
npm or pnpm

Installation

Clone or Generate Project: The qstack startproject todo command generates the structure above.
Environment Setup: Copy .env.example to .env and update variables (e.g., database credentials).
Run Locally:docker-compose up --build


Frontend: http://localhost:5173
Backend: http://localhost:8000/api/todos/


Test Database: Default is PostgreSQL. To switch to SQLite or MySQL, update docker-compose.yml and backend/todo_project/settings.py.

Key Files and Configurations
1. Frontend Setup (React, Vite, Tailwind CSS 4.0)
The frontend is a Vite-based React app with Tailwind CSS 4.0 for styling.
frontend/vite.config.js:
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    port: 5173,
    proxy: {
      '/api': 'http://backend:8000',
    },
  },
});

frontend/tailwind.config.js:
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: { extend: {} },
  plugins: [],
};

frontend/src/index.css:
@import "tailwindcss";

frontend/src/App.jsx:
import { useState, useEffect } from 'react';
import TodoItem from './components/TodoItem';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');

  useEffect(() => {
    fetch('/api/todos/')
      .then((res) => res.json())
      .then((data) => setTodos(data));
  }, []);

  const addTodo = async (e) => {
    e.preventDefault();
    const res = await fetch('/api/todos/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: newTodo, completed: false }),
    });
    const todo = await res.json();
    setTodos([...todos, todo]);
    setNewTodo('');
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
        <h1 className="text-2xl font-bold text-center mb-4">Todo App</h1>
        <form onSubmit={addTodo} className="mb-4">
          <input
            type="text"
            value={newTodo}
            onChange={(e) => setNewTodo(e.target.value)}
            className="w-full p-2 border rounded"
            placeholder="Add a todo"
          />
          <button
            type="submit"
            className="mt-2 w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
          >
            Add Todo
          </button>
        </form>
        <ul>
          {todos.map((todo) => (
            <TodoItem key={todo.id} todo={todo} setTodos={setTodos} />
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;

frontend/src/components/TodoItem.jsx:
import { useState } from 'react';

export default function TodoItem({ todo, setTodos }) {
  const [isCompleted, setIsCompleted] = useState(todo.completed);

  const toggleTodo = async () => {
    const res = await fetch(`/api/todos/${todo.id}/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...todo, completed: !isCompleted }),
    });
    const updatedTodo = await res.json();
    setTodos((prev) =>
      prev.map((t) => (t.id === updatedTodo.id ? updatedTodo : t))
    );
    setIsCompleted(!isCompleted);
  };

  const deleteTodo = async () => {
    await fetch(`/api/todos/${todo.id}/`, { method: 'DELETE' });
    setTodos((prev) => prev.filter((t) => t.id !== todo.id));
  };

  return (
    <li className="flex justify-between items-center p-2 border-b">
      <span
        className={`cursor-pointer ${isCompleted ? 'line-through text-gray-500' : ''}`}
        onClick={toggleTodo}
      >
        {todo.title}
      </span>
      <button
        onClick={deleteTodo}
        className="text-red-500 hover:text-red-700"
      >
        Delete
      </button>
    </li>
  );
}

frontend/Dockerfile:
FROM node:20-alpine AS base
WORKDIR /app
COPY package*.json .
RUN npm install && npm install tailwindcss @tailwindcss/vite
COPY . .
EXPOSE 5173
CMD ["npm", "run", "dev"]

frontend/package.json:
{
  "name": "todo-frontend",
  "version": "0.0.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@tailwindcss/vite": "^4.0.0-alpha.28",
    "@vitejs/plugin-react": "^4.2.1",
    "tailwindcss": "^4.0.0-alpha.28",
    "vite": "^6.1.1"
  }
}

2. Backend Setup (Django)
The backend uses Django with Django REST Framework to provide a REST API for the todo app.
backend/requirements.txt:
Django==5.0.6
djangorestframework==3.15.1
psycopg2-binary==2.9.9

backend/todo_project/settings.py:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'todo',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo_db',
        'USER': 'todo_user',
        'PASSWORD': 'todo_password',
        'HOST': 'db',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

backend/todo/models.py:
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

backend/todo/serializers.py:
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'completed', 'created_at']

backend/todo/views.py:
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

backend/todo/urls.py:
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

backend/todo_project/urls.py:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
]

backend/Dockerfile:
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todo_project.wsgi"]

3. Docker Setup
Docker Compose orchestrates the frontend, backend, and database services.
docker-compose.yml:
version: '3.8'
services:
  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
    volumes:
      - ./frontend:/app
    depends_on:
      - backend
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://todo_user:todo_password@db:5432/todo_db
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=todo_db
      - POSTGRES_USER=todo_user
      - POSTGRES_PASSWORD=todo_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
volumes:
  postgres_data:

4. Environment Configuration
.env.example:
DATABASE_URL=postgresql://todo_user:todo_password@db:5432/todo_db
DJANGO_SECRET_KEY=your-secret-key-here

5. Git Ignore
.gitignore:
node_modules/
__pycache__/
*.pyc
.env
dist/
postgres_data/

6. Documentation for Vibecoders
README.md:
# Todo App

A full-stack todo application built with React, Vite, Tailwind CSS 4.0, Django, and Docker.

## Quick Start
1. Ensure Docker is running.
2. Run `docker-compose up --build`.
3. Access the app at `http://localhost:5173`.
4. API endpoints: `http://localhost:8000/api/todos/`.

## Development
- **Frontend**: Edit files in `frontend/src/`. Vite’s HMR updates the browser instantly.
- **Backend**: Edit models, views, or serializers in `backend/todo/`. Run migrations with `docker-compose exec backend python manage.py migrate`.
- **Database**: Default is PostgreSQL. To switch, update `docker-compose.yml` and `backend/todo_project/settings.py`.

## Deployment
- Build: `docker-compose build`.
- Deploy to DigitalOcean or Render using the `dist` folder from `frontend` and Docker images.

## Progress Tracking
See `defineprojectscope.md` for tasks and implementation status.

defineprojectscope.md:
# Project Scope: Todo App

This document outlines the todo app’s scope and tracks progress for vibecoders. Written in simple English for AI tools like Cursor to interpret and assist.

## Features
1. **List Todos**
   - Description: Display all todos from the API.
   - Status: Implemented ✓
   - Test: Visit `http://localhost:5173` and see todos listed.
2. **Add Todo**
   - Description: Add a new todo via a form.
   - Status: Implemented ✓
   - Test: Enter text in the form and click "Add Todo".
3. **Toggle Todo**
   - Description: Mark todos as completed or not.
   - Status: Implemented ✓
   - Test: Click a todo to toggle its status.
4. **Delete Todo**
   - Description: Remove a todo from the list.
   - Status: Implemented ✓
   - Test: Click "Delete" next to a todo.
5. **Responsive Design**
   - Description: App looks good on mobile and desktop.
   - Status: Implemented ✓
   - Test: Resize browser or view on mobile.

## Next Steps
- Add user authentication.
- Implement todo categories.
- Add due dates for todos.

## Instructions for Vibecoders
- **Track Progress**: Check the "Status" column above. Update to "Tested ✓" after verifying each feature.
- **Extend Features**: Use simple English to describe new features in this file. AI tools can read this and suggest code.
- **Test**: Run `docker-compose up` and follow test instructions above.
- **Ask AI**: Use tools like Cursor to generate code for new features by referencing this file.

Database Flexibility
To change the database:

SQLite: Update backend/todo_project/settings.py:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/db.sqlite3',
    }
}

Remove the db service from docker-compose.yml.
MySQL: Update docker-compose.yml to use mysql:8 and update settings.py:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'todo_db',
        'USER': 'todo_user',
        'PASSWORD': 'todo_password',
        'HOST': 'db',
        'PORT': '3306',
    }
}



Deployment
For automated deployment:

Push to a GitHub repository.
Use a GitHub Action to build and deploy to DigitalOcean App Platform or Render:name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build and push Docker images
        run: |
          docker build -t todo-frontend ./frontend
          docker build -t todo-backend ./backend
          docker push todo-frontend
          docker push todo-backend



Notes for Vibecoders

Simple English: The defineprojectscope.md uses clear language for AI tools to parse and generate code suggestions.
Progress Tracking: Update the status in defineprojectscope.md as you implement and test features.
Extensibility: Add new features to defineprojectscope.md in plain English, and use AI tools to generate code.
Logs: View logs with docker-compose logs to debug issues.
Commands:
qstack startproject {name}: Create a new project.
qstack changedb {sqlite|mysql|postgres}: Update database configuration.



Future Improvements

Add qstack addfeature {feature_name} to generate boilerplate code.
Integrate AI-assisted code generation directly in qstack.
Support additional frameworks (e.g., Vue, Svelte).
