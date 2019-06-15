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

# class for measured Wifi data,
# such as the BSSID and related RSSI

def get_rel_data(line):
    rel_data_wlan = ""
    # go through line and save relevant data in new string
    print(line)
    counter = 1
    tmp = ""
    for char in line:
        if (
                counter == 2 or counter == 3 or counter == 4 or counter == 6 or counter == 8 or counter == 9 or
                counter == 11 or counter == 13 or counter == 14 or counter == 16 or counter == 18 or counter == 19 or
                counter == 21 or counter == 23 or counter == 24 or counter == 26 or counter == 28 or counter == 29 or
                counter == 31 or counter == 33 or counter == 34 or counter == 36 or counter == 38 or counter == 39 or
                counter == 41 or counter == 43 or counter == 44 or counter == 46 or counter == 48 or counter == 49 or
                counter == 51 or counter == 53 or counter == 54 or counter == 56 or counter == 58 or counter == 59 or
                counter == 61 or counter == 63 or counter == 64 or counter == 66 or counter == 68 or counter == 69 or
                counter == 71):
            if (char == ";"):
                counter += 1
        else:
            if (char == ";"):
                counter += 1
                tmp += char
                rel_data_wlan += tmp
                tmp = ""
            else:
                tmp += char
    return rel_data_wlan
