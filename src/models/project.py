from typing import ClassVar
from longlink import Table
from sqlmodel import Field


class Project(Table, table=True):
    """Minimal project table used by the showcase route."""

    __tablename__: ClassVar[str] = "projects"

    id: str = Field(primary_key=True, description="Unique project identifier")
    name: str = Field(description="Project name")
    owner: str = Field(description="Project owner name or ID")
