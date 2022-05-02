#Checks the for duplicates in the dataset, and number saved
total_solutions = 6670903752021072936960
fileLocation = "ML_Storage.txt"
fileLocation = "With_Training/ML_250000.txt"
#fileLocation = "Without_Training/ML_1000.txt"
file = open(fileLocation, "r")
lines = file.readlines()
print("No. of Records: ", len(lines))
if len(lines) != len(set(lines)):
    print("Duplicates")
else:
    print("All are Unique")

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
logging.warning('Admin logged out')
logging.info(f"This is a message")