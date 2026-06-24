x = int(input("whats x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")

elif x > y:
    print(" x is greater than y.")

else:
    print("x is equal to y")
    
# elif id better than if as its faster a goes through fewer lines of code than if
# where we go through evry condition regardless whether its prev ques. tru or not

#elif asks a ques tions taking into acc. whether the prev question was true/false. 

# else is even better as its saves writing an extra which already is not needed
#  as its obv from the first teo conditions 