from fastapi import FastAPI
import uvicorn



app = FastAPI()

@app.get("/")
async def app_running(): 
    return {"Server": "Is Running!"}

if __name__ == "__main__": 
    uvicorn.run("app.main:app", port=8000)