#EXTRACTION
#it hands the job posting to Gemini like a person reading it, and asks “list the skills this job needs.” Gemini sends back a list, and your code turns it into a Python list.

import json #Convert the model's text answer into a Python list. 
from dotenv import load_dotenv #Reads your .env file, so the key is available. 
from google import genai  #Gemini library 
from google.genai import types # types Holds its settings objects 

load_dotenv()
client=genai.Client() #Create the connection to Gemini once, at the top. 

def extract_requirements(job_text):
    prompt=f""" list the technical skills this job requires.
Return ONLY a json array pf short lowercase strings , with no other text.
Example : [ "python","sql","docker]


    
job posting:
{job_text}"""
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json"),
    )
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        return[]

    

def compare_skills(job_text, my_skills):
    prompt = f"""Read the job posting below and work out the technical skills it requires.
Compare them to MY SKILLS. Skills that mean the same thing count as a match
(for example, docker covers containerization).

Return ONLY a JSON object with two keys, and no other text:
"matched": required skills I have
"gaps": required skills I do not have
Use short lowercase strings.
Example: {{"matched": ["python"], "gaps": ["aws"]}}

MY SKILLS: {json.dumps(my_skills)}

Job posting:
{job_text}"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json"),
    )
    try:
        return json.loads(response.text)
    except (json.JSONDecodeError, TypeError):
        return {"matched": [], "gaps": []}