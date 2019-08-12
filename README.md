# DataModelling
This program was developed in the context of the master theesis of wurmc.

Program's menu offers 5 possible choices:
1) Select relevant data from measured sensor data and store it into a csv file
2) Assemble fingerprints with linear values and store it into a csv file
3) Select reference fingerprint by creating a fictional average fingerprint for one position and store it into a csv file
4) Calculate distance between two sets of relevant data (lists of fingerprints

#####1) Select relevant data from measured sensor data and store it into a csv file
This point selects relevant data from a given txt input file of a sensor measured by DataLogger app (https://github.com/sussexwearlab/DataLogger), such as timestamps, BSSID and RSSI of WLAN data.
The relevant data is stored in a new given csv file. The targeted sensor can be chosen during run time.

#####2) Assemble fingerprints with linear values and store it into a csv file
This point assembles fingerprints out of WLAN, BT and Cell sensor data like structured in "FP_DataModel.drawio".
The data is stored with linear values (instead of original dBm" into a new csv file, like exemplary shown in "Fingerprint/csvStructure.txt".

#####3) Select reference fingerprint by creating a fictional average fingerprint for one position and store it into a csv file
This point selects a reference fingerprint which is located as near in the middle of all fingerprints of the list as possible.
This is done by calculating an average fingerprint out of the whole list and calculating the distance between it and all original fingerprints to find the reference one.
The found reference fingerprint is then stored into a new csv file.

#####4) Calculate distance between two sets of relevant data (lists of fingerprints)
This point calculates the distance between each fingerprint pair out of two lists of fingerprints from previously stored fingerprint csv files.
If each list contains 10 fingerprints, 10x10=100 distances are calculated.