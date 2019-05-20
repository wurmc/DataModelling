
# class for measured Magnetometer data,
# such as the sensor event value as float

def getRelData(line):
    rel_data_Magnet = ""
    # go through line and save relevant data in new string
    print(line)
    counter = 1
    help = ""
    for char in line:
        if (
                counter == 3):
            if (char == ";"):
                counter += 1
        else:
            if (char == ";"):
                counter += 1
                help += char
                rel_data_Magnet += help
                help = ""
            else:
                help += char



    return rel_data_Magnet