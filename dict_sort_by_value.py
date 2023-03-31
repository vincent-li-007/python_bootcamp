# Considering the following dict, get a dict representation sorted by key.
# A dict representation means viewing or printing the dict

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

view = sorted(d1.items(), key = lambda x: x[1], reverse=True)
print(view)