"""
Name: Emily Su
Project: Sports Data Repository
"""
from pathlib import Path
import csv
import glob, os
from SportClub import SportClub


'''custom exceptions'''
class CorruptFile(Exception):
    '''File cannot be read by readOneFile'''
    pass


# Function to read one .csv file in the current working directory. Returns a list of tuples of three fields (City, Name and Sport).
# Takes file name as an argument (with .csv). For example, name could be test.csv
def readOneFile(name):
    listOfItems = []
    corrupted = False

    csvFile = open(name, 'r')
    csvReader = csv.reader(csvFile)

    header = next(csvReader)
    if header[0] != "City" or header[1] != "Team Name" or header[2] != "Sport":
        corrupted = True

    for row in csvReader:
        ## invalid file: more/less columns than expected
        if len(row) != 3:
            corrupted = True
        ## invalid file: check for empty cells
        elif row[0] == "" or row[1] == "" or row[2] == "":
            corrupted = True
        ## invalid file: not a pre-defined sport
        elif row[2] not in ["NFL", "NBA", "MLB", "NHL"]:
            corrupted = True

        if corrupted == False:
            listOfItems.append(tuple([row[0], row[1], row[2]]))
        else:
            break

    csvFile.close()
    if corrupted == True:
        raise CorruptFile

    return listOfItems


# Function to read all .csv files in the current working directory. Returns a list of SportClub objects.
# This function should create a SportClub object if the tuples fields are new or just increment if an object already made.
# This function will produce a file called Report.txt which has information about the files you read.
# This function will produce a file called Error log.txt which has information about the error files you read.
def readAllFiles():
    fileCount = 0
    itemCount = 0
    SportDict = {}
    report = open('Report.txt', 'w')
    error = open('Error log.txt', 'w')
    errorList = ""
    listOfItems = []
    corrupted = False

    csv_files = glob.glob("file*.csv")
    for name in csv_files:
        try:
            ## listOfItems is a list containing tuples in the format (City, Team Name, Sport)
            listOfItems = readOneFile(name)
            fileCount += 1
            itemCount += len(listOfItems)

            ## row is an individual tuple in the format (City, Team Name, Sport)
            for row in listOfItems:
                key = row[0] + row[1]
                ## check if Team Name has been recorded before
                if key in SportDict.keys():
                    SportDict[key].incrementCount()
                else:
                    obj = SportClub()
                    obj.setCity(row[0])
                    obj.setName(row[1])
                    obj.setSport(row[2])
                    obj.incrementCount()
                    SportDict[key] = obj

        except CorruptFile:
            corrupted = True
            if len(errorList) == 0:
                errorList = errorList + name
            else:
                errorList = errorList + ',' + name

    if corrupted == True:
        error.write(errorList)
    else:
        error.write("None")
    error.close()

    report.write('Number of files read: ' + str(fileCount)+ '\n')
    report.write('Number of items read: ' + str(itemCount))
    report.close()

    return list(SportDict.values())

