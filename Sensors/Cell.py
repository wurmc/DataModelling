
# class for measured Cell data,
# such as the type (LTE etc.), the PCI and related RSRP

# TODO: something is not correct yet
def getRelData(line):
    rel_data_Cell = ""
    # go through line and save relevant data in new string
    print(line)
    counter = 1
    help = ""
    for char in line:
        if (
                counter == 3 or counter == 4 or counter == 6 or counter == 7 or counter == 8 or counter == 9 or
                counter == 11 or counter == 12 or counter == 14 or counter == 16 or counter == 17 or counter == 18 or
                counter == 19 or counter == 21 or counter == 2 or counter == 24):
            if (char == ";"):
                counter += 1
        elif ((counter == 5 or counter == 15 or counter == 25) and help == "LTE"):
            if (char == ";"):
                counter += 1
                help += char
                rel_data_Cell += help
                help = ""
            else:
                help += char
        else:
            if (char == ";"):
                counter += 1
                help += char
                rel_data_Cell += help
                help = ""
            else:
                help += char
    return rel_data_Cell

