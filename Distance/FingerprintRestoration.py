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

from Fingerprint import Fingerprint
from Fingerprint import FingerprintAssembly
from Fingerprint.SensorData import WLAN
from Fingerprint.SensorData import BT
from Fingerprint.SensorData import Cell


# start help functions
def select_file_path():
    file_path = str(input("Please enter the absolute Path of the fingerprint csv file you want to restore:"))
    return file_path


def set_meta_data(fp, line):
    arr_line = line.split(";")
    fp.posID = arr_line[1]
    fp.index = int(arr_line[2])
    fp.minTime = int(arr_line[3])
    fp.maxTime = int(arr_line[4])
    return fp


# function to set the measured values of WLAN. Called with the fingerprint FP, the line string and an int for: 1:storation, 2:restoration. Returning the fingerprint with new data added
def set_wlan_data(fp, line, num):
    arr_line = line.split(";")
    counter = 1
    while ((counter + 1) < len(arr_line)):
        tmp_wlan = WLAN.WLAN()
        tmp_wlan.BSSID = arr_line[counter]
        if (num == 1):
            tmp_wlan.RSSI = FingerprintAssembly.delog(float(arr_line[counter + 1]))
        elif (num == 2):
            tmp_wlan.RSSI = float(arr_line[counter + 1])
        counter += 2
        fp.wlans.append(tmp_wlan)
        del tmp_wlan
    return fp


# function to set the measured values of BT. Called with the fingerprint FP, the line string and an int for: 1:storation, 2:restoration. Returning the fingerprint with new data added
def set_bt_data(fp, line, num):
    arr_line = line.split(";")
    counter = 1
    while ((counter + 1) < len(arr_line)):
        tmp_bt = BT.BT()
        tmp_bt.MAC = arr_line[counter]
        if (num == 1):
            tmp_bt.RSSI = FingerprintAssembly.delog(float(arr_line[counter + 1]))
        elif (num == 2):
            tmp_bt.RSSI = float(arr_line[counter + 1])
        counter += 2
        fp.bts.append(tmp_bt)
        del tmp_bt
    return fp


# function to set the measured values of Cell. Called with the fingerprint FP, the line string and an int for: 1:storation, 2:restoration. Returning the fingerprint with new data added
def set_cell_data(fp, line, num):
    arr_line = line.split(";")
    counter = 1
    while ((counter + 1) < len(arr_line)):
        tmp_cell = Cell.Cell()
        tmp_cell.typeID = arr_line[counter]
        if (num == 1):
            tmp_cell.RSRP = FingerprintAssembly.delog(float(arr_line[counter + 1]))
        elif (num == 2):
            tmp_cell.RSRP = float(arr_line[counter + 1])
        counter += 2
        fp.cells.append(tmp_cell)
        del tmp_cell
    return fp


# end help functions

# function to restore a fingerprint from a csv file
def restore_fp():
    file_path = select_file_path()
    # open fingerprint file
    fp_file = open(file_path, "r")
    # array of fingerprints
    arr_fps = []
    # read data from txt files line by line and save in array
    fp_lines = fp_file.readlines()
    counter = 0
    for line in fp_lines:
        if (line.find("FP") != -1):
            fp = Fingerprint.Fingerprint()
            # store metadata in right structure
            fp = set_meta_data(fp, line)
            counter += 1
        elif (line.find("WLAN") != -1):
            # store WLAN data in right structure
            fp = set_wlan_data(fp, line, 2)
            counter += 1
        elif (line.find("BT") != -1):
            # store BT data in right structure
            fp = set_bt_data(fp, line, 2)
            counter += 1
        elif (line.find("Cell") != -1):
            # store Cell data in right structure
            fp = set_cell_data(fp, line, 2)
            counter += 1
        if (counter != 0 and counter % 4 == 0):
            arr_fps.append(fp)
            del fp
    return arr_fps
