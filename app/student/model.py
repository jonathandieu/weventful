from typing import Optional

from sqlalchemy import Column, event
from sqlalchemy.databases import postgres
from sqlmodel import Field, SQLModel

class StudentBase(SQLModel):
    uuid: int = Field()