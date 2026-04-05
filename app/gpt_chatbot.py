import requests

def gpt_chat(query, analysis):
    prompt = f"""
You are an expert AI tutor.

Student Performance:
{analysis}

Student Question:
{query}

Give:
1. Simple explanation
2. Step-by-step improvement plan
3. Focus on weak areas
4. Keep it short, clear, and motivating
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()