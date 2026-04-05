def student_chatbot(query, analysis):

    query = query.lower()

    weaknesses = analysis.get("weaknesses", [])
    strengths = analysis.get("strengths", [])
    speed = analysis.get("speed")

    # Weakness related
    for topic in weaknesses:
        if topic.lower() in query:
            return f"You are weak in {topic}. Focus on concepts, solve basic to advanced problems, and revise daily."

    # Strength related
    for topic in strengths:
        if topic.lower() in query:
            return f"{topic} is your strength. Keep practicing to maintain it."

    # Speed related
    if "speed" in query or "time" in query:
        if speed == "slow":
            return "You are slow. Practice with a timer and avoid overthinking."
        elif speed == "medium":
            return "You have average speed. Try timed practice sets."
        else:
            return "Your speed is good. Maintain consistency."

    # General help
    return "Focus on weak areas, practice daily, and revise concepts regularly."