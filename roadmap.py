def generate_roadmap(data):
    roadmap = []

    if not data["readme"]:
        roadmap.append("Add a detailed README with project overview and setup steps")

    if data["commits"] < 5:
        roadmap.append("Improve commit frequency with meaningful messages")

    roadmap.extend([
        "Add unit and integration tests",
        "Improve folder structure and modularity",
        "Follow Git best practices (branches & PRs)",
        "Add CI/CD using GitHub Actions",
        "Improve code readability and documentation"
    ])

    return roadmap