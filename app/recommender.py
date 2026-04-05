def generate_recommendations(analysis):

    recommendations = []

    # Weak chapters
    for chapter in analysis.get("weaknesses", []):
        recommendations.append(f"Revise {chapter} with basic concepts")
        recommendations.append(f"Practice previous questions on {chapter}")

    # No strengths
    if not analysis.get("strengths"):
        recommendations.append("Focus on building at least one strong subject")

    # Speed improvement
    speed = analysis.get("speed")

    if speed == "slow":
        recommendations.append("Work on time management (use timer while solving)")
    elif speed == "medium":
        recommendations.append("Try to improve speed with timed practice")
    else:
        recommendations.append("Good speed, maintain consistency")

    # Low score
    if analysis.get("avg_score", 0) < 50:
        recommendations.append("Revise basics and solve easy → medium level questions")

    return recommendations