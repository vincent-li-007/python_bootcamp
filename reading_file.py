#
# reading the file by entering specific position
# ##############################################


f = open('configuration.txt')

'''
read the first 5 characters & 
print them out
'''
content = f.read(5)
print(content)

'''
read the next following 3 characters
& print them out
'''
content = f.read(3)
print(content)

print(f.tell()) # print out the cursor's location
f.seek(2) # place the cursor in the second position
content = f.read(3)
print(content)