def main():
    difficulty = input("Difficult or casual?")
    players = input("Multiplayer or Singleplayer?")
    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("poker")
        else:
            recommend("Klondike")

    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Singleplayer":
            recommend("Clock")
        else:
            print("Enter a valid player count")

    else:
        print("Enter a valid difficulty")


def recommend(game):
    print("You might like", game)

main()