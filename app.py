from fastapi import FastAPI
from utils.run_doc import get_value
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/test")
async def test():
    return get_value("test")

# To run the app, use the command: uvicorn app:app --host 0.0.0.0 --port 8001

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)