from datetime import datetime
import time

now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

print("Today's date is " + mm + "/" + dd + "/" + yyyy + " and the time is " + hour + ":" + mi + ":" + ss)
 