# class for measured Wifi data,
# such as the BSSID and related RSSI

def getRelData(line):
    rel_data_Wifi = ""
    # go through line and save relevant data in new string
    print(line)
    counter = 1
    help = ""
    for char in line:
        if (
                counter == 3 or counter == 4 or counter == 6 or counter == 8 or counter == 9 or counter == 11 or
                counter == 13 or counter == 14 or counter == 16 or counter == 18 or counter == 19 or counter == 21 or
                counter == 23 or counter == 24 or counter == 26 or counter == 28 or counter == 29 or counter == 31 or
                counter == 33 or counter == 34 or counter == 36 or counter == 38 or counter == 39 or counter == 41 or
                counter == 43 or counter == 44 or counter == 46 or counter == 48 or counter == 49 or counter == 51 or
                counter == 53 or counter == 54 or counter == 56 or counter == 58 or counter == 59 or counter == 61 or
                counter == 63 or counter == 64 or counter == 66 or counter == 68 or counter == 69 or counter == 71):
            if (char == ";"):
                counter += 1
        else:
            if (char == ";"):
                counter += 1
                help += char
                rel_data_Wifi += help
                help = ""
            else:
                help += char
    return rel_data_Wifi
