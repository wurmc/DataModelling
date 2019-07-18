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

# functionality to calculate the distance between 2 fingerprints

from Distance import FingerprintRestoration
import math


# find differences between 2 sets of strings (BSSID, MAC or typeID)
def find_set_diff(x_set, y_set):
    diff_set = x_set.symmetric_difference(y_set)
    return diff_set  # len(diff_set) * 2 = difference of unmatched fields (case 3)


# find intersections between 2 sets of strings (BSSID, MAC orr typeID)
def find_set_intersect(x_set, y_set):
    inter_set = x_set.intersection(y_set)
    return inter_set  # prep for calc float diff for matched fields


# calculate the sum of sifferences between fingerprints
def calc_diff(x_fp, y_fp):
    # initializations
    diff_sum = 0.0
    x_set_wlan = set()
    x_set_bt = set()
    x_set_cell = set()
    y_set_wlan = set()
    y_set_bt = set()
    y_set_cell = set()

    # wlans
    for x_wlan in x_fp.wlans:
        x_set_wlan.add(x_wlan.BSSID)
    for y_wlan in y_fp.wlans:
        y_set_wlan.add(y_wlan.BSSID)

    # calculate differences for number of fields
    diff_set_wlan = find_set_diff(x_set_wlan, y_set_wlan)  # for every sensor
    # len(diff_set) * 2 = difference of unmatched fields (case 3)
    diff_sum += len(diff_set_wlan) * 2

    # calculate differences for signal strengths
    inter_set_wlan = find_set_intersect(x_set_wlan, y_set_wlan)  # for every sensor
    for i in inter_set_wlan:
        tmp_x = 0.0
        tmp_y = 0.0
        for x in x_fp.wlans:
            if (i == x.BSSID):
                tmp_x = x.RSSI
        for y in y_fp.wlans:
            if (i == y.BSSID):
                tmp_y = y.RSSI
        diff_sig = math.sqrt((tmp_x - tmp_y) ** 2) / max(tmp_x, tmp_y)
        diff_sum += diff_sig

    # bts
    for x_bt in x_fp.bts:
        x_set_bt.add(x_bt.MAC)
    for y_bt in y_fp.bts:
        y_set_bt.add(y_bt.MAC)

    # calculate differences for number of fields
    diff_set_bt = find_set_diff(x_set_bt, y_set_bt)  # for every sensor
    # len(diff_set) * 2 = difference of unmatched fields (case 3)
    diff_sum += len(diff_set_bt) * 2

    # calculate differences for signal strengths
    inter_set_bt = find_set_intersect(x_set_bt, y_set_bt)  # for every sensor
    for i in inter_set_bt:
        tmp_x = 0.0
        tmp_y = 0.0
        for x in x_fp.bts:
            if (i == x.MAC):
                tmp_x = x.RSSI
        for y in y_fp.bts:
            if (i == y.MAC):
                tmp_y = y.RSSI
        diff_sig = math.sqrt((tmp_x - tmp_y) ** 2) / max(tmp_x, tmp_y)
        diff_sum += diff_sig

    # cells
    for x_cell in x_fp.cells:
        x_set_cell.add(x_cell.typeID)
    for y_cell in y_fp.cells:
        y_set_cell.add(y_cell.typeID)

    # calculate differences for number of fields
    diff_set_cell = find_set_diff(x_set_cell, y_set_cell)  # for every sensor
    # len(diff_set) * 2 = difference of unmatched fields (case 3)
    diff_sum += len(diff_set_cell) * 2

    # calculate differences for signal strengths
    inter_set_cell = find_set_intersect(x_set_cell, y_set_cell)  # for every sensor
    for i in inter_set_cell:
        tmp_x = 0.0
        tmp_y = 0.0
        for x in x_fp.cells:
            if (i == x.typeID):
                tmp_x = x.RSRP
        for y in y_fp.cells:
            if (i == y.typeID):
                tmp_y = y.RSRP
        diff_sig = math.sqrt((tmp_x - tmp_y) ** 2) / max(tmp_x, tmp_y)
        diff_sum += diff_sig

    return diff_sum


# save the distance array in csv file
def save_dist(arr_d, x_arr_index, y_arr_index):
    file_path = str(input("Where shall the distances be saved?"))
    file = open(file_path, "w")
    for d, x, y in zip(arr_d, x_arr_index, y_arr_index):
        file.write(str(x))
        file.write(";")
        file.write(str(y))
        file.write(";")
        file.write(str(d))
        file.write("\n")
    print("File written!")


# clculate distance between fingerprints
def start_distance_calc():
    # restore fingerprints from saved csv
    x_arr_fps = FingerprintRestoration.restore_fp()
    y_arr_fps = FingerprintRestoration.restore_fp()
    print("X: ")
    print(x_arr_fps)
    print("Y: ")
    print(y_arr_fps)

    # initialise array for distances
    arr_d = []
    x_arr_index = []
    y_arr_index = []

    # go through fingerprint arrays
    for x_fp in x_arr_fps:
        for y_fp in y_arr_fps:
            d = calculate_distance(x_fp, y_fp)
            arr_d.append(d)
            x_arr_index.append(x_arr_fps.index(x_fp) + 1)
            y_arr_index.append(y_arr_fps.index(y_fp) + 1)

    # save calculated distances in csv file
    save_dist(arr_d, x_arr_index, y_arr_index)


def calculate_distance(x_fp, y_fp):
    # initializations
    n_x = 0
    n_y = 0
    n_max = 0
    d = 0.0
    # compare number of data fields in fingerprint
    n_x = (len(x_fp.wlans) * 2) + (len(x_fp.bts) * 2) + (len(x_fp.cells) * 2)
    n_y = (len(y_fp.wlans) * 2) + (len(y_fp.bts) * 2) + (len(y_fp.cells) * 2)
    n_max = n_x + n_y

    # calculate distance out of differences
    d = (1 / n_max) * calc_diff(x_fp, y_fp)

    # print calculated distances
    # print(x_fp)
    # print(y_fp)
    # print("The distance between the two fingerprints is: " + str(d))

    return d
