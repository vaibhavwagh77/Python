f= open("score.txt","w")

def game():
    s = input("Enter the Score: ")
    if(s>0):
        f.write(s)
    else:
        print("Not High Score.")
    data=f.read()
f.close()
game()