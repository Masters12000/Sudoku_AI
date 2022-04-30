import time

class Timer:
    def __init__(self):
        """
        Start the timer
        """
        self._start = time.time()
        self._lap = time.time()
        self._end = 0.0

    def lap(self): #every n cycles call lap
        """
        Lap timer
        @return: time since last call
        """
        self._end = time.time()
        temp = self._end - self._lap
        self._lap = self._end
        return temp

    def exit(self):
        """
        End the timer
        @return: time elapsed since start
        """
        self._end = time.time()
        seconds = self._end - self._start
        return seconds

    def current(self):
        """
        Get the current time
        @return: current time
        """
        obj = time.localtime()
        t = time.asctime(obj)
        return t
