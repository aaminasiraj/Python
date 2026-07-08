text = input("camelCase: ")
    
for letter in text:
    if letter.isupper():
        print("_" + letter.lower(), end ="")

    else :
        print(letter, end="")

print()