from analyzer import analyze_repo
from scorer import calculate_score, level
from roadmap import generate_roadmap

def main():
    url = input("Enter GitHub Repository URL: ")

    data = analyze_repo(url)
    score = calculate_score(data)
    grade = level(score)
    roadmap = generate_roadmap(data)

    print("\n===== GitGrade Report =====\n")
    print("Score:", score, "/ 100")
    print("Level:", grade)

    print("\nSummary:")
    if score >= 80:
        print("Excellent project with strong structure and consistency.")
    elif score >= 50:
        print("Decent project but documentation and testing need improvement.")
    else:
        print("Basic project with weak structure and limited best practices.")

    print("\nPersonalized Roadmap:")
    for step in roadmap:
        print("•", step)

if __name__ == "__main__":
    main()