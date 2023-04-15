from datetime import datetime
import time

# Create an date objecto with this date
dt1 = datetime(2023, 1, 1)
# Get current date
dt2 = datetime.now()
# Convert datetime to string
# dt = datetime.strptrime("2023/01/01", "%Y/%m/%d")
# dt.strftime("%Y/%m")  # is the opositive of the last one
# Convertir timestamp to date onject
dt = datetime.fromtimestamp(time.time())

print(dt)
# Dar formato
print(f"{dt.year}/{dt.month}/{dt.day}")
print(dt.strftime("%Y/%m"))

print(dt1 > dt2)
