from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    [cite_start]return {"message": "Hello World"} [cite: 26]