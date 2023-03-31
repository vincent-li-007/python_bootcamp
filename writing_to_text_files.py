# Writing to text files

# open a text file with 'w' --> write mode
# if the file name is existing then overwrite the file
# otherwise a new file with file name will be created
with open('myfile.txt', 'w') as f:
    f.write('This is the first line.\n')
    f.write('This is the 2nd line\n')

# open a text file with 'a' --> append mode
# it will add the new strings at the end of the file
with open('myfile.txt', 'a') as f:
    f.write('This line is appended after the lines.\n')


# open a text file with 'r+' --> add the string
# at the beginning of the file
with open('myfile.txt', 'r+') as f:
    f.seek(5)
    f.write('100')
    f.write('Lind added with r+.\n')
    f.seek(10)
    print(f.read())

