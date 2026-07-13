amtdue = 50

while amtdue > 0:
    print("Amount Due:", amtdue )
    
    coin = int(input("Insert Coin: "))

    if coin in [25, 10, 5]:
        amtdue = amtdue - coin

print("Change Owed:", amtdue - 50)
