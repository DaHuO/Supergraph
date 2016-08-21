__author__ = 'fbleite'

import time

class PerformanceMeasure :
    def __init__(self, fut):
        self.startTime = None
        self.endTime = None
        self.fut = fut

    def startTimer(self):
        self.startTime = time.time()

    def endTimer(self):
        self.endTime = time.time()

    def printElapsedTime(self):
        print("{} Seconds".format(self.endTime - self.startTime))

    def runFuntionAndCheckPerformance(self):
        self.startTimer()
        self.fut()
        self.endTimer()
        # self.printElapsedTime()

# def wasteTime():
#     time.sleep(5.10)
# perfMeasure = PerformanceMeasure(wasteTime)
# perfMeasure.runFuntionAndCheckPerformance()