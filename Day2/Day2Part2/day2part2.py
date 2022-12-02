ROCK = "A"
PAPER = "B"
SCISSORS = "C"

def main():
    # We are making a rock, paper, scissors game
    # Points are determined by the shape you select,
    # rock = 1pt, paper = 2pts, scissors = 3pts
    # PLUS the outcome. Win = 6pts, Draw = 3pts, Lose = 0pts

    # A = Rock
    # B = Paper
    # C = Scissors

    # X means you need to lose
    # Y means you need to draw
    # Z means you need to win

    # Declare variables
    player2Total = 0

    # Read in input file
    with open("input.txt", "r") as f:
        for line in f:
            player1_shape = line[0]
            needed_outcome = line[2]

            # Determine player 2 shape
            player2_shape = find_shape(player1_shape, needed_outcome)

            # Determine player 2 points
            if player2_shape == ROCK:
                player2Total += 1
            elif player2_shape == PAPER:
                player2Total += 2
            elif player2_shape == SCISSORS:
                player2Total += 3

            # Determine player 2 outcome
            if needed_outcome == "X":
                player2Total += 0
            elif needed_outcome == "Y":
                player2Total += 3
            elif needed_outcome == "Z":
                player2Total += 6

    print(player2Total)

# Determine player 2 shape
def find_shape(given_shape, needed_outcome):
    
    # If we need to lose
    if needed_outcome == "X":
        if given_shape == ROCK:
            return SCISSORS
        elif given_shape == PAPER:
            return ROCK
        elif given_shape == SCISSORS:
            return PAPER

    # If we need to draw, simply return the same shape
    if needed_outcome == "Y":
        return given_shape

    # If we need to win
    if needed_outcome == "Z":
        if given_shape == ROCK:
            return PAPER
        elif given_shape == PAPER:
            return SCISSORS
        elif given_shape == SCISSORS:
            return ROCK

# use main function
if __name__ == "__main__":
    main()
