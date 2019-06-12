# contains all function calls and main functionality to structure the project

from RelData import SelectRelData
from Fingerprint import AssembleFingerprint
from Fingerprint import delog
from Distance import CalcDistance

# main menu for calling drifferent functionality in while loop
x = 404
while (x != 0):
    x = int(input("Please enter an integer from 0 to 4 for the following choices: \n0: exit and stop program, "
                  "\n1: Select relevant data from measured sensor data,  \n2: Assemble Fingerprint with dBm values, "
                  "\n3: Delog RSSI values from assembled fingerprint, "
                  "\n4: Calculate distance between two data sets of relevant data"))
    # error for invalid input
    if (x >= 4):
        print("Invalid input. Please enter int from 0 to 4.")

    # handling of different options
    if (x == 1):
        SelectRelData.selectRelData()
    elif (x == 2):
        AssembleFingerprint
    elif (x == 3):
        delog
    elif (x == 4):
        CalcDistance
