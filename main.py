import json 

matched=[]
missing=[]
gaps=[]


# my_skills = ["python", "sql", "git", "fastapi"]  #deleted bcuz made the json list in json program
try:
    with open("skills.json", "r")as f:
        my_skills=json.load(f)
except FileNotFoundError:
    print("skills.json not found:( ")
    exit()


job_wants = ["python", "sql", "git", "fastapi", "docker", "mlops", "llm", "aws", "pytorch"]

try:
    with open("job.txt","r") as f:
        job_text=f.read().strip().lower()
except FileNotFoundError:
    print("job.txt not found")
    exit()


for skill in job_wants:
    if skill in job_text and skill not  in my_skills:
        gaps.append(skill)

print("Gaps:",gaps)


for skill in my_skills:
    if skill.lower() in job_text:
        matched.append(skill)
    else:
        missing.append(skill)

print("Matched:",matched)
print("Missing:",missing)