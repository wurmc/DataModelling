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

# all functionality to assemble fingerprints

from Fingerprint import Fingerprint
from Fingerprint import FingerprintStorage
from Distance import FingerprintRestoration


# begin help functions
# function to delog signal values
def delog(signal_db):
    signal_lin = 10 ** (signal_db / 10)
    return signal_lin


# function to get the right file path of the user
def select_file_path(type):
    file_path = str(
        input("Please enter the absolute path of the " + type + " file you want to read (use / not win \): "))
    return file_path


# parameter for sort()
def take_time(elem):
    return elem[:12]


# function to get the right position id from the user
def set_pos_id():
    pos_id = str(input("Please enter the position ID for this fingerprint:"))
    return pos_id


# take first lines of w, b, c and find out, which timestamp is the smallest, save them in list to sort?
# therefor extraction of timestamps (13 digits) needed
def find_min_time(w_line, b_line, c_line):
    min_time = min(int(w_line[:13]), int(b_line[:13]), int(c_line[:13]))
    return min_time


def find_max_time(w_line, b_line, c_line):
    max_time = max(int(w_line[:13]), int(b_line[:13]), int(c_line[:13]))
    # catch empty data lines with dummy timestamp and set max_time to relevant timestamp
    if (max_time == 9999999999999):
        tmp = [int(w_line[:13]), int(b_line[:13]), int(c_line[:13])]
        while (9999999999999 in tmp):
            tmp.remove(9999999999999)
        max_time = max(tmp)
    return max_time


def find_time(time, index, arr_w_lines, arr_b_lines, arr_c_lines):
    if (arr_w_lines[index].find(str(time)) != -1):
        return arr_w_lines
    elif (arr_b_lines[index].find(str(time)) != -1):
        return arr_b_lines
    elif (arr_c_lines[index].find(str(time)) != -1):
        return arr_c_lines


def find_index(time, diff, arr):
    for el in arr:
        if (time <= int(el[:13]) < (time + diff)):
            return arr.index(el)
        else:
            return -1


# end help functions

# main function to assemble a fingerprint
def assemble_fingerprint():
    # read data from files: WLAN, BT, Cells
    wlan_file_path = select_file_path("WLAN")
    # wlan_file_path = "E:/Clara/Studium/Master/MA/Datenverarbeitung/20190519_Verarbeitungskette/20190616_Test_Fingerprint_Assembly/User_Hand_1306191731499629_WiFi__154358522871920__0.csv"
    bt_file_path = select_file_path("BT")
    # bt_file_path = "E:/Clara/Studium/Master/MA/Datenverarbeitung/20190519_Verarbeitungskette/20190616_Test_Fingerprint_Assembly/User_Hand_1306191731499629_Bluetooth__154358544046191__0.csv"
    cell_file_path = select_file_path("Cell")
    # cell_file_path = "E:/Clara/Studium/Master/MA/Datenverarbeitung/20190519_Verarbeitungskette/20190616_Test_Fingerprint_Assembly/User_Hand_1306191731499629_Cells__154358527039733__0.csv"

    # open source files
    wlan_file = open(wlan_file_path, "r")
    bt_file = open(bt_file_path, "r")
    cell_file = open(cell_file_path, "r")

    # read data from txt files line by line and save in array
    wlan_lines = wlan_file.readlines()
    arr_wlan_lines = []
    for WLAN_line in wlan_lines:
        arr_wlan_lines.append(WLAN_line)

    bt_lines = bt_file.readlines()
    arr_bt_lines = []
    for bt_line in bt_lines:
        arr_bt_lines.append(bt_line)

    cell_lines = cell_file.readlines()
    arr_cell_lines = []
    for cell_line in cell_lines:
        arr_cell_lines.append(cell_line)

    # check if lines of each sensor are properly sorted, if not: sort them
    arr_wlan_lines.sort(key=take_time)
    arr_bt_lines.sort(key=take_time)
    arr_cell_lines.sort(key=take_time)
    # Counter for number of relevant fingerprints:
    fp_counter = max(len(arr_wlan_lines), len(arr_bt_lines), len(arr_cell_lines))

    # make sure, every data array has the same length to avoid errors while parsing
    while (len(arr_wlan_lines) < fp_counter):
        arr_wlan_lines.append("9999999999999")
    while (len(arr_bt_lines) < fp_counter):
        arr_bt_lines.append("9999999999999")
    while (len(arr_cell_lines) < fp_counter):
        arr_cell_lines.append("9999999999999")

    # store data in data structure
    pos_id = set_pos_id()

    arr_fp = []
    for i in range(0, fp_counter):
        # take first lines of w, b, c and find out, which timestamp is the smallest, save them in list to sort?
        # therefor extraction of timestamps (13 digits) needed
        # set min_time = smallest timestamp of 1st sensor
        min_time = find_min_time(arr_wlan_lines[0], arr_bt_lines[0], arr_cell_lines[0])
        arr = find_time(min_time, 0, arr_wlan_lines, arr_bt_lines, arr_cell_lines)

        # take 2nd timestamp of sensor with smallest 1st timestamp (reference sensor) and calculate difference
        if (len(arr) >= 2):
            help_time = int(arr[1][:13])
            diff = help_time - min_time
            print(diff)

        # check if timestamps of sensors are in between 1st and 2nd timestamp of reference sensor
        # take data of all sensors which is between 1st and 2nd timestamp of reference sensor as start point for fingerprint assembly
        # Index of array for matching WLAN values to begin with
        w_arr_index = find_index(min_time, diff, arr_wlan_lines)
        # Index of array for matching BT values to begin with
        b_arr_index = find_index(min_time, diff, arr_bt_lines)
        # Index of arry for matching Cell values to begin with
        c_arr_index = find_index(min_time, diff, arr_cell_lines)

        # find max time for first fingerprint
        # set max_time = largest timestamp of 3rd sensor
        max_time = find_max_time(arr_wlan_lines[w_arr_index], arr_bt_lines[b_arr_index], arr_cell_lines[c_arr_index])

        # initialise fingerprint with position ID and time index
        fp = Fingerprint.Fingerprint(pos_id)
        fp.index = i
        # set timestamps belonging to time index
        fp.minTime = min_time
        fp.maxTime = max_time
        # set WLAN, BT and Cell value arrays
        if (w_arr_index != -1):
            fp = FingerprintRestoration.set_wlan_data(fp, arr_wlan_lines[w_arr_index], 1)
            # delete parsed array elements !!
            del arr_wlan_lines[w_arr_index]
        if (b_arr_index != -1):
            fp = FingerprintRestoration.set_bt_data(fp, arr_bt_lines[b_arr_index], 1)
            # delete parsed array elements !!
            del arr_bt_lines[b_arr_index]
        if (c_arr_index != -1):
            fp = FingerprintRestoration.set_cell_data(fp, arr_cell_lines[c_arr_index], 1)
            # delete parsed array elements !!
            del arr_cell_lines[c_arr_index]
        arr_fp.append(fp)
        # print(arr_fp[i])

    FingerprintStorage.store_fingerprint(arr_fp)
