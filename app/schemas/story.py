from pydantic import BaseModel

class StoryBase(BaseModel):
    title: str
    summary: str | None = None
    level_id: int
    cover_image_url: str | None = None
    text_html: str | None = None
    audio_url: str | None = None
    estimated_duration: int | None = None

class StoryCreate(StoryBase):
    pass

class StoryUpdate(StoryBase):
    pass

class StoryOut(StoryBase):
    id: int

    class Config:
        orm_mode = True
