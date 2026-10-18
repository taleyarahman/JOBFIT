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