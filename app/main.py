from fastapi import FastAPI
from app.analyzer import analyze_student
from app.chatbot import student_chatbot
from app.analyzer import analyze_student
from app.gpt_chatbot import gpt_chat

app = FastAPI()

@app.post("/analyze/{student_id}")
def analyze(student_id: str):
    return analyze_student(student_id)

@app.post("/chat/{student_id}")
def chat(student_id: str, query: str):
    analysis = analyze_student(student_id)
    return {
        "response": student_chatbot(query, analysis)
    }

@app.post("/gpt-chat/{student_id}")
def gpt_chat_api(student_id: str, query: str):
    analysis = analyze_student(student_id)
    response = gpt_chat(query, analysis)

    return {
        "response": response
    }
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)