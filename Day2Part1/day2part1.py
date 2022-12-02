# declare main function
def main():
    # We are making a rock, paper, scissors game
    # Points are determined by the shape you select,
    # rock = 1pt, paper = 2pts, scissors = 3pts
    # PLUS the outcome. Win = 6pts, Draw = 3pts, Lose = 0pts

    # A, X = Rock
    # B, Y = Paper
    # C, Z = Scissors

    # Declare variables
    player2Total = 0

    # Read in input file
    with open("input.txt", "r") as f:
        for line in f:
            # create an outcome variable, and set it to -1
            outcome = -1
            # the first char is player1's choice
            player1_choice = line[0]

            # second char is player2's choice
            player2_choice = line[2]

            # call the check_choices function
            outcome = check_choices(player1_choice, player2_choice)

            shape = check_shape(player2_choice)

            if(shape == -1 or outcome == -1):
                print("Invalid input")
                return

            # add the value for the (outcome + shape choice) to the player's totals
            player2Total += shape + outcome
        
    print(player2Total)
            
def check_choices(player1_choice, player2_choice):
    match player1_choice:
                case "A":
                    if(player2_choice == "X"):
                        return 3
                    elif(player2_choice == "Y"):
                        return 6
                    elif(player2_choice == "Z"):
                        return 0
                    else:
                        return -1
                case "B":
                    if(player2_choice == "X"):
                        return 0
                    elif(player2_choice == "Y"):
                        return 3
                    elif(player2_choice == "Z"):
                        return 6
                    else:
                        return -1
                case "C":
                    if(player2_choice == "X"):
                        return 6
                    elif(player2_choice == "Y"):
                        return 0
                    elif(player2_choice == "Z"):
                        return 3
                    else:
                        return -1
                case _:
                    return -1

def check_shape(player_choice):
    match player_choice:
        case "A":
            return 1
        case "B":
            return 2
        case "C":
            return 3
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3
        case _:
            return -1

# use main function
if __name__ == "__main__":
    main()
