try:
    x = int(input("Whats x?"))
    print(f"x is {x}")
except ValueError:
    print("X is not an integer")