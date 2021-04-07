from datetime import datetime

import ClassStart
import classlinks

now = datetime.now()

currentdate = now.strftime("%A")

if currentdate == "Monday" or "Tuesday" or "Wednesday":
    link = classlinks.links["Sst"]

    english = ClassStart.classstart()
    english.join(link)

elif currentdate == "Thursday" or "Friday":
    link = classlinks.links["Isl"]

    english = ClassStart.classstart()
    english.join(link)

else:
    print("Did not got wanted date")
