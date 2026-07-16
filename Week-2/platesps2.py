def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if num(s) and start(s) and sign(s) and mid( s):
        return True
        

def num(s):
    return 2 <= len(s) <=6



def start(s):
    return s[0].isalpha() and s[1].isalpha()
        
def sign(s):
    if s.isalnum():
        return True
    else:
        return False
    

def mid(s):
    started = False

    for i in s:
        if i.isdigit():
            if not started and i == "0":
                return False

            started = True

        elif started:
            return False

    return True



    


main()

