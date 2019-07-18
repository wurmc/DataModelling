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

# functionality to find and calculate the average fp of a fp array

from Fingerprint import Fingerprint
from Fingerprint.SensorData import WLAN
from Fingerprint.SensorData import BT
from Fingerprint.SensorData import Cell
from Fingerprint import AvgBase
import statistics


def find_index(string, list):
    for x in list:
        if (x.id == string):
            i = list.index(x)
            return i
    return -1


def build_avg_fp(arr_fps):
    avg_fp = Fingerprint.Fingerprint()

    # initialize meta data of avg fp
    avg_fp.posID = arr_fps[0].posID
    avg_fp.index = -1
    avg_fp.minTime = arr_fps[0].minTime
    avg_fp.maxTime = arr_fps[-1].maxTime

    # set resource sensor data for avg fp
    arr_wlans = []
    arr_bts = []
    arr_cells = []
    for o_fp in arr_fps:
        for o_wlan in o_fp.wlans:
            x = find_index(o_wlan.BSSID, arr_wlans)
            if (x == -1):
                base_wlan = AvgBase.AvgBase(o_wlan.BSSID)
                base_wlan.signals.append(o_wlan.RSSI)
                arr_wlans.append(base_wlan)
                del base_wlan
            else:
                arr_wlans[x].signals.append(o_wlan.RSSI)
        for o_bt in o_fp.bts:
            x = find_index(o_bt.MAC, arr_bts)
            if (x == -1):
                base_bt = AvgBase.AvgBase(o_bt.MAC)
                base_bt.signals.append(o_bt.RSSI)
                arr_bts.append(base_bt)
                del base_bt
            else:
                arr_bts[x].signals.append(o_bt.RSSI)
        for o_cell in o_fp.cells:
            x = find_index(o_cell.typeID, arr_cells)
            if (x == -1):
                base_cell = AvgBase.AvgBase(o_cell.typeID)
                base_cell.signals.append(o_cell.RSRP)
                arr_cells.append(base_cell)
                del base_cell
            else:
                arr_cells[x].signals.append(o_cell.RSRP)

    # # help function to create histograms of sensor data
    # w_name = "E:/Clara/Studium/Master/MA/Messungen/20190625_FP_Referenz/4Flur/Mi9/20190625_D14-4Hall-11_WLAN_signals.csv"
    # b_name = "E:/Clara/Studium/Master/MA/Messungen/20190625_FP_Referenz/4Flur/Mi9/20190625_D14-4Hall-11_BT_signals.csv"
    # c_name = "E:/Clara/Studium/Master/MA/Messungen/20190625_FP_Referenz/4Flur/Mi9/20190625_D14-4Hall-11_Cell_signals.csv"
    #
    # w_file = open(w_name, 'w')
    # b_file = open(b_name, 'w')
    # c_file = open(c_name, 'w')
    # for w_item in arr_wlans:
    #     w_file.write(w_item.id)
    #     w_file.write(';')
    #     for w_sig in w_item.signals:
    #         w_file.write(str(w_sig))
    #         w_file.write(';')
    #     w_file.write('\n')
    # for b_item in arr_bts:
    #     b_file.write(b_item.id)
    #     b_file.write(';')
    #     for b_sig in b_item.signals:
    #         b_file.write(str(b_sig))
    #         b_file.write(';')
    #     b_file.write('\n')
    # for c_item in arr_cells:
    #     c_file.write(c_item.id)
    #     c_file.write(';')
    #     for c_sig in c_item.signals:
    #         c_file.write(str(c_sig))
    #         c_file.write(';')
    #     c_file.write('\n')
    # w_file.close()
    # b_file.close()
    # c_file.close()

    # find avg of every wlan, bt, cell signal
    for wlan_base in arr_wlans:
        tmp_wlan = WLAN.WLAN()
        tmp_wlan.BSSID = wlan_base.id
        tmp_wlan.RSSI = statistics.mean(wlan_base.signals)
        avg_fp.wlans.append(tmp_wlan)
        del tmp_wlan

    for bt_base in arr_bts:
        tmp_bt = BT.BT()
        tmp_bt.MAC = bt_base.id
        tmp_bt.RSSI = statistics.mean(bt_base.signals)
        avg_fp.bts.append(tmp_bt)
        del tmp_bt

    for cell_base in arr_cells:
        tmp_cell = Cell.Cell()
        tmp_cell.typeID = cell_base.id
        tmp_cell.RSRP = statistics.mean(cell_base.signals)
        avg_fp.cells.append(tmp_cell)
        del tmp_cell

    return avg_fp
