"""
This script convers three dates (in YYYY-MM-DDThh:mm:ss) into two time differences in decimal hours.
"""
from datetime import datetime

timestring1 = "2025-04-27T15:20:19"
timestring2 = "2025-05-02T15:28:33"
timestring3 = "2025-05-04T15:12:07"

t1 = datetime.strptime(timestring1, "%Y-%m-%dT%H:%M:%S")
t2 = datetime.strptime(timestring2, "%Y-%m-%dT%H:%M:%S")
t3 = datetime.strptime(timestring3, "%Y-%m-%dT%H:%M:%S")

d1 = (t2 - t1).total_seconds()
d2 = (t3 - t2).total_seconds()

print("Delta1: " + str(d1/3600.))
print("Delta2: " + str(d2/3600.))