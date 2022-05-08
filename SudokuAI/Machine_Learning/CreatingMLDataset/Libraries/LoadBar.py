import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
class Load_Bar:
    def __init__(self, input_range = 0, gap = 5):
        self._load_bar = [0]
        self._gap = gap
        self._range = input_range

        self._current = 0
        self._title = "Program"

        self._createLoadBar()

    def _createLoadBar(self):
        """
        Create the spacing for loadbar intervals
        @return: None
        """
        incriments = self._range * (self._gap / 100)
        temp = incriments
        while temp <= self._range:
            self._load_bar.append(temp)
            temp += incriments

    def updateLoadBar(self, currentPosition, title = "program"):
        """
        Update LoadBar with current progress
        @param currentPosition: current progress
        @param title: optional - program title
        @return: None
        """
        if currentPosition in self._load_bar:
            percentage = (currentPosition / self._range) * 100
            percentage = round(percentage, 3)
            logging.debug(f"{title} - Loading: {percentage}%")
            if percentage == 100:
                print(f"{title} Completed")