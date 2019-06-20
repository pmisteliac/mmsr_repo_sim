import csv
import os


# read a vsc file with the following format:
# first column of each row is the name of the repository
# other columns of each row represent all features of the repository
def read(filepath):
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile)
        names = []
        features = []
        for row in reader:
            names.append(row[0])
            features.append(row[1:])

        print("Red ",  filepath)
        return names, features


# write content to a csv file
def write(filePath, content):
    with open(filePath, mode='w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow([element for element in content])
        print("Wrote to ", filePath)


def createDir(dirPath):
    os.mkdir(dirPath)
    print('Created directory: ' + dirPath)