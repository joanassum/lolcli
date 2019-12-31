import csv
import os

storage_path = os.environ['LOLCLI_PATH'] + '/runes.csv'

def addrunes(name, runes_dict):
    # Create csv file for storage if not exist
    open(storage_path, "a")

    # Read the csv file to check if the runes with same name already exist.
    with open(storage_path, 'r') as csvfile:
        for line in csvfile:
            if line.split(",")[0] == name:
                print("Runes set with the same name already exist")
                # TODO prompt for y/n to continue
                return

    # Organise the row of data
    # [name, primary path, keystone, primary slot 1, 2, 3, secondary path, secondary slot 1, 2, offensive, flex, defence]
    runes = [name, runes_dict['primarypath'], runes_dict['keystone'], runes_dict['primaryslot1'], runes_dict['primaryslot2'], runes_dict['primaryslot3'],
        runes_dict['secondarypath'], runes_dict['secondaryslot1'], runes_dict['secondaryslot2'], runes_dict['offensive'], runes_dict['flex'], runes_dict['defence']]

    # Write to the csv file
    with open(storage_path, 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(runes)
