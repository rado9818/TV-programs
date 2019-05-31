from datetime import datetime

def getDifference():
    a = '22:06'
    b = '18:00'
    time1 = datetime.strptime(a,"%H:%M") # convert string to time
    time2 = datetime.strptime(b,"%H:%M")
    diff = time1 -time2
    diff.total_seconds()/60    # seconds to minutes
    return diff.total_seconds()/60