# a - z = 97 - 122
# A - Z = 65 - 90
def main():
    with open("input.txt") as input_file:
        contents = input_file.read()

    # split the contents into a list of strings by line
    contents = contents.splitlines()

    priority_values = list()

    for i in range(0, len(contents), 3): # iterate by 3
        # split the list by every three lines
        string1 = contents[i]
        string2 = contents[i+1]
        string3 = contents[i+2] 

        # find the common letter between the three strings
        common_letter = find_common_letter(string1, string2, string3)

        if(common_letter == ""): # make sure our letters are valid
            print("No common letter found")
            return -1

        priority_value = ord(common_letter)

        if((priority_value < 65 and priority_value > 90) 
        or (priority_value < 97 and priority_value > 122)): # make sure our letters are valid
            print("Invalid character found")
            return -1

        priority_values.append(priority_value)

    sum = 0
    for i in range(len(priority_values)):
        if(priority_values[i] >= 65 and priority_values[i] <= 90): # A-Z
            sum += priority_values[i] - 64 + 26 # subtract 64 for ASCII offset, add 26 for A-Z offset
        elif(priority_values[i] >= 97 and priority_values[i] <= 122): # a-z
            sum += priority_values[i] - 96 # subtract 96 for ASCII offset
        else:
            print("Invalid character found")
            return -1

    print(sum)

def find_common_letter(string1, string2, string3):
    # find the common letter between the three strings
    common_letter = ""

    for i in range(len(string1)):
        for j in range(len(string2)):
            for k in range(len(string3)):
                if(string1[i] == string2[j] and string2[j] == string3[k]):
                    common_letter = string1[i]

    return common_letter

# call main method
if __name__ == "__main__":
    main()