with open('macs.txt', 'r') as f:
    addresses = f.read().split()

   # print(addresses)

    # Eliminating the duplicate
    content = list(set(addresses))
    print(content)

# Writing to file
with open('mac_unique.txt', 'w', newline='') as f:
    for mac in content:
        f.write(f'{mac}\n')


