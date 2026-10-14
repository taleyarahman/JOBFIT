import matcher

job_wants=["python", "sql", "git", "fastapi", "docker", "mlops", "llm", "aws", "pytorch"]

my_skills=matcher.load_skills()
job_text=matcher.load_job()

gaps=matcher.find_gaps(job_text,my_skills,job_wants)
matched=matcher.find_matches(job_text,my_skills)

print("Gaps:",gaps)
print("Matched: ",matched)