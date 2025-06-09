from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.Base import Base

class QuizQuestion(Base):
    __tablename__ = "quiz_question"

    id: Mapped[int] = mapped_column(primary_key=True)
    permission_group: Mapped[int]
    question_text: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(60))
    allow_multiple_answers: Mapped[bool]

    quiz_id: Mapped[int] = mapped_column(ForeignKey("quiz.id"))
    quiz = relationship("Quiz",back_populates="quiz_question")
