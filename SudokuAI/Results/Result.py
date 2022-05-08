import csv

class Result:
    def __init__(self):
        self._fieldnames = ["method", "success", "fails", "cycles",
                            "Min_Time_Per_Cycle", "Avg_Time_Per_Cycle", "Max_Time_Per_Cycle", "timeSpent",
                            "Min_Attempts_Taken", "Avg_Attempts_Taken", "Max_Attempts_Taken",
                            "Min_CPU_frequency", "Avg_CPU_frequency", "Max_CPU_frequency",
                            "Min_CPU_percentage", "Avg_CPU_percentage", "Max_CPU_percentage",
                            "Min_RAM_Bytes", "Avg_RAM_bytes", "Max_RAM_Bytes",
                            "Min_RAM_percentage", "Avg_RAM_percentage", "Max_RAM_percentage",
                            "SaveID", "ML_Range"]
        self.results = {
            "method": "",
            "success": 0,
            "fails": 0,
            "cycles": 0,
            "Min_Time_Per_Cycle": 0,
            "Avg_Time_Per_Cycle": 0,
            "Max_Time_Per_Cycle": 0,
            "timeSpent": 0,
            "Min_Attempts_Taken": 1,
            "Avg_Attempts_Taken": 1,
            "Max_Attempts_Taken": 1,
            "Min_CPU_frequency": 0,
            "Avg_CPU_frequency": 0,
            "Max_CPU_frequency": 0,
            "Min_CPU_percentage": 0,
            "Avg_CPU_percentage": 0,
            "Max_CPU_percentage": 0,
            "Min_RAM_Bytes": 0,
            "Avg_RAM_bytes": 0,
            "Max_RAM_Bytes": 0,
            "Min_RAM_percentage": 0,
            "Avg_RAM_percentage": 0,
            "Max_RAM_percentage": 0,
            "SaveID": " ",
            "ML_Range": 0
        }

        self._fileName = "Results/Results.csv"

    def csvSave(self):
        """
        Save Dictonary to csv file
        @return: None
        """
        try:
            with open(self._fileName, "a", encoding='UTF8', newline='') as csvFile:
                typist = csv.DictWriter(csvFile, fieldnames=self._fieldnames)
                if csvFile.tell() == 0:
                    typist.writeheader()

                typist.writerow(self.results)

        except IOError:
            print("Error with creating Results.csv file")

        finally:
            csvFile.close()

    def saveID(self, val):
        """
        Update SaveID, used in tracking (cycles, repeats)
        @param val: cycles: repeats
        @return: None
        """
        self.results["SaveID"] = val

    def updateMLSaved(self, val):
        """
        Update the number of saved solutions ML has, useful in identifying results
        @param val: number of saved solutions
        @return: None
        """
        self.results["ML_Range"] = val