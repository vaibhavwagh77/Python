marks1=print(int(input("Enter the marks of first sub: ")))
marks2=print(int(input("Enter the marks of second sub: ")))
marks3=print(int(input("Enter the marks of third sub: ")))

total=marks1 + marks2 + marks3
print(total)
total_percentage=(100*total)/300

if(total_percentage>=40):
    print("You are pass")
else:
    print("You are fail")