from flask import Flask, render_template, request
from analyzer import analyze_repo
from scorer import calculate_score, level
from roadmap import generate_roadmap

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["repo"]

        data = analyze_repo(url)
        score = calculate_score(data)
        grade = level(score)
        roadmap = generate_roadmap(data)

        if score >= 80:
            summary = "Excellent project with strong structure and consistency."
        elif score >= 50:
            summary = "Decent project but documentation and testing need improvement."
        else:
            summary = "Basic project with weak structure and limited best practices."

        result = {
            "score": score,
            "grade": grade,
            "summary": summary,
            "roadmap": roadmap
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)