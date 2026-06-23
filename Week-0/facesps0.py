#make main
 #ask for i/p
 #print the o/p
def main():
    text = input("enter text. ")
    print(convert(text))

#make convert
def convert(to):
    return to.replace(":)", "😊").replace(":(", "☹️")

#call main
main()