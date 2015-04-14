#friday.py

import time

today = time.strftime("%E")

print(today)

if today == "Friday":
    print ("It's Friday")
else:
    print ("It isn't Friday ;( Today is " + today)
