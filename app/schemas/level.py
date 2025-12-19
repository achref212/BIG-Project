from pydantic import BaseModel

class LevelBase(BaseModel):
    name: str
    code: str
    order_index: int

class LevelCreate(LevelBase):
    pass

class LevelUpdate(LevelBase):
    pass

class LevelOut(LevelBase):
    id: int

    class Config:
        orm_mode = True
