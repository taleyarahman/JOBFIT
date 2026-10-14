# JobFit

Reading through every job posting to check which requirements I'm missing takes
a lot of time. JobFit compares my skills (saved in `skills.json`) against a job
description and lists the skills the job asks for that I don't have yet.

## How it works

1. Your skills are stored in `skills.json`
2. You paste a job description into `job.txt`
3. JobFit lists the skills the job asks for that you don't have yet

## How to run

1. Put `skills.json` and `job.txt` in the project folder
2. Run:

```
python main.py
```

## Example output

```
Gaps: ['llm', 'aws']
Matched: ['python', 'sql']

```

## Planned

- Use an LLM to extract requirements, so "relational databases" matches `sql`
- FastAPI endpoint
- PostgreSQL to save every job checked
- Deploy it online