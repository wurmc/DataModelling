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

# start of help functions
def set_file_path():
    file_path = str(input(
        "Please enter absolute file path including the name of the file you want to create for storing the fingerprints"))
    return file_path


# end of help functions

# function to store the fingerprint in a csv file
def store_fingerprint(arr_fp):
    file_path = set_file_path()
    fp_file = open(file_path, "a")
    for fp in arr_fp:
        # append metadata to file
        fp_file.write("fp;")
        fp_file.write(fp.posID + ";")
        fp_file.write(fp.index + ";")
        fp_file.write(fp.minTime + ";")
        fp_file.write(fp.maxTime + "\n")

        # append WLAN data to file
        fp_file.write("WLAN;")
        for wlan in fp.wlans:
            fp_file.write(wlan.BSSID + ";")
            fp_file.write(wlan.RSSI + ";")
        fp_file.write("\n")

        # append BT data to file
        fp_file.write("BT;")
        for bt in fp.bts:
            fp_file.write(bt.MAC + ";")
            fp_file.write(bt.RSSI + ";")
        fp_file.write("\n")

        # append Cell data to file
        fp_file.write("Cell;")
        for cell in fp.cells:
            fp_file.write(cell.typeID + ";")
            fp_file.write(cell.RSRP + ";")
        fp_file.write("\n")
    fp_file.close()
