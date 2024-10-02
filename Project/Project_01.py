import random
'''
The Snake, Gun, Water game in python
(1=water
-1= snake
0=gun)

'''

computer=random.choice([-1,0,1])
print(computer)
youstr=input("Enter your choice: ")
youDict={"s": 1, "p": -1, "s": 0}
reverseDict = {1: "Stone", -1: "Paper", 0: "sezer"}

you = youDict[youstr]
print(f"Your choice is{reverseDict[you]} and computer choice is {reverseDict[computer]}")

if(you==computer):
    print("Equal no one win")
else:
    if(computer == 1 and you== -1):
        print("You Win!")
        
    elif(computer == 1 and you== -0):
        print("You Not Win!")
        
    elif(computer == -1 and you== 0):
        print("You Win!")
        # reverseDict = {1:"Stone", -1:"Paper", 0:"sezer"}
    elif(computer == 0 and you== 1):
        print("You Win!")
        
    elif(computer == 0 and you== -1):
        print("You Not Win!")
    elif(computer == 1 and you== -1):
        print("You Not Win!")
    # if(computer == 0 and you== -1):
    #     print("You Not Win!")
        