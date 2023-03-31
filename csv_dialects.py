import csv

# with open('passwd.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=':', lineterminator='\n')
#     for row in reader:
#         print(row)
#
#
# # A dialect discribes the properties of a csv file
# print(csv.list_dialects())

csv.register_dialect('hashes', delimiter="#", quoting=csv.QUOTE_NONE, lineterminator='\n')

#Open the CSV file
with open('items.csv','r') as csvfile:
    reader = csv.reader(csvfile, dialect='hashes')

    for row in reader:
        print(row)

with open('items.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, dialect='hashes')

    writer.writerow(('spoon', 3, 1.5))
