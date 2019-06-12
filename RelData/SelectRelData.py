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
from RelData import Wifi


# Help functions:
# create function, which asks user for choice of file including the absolute path of it
def selectExFile():
    existingFilePath = str(
        input("Please enter the absolute path of the existing file you want to work with (use / not win \): "))
    return existingFilePath


def selectNewFile():
    newFilePath = str(
        input("Please enter the absolute path of the new file you want to work with (use / not win \): "))
    return newFilePath


# create function, which asks user for choice of sensor
def choseSensor(x):
    while (x < 1 or x > 9):
        x = int(input(
            "Please enter an integer of 1 to 9 (1: Bluetooth, 2: Cell, 3: Light, 4: Location, 5: Magnetometer, 6: Orientation, 7: Pressure, 8: Satellite, 9: Wifi): "))
    return x


# create function, which calls the getRelData method of the sensor
def selectSensor(x, line):
    if (x == 1):
        rel_data_tmp = Bluetooth.getRelData(line)
        return rel_data_tmp
    elif (x == 2):
        rel_data_tmp = Cell.getRelData(line)
        return rel_data_tmp
    elif (x == 3):
        rel_data_tmp = Light.getRelData(line)
        return rel_data_tmp
    elif (x == 4):
        rel_data_tmp = Location.getRelData(line)
        return rel_data_tmp
    elif (x == 5):
        rel_data_tmp = Magnetometer.getRelData(line)
        return rel_data_tmp
    elif (x == 6):
        rel_data_tmp = Orientation.getRelData(line)
        return rel_data_tmp
    elif (x == 7):
        rel_data_tmp = Pressure.getRelData(line)
        return rel_data_tmp
    elif (x == 8):
        rel_data_tmp = Satellite.getRelData(line)
        return rel_data_tmp
    elif (x == 9):
        rel_data_tmp = Wifi.getRelData(line)
        return rel_data_tmp


def selectRelData():
    # select the right file to read, maybe by asking the user for an absolute path
    exFilePath = selectExFile()
    newFilePath = selectNewFile()

    # open existing txt file to read from
    # exFilePath = "E:/Clara/Studium/Master/MA/20190519_Verarbeitungskette/test_BT.txt"
    ef = open(exFilePath, "r")

    # open new csv file to write in with adaptet path and same name
    # newFilePath = "E:/Clara/Studium/Master/MA/20190519_Verarbeitungskette/neu/test_BT.csv"
    nf = open(newFilePath, "w")

    # ask user for choice of sensor
    x = 0
    x = choseSensor(x)

    # create empty string, which is needed later
    rel_data_final = ""

    # read data from txt files line by line
    ef_lines = ef.readlines()
    for line in ef_lines:
        print(line);

        # call specific sensor to select and return relevant data
        rel_data = selectSensor(x, line)

        # add returned data (complete line) to string
        rel_data_final += rel_data

        # write string with relevant line of data into the new csv file and close with newline
        rel_data_final += "\n"
        nf.write(rel_data_final)
        rel_data_final = ""

    # close all open files
    ef.close()
    nf.close()
