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

# class for measured Satellite data,
# such as the PRN and related SNR

# def get_rel_data(line):
#     rel_data_gps = ""
#     # go through line and save relevant data in new string
#     print(line)
#     counter = 1
#     tmp = ""
#     for char in line:
#         if (
#                 counter == 2 or counter == 3 or counter == 6 or counter == 7 or counter == 10 or counter == 11 or counter == 14 or
#                 counter == 15 or counter == 18 or counter == 19 or counter == 22 or counter == 23 or counter == 26 or
#                 counter == 27 or counter == 30 or counter == 31 or counter == 34 or counter == 35 or counter == 38 or
#                 counter == 3 or counter == 42 or counter == 43 or counter == 46 or counter == 47 or counter == 50 or
#                 counter == 51 or counter == 54 or counter == 55 or counter == 58 or counter == 59 or counter == 62 or
#                 counter == 63 or counter == 66 or counter == 67 or counter == 70 or counter == 71 or counter == 74 or
#                 counter == 75 or counter == 78 or counter == 79 or counter == 82 or counter == 83 or counter == 86 or
#                 counter == 87 or counter == 90 or counter == 91 or counter == 94 or counter == 95 or counter == 98 or
#                 counter == 99 or counter == 102 or counter == 103 or counter == 106 or counter == 107 or
#                 counter == 110 or counter == 111 or counter == 114 or counter == 115 or counter == 118 or
#                 counter == 119 or counter == 122 or counter == 123 or counter == 126 or counter == 127 or
#                 counter == 130 or counter == 131 or counter == 134 or counter == 135 or counter == 138 or
#                 counter == 139 or counter == 142 or counter == 143 or counter == 146 or counter == 147 or
#                 counter == 150 or counter == 151 or counter == 154 or counter == 155):
#             if (char == ";"):
#                 counter += 1
#         else:
#             if (char == ";"):
#                 counter += 1
#                 tmp += char
#                 rel_data_gps += tmp
#                 tmp = ""
#             else:
#                 tmp += char
#     return rel_data_gps

def get_rel_data(line):
    rel_data_gps = ""
    # go through line and save relevant data in new string
    print(line)
    arr_line = line.split(";")
    counter = 3
    rel_data_gps += arr_line[0]
    rel_data_gps += ";"
    while (counter < len(arr_line)):
        rel_data_gps += arr_line[counter]
        rel_data_gps += ";"
        rel_data_gps += arr_line[counter + 1]
        rel_data_gps += ";"
        counter += 4
    return rel_data_gps[:-1]
