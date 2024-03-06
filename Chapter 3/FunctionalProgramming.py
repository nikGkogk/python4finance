def f(x):
    return x ** 2


print(f(2))


def even(x):
    return x % 2 == 0


print(even(3))

# run the even function through the range
lst = list(map(even, range(10)))
print(lst)

# run anonymous lambda function through the range
lst = list(map(lambda x: x ** 2, range(10)))
print(lst)

# run the even function through the range, filter out False returns
lst = list(filter(even, range(10)))
print(lst)
