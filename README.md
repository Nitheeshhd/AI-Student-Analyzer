# 🎓 AI Student Performance Analyzer & Tutor

## 🚀 Overview
This project is an AI-powered system that analyzes student performance data and provides personalized study recommendations and guidance.

It uses **FastAPI for backend APIs** and **LLaMA 3 (via Ollama)** for intelligent responses, simulating a real AI tutor.

---

## 🔥 Features

- 📊 Student performance analysis across multiple sessions  
- 📚 Subject-wise and chapter-wise insights  
- ⚡ Strength & weakness identification  
- 🤖 AI-powered chatbot (LLaMA 3) for personalized guidance  
- 📅 Smart study plan generation  
- 🌐 Simple frontend UI for interaction  

---

## 🧠 How It Works

1. The system analyzes student attempts and calculates:
   - Average score
   - Subject performance
   - Chapter performance
   - Speed (fast/medium/slow)

2. Based on analysis:
   - Weak areas are identified
   - Recommendations are generated
   - Study plan is created

3. AI chatbot uses this data to provide:
   - Personalized suggestions
   - Improvement strategies
   - Learning guidance

---

## 🛠 Tech Stack

- **Backend:** FastAPI (Python)
- **AI Model:** LLaMA 3 via Ollama (local LLM)
- **Frontend:** HTML, JavaScript
- **Data Processing:** Python

---

## ▶️ How to Run

### 1. Clone the repository
git clone https://github.com/Nitheeshhd/AI-Student-Analyzer.git

cd AI-Student-Analyzer


### 2. Install dependencies

pip install -r requirements.txt


### 3. Run AI model (Ollama)

ollama run llama3


### 4. Run backend server

python -m uvicorn app.main:app --reload


### 5. Open frontend
Open `frontend.html` in your browser

---

## 📡 API Endpoints

### 🔹 Analyze Student

POST /analyze/{student_id}


### 🔹 AI Chatbot

POST /gpt-chat/{student_id}?query=your_question


---

## 💡 Example Usage

- **Student ID:** `001`
- **Query:**  

How can I improve physics?


---

## 🎯 Sample Output

- Weakness: Thermodynamics, Kinematics  
- Speed: Slow  
- AI Suggestion:
  - Focus on concepts
  - Practice numericals
  - Use timer-based solving

---

## 📸 Screenshots

*(Add your frontend screenshot here)*

Example:


---

## 🚀 Key Highlights

- Real-world EdTech use case  
- AI integration using local LLM (no API cost)  
- Clean backend architecture  
- End-to-end system (analysis → AI → UI)

---

## 🔮 Future Improvements

- User authentication system  
- Dashboard with charts  
- Chat history memory  
- Voice-based interaction  

---

## 👨‍💻 Author

**Nitheesh H D**  
- GitHub: https://github.com/Nitheeshhd  
- LinkedIn: (add your link here)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
