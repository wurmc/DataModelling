# class for measured Satellite data,
# such as the PRN and related SNR

def getRelData(line):
    rel_data_GPS = ""
    # go through line and save relevant data in new string
    print(line)
    counter = 1
    help = ""
    for char in line:
        if (
                counter == 3 or counter == 6 or counter == 7 or counter == 10 or counter == 11 or counter == 14 or
                counter == 15 or counter == 18 or counter == 19 or counter == 22 or counter == 23 or counter == 26 or
                counter == 27 or counter == 30 or counter == 31 or counter == 34 or counter == 35 or counter == 38 or
                counter == 3 or counter == 42 or counter == 43 or counter == 46 or counter == 47 or counter == 50 or
                counter == 51 or counter == 54 or counter == 55 or counter == 58 or counter == 59 or counter == 62 or
                counter == 63 or counter == 66 or counter == 67 or counter == 70 or counter == 71 or counter == 74 or
                counter == 75 or counter == 78 or counter == 79 or counter == 82 or counter == 83 or counter == 86 or
                counter == 87 or counter == 90 or counter == 91 or counter == 94 or counter == 95 or counter == 98 or
                counter == 99 or counter == 102 or counter == 103 or counter == 106 or counter == 107 or
                counter == 110 or counter == 111 or counter == 114 or counter == 115 or counter == 118 or
                counter == 119 or counter == 122 or counter == 123 or counter == 126 or counter == 127 or
                counter == 130 or counter == 131 or counter == 134 or counter == 135 or counter == 138 or
                counter == 139 or counter == 142 or counter == 143 or counter == 146 or counter == 147 or
                counter == 150 or counter == 151 or counter == 154 or counter == 155):
            if (char == ";"):
                counter += 1
        else:
            if (char == ";"):
                counter += 1
                help += char
                rel_data_GPS += help
                help = ""
            else:
                help += char
    return rel_data_GPS
