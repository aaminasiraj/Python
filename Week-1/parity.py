def main():
    x = int(input("What's x? "))
    if even(x):
        print("even.")
    else:
        print("Odd")

def even(n):
    return (n % 2 == 0)

main()



#vers 1
#def even(n):
#   if n % 2 == 0:
#        return True
#    else:
#       return False
#COLLAPSED INTO ONE LINE ABOVE.

#vers 2
# return True if n % 2 == 0 else False

#vers 3
# if the exp. is already a boolean expression aka t/f ans. then we dont even need to to use conditionals
#although no need.
