from fastapi import FastAPI
import uvicorn

from app.tasks.router import router as tasks_router
from app.users.router import router as users_router 
from app.projects.router import router as project_router

app = FastAPI(lifespan=lifespan)


app.include_router(tasks_router)
app.include_router(users_router)
app.include_router(projet_router)

@app.get("/")
async def app_running(): 
    return {"Server": "Is Running!"}

if __name__ == "__main__": 
    uvicorn.run("app.main:app", port=8000)
