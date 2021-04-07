from datetime import datetime

import ClassStart
import classlinks

now = datetime.now()

currentdate = now.strftime("%A")

if currentdate == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
    link = classlinks.links["Maths"]
    Maths = ClassStart.classstart()
    Maths.join(link)
else:
    quit()
    exit()
