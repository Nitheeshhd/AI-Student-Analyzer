from app.utils import normalize_marks, load_json
from app.recommender import generate_recommendations
from app.study_plan import generate_study_plan
import os

# Load data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "student_performance.json")

data = load_json(DATA_PATH)


def analyze_student(student_id):

    student_attempts = []

    # Step 1: Find correct student
    for student in data:
        sid = student.get("student_id", "")

        if "_" in sid:
            sid_num = sid.split("_")[1]

            if sid_num == student_id:
                student_attempts = student.get("attempts", [])
                break

    if not student_attempts:
        return {"error": "Student not found"}

    scores = []
    subject_scores = {}
    chapter_scores = {}

    total_time = 0
    total_questions = 0

    # Step 2: Loop through attempts
    for attempt in student_attempts:

        marks = normalize_marks(attempt.get("marks", 0))
        scores.append(marks)

        subject = attempt.get("subject", "Unknown")
        chapters = attempt.get("chapters", [])

        subject_scores.setdefault(subject, []).append(marks)

        for ch in chapters:
            chapter_scores.setdefault(ch, []).append(marks)

        total_time += attempt.get("time_taken_minutes", 0) or 0
        total_questions += attempt.get("attempted", 0) or 0

    avg_score = sum(scores) / len(scores) if scores else 0

    subject_avg = {
        k: sum(v)/len(v) if v else 0
        for k, v in subject_scores.items()
    }

    chapter_avg = {
        k: sum(v)/len(v) if v else 0
        for k, v in chapter_scores.items()
    }

    strengths = [k for k, v in chapter_avg.items() if v >= 70]
    weaknesses = [k for k, v in chapter_avg.items() if v < 40]

    avg_time_per_q = total_time / total_questions if total_questions else 0

    if avg_time_per_q > 2:
        speed = "slow"
    elif avg_time_per_q > 1:
        speed = "medium"
    else:
        speed = "fast"

    # ✅ MUST BE INSIDE FUNCTION
    analysis_result = {
        "avg_score": round(avg_score, 2),
        "subject_performance": subject_avg,
        "chapter_performance": chapter_avg,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "speed": speed
    }

    # ✅ ADD RECOMMENDATIONS
    analysis_result["recommendations"] = generate_recommendations(analysis_result)
    analysis_result["study_plan"] = generate_study_plan(analysis_result)

    return analysis_result