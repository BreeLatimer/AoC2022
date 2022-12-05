# create main function
def main():
    # scan in the input file
    with open('input.txt', 'r') as f:
        # read in the input file
        input = f.read()

    # split the input into a list of strings
    input = input.splitlines()

    # create the 9 stacks
    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    stack5 = []
    stack6 = []
    stack7 = []
    stack8 = []
    stack9 = []
    
    # store the stacks in a list
    stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

    moveIndex = 0

    # loop through the input until we come across the word "move"
    for line in input:
        if line[1] == "1":
            moveIndex = input.index(line)+2
            print(moveIndex)
            break

        if line[1] != " ":
            stack1.insert(0, line[1])
        if line[5] != " ":
            stack2.insert(0, line[5])
        if line[9] != " ":
            stack3.insert(0, line[9])
        if line[13] != " ":
            stack4.insert(0, line[13])
        if line[17] != " ":
            stack5.insert(0, line[17])
        if line[21] != " ":
            stack6.insert(0, line[21])
        if line[25] != " ":
            stack7.insert(0, line[25])
        if line[29] != " ":
            stack8.insert(0, line[29])
        if line[33] != " ":
            stack9.insert(0, line[33])

    iterator = 1
    for stack in stacks:
        print(iterator, ":", stack)
        iterator += 1

    # loop through input from the move index to the end
    for line in input[moveIndex:]:
        line = line.split(" ")

        numToMove = int(line[1])
        fromStack = stacks[int(line[3])-1]
        toStack = stacks[int(line[5])-1]

        for i in range(numToMove):
            toStack.append(fromStack.pop())

    print()
    print("AFTER MOVE:")
    print("Top of each stack:")

    outputString = ""
    for stack in stacks:
        outputString += stack.pop()

    print(outputString)

# call main function
if __name__ == "__main__":
    main()
