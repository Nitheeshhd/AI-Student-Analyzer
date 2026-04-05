def generate_study_plan(analysis):

    plan = {}

    weaknesses = analysis.get("weaknesses", [])
    speed = analysis.get("speed")

    day = 1

    # Cover weaknesses first
    for topic in weaknesses:
        plan[f"Day {day}"] = [
            f"Revise concepts of {topic}",
            f"Practice 20 MCQs from {topic}",
            "Analyze mistakes"
        ]
        day += 1

    # Add general improvement days
    plan[f"Day {day}"] = [
        "Mixed practice (Physics + Chemistry)",
        "Focus on weak areas",
        "Revise formulas"
    ]
    day += 1

    # Speed improvement day
    if speed == "slow":
        plan[f"Day {day}"] = [
            "Solve questions with timer",
            "Try to reduce time per question",
            "Avoid overthinking"
        ]
    elif speed == "medium":
        plan[f"Day {day}"] = [
            "Timed practice sets",
            "Improve accuracy + speed"
        ]
    else:
        plan[f"Day {day}"] = [
            "Maintain speed",
            "Focus on accuracy"
        ]

    return plan