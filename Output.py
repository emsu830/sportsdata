import csv
import SportClub
import itertools
import operator


# Function to sort a list of SportClub objects by sport. Returns 4 different lists each represents a sport (NFL, NBA, MLB, NHL)
# Takes a list of SportClub objects as an argument.
def sortBySport(l):
    NFL = []
    NBA = []
    MLB = []
    NHL = []

    for obj in l:
        if obj.getSport() == 'NFL':
            NFL.append(obj)
        if obj.getSport() == 'NBA':
            NBA.append(obj)
        if obj.getSport() == 'MLB':
            MLB.append(obj)
        if obj.getSport() == 'NHL':
            NHL.append(obj)
        
    return NFL, NBA, MLB, NHL


# Function to sort a list of SportClub objects by rank. Returns a list represents the sorted SportClub objects.
# Takes a list of SportClub objects of the same sport as an argument.
def sortByRank(sport):
    sport.sort(key=operator.attrgetter('city'))
    sport.sort(key=operator.attrgetter('count'), reverse=True)

    for obj in sport:
        obj.setRank(sport.index(obj) + 1)

    return sport


# Function to format the output file and output the first 3 ranked teams from each sport to a .csv file named Survey Database.csv
# in the current working directory.
# Takes 4 lists of sorted SportClub objects of the same sport as an argument.
def outputSports(NFL, NBA, MLB, NHL):
    sportList = [NFL, NBA, MLB, NHL]
    
    with open('Survey Database.csv', 'w', newline='') as outputFile:
        outputWriter = csv.writer(outputFile)
        ## header titles
        outputWriter.writerow(['City','Team Name','Sport','Team Ranking','Number of Times Picked'])

        for sport in sportList:
            for i in range(len(sport)):
                if i == 3:
                    break

                # list(sport).sort(key=lambda obj: (obj.getRank(), obj.getCity()))
                outputWriter.writerow([sport[i].getCity(), sport[i].getName(), sport[i].getSport(), sport[i].getRank(), sport[i].getCount()])