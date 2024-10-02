def reccursion(n):

    if(n==0 or n==1):
        return 1
    return reccursion(n-1)+n

n= int(input("Enter the number: "))
print(reccursion(n))
    