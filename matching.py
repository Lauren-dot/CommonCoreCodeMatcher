#Matching Algorithm, Brute Force Method

assignment = str(input("What was the assignment?: "))
assignment.lower()

#English Language Arts Matching 

def reading_code_match(assignment):
    if assignment == "summarize":
        code_match = "CCSS.ELA-LITERACY.RL.5.5"
        print(code_match)
        return(code_match)
    if assignment == "read":
        code_match = "CCSS.ELA-LITERACY.RL.5.5" #to be changed
        print(code_match)
        return(code_match)
    else:
        print("I am sorry; you will have to match that up by hand.")

reading_code_match(assignment)

#TO DO:
# 1. Create matching algorithms for each Common Core Code
# 2. Eventually replace each assignment key word with a RegEx to ease searching/matching
