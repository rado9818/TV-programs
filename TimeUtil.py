from datetime import datetime
from Constants import SECONDS_IN_MINUTE
import time
def getDifference(start):
    hour, minute = time.strftime("%H,%M").split(',')
    a = start
    b = "%s:%s"%(hour,minute)
    time1 = datetime.strptime(a,"%H:%M") # convert string to time
    time2 = datetime.strptime(b,"%H:%M")
    diff = time1 -time2
    return diff.total_seconds()/SECONDS_IN_MINUTE