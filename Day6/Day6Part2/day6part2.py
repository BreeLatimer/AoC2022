def main():
    # read in the input file
    with open('input.txt', 'r') as f:
        input = f.read()

    i = 0
    marker_found = False
    while i < len(input)-14:
        evalString = input[i:i+14]
        print(evalString)

        charSet = set()
        for char in evalString:
            if char in charSet:
                break
            else:
                charSet.add(char)

        if len(charSet) == 14:
            print(i+14)
            break

        i += 1

if __name__ == "__main__":
    main()
