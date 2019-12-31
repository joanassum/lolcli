import csv
import os

storage_path = os.environ['LOLCLI_PATH'] + '/runes.csv'

def add_runes(name, runes_dict):
    # Create csv file for storage if not exist
    open(storage_path, "a")

    # Read the csv file to check if the runes with same name already exist.
    with open(storage_path, 'r') as csvfile:
        for line in csvfile:
            if line.split(",")[0] == name:
                print("Runes set with the same name already exist")
                # TODO prompt for y/n to continue
                return

    # Convert dict of data to row
    # [name, primary path, keystone, primary slot 1, 2, 3, secondary path, secondary slot 1, 2, offensive, flex, defence]
    runes = to_row(name, runes_dict)

    # Write to the csv file
    with open(storage_path, 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(runes)

def to_row(name, runes_dict):
    return [name, runes_dict['primarypath'], runes_dict['keystone'], runes_dict['primaryslot1'], runes_dict['primaryslot2'], runes_dict['primaryslot3'],
        runes_dict['secondarypath'], runes_dict['secondaryslot1'], runes_dict['secondaryslot2'], runes_dict['offensive'], runes_dict['flex'], runes_dict['defence']]

def to_dict(row):
    return {
        'primarypath': row[1],
        'keystone': row[2],
        'primaryslot1': row[3],
        'primaryslot2': row[4],
        'primaryslot3': row[5],
        'secondarypath': row[6],
        'secondaryslot1': row[7],
        'secondaryslot2': row[8],
        'offensive': row[9],
        'flex': row[10],
        'defence': row[11],
    }

def get_runes(name):
    # Read the csv file to check if the runes with same name already exist.
    with open(storage_path, 'r') as csvfile:
        for line in csv.reader(csvfile):
            if line[0] == name:
                return to_dict(line)