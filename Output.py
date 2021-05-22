import csv
import SportClub
import operator


'''
parameter: list of unsorted SportClub objects
return: 4 lists containing SportClub objects for each sport
sorts the list of SportClub objects by sport (NFL, NBA, MLB, NHL)
'''
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


'''
parameter: list of SportClub objects of the same sport
return: sorted list of SportClub objects of the same sport
'''
def sortByRank(sport):
    sport.sort(key=operator.attrgetter('city'))
    sport.sort(key=operator.attrgetter('count'), reverse=True)

    for obj in sport:
        obj.setRank(sport.index(obj) + 1)

    return sport


'''
parameter: sorted list of SportClub objects of the same sport
return: Survey Database.csv
the consolidated Survey Database.csv file contains the top 3 ranked teams
'''
def outputSports(NFL, NBA, MLB, NHL):
    sportList = [NFL, NBA, MLB, NHL]
    
    with open('Survey Database.csv', 'w', newline='') as outputFile:
        outputWriter = csv.writer(outputFile)
        ## database header titles
        outputWriter.writerow(['City','Team Name','Sport','Team Ranking','Number of Times Picked'])

        for sport in sportList:
            for i in range(len(sport)):
                if i == 3:
                    break

                outputWriter.writerow([sport[i].getCity(), sport[i].getName(), sport[i].getSport(), sport[i].getRank(), sport[i].getCount()])
