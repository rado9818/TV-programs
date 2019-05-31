from datetime import datetime
from Constants import SECONDS_IN_MINUTE
def getDifference():
    a = '22:06'
    b = '18:00'
    time1 = datetime.strptime(a,"%H:%M") # convert string to time
    time2 = datetime.strptime(b,"%H:%M")
    diff = time1 -time2
    return diff.total_seconds()/SECONDS_IN_MINUTE