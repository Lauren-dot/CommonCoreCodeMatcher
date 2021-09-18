#Matching Algorithm, Brute Force Method

assignment = str(input("What was the assignment?: "))

def reading_code_match(assignment):
    if assignment == "summarize":
        code_match = "CCSS.ELA-LITERACY.RL.5.5"
        print(code_match)
        return(code_match)
    else:
        print("I am sorry; you will have to match that up by hand.")

reading_code_match(assignment)
