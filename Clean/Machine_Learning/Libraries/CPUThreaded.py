from threading import Thread
import time
import logging
import psutil

class CPUThreaded:
    """
    Run as a single Thread, starting with run and ending with terminate
    """

    def __init__(self):
        self._frequency = [ ]
        self._percentage = [ ]
        self._active = True


    def terminate(self):
        self._active = False

    def run(self, timeInterval):
        while self._active:
            self._cycle()
            time.sleep(timeInterval)
            logging.debug("updating lists")

    def _cycle(self):
        self._frequency.append(psutil.cpu_freq().current)
        self._percentage.append(psutil.cpu_percent())

    def getSumFrequency(self):
        return sum(self._frequency)

    def getCountFrequency(self):
        return len(self._frequency)

    def getAverageFrequency(self):
        sum = self.getSumFrequency()
        count = self.getCountFrequency()
        return sum/count

    def getMinFrequency(self):
        return min(self._frequency)

    def getRawFrequency(self):
        return self._frequency

    def getMaxFrequency(self):
        return max(self._frequency)

    def getLatestFrequency(self):
        return self._frequency[-1]

    #Percentage
    def getSumPercent(self):
        return sum(self._percentage)

    def getCountPercent(self):
        return len(self._percentage)

    def getAveragePercent(self):
        sum = self.getSumPercent()
        count = self.getCountPercent()
        return sum/count

    def getMinPercent(self):
        return min(self._percentage)

    def getRawPercent(self):
        return self._percentage

    def getMaxPercent(self):
        return max(self._percentage)

    def getLatestPercent(self):
        return self._percentage[-1]