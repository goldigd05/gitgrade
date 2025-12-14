 1. GitGrade – GitHub Repository Analyzer

 @ Problem Statement
Students often create GitHub repositories but do not know how good their code quality,
structure, and documentation appear to recruiters or mentors.
This project evaluates a GitHub repository and converts it into a meaningful
Score, Summary, and Personalized Roadmap.

@  Solution Overview
GitGrade is an intelligent repository analysis system that:
- Accepts a public GitHub repository URL
- Analyzes repository structure, commits, and documentation
- Generates an honest score and developer feedback
- Provides a personalized improvement roadmap

@ Approach
1. Takes GitHub repository URL as input  
2. Fetches public repository data using GitHub API  
3. Analyzes:
   - Number of files and folders  
   - Commit history  
   - README presence  
   - Overall project structure  
4. Applies rule-based scoring logic  
5. Generates:
   - Score & level  
   - Summary of repository quality  
   - Actionable roadmap for improvement  

@ Features
- Repository Score (0–100)
- Skill Level (Beginner / Intermediate / Advanced)
- Clear project quality summary
- Personalized improvement roadmap
- Simple and clean Web UI
- Works on any public GitHub repository

@ Tech Stack
- Python  
- Flask  
- GitHub REST API  
- HTML & CSS  


imp@  ----How to Run the Project

```bash
pip install -r requirements.txt
python web.py

 @  Conclusion
GitGrade acts as a "Repository Mirror" that honestly reflects the strengths and
weaknesses of a GitHub project and guides students toward real-world coding standards.
 Team name -: AI-Code-Lens
 made by Goldi