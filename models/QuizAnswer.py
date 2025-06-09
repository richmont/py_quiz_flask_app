from typing import List
from sqlalchemy import Integer, String, Float ,ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.Base import Base

class QuizAnswer(Base):
    __tablename__ = "quiz_answer"

    id: Mapped[int] = mapped_column(primary_key=True)
    permission_group: Mapped[int]
    answer_text: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(60))
    allow_multiple_answers: Mapped[bool]
    weight: Mapped[float] = mapped_column(Float)

    quiz_question_id: Mapped[int] = mapped_column(ForeignKey("quiz_question.id"))
    quiz_question = relationship("QuizQuestion",back_populates="quiz_answer")

