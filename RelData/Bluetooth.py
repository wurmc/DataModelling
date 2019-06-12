# class for measured Bluetooth data,
# such as the address and related RSSI

def getRelData(line):
    rel_data_BT = ""
    # go through line and save relevant data in new string
    print(line)
    counter = 1
    help = ""
    for char in line:
        if (
                counter == 2 or counter == 3 or counter == 4 or counter == 7 or counter == 10 or counter == 13 or
                counter == 16 or counter == 19 or counter == 22 or counter == 25 or counter == 28 or counter == 31):
            if (char == ";"):
                counter += 1
        else:
            if (char == ";"):
                counter += 1
                help += char
                rel_data_BT += help
                help = ""
            else:
                help += char
    return rel_data_BT
