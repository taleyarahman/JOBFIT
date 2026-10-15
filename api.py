from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"JOBFIT  is running"}

@app.get("/about")
def about():
    description="""Reading through every job posting to check which requirements I'm missing takes
a lot of time. JobFit compares my skills (saved in `skills.json`) against a job
description and lists the skills the job asks for that I don't have yet."""
    return {"description":description}