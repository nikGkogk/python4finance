from pprint import pprint

print('Everything is object')
print('Integer:')
n = 5
pprint(n.bit_length())

print('List:')
l = [1, 2, 3, 4]
l.append(10)
pprint(l)

print('Classes :')


class FinancialInstrument(object):
    author = 'Nikos Gkogktzilas'  # Class attribute (inherited by every instance)

    def __init__(self, symbol, price):  # Constructor
        self.symbol = symbol  # public attribute
        self.__price = price  # private attribute

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


fi = FinancialInstrument('AAPL', 100)
print('Access private attribute through getter')
print(fi.get_price())
# fi.__price would throw an exception as it is private
print('Access attribute even though its private ')
fi._FinancialInstrument__price = 200
print(fi._FinancialInstrument__price)


class PortfolioPosition(object):
    def __init__(self, financial_instrument, position_size):  # Accept a FinancialInstrument object
        self.position = financial_instrument
        self.__position_size = position_size

    def get_position_size(self):
        return self.__position_size

    def update_position_size(self, position_size):
        self.__position_size = position_size

    def get_position_value(self):
        return self.__position_size * self.position.get_price()


print('Portfolio Position of Financial Instrument')
pp = PortfolioPosition(fi, 10)
print(pp.get_position_value())  # Calculates the position value based on the attributes.
pp.position.set_price(300)  # Update the price of the financial instrument.
print(pp.get_position_value())  # Calculates new position value


# Vector Class example

class Vector(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        # The special method __repr__ allows the definition of custom string representations:
        return 'Vector(%r, %r, %r)' % (self.x, self.y, self.z)

    # abs() and bool() are two standard Python functions whose behavior on the Vector
    # class can be defined via the special methods __abs__ and __bool__
    def __abs__(self):
        # Define abs() behavior on the Vector class
        # Returns the Euclidean norm given the three attribute values.
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __bool__(self):
        # Define bool() behavior on the Vector class
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar,
                      self.y * scalar,
                      self.z * scalar)

    def __len__(self):
        # All instances of the Vector class have a length of three.
        return 3

    def __getitem__(self, i):
        if i in [0, -3]:
            return self.x
        elif i in [1, -2]:
            return self.y
        elif i in [2, -1]:
            return self.z
        else:
            raise IndexError('Index out of range.')

    def __iter__(self):
        # make Vector object iterable
        for i in range(len(self)):
            yield self[i]


print('Vector Class')
v = Vector(1, 2, 3)

print('Vector Class string representation')
print(v)

print('Vector Class abs() defined behaviour')
print(abs(v))

print('Vector Class add (+) an other Vector')
v2 = v + Vector(2, 3, 4)
print(v2)

print('Vector Class iteration')
for coordinate in v:
    print(coordinate)
