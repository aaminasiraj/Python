# take input
op = input("whats the operation? ")

# split input and assign values x y z
x, y, z = op.split(" ")
x = float(x)
z = float(z)

#conditions by interpreting middle input acc. use match case. +take int value of xand z
match y:
    case "+":
        n = x + z
    case "-":
        n = x - z
    case "/":
        n = x / z
    case "*":
        n = x * z
    case "%":
        n = x % z
    case _:
        print("invalid operation.")

#print
print("the result of", op, "is", f"{n:.2f}")
