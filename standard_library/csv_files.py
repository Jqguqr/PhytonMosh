import csv

# Create CVS file
"""
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([12483, "prod00876", 58])
    writer.writerow([78135, "prod00884", 32])
"""

# Read CVS file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader)) # we can not read an iterable twis
    for row in reader:
        print(row)
