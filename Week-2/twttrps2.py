# prompt fot input, lowercase it
text = input("Input: ").lower()

#search for a,e,i ,o,u
#omit them
#o/p
for i in text:
    if i not in ["a", "e", "i", "o", "u"]:
        print(i, end=" ")

print()
