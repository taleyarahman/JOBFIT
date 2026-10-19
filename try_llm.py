#throw away file
from llm import compare_skills
job = "We need containerization, relational databases and cloud experience."
print(compare_skills(job, ["python", "sql", "docker", "git"]))