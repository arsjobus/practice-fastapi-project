from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import IntEnum

class Priority(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=255, description="Name of the todo list item.")
    todo_description: str = Field(..., description="Description of the todo list item.")
    todo_priority: Priority = Field(default=Priority.MEDIUM, description="Priority of the todo list item.")

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description="Unique Identifier")

class TodoUpdate(TodoBase):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=255, description="Name of the todo list item.")
    todo_description: Optional[str] = Field(None, description="Description of the todo list item.")
    todo_priority: Optional[Priority] = Field(None, description="Priority of the todo list item.")

todo_items: List[Todo] = [
    Todo(todo_id=1, todo_name="Brush my teeth", todo_description="Brush my teeth in the morning", todo_priority=Priority.HIGH),
    Todo(todo_id=2, todo_name="Vacuum carpet", todo_description="Vacuum the living room rug.", todo_priority=Priority.MEDIUM),
    Todo(todo_id=3, todo_name="Play video games", todo_description="Play video games or use free time", todo_priority=Priority.LOW)
]

api = FastAPI()

@api.get("/")
def api_root():
    return { "API" : "/" }

@api.get("/todo-items")
def list_todo_items(limit: int = 10):
    return { "result": todo_items[:limit] }

@api.get("/todo-items/{todo_id}")
def read_todo_items(todo_id: int):
    for index, todo in enumerate(todo_items):
        if todo.todo_id == todo_id:
            return { "result": todo_items[index] }
    raise HTTPException(status_code=404, detail="Todo not found")

@api.post("/todo-items")
def create_todo_item(todo: TodoCreate):
    todo_index = max((t.todo_id for t in todo_items), default = 1) + 1
    new_todo_item = Todo(
        todo_id = todo_index,
        todo_name = todo.todo_name,
        todo_description = todo.todo_description,
        todo_priority = todo.todo_priority
    )
    todo_items.append(new_todo_item)
    return { "result": new_todo_item }

@api.put("/todo-items/{todo_id}")
def update_todo_item(todo_id: int, updated_todo: TodoUpdate):
    for todo in todo_items:
        if todo.todo_id == todo_id:
            todo.todo_name = updated_todo.todo_name or todo.todo_name
            todo.todo_description = updated_todo.todo_description or todo.todo_description
            todo.todo_priority = updated_todo.todo_priority or todo.todo_priority
            return { "result": todo }
    raise HTTPException(status_code=404, detail="Todo not found")

@api.delete("/todo-items/{todo_id}")
def delete_todo_item(todo_id: int):
    for index, todo in enumerate(todo_items):
        if todo.todo_id == todo_id:
            delete_todo = todo_items.pop(index)
            return delete_todo
    raise HTTPException(status_code=404, detail="Todo not found")