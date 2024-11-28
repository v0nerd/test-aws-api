from fastapi import FastAPI
from utils.run_doc import get_value
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def hello():
    return "Hello World from FastAPI and AppRunner!"

@app.get("/test")
async def test():
    return get_value("test")

# To run the app, use the command: uvicorn app:app --host 0.0.0.0 --port 8001

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)