from matcher import find_gaps, find_matches

def test_find_gaps():
    result=find_gaps("we need python and aws",["python"],["python","aws","docker"]) #Job text is the actual job posting. #My skills Is what you have, which is Python #Job wants is the checklist the program scans for. 
    assert result== ["aws"] 

def test_find_matched():
    result =find_matches("we need python and aws",["python","sql"])
    assert result == ["python"]

def test_find_matches_none():
    result=find_matches("We need Java and Docker. ",["Python, SQL "])
    assert result==[]