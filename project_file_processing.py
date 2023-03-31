# Project File Processing

with open('devices.txt') as f:
    content = f.read().splitlines()
    print(content)

    devices = list()
    #will start to iterate from position 1
    for line in content[1:]:
        devices.append(line.split(':')) # separate the words by ':'

    print(devices)

    for device in devices:
        print(f'pinging {device[1]}')