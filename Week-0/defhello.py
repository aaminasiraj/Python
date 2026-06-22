
def main():
    hello()
    name = input("whats your name? ").strip().title()
    hello(name)

def hello(to="World"):
    print("Hello", to)
 
main()

# so the algo is this:
#we write main code and then alll the def functions and then we call main
# we take name as input 
#then call hello with that name as inoput to this func
# in hello to shall be equal to name and t=hece its shall take the place of to in the print func
#then the terminal shall execute the print line.