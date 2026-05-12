from fastapi import FastAPI
import uvicorn

from app.tasks.router import router as tasks_router

app = FastAPI()
app.include_router(tasks_router)

@app.get("/")
async def app_running(): 
    return {"Server": "Is Running!"}

if __name__ == "__main__": 
    uvicorn.run("app.main:app", port=8000)
