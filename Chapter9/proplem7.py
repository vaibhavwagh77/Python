with open ("log.txt") as f:
    content = f.readlines()

lineno=1
for line in content:
    if("Vaibhav" in line):
        print(f"the line number is:{lineno}")
        lineno +=1
        break
else:
    print("no word is present")
