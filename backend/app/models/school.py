from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.student import Student

class School(SQLModel, table=True):
    __tablename__ = "schools"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    students: List["Student"] = Relationship(back_populates="school")