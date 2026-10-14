matched=[]
missing=[]


my_skills = ["python", "sql", "git", "fastapi","Docker","MLOps","LLM"]

try:
    with open("job.txt","r") as f:
        job_text=f.read().strip().lower()
except FileNotFoundError:
    print("job.txt not found")
    exit()
# print(job_text[:300])

for skill in my_skills:
    if skill.lower() in job_text:
        matched.append(skill)
    else:
        missing.append(skill)

print("Matched:",matched)
print("Missing:",missing)