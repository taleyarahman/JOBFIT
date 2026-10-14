import json 


def load_skills():
    try:
        with open("skills.json", "r")as f:
            return json.load(f)
    except FileNotFoundError:
        print("skills.json not found:( ")
        exit()

def load_job():
    try:
        with open("job.txt","r") as f:
            return f.read().strip().lower()
    except FileNotFoundError:
        print("job.txt not found")
        exit()


def find_gaps(job_text,my_skills,job_wants):
    gaps=[] 
    for skill in job_wants:
        if skill in job_text and skill not  in my_skills:
            gaps.append(skill)
    return gaps


def find_matches(job_text,my_skills):
    matched=[]
    for skill in my_skills:
        if skill.lower() in job_text:
            matched.append(skill)
    return matched

