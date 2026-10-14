matched=[]
missing=[]


my_skills = ["python", "sql", "git", "fastapi"]
job_text = "we need an ai engineer with python, docker and sql experience"

for skill in my_skills:
    if skill in job_text:
        matched.append(skill)
    else:
        missing.append(skill)

print("Matched:",matched)
print("Missing:",missing)