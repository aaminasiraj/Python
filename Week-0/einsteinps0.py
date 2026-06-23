#ask for input and assign variable in main conv to int
def main():
    m = int(input("whats the mass in kgs? "))
    print("the value of the energy equivalent acc to the mass of", m, "kgs is", energy(m), "joules")

#make func energy by using arimatic func
def energy(mass):
    return mass*pow(300000000, 2)

#call main
main()