from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.invoice import Invoice
    from models.school import School

class Student(SQLModel, table=True):
    __tablename__ = "students"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    school_id: int = Field(foreign_key="schools.id")
    school: "School" = Relationship(back_populates="students")

    invoices: List["Invoice"] = Relationship(back_populates="student")