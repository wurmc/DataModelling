
# class for measured Location data,
# such as the Latitude and the Longitude

def getRelData(line):
    rel_data_Loc = ""
    # go through line and save relevant data in new string
    print(line)
    counter = 1
    help = ""
    for char in line:
        if (
                counter == 3 or counter == 4 or counter == 7):
            if (char == ";"):
                counter += 1
        else:
            if (char == ";"):
                counter += 1
                help += char
                rel_data_Loc += help
                help = ""
            else:
                help += char
    return rel_data_Loc