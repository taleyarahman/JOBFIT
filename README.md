# JobFit

Reading through every job posting to check which requirements I'm missing takes
a lot of time. JobFit compares my skills (saved in `skills.json`) against a job
description and lists the skills the job asks for that I don't have yet.

## How it works

1. Your skills are stored in `skills.json`
2. You paste a job description into `job.txt`
3. JobFit lists the skills the job asks for that you don't have yet

## Run from the command line 

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

## Run the API

```
uvicorn api:app --reload
```

Then open `http://127.0.0.1:8000/docs`. Send a job description to `POST /analyze` (keyword matching) or `POST /analyze-ai` (Gemini). Both return `matched`, the skills you have, and `gaps`, the skills you're missing.

## Keyword vs AI

Same job posting sent to both endpoints:

> We need containerization, relational databases, and cloud experience. 

`POST /analyze` (Keyword matching ) finds nothing, because the posting never uses the exact words on the checklist:

```json
{"gaps":[],"matched":[]}
```

`POST /analyze-ai` (Gemini) understands what the posting means:

```json
{"matched": ["relational databases"], "gaps": ["containerization", "cloud experience"]}
```

To use `/analyze-ai`, create a `.env` file with `GEMINI_API_KEY=your-key`. The key is never committed.


## Run the tests

```
pytest
```

## Planned

- PostgreSQL to save every job checked
- Deploy it online