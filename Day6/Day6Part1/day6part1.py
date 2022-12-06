def main():
    # read in the input file
    with open('input.txt', 'r') as f:
        input = f.read()

    i = 0
    marker_found = False
    while i < len(input)-4:
        evalString = input[i:i+4]
        print(evalString)

        charSet = set()
        for char in evalString:
            if char in charSet:
                break
            else:
                charSet.add(char)

        if len(charSet) == 4:
            print(i+4)
            break

        i += 1

if __name__ == "__main__":
    main()
