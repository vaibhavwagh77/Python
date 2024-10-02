def rem(list,word):
    for item in list:
        list.remove(word)
        return list 
    
list=[]
list.append("Vaibhav")
list.append("Bhai")
list.append("Apple")
list.append("Mango")
list.append("le")
word = input("Enter the word: ")
print(rem(list,word))
    