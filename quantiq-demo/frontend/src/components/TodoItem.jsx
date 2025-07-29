import { useState } from 'react'

export default function TodoItem({ todo, setTodos }) {
  const [isUpdating, setIsUpdating] = useState(false)

  const toggleTodo = async () => {
    if (isUpdating) return
    setIsUpdating(true)

    try {
      const response = await fetch(`/api/todos/${todo.id}/`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          ...todo, 
          completed: !todo.completed 
        }),
      })

      if (response.ok) {
        const updatedTodo = await response.json()
        setTodos((prev) =>
          prev.map((t) => (t.id === updatedTodo.id ? updatedTodo : t))
        )
      }
    } catch (error) {
      console.error('Error updating todo:', error)
    } finally {
      setIsUpdating(false)
    }
  }

  const deleteTodo = async () => {
    if (isUpdating) return
    setIsUpdating(true)

    try {
      const response = await fetch(`/api/todos/${todo.id}/`, { 
        method: 'DELETE' 
      })

      if (response.ok) {
        setTodos((prev) => prev.filter((t) => t.id !== todo.id))
      }
    } catch (error) {
      console.error('Error deleting todo:', error)
      setIsUpdating(false)
    }
  }

  return (
    <div className="flex items-center justify-between p-3 border border-gray-200 rounded-md hover:bg-gray-50">
      <div className="flex items-center space-x-3">
        <input
          type="checkbox"
          checked={todo.completed}
          onChange={toggleTodo}
          disabled={isUpdating}
          className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
        />
        <span
          className={`${
            todo.completed 
              ? 'line-through text-gray-500' 
              : 'text-gray-900'
          } ${isUpdating ? 'opacity-50' : ''}`}
        >
          {todo.title}
        </span>
      </div>
      
      <button
        onClick={deleteTodo}
        disabled={isUpdating}
        className="text-red-500 hover:text-red-700 focus:outline-none disabled:opacity-50"
      >
        <svg 
          className="h-4 w-4" 
          fill="none" 
          stroke="currentColor" 
          viewBox="0 0 24 24"
        >
          <path 
            strokeLinecap="round" 
            strokeLinejoin="round" 
            strokeWidth={2} 
            d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" 
          />
        </svg>
      </button>
    </div>
  )
}