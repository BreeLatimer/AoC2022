def main():
    validPairs = 0
    
    # Read the input file
    with open('input.txt') as f:
        data = f.read().splitlines()

    for line in data:
        # Split the line into words
        ranges = line.split(',')

        range1 = ranges[0].split("-")
        range2 = ranges[1].split("-")
        
        fullList1 = list()
        fullList2 = list()

        for i in range(int(range1[0]), int(range1[1]) + 1):
            fullList1.append(i)

        for i in range(int(range2[0]), int(range2[1]) + 1):
            fullList2.append(i)

        list1containsList2 = False
        list2containsList1 = False

        for i in fullList1:
            if i in fullList2:
                list1containsList2 = True
            else:
                list1containsList2 = False
                break

        for i in fullList2:
            if i in fullList1:
                list2containsList1 = True
            else:
                list2containsList1 = False
                break

        if(list1containsList2 or list2containsList1):
            validPairs += 1
    
    print(validPairs)

if __name__ == "__main__":
    main()