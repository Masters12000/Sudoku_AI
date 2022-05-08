lines = []
fileLocation = "ML_Storage.txt"
NoToSave = 500000
fileName = "ML_" + str(NoToSave) + ".txt"
print(f"Saving to {fileName}")

source = open(fileLocation, "r")
sourceLines = source.readlines()
if len(sourceLines) >= NoToSave:
    for l in range(NoToSave):
        lines.append(sourceLines[l])

    with open(fileName, "w") as destination:
        destination.writelines(lines)
        destination.close()
        print("Saved")
else:
    print(f"Error - Source does not have enough records (Source-> {len(sourceLines)} < {NoToSave} <-Requested)")