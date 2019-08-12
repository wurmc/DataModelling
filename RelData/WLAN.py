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

# functionality to filter for relevant WLAN data
# such as the BSSID and related RSSI
def get_rel_data(line):
    rel_data_wlan = ""
    # go through line and save relevant data in new string
    print(line)
    arr_line = line.split(";")
    counter = 4
    rel_data_wlan += arr_line[0]
    rel_data_wlan += ";"
    while (counter < len(arr_line)):
        rel_data_wlan += arr_line[counter]
        rel_data_wlan += ";"
        rel_data_wlan += arr_line[counter + 2]
        rel_data_wlan += ";"
        counter += 5
    # return assembled string without last ;
    return rel_data_wlan[:-1]
