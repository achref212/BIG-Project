from pydantic import BaseModel

class MockExamBase(BaseModel):
    title: str
    description: str | None = None
    level_id: int

class MockExamCreate(MockExamBase):
    pass

class MockExamUpdate(MockExamBase):
    pass

class MockExamOut(MockExamBase):
    id: int

    class Config:
        orm_mode = True
