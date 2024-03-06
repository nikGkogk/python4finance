from random import randint

# -- Tuple --
tpl = (1, 2.5, 'data')

print(type(tpl))

# -- List --
lst = [1, 2.5, 'data']
print(type(lst))

lst = list(tpl)
print(type(tpl))

lst.append([4, 3])  # add as last item
lst.extend([1.0, 1.5, 2.0])  # add each item at the end
lst.insert(1, 'insert')  # insert item at index
lst.remove('data')  # find and remove item
subLst = lst.pop(3)
print(lst, subLst)

subLst = lst[2:5]  # slice part of array
print(subLst)

# list comprehensions
lst = [i ** 2 for i in range(5)]  # square root for each item in range
print(lst)

# -- Dicts --
dct = {
    'Name': 'Angela Merkel',
    'Country': 'Germany',
    'Profession': 'Chancelor',
    'Age': 64
}
print(type(dct))
print(dct['Name'], dct['Age'])

dct.keys()  # get dictionary keys
dct.values()  # get dictionary values
dct.items()  # get key-value pairs

for value in dct.values():
    print(type(value))

# -- Sets --
s = {'u', 'd', 'ud', 'du', 'd', 'du'}
print(s)

t = {'d', 'dd', 'uu', 'u'}

s.union(t)  # all of s and t
s.intersection(t)  # items in both s and t
s.difference(t)  # items in s bunt not in t
s.symmetric_difference(t)  # items in either s or t but not both

lst = [randint(0, 10) for i in range(20)]
print(lst)
s = set(lst)  # converting to set will remove duplicates
print(s)

