from typing import List, Optional
from pydantic import BaseModel, Field
from enum import IntEnum

# Add the Priority as an IntEnum
class Priority(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

# Add the Type: TodoBase
class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description="Name of the todo")
    todo_description: str = Field(..., description="Description of the todo")
    todo_priority: Priority = Field(default=Priority.LOW, description="Priority of the todo")

# Add the Type: TodoCreate
class TodoCreate(TodoBase):
    pass

# Add the Type: Todo
class Todo(TodoBase):
    todo_id: int = Field(..., description="Unique identifier")

# Add the Type: TodoUpdate
class TodoUpdate(TodoBase):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description="Name of the todo")
    todo_description: Optional[str] = Field(None, description="Description of the todo")
    todo_priority: Optional[Priority] = Field(None, description="Priority of the todo")

todo_items = [
    Todo(todo_id=1, todo_name="brush teeth", todo_description="some test about the todo item", todo_priority=Priority.HIGH),
    Todo(todo_id=2, todo_name="take a shower", todo_description="some test about the todo item", todo_priority=Priority.HIGH),
    Todo(todo_id=3, todo_name="wash dishes", todo_description="some test about the todo item", todo_priority=Priority.HIGH)
]