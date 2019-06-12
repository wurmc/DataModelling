# class for measured Cell data,
# such as the type (LTE etc.), the PCI and related RSRP

def getRelData(line):
    rel_data_Cell = ""
    # go through line and save relevant data in new string
    print(line)
    counter = 1
    counter2 = 0
    help = ""
    help2 = ""
    for char in line:
        if (
                counter == 2 or counter == 3 or counter == 4):
            if (char == ";"):
                counter += 1
        elif (counter == 5 or counter == 22 or counter == 39 or counter == 56 or counter == 73 or counter == 90 or
              counter == 107 or counter == 124 or counter == 141 or counter == 158):
            if (help == "GSM"):
                help2 = help
                counter2 = counter
                counter += 1
                rel_data_Cell += help
                help = ""
            elif (help == "CDMA"):
                help2 = help
                counter2 = counter
                counter += 1
                rel_data_Cell += help
                help = ""
            elif (help == "LTE"):
                help2 = help
                counter2 = counter
                counter += 1
                rel_data_Cell += help
                help = ""
            elif (help == "WCDMA"):
                help2 = help
                counter2 = counter
                counter += 1
                rel_data_Cell += help
                help = ""
            else:
                help += char
        else:
            if (char == ";"):
                if (help2 == "GSM"):
                    if (counter == counter2 + 2 or counter == counter2 + 7):
                        counter += 1
                        help += char
                        rel_data_Cell += help
                        help = ""
                    else:
                        counter += 1
                        help = ""
                elif (help2 == "CDMA"):
                    if (counter == counter2 + 2 or counter == counter2 + 11):
                        counter += 1
                        help += char
                        rel_data_Cell += help
                        help = ""
                    else:
                        counter += 1
                        help = ""
                elif (help2 == "LTE"):
                    if (counter == counter2 + 5 or counter == counter2 + 8):
                        counter += 1
                        help += char
                        rel_data_Cell += help
                        help = ""
                    else:
                        counter += 1
                        help = ""
                elif (help2 == "WCDMA"):
                    if (counter == counter2 + 2 or counter == counter2 + 8):
                        counter += 1
                        help += char
                        rel_data_Cell += help
                        help = ""
                    else:
                        counter += 1
                        help = ""
                else:
                    counter += 1
                    help += char
                    rel_data_Cell += help
                    help = ""
            else:
                help += char
    return rel_data_Cell
