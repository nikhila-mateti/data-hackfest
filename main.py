from fastapi import FastAPI

app = FastAPI()

@app.get("/chat")
def getChat():
    return {"response": "Hello World"}