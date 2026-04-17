from fastapi import FastAPI
from app.gpt_service import ask_gpt

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI API Running"}

@app.post("/chat")
def chat(prompt: str):
    response = ask_gpt(prompt)
    return {"response": response}