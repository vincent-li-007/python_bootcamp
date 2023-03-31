import csv

# csv.register_dialect('comma', delimiter=",", quoting=csv.QUOTE_NONE, lineterminator='\n')
# with open('people.csv', 'r') as f:
#     content = csv.reader(f, dialect='comma')
#     for row in content:
#         print(row)
#
#
# with open('people1.csv', 'w') as f:
#     writer = csv.writer(f)
#     # writer.writerow(content)
#
#     for c in content:
#         writer.writerows(c)

'''
Challenge #1
Consider the following Python list:
people = [

['Dan', 34, 'Bucharest'],

['Andrei',21, 'London'],

['Maria', 45, 'Paris']

]
Using the CSV module write each element of the list (which is another list) into a CSV file called people1.csv
After writing into the file, read and print out the file contents.
Use the default , (comma) as the delimiter.
'''
people = [

['Dan', 34, 'Bucharest'],

['Andrei',21, 'London'],

['Maria', 45, 'Paris']

]

# Writing into a csv file
with open('people1.csv', 'w') as f:
    writer = csv.writer(f)
    for item in people:
        writer.writerow(item)

# Reading a csv file
with open('people1.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

'''
Change the solution from the previous challenge and use : (colon) as the delimiter.
'''
csv.register_dialect('colon', delimiter=":", quoting=csv.QUOTE_NONE, lineterminator='\n')

with open('people1.csv', 'r') as f:
    reader = csv.reader(f, delimiter=":")
    for row in reader:
        print(row)


