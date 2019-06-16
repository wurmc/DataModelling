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

# TODO:
# create public 2-dimensional array
# with columns for every data of sensors to list their measured data in rows

from RelData import Bluetooth
from RelData import Cell
from RelData import Light
from RelData import Location
from RelData import Magnetometer
from RelData import Orientation
from RelData import Pressure
from RelData import Satellite
from RelData import WLAN

# Help functions:
# create function, which asks user for choice of file including the absolute path of it
def select_ex_file():
    existing_file_path = str(
        input("Please enter the absolute path of the existing file you want to work with (use / not win \): "))
    return existing_file_path


def select_new_file():
    new_file_path = str(
        input("Please enter the absolute path of the new file you want to work with (use / not win \): "))
    return new_file_path


# create function, which asks user for choice of sensor
def choose_sensor(x):
    while (x < 1 or x > 9):
        x = int(input(
            "Please enter an integer of 1 to 9 (1: Bluetooth, 2: Cell, 3: Light, 4: Location, 5: Magnetometer, 6: Orientation, 7: Pressure, 8: Satellite, 9: Wifi): "))
    return x


# create function, which calls the get_rel_data method of the sensor
def select_sensor(x, line):
    if (x == 1):
        rel_data_tmp = Bluetooth.get_rel_data(line)
        return rel_data_tmp
    elif (x == 2):
        rel_data_tmp = Cell.get_rel_data(line)
        return rel_data_tmp
    elif (x == 3):
        rel_data_tmp = Light.get_rel_data(line)
        return rel_data_tmp
    elif (x == 4):
        rel_data_tmp = Location.get_rel_data(line)
        return rel_data_tmp
    elif (x == 5):
        rel_data_tmp = Magnetometer.get_rel_data(line)
        return rel_data_tmp
    elif (x == 6):
        rel_data_tmp = Orientation.get_rel_data(line)
        return rel_data_tmp
    elif (x == 7):
        rel_data_tmp = Pressure.getRelData(line)
        return rel_data_tmp
    elif (x == 8):
        rel_data_tmp = Satellite.get_rel_data(line)
        return rel_data_tmp
    elif (x == 9):
        rel_data_tmp = WLAN.get_rel_data(line)
        return rel_data_tmp


def select_rel_data():
    # select the right file to read, maybe by asking the user for an absolute path
    ex_file_path = select_ex_file()
    new_file_path = select_new_file()

    # open existing txt file to read from
    # ex_file_path = "E:/Clara/Studium/Master/MA/20190519_Verarbeitungskette/test_BT.txt"
    ef = open(ex_file_path, "r")

    # open new csv file to write in with adaptet path and same name
    # new_file_path = "E:/Clara/Studium/Master/MA/20190519_Verarbeitungskette/neu/test_BT.csv"
    nf = open(new_file_path, "w")

    # ask user for choice of sensor
    x = 0
    x = choose_sensor(x)

    # create empty string, which is needed later
    rel_data_final = ""

    # read data from txt files line by line
    ef_lines = ef.readlines()
    for line in ef_lines:
        # print(line);

        # call specific sensor to select and return relevant data
        rel_data = select_sensor(x, line)

        # add returned data (complete line) to string
        rel_data_final += rel_data

        # write string with relevant line of data into the new csv file and close with newline
        rel_data_final += "\n"
        nf.write(rel_data_final)
        rel_data_final = ""

    # close all open files
    ef.close()
    nf.close()
