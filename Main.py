import Input
import Output
import SportClub
import csv

def main():
    # with open('file4.csv', 'r') as csvFile:
    #     csvReader = csv.reader(csvFile, delimiter=',')
    #
    #     for row in csvReader:
    #         print(row, len(row))
    #

    NFL, NBA, MLB, NHL = Output.sortBySport(Input.readAllFiles())
    sortedNFL = Output.sortByRank(NFL)
    sortedNBA = Output.sortByRank(NBA)
    sortedMLB = Output.sortByRank(MLB)
    sortedNHL = Output.sortByRank(NHL)
    Output.outputSports(sortedNFL, sortedNBA, sortedMLB, sortedNHL)


if __name__ == "__main__":
    main()
