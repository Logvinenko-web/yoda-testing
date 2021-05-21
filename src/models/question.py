from pydantic import BaseModel


class BaseQuestion(BaseModel):
    pass

class QuestionCreate(BaseQuestion):
    text_question: str

class Question(BaseQuestion):
    id: int

    class Config:
        orm_mode = True


