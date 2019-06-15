#  Copyright (c) 2019. Clara Wurm
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of
#  this software and associated documentation files (the "Software"), to deal in
#  the Software without restriction, including without limitation the rights to use,
#  copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
#  Software, and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#  FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHOR OR
#  COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#  IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#  CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# class for measured Cell data,
# such as the type (LTE etc.), the PCI and related RSRP

def get_rel_data(line):
    rel_data_cell = ""
    # go through line and save relevant data in new string
    print(line)
    counter = 1
    counter2 = 0
    tmp = ""
    tmp2 = ""
    for char in line:
        if (
                counter == 2 or counter == 3 or counter == 4):
            if (char == ";"):
                counter += 1
        elif (counter == 5 or counter == 22 or counter == 39 or counter == 56 or counter == 73 or counter == 90 or
              counter == 107 or counter == 124 or counter == 141 or counter == 158):
            if (tmp == "GSM"):
                tmp2 = tmp
                counter2 = counter
                counter += 1
                rel_data_cell += tmp
                tmp = ""
            elif (tmp == "CDMA"):
                tmp2 = tmp
                counter2 = counter
                counter += 1
                rel_data_cell += tmp
                tmp = ""
            elif (tmp == "LTE"):
                tmp2 = tmp
                counter2 = counter
                counter += 1
                rel_data_cell += tmp
                tmp = ""
            elif (tmp == "WCDMA"):
                tmp2 = tmp
                counter2 = counter
                counter += 1
                rel_data_cell += tmp
                tmp = ""
            else:
                tmp += char
        else:
            if (char == ";"):
                if (tmp2 == "GSM"):
                    if (counter == counter2 + 2 or counter == counter2 + 7):
                        counter += 1
                        tmp += char
                        rel_data_cell += tmp
                        tmp = ""
                    else:
                        counter += 1
                        tmp = ""
                elif (tmp2 == "CDMA"):
                    if (counter == counter2 + 2 or counter == counter2 + 11):
                        counter += 1
                        tmp += char
                        rel_data_cell += tmp
                        tmp = ""
                    else:
                        counter += 1
                        tmp = ""
                elif (tmp2 == "LTE"):
                    if (counter == counter2 + 5 or counter == counter2 + 8):
                        counter += 1
                        tmp += char
                        rel_data_cell += tmp
                        tmp = ""
                    else:
                        counter += 1
                        tmp = ""
                elif (tmp2 == "WCDMA"):
                    if (counter == counter2 + 2 or counter == counter2 + 8):
                        counter += 1
                        tmp += char
                        rel_data_cell += tmp
                        tmp = ""
                    else:
                        counter += 1
                        tmp = ""
                else:
                    counter += 1
                    tmp += char
                    rel_data_cell += tmp
                    tmp = ""
            else:
                tmp += char
    return rel_data_cell
