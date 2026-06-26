
def main():
    t = input("whats the time? ")
    hours = convert(t)

    if 7 <= hours <= 8:
        print("Breakfast time !")
    elif 12 <= hours <= 13:
        print("Lunch time !")
    elif 18 <= hours <= 19:
        print("Dinner time !")
   


def convert(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m) / 60
    return m + h

main()
