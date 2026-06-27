def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Whats n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
         print("meaow")

main()




#vers 3
# print("meow\n" * 3, end="")


#vers2
#for _ in range(3):
#    print("meow")
# instead o [ lists ] we use "range" which are the no. of values we want back starts from 0.
# using i is fine but then people will wonder where did i use it( we use it for 
# counting but not exactly in the code itself) so we use _ to say that yes its
#  a var but im not using it anywher.

# vers 1
#i = 0
#while i < 3:
#    print("meow")
#    i += 1