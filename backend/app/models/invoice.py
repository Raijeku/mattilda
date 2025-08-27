from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.student import Student

class Invoice(SQLModel, table=True):
    __tablename__ = "invoices"

    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float

    student_id: int = Field(foreign_key="students.id")
    student: "Student" = Relationship(back_populates="invoices")