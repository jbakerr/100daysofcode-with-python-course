from datetime import datetime
from datetime import date


christmas = date(2018, 12, 25)

today_date = date.today()

if christmas is not today_date:
    print(
        "Sorry there are still "
         + str((christmas-today_date).days) +
          " days until Christmas"
  )
else:
    print("yay")
