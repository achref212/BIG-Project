from fastapi import FastAPI
from app.routers import (
    auth_router,
    users_router,
    levels_router,
    subjects_router,
    lessons_router,
    quizzes_router,
    stories_router,
    mock_exams_router,
    multiplayer_router,
    badges_router,
    subscriptions_router,
    admin_router,
)

app = FastAPI(
    title="EduApp API",
    version="1.0.0",
    description="Plateforme éducative – Langue Française"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(levels_router)
app.include_router(subjects_router)
app.include_router(lessons_router)
app.include_router(quizzes_router)
app.include_router(stories_router)
app.include_router(mock_exams_router)
app.include_router(multiplayer_router)
app.include_router(badges_router)
app.include_router(subscriptions_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {"status": "API running"}
