# Rading files into a List

# 1. f.read().splitlines()

with open('configuration.txt') as f:
    content = f.read().splitlines()
    print(content)
    print('#'* 50)

# 2. f.readlines()
# read the files until the end of the files

with open('configuration.txt') as f:
    content = f.readlines()
    print(content)
    print('#'*50)

# 2.1 f.readline()
# Read the one line of the file
with open('configuration.txt') as f:
    content = f.readline()
    print(content)
    print('#' * 50)

# 3. list(f)
with open('configuration.txt') as f:
    content = list(f)
    print(content)
    print('#' * 50)
    
# 4. iterate over a file
with open('configuration.txt') as f:
    for line in f:
        print(line, end='')