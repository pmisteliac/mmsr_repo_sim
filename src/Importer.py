import csv


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

        return names, features