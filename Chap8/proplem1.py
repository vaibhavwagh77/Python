def great():
    n1=int(input("Enter the number: "))
    n2=int(input("Enter the number: "))
    n3=int(input("Enter the number: "))
    if(n1>n2,n1>n3):
        print("The n1 is great")
    elif(n2>n1,n2>n3):
        print("The n2 is great")
    elif(n3>n1,n3>n2):
        print("The n3 is great")
    else:
        print("The number is equal")



print(great())