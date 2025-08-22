clearance_steps = ["Get Principal's Signature", "Get VP's Signature", "Get Bursar's Signature"]

clearance_steps.append("Get Librarian's Signature")
clearance_steps.append("Return Borrowed Book")

step = clearance_steps.pop()
while step:
    print(step)
    if(len(clearance_steps) == 0):
        print("You're cleared!")
        break
    step = clearance_steps.pop()