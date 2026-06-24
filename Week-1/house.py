name = input("whats the name? ").title()

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who? ")

# vers 1
#name = input("whats the name? ").title()

#if name == "Harry" or name == "Hermione" or name == "Ron": 
#    print("Griffindor")

#elif name == "Draco":
#    print ("Slytherin")

#else:
#    print("Who? ")
