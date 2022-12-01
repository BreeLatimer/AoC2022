# main method
def main():
    with open("calory_input.txt") as input_file:
        contents = input_file.read()

    # split the contents into a list of strings
    contents = contents.splitlines()

    # list of elves
    elves = [0]

    current_elf = 0
    for line in contents:
        if(line.strip()):
            #cast the line to an int
            calories = int(line)

            # add the calories to the current elf
            elves[current_elf] += calories
        else:
            # add an elf to the list
            elves.append(0)
            current_elf += 1

    # print the top 3 elves
    print(sum(sorted(elves, reverse=True)[:3]))

# call main method
if __name__ == "__main__":
    main()