from datetime import datetime

import ClassStart
import classlinks

now = datetime.now()

currentdate = now.strftime("%A")

if currentdate == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
    link = classlinks.links["Isl"]
    Isl = ClassStart.classstart()
    Isl.join(link)
else:
    quit()
    exit()
