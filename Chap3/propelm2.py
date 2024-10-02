name= input("Enter the name: ")
date= input("Enter the date: ")
letter= '''Dear Name
You are selected!
date'''
print(letter.replace("Name",name).replace("date",date))