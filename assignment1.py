############################
# Reading the file in list #
############################

# with open('devices_assign.txt', 'r') as f:
#     content = f.read().splitlines()# will print out the file in a list without '\n'
#    # print(content)
#
#     devices = list()
#
#     for device in content:
#         devices.append(device.split(':'))
#     print(devices)

# with csv function

import csv
with open('devices_assign.txt') as f:
    reader = csv.reader(f, delimiter=':')
    mylist = list()

    for row in reader:
        mylist.append(row)
    print(mylist)
