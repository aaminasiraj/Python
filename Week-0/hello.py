#Ask name + remove whitespacesbyt  + apatalize using capitalize and title
name = input("What's your name? ").strip().title()

#spilt the input
first, last = name.split(" ")

#say hello to user
print(f"Hello, {first}")

#THESE ARE STRING METHODS :built in actions in any string
#strip :removes white spaces right and left of the string
#capitalize: Caps the first letter of the first word
#title: caps every first letter of every word
#spilt: splits the string into smaller strs
