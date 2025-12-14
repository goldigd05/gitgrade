import requests

GITHUB_API = "https://api.github.com/repos"

def parse_repo(url):
    parts = url.rstrip("/").split("/")
    return parts[-2], parts[-1]

def fetch_repo(owner, repo):
    repo_data = requests.get(f"{GITHUB_API}/{owner}/{repo}").json()
    contents = requests.get(f"{GITHUB_API}/{owner}/{repo}/contents").json()
    commits = requests.get(f"{GITHUB_API}/{owner}/{repo}/commits").json()
    return repo_data, contents, commits

def analyze_repo(url):
    owner, repo = parse_repo(url)
    repo_data, contents, commits = fetch_repo(owner, repo)

    files = sum(1 for i in contents if i["type"] == "file")
    folders = sum(1 for i in contents if i["type"] == "dir")
    readme = any(i["name"].lower() == "readme.md" for i in contents)
    commit_count = len(commits)

    return {
        "files": files,
        "folders": folders,
        "readme": readme,
        "commits": commit_count,
        "language": repo_data.get("language", "Unknown")
    }