class GenResults():
    def __init__(self):
        self.listOfResults = []
        self._resultsDict = {
            "method": "Test",
            "success": 0,
            "fails": 0,
            "cycles": 0,
            "Min_Time_Per_Cycle": 100000000000,
            "Avg_Time_Per_Cycle": 0,
            "Max_Time_Per_Cycle": 0,
            "timeSpent": 0,
            "Min_Attempts_Taken": 100000000000,
            "Avg_Attempts_Taken": 1,
            "Max_Attempts_Taken": 1,
            "Min_CPU_frequency": 100000000000,
            "Avg_CPU_frequency": 0,
            "Max_CPU_frequency": 0,
            "Min_CPU_percentage": 100000000000,
            "Avg_CPU_percentage": 0,
            "Max_CPU_percentage": 0,
            "Min_RAM_Bytes": 100000000000,
            "Avg_RAM_bytes": 0,
            "Max_RAM_Bytes": 0,
            "Min_RAM_percentage": 100000000000,
            "Avg_RAM_percentage": 0,
            "Max_RAM_percentage": 0,
            "SaveID": "",
            "ML_Range": 0
        }
        self._methods = {}


    def addResult(self, result):
        """
        Add result to list
        @param result: result
        @return: None
        """
        self.listOfResults.append(result)

    def getResult(self):
        """
        Returns one result with the average/count of values from all entered
        @return:
        """
        self._handleAll()
        for method in self._methods:

            self._methods[method] = self._merge(self._methods[method], method)
        return self._methods

    def _merge(self, dictList, method):
        """
        Merge results with from the same method/algorithm
        @param dictList: dictonary list from handleAll
        @param method: method identifier
        @return: Dictonary - merged results
        """
        avg = lambda listDictValues: sum(listDictValues) / len(listDictValues)
        laps = []
        cpuFreq = []
        cpuPercent = []
        attempts = []
        ramBytes = []
        ramPercent = []

        self._resultsDict = {
            "method": method,
            "success": 0,
            "fails": 0,
            "cycles": 0,
            "Min_Time_Per_Cycle": 100000000000,
            "Avg_Time_Per_Cycle": 0,
            "Max_Time_Per_Cycle": 0,
            "timeSpent": 0,
            "Min_Attempts_Taken": 100000000000,
            "Avg_Attempts_Taken": 1,
            "Max_Attempts_Taken": 1,
            "Min_CPU_frequency": 100000000000,
            "Avg_CPU_frequency": 0,
            "Max_CPU_frequency": 0,
            "Min_CPU_percentage": 100000000000,
            "Avg_CPU_percentage": 0,
            "Max_CPU_percentage": 0,
            "Min_RAM_Bytes": 100000000000,
            "Avg_RAM_bytes": 0,
            "Max_RAM_Bytes": 0,
            "Min_RAM_percentage": 100000000000,
            "Avg_RAM_percentage": 0,
            "Max_RAM_percentage": 0,
            "SaveID": "",
            "ML_Range": 0
        }

        for value in dictList:
            if value.success:
                self._resultsDict["success"] += 1
            else:
                self._resultsDict["fails"] += 1

            self._resultsDict["cycles"] += 1
            laps.append(value.timeSpent)
            cpuFreq.append(value.frequency)
            cpuPercent.append(value.percentage)
            attempts.append(value.attemptsTaken)
            ramBytes.append(value.ramBytes)
            ramPercent.append(value.ramPercent)

        self._resultsDict["Min_Time_Per_Cycle"] = min(laps)
        self._resultsDict["Avg_Time_Per_Cycle"] = avg(laps)
        self._resultsDict["Max_Time_Per_Cycle"] = max(laps)
        self._resultsDict["timeSpent"] = sum(laps)

        self._resultsDict["Min_Attempts_Taken"] = min(attempts)
        self._resultsDict["Avg_Attempts_Taken"] = avg(attempts)
        self._resultsDict["Max_Attempts_Taken"] = max(attempts)

        self._resultsDict["Min_CPU_frequency"] = min(cpuFreq)
        self._resultsDict["Avg_CPU_frequency"] = avg(cpuFreq)
        self._resultsDict["Max_CPU_frequency"] = max(cpuFreq)

        self._resultsDict["Min_CPU_percentage"] = min(cpuPercent)
        self._resultsDict["Avg_CPU_percentage"] = avg(cpuPercent)
        self._resultsDict["Max_CPU_percentage"] = max(cpuPercent)

        self._resultsDict["Min_RAM_Bytes"] = min(ramBytes)
        self._resultsDict["Avg_RAM_bytes"] = avg(ramBytes)
        self._resultsDict["Max_RAM_Bytes"] = max(ramBytes)

        self._resultsDict["Min_RAM_percentage"] = min(ramPercent)
        if self._resultsDict["Min_RAM_percentage"] < 0:
            self._resultsDict["Min_RAM_percentage"] = float(0)
        self._resultsDict["Avg_RAM_percentage"] = avg(ramPercent)
        self._resultsDict["Max_RAM_percentage"] = max(ramPercent)

        #Attempt to reduce ram usage between cycles
        laps.clear()
        cpuFreq.clear()
        cpuPercent.clear()
        attempts.clear()
        ramBytes.clear()
        ramPercent.clear()

        return self._resultsDict

    def _handleAll(self):
        """
        split into the different methods, used when multiple methods are tested at once
        @return: None
        """
        self._methods = {}
        for result in self.listOfResults:
            if result.method not in self._methods.keys():
                self._methods[result.method] = [result]
            else:
                self._methods[result.method].append(result)
