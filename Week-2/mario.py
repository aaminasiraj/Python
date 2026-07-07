def main():
    print_square(3)

#for each row in square
def print_square(size):
#for each brick
    for i in range(size):
#print brick
        print_brick(size)

def print_brick(width):
    print("#" * width)

main() 
