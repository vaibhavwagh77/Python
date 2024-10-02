f = open("file.txt","r")
data=f.read()
print(data)
f.close()
if("vaibhav" in data):
    print("the word is there")
else:
    print("Not there")