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

# contains all function calls and main functionality to structure the project

from RelData import RelDataSelection
from Fingerprint import FingerprintAssembly
from Distance import DistanceCalculation

# main menu for calling drifferent functionality in while loop
x = 404
while (x != 0):
    x = int(input("Please enter an integer from 0 to 4 for the following choices: \n0: exit and stop program, "
                  "\n1: Select relevant data from measured sensor data,  \n2: Assemble Fingerprint with linear values, "
                  "\n3: Calculate distance between two data sets of relevant data"))
    # error for invalid input
    if (x > 3):
        print("Invalid input. Please enter int from 0 to 4.")

    # handling of different options
    if (x == 1):
        RelDataSelection.select_rel_data()
    elif (x == 2):
        FingerprintAssembly.assemble_fingerprint()
    elif (x == 3):
        DistanceCalculation.calculate_distance()
