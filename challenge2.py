#############################################################
# Create a Python script that reads a text file into a list #
# and then converts the list into a string that has the     #
# entire file content.                                      #
#############################################################

# Read the txt file into a list
with open('sample_file.txt', 'r') as f:
    content = f.read().splitlines()

    print(content)

    # Concatenating the list back to a string
    string = '\n'.join(content)
    print(string)

'''
Challenge #3

Create a Python script that removes all empty lines 
including those that contain only spaces from a file.
'''
with open('file.txt', 'r') as file:
    content = file.readlines()
    # print(f'The new line is: {line}')
# Create a new list eliminating the elements that are empty strings or contain only spaces
my_list = [line for line in content if line.strip() !='']
print(my_list)

# Write to a new file
with open('file_without_blanks.txt', 'w') as f:
    f.write(''.join(my_list))

'''
Challenge #4
Create a Python function called tail that reads the last n lines of a text file. 
The function has two arguments: 
the file name and n (the number of lines to read). This is similar to the Linux `tail` command.
Example: tail('sample_file.txt', 5) will return the last 5 lines from sample_file.txt.
'''

def tail(file, n):
    with open(file, 'r') as f:
        # Read the file into a list
        content = f.read().splitlines()
        #print(content)
        # Get the last n element of the list
        last_element = content[len(content)-n:]
        #print(last_element)
        # Concatenating the list back to a string
        my_string = '\n'.join(last_element)
        return my_string

#print(tail('sample_file.txt', 3))
'''
Challenge 5
Change the solution from the previous challenge so that the script that prints out 
the last n lines of the file refreshes the output every 3 seconds 
(as the file changes or updates). 
This is similar to the tail -f Linux command.
'''
# import time
#
# while True:
#     t = tail('sample_file.txt', 3)
#     print(t)
#     time.sleep(3)
#     print('')

'''
Challenge #6

Write a Python program to count the number of lines, words, and characters 
in a text file. This is similar to the Linux `wc` command. Create a function, if possible.
'''
def wc(file):
    with open(file, 'r') as f:
        # Reading file into list
        content = f.read().splitlines()
        lines_count = len(content)

        # Iterating the words in the list
        words = 0
        for word in content:
            words += len(word.split())
        # Iterating the characters in the list
        chars = 0
        for char in content:
            chars += len(list(char))

        return lines_count, words, chars

print(wc('sample_file.txt'))

'''
Challenge #7
Write a Python program that calculates the net amount of a bank account 
based on the transactions that are saved in a text file.
The file format is as follows
D:50
W:100
D means deposit while W means withdrawal.
Suppose that the following file is supplied to the program:
D:300
D:300
W:500
D:200
Then, the output should be: 300
'''

with open('banking.txt', 'r') as f:
    # Read file into list
    content = f.read().splitlines()
    print(content)

    deposit, withdraw = 0, 0
    for item in content:
        # Separate by ':'
        mylist = item.split(':')
        print(mylist)
        if mylist[0] == 'D':
            deposit += int(mylist[1])
        elif mylist[0] == 'W':
            withdraw += int(mylist[1])
        else:
            print('File format error!')
    balance = deposit - withdraw
    print(f'The net balance: {balance}')

'''
Challenge #8
Write a Python script that compares line by line two text files 
and displays the lines that differ.
'''
with open('macs.txt', 'r') as f:
    file1 = f.read().splitlines()
    #print(file1)
with open('mac_unique.txt', 'r') as f:
    file2 = f.read().splitlines()
    #print(file2)

file = list(zip(file1,file2))
#print(file)

i = 0
for line in file:
    i += i
    if line[0] != line[1]:
        print(f'file1({i}): {line[0]}, file2({i}): {line[1]}')

'''
Challenge #9
Consider this dictionary file.
Write a Python script that reads the file in a dictionary. 
The words in the file will be the dictionary keys and the 
length of each word the corresponding values.
'''

with open('american-english.txt') as f:
    words = f.read().splitlines()

    words_and_length = dict()
    for values in words:
        words_and_length[values] = len(values)

    for k, v in words_and_length.items():
        print(f'{k} -> {v}')


#print(words_and_length)
# Remember the sorted() method accepts a third value called reverse.
# reverse with a value of True will arrange the sorted dictionary in descending order.
view = sorted(words_and_length.items(), key = lambda x: x[1], reverse=True)

# 1 represents the indexes of the values. The keys are 0.
# Remember that a programmer starts counting from 0, not 1
print(view[:100])
# Convert list into dictionary
converted_dict = dict(view[:10])
print(f'The converted dictionary:\n{converted_dict}')

'''
Challenge #11
Consider this dictionary file.
Write a Python script that finds the number of occurrences of each letter of the alphabet 
in all the words of the dictionary. Make a distinction between lower and uppercase letters.
You want to see how many times 'a', 'A', 'b', 'B', 'c', 'C', 'd' 
and so on appear in all the words in the dictionary.
Which is the most frequently used letter in English words? But the least frequently used one?
'''
import string

# Create an empty dictionary
letters = dict()

# Initializing the dictionary with all letters as keys and 0 as values
# Iterating all the letter in ascii list: a/A,b/B,c/C...

#for char in string.ascii_letters:
'''
Challenge #12
Change the solution from the previous challenge so that the script considers all letters lowercase
(it makes no distinction between lower and uppercase letters).
'''
for char in string.ascii_letters.lower(): # string.ascii_lowercase:
    letters[char] = 0

    #print(letters)

with open('american-english.txt', 'r') as words:
    for c in words:
        #for letter in string.ascii_letters:
        for letter in string.ascii_letters.lower():
            letters[letter] += c.count(letter)

print(letters)

# Challenge #13
# Continue the previous challenge and find the 3 most frequently used letters in all English Words.
# You should get: ('e', 67681), ('s', 50872), ('i', 50818)
# Sort the dictionary by maximum number that occur in the file
sorted_list = sorted(letters.items(), key = lambda x: x[1], reverse=True)
print(sorted_list[:3])

