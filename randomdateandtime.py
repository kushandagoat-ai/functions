import random
import time
def getRandomDate(StartDate, endDate):
    print("Printing random date between", StartDate, "And", endDate )
    randomgenerator = random.random()
    dateformat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(StartDate, dateformat))
    endtime = time.mktime(time.strptime(endDate,dateformat))
    randomtime = startTime + randomgenerator * (endtime - startTime)
    RandomDate = time.strftime(dateformat, time.localtime(randomtime))
    return RandomDate
print("Random date = ", getRandomDate("4/6/2026", "12/31/2030"))