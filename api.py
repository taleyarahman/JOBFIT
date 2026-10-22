import matcher 

from llm import compare_skills

from fastapi import FastAPI

from pydantic import BaseModel

class JobRequest(BaseModel):
    text:str

app = FastAPI()
job_wants = ["python", "sql", "git", "fastapi", "docker", "mlops", "llm", "aws", "pytorch"]

@app.get("/")
def home():
    return {"message":"JOBFIT is running"}

@app.get("/about")
def about():
    description="""Reading through every job posting to check which requirements I'm missing takes
a lot of time. JobFit compares my skills (saved in `skills.json`) against a job
description and lists the skills the job asks for that I don't have yet."""
    return {"description":description}

@app.get("/gaps")
def gaps():
    my_skills = matcher.load_skills()
    job_text = matcher.load_job()
    result=matcher.find_gaps(job_text,my_skills,job_wants)
    return {"gaps": result}

@app.post("/analyze")
def analyze(job: JobRequest):
    my_skills = matcher.load_skills()
    job_text=job.text.strip().lower()
    result=matcher.find_gaps(job_text, my_skills,job_wants)
    matched=matcher.find_matches(job_text,my_skills)
    return {"gaps":result, "matched":matched}

@app.post("/analyze-ai")
def analyze_ai(job: JobRequest):
    my_skills = matcher.load_skills()
    return compare_skills(job.text, my_skills)