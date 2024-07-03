import csv 
with open('data.csv', mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])

