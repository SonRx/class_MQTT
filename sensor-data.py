import sys
import csv

infile = open(sys.argv[1])
reader = csv.reader(infile)
headings = []
rows = []

maxTemp = 0
minTemp = 99
avgTemp = 0

headings = reader.next()

for line in reader:
    rows.append(float(line[1]))
    if float(line[1]) > maxTemp:
        maxTemp = float(line[1])
    if float(line[1]) < minTemp:
        minTemp = float(line[1])

Total = sum(rows)
avgTemp = Total/len(rows)

print "Temperature Report"
print "Average: ", avgTemp
print "Maximum: ", maxTemp
print "Minimum: ", minTemp
