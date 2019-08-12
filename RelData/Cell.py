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

# functionality to filter for relevant Cell data
# such as the type (LTE etc.), the PCI and related RSRP
def get_rel_data(line):
    rel_data_cell = ""
    # go through line and save relevant data in new string
    print(line)
    arr_line = line.split(";")
    counter = 4
    rel_data_cell += arr_line[0]
    rel_data_cell += ";"
    while (counter < len(arr_line)):
        if (arr_line[counter] == "GSM"):
            rel_data_cell += arr_line[counter]
            rel_data_cell += arr_line[counter + 2]
            rel_data_cell += ";"
            rel_data_cell += arr_line[counter + 7]
            rel_data_cell += ";"
        elif (arr_line[counter] == "CDMA"):
            rel_data_cell += arr_line[counter]
            rel_data_cell += arr_line[counter + 2]
            rel_data_cell += ";"
            rel_data_cell += arr_line[counter + 11]
            rel_data_cell += ";"
        elif (arr_line[counter] == "LTE"):
            rel_data_cell += arr_line[counter]
            rel_data_cell += arr_line[counter + 5]
            rel_data_cell += ";"
            rel_data_cell += arr_line[counter + 8]
            rel_data_cell += ";"
        elif (arr_line[counter] == "WCDMA"):
            rel_data_cell += arr_line[counter]
            rel_data_cell += arr_line[counter + 2]
            rel_data_cell += ";"
            rel_data_cell += arr_line[counter + 8]
            rel_data_cell += ";"
        counter += 17
    # return assembled string without last ;
    return rel_data_cell[:-1]
