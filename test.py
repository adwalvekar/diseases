import csv
import sys

f = open('measles.csv', 'rt')
f2 = open('rest.csv', 'wb')
try:
    reader = csv.reader(f)
    writer = csv.writer(f2)
    for row in reader:
        row.append(int((int(row[0])-192801)/52) +1900)
        print '1'
        writer.writerow(row)
finally:
    f.close()