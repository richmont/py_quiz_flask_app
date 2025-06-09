from typing import List
from sqlalchemy import Integer, String, ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.Base import Base



class Quiz(Base):
    __tablename__ = "quiz"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(60))
    permission_group: Mapped[int]
    quiz_question: Mapped[List["QuizQuestion"]] = relationship(back_populates="quiz")