import csv
with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip the first row
    year_1958 = dict()
    # for row in reader:
    #     print(row)

    for row in reader:
        year_1958[row[0]] = row[1]
    print(year_1958)

    max_1958 = max(year_1958.values())
    print(f'The maximum numbers of flights is {max_1958}')

    # Also print the month
    # Iterate the key and value
    for k, v in year_1958.items():
        if max_1958 == v:
            print(f'Busiest Month in 1958: {k}, Flights:{v.strip()}') # strip(): reduce the white space in front of the value
