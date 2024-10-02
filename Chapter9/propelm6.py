
word = "python"
with open("log.txt") as f:
    content = f.read()

if word in content:
    print("The word is present")
else:
    with open("log.txt", "w") as f:
        f.write(word)
