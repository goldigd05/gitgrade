def calculate_score(data):
    score = 0

    score += min(data["files"] * 2, 20)
    score += min(data["folders"] * 3, 20)
    score += 20 if data["readme"] else 0
    score += min(data["commits"] * 2, 40)

    return min(score, 100)

def level(score):
    if score >= 80:
        return "Advanced (Gold)"
    elif score >= 50:
        return "Intermediate (Silver)"
    else:
        return "Beginner (Bronze)"