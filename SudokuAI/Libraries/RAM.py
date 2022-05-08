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

    def lap(self):
        """
        Measure time since last call
        @return: None
        """
        self._laps.append(psutil.virtual_memory()[2])

    def end(self):
        """
        End the Thread
        @return: start time, highest recorded and array - laps
        """
        self._continue = False
        return self._start, self._highest, self._laps

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
        self._laps = []

"""
rd = RamDetection()
tr = threading.Thread(target=rd.start, args = (1, ))
for t in range(20):
    rd.lap()
    time.sleep(1)
temp = []
#for i in range(100):
    #temp.append("This is a testing environment")

start, highest, laps = rd.end()
#print(f"{start, highest} \n {rd.startUsed(), rd.startPercent(), rd.available()} \n {rd.highestUsed(), rd.highestPercent()} \n {rd.differencePercent(), rd.differenceUsed()}")
print(f"{laps, max(laps), len(laps)}")
print(f"{start, min(laps), max(laps)}")"""