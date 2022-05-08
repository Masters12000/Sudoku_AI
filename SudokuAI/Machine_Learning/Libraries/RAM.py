import time
import psutil

class RamDetection():
    def __init__(self):
        self._start = psutil.virtual_memory()
        self._highest = psutil.virtual_memory()
        self._continue = True
        self._laps = []

    def start(self, interval = 1):
        """
        Start of Thread
        @param interval: Time Interval between recording
        @return: None
        """
        while self._continue:
            temp = psutil.virtual_memory()
            if self._highest[3] < temp[3]:
                self._highest = temp
            time.sleep(interval)

    def end(self):
        """
        End the Thread
        @return: start time, highest recorded and array - laps
        """
        self._continue = False
        return self._start, self._highest

    def startPercent(self):
        return self._start[2]

    def startUsed(self):
        return self._start[3]

    def available(self):
        return self._start[1]

    def highestPercent(self):
        return self._highest[2]

    def highestUsed(self):
        return self._highest[1]

    def differencePercent(self):
        return self._highest[2] - self._start[2]

    def differenceUsed(self):
        return self._highest[3] - self._start[3]

    def refresh(self):
        self._start = psutil.virtual_memory()
        self._highest = psutil.virtual_memory()
