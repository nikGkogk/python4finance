import decimal

from decimal import Decimal
from pprint import pprint

# show decimal context
pprint(decimal.getcontext())

d = Decimal(1) / Decimal(11)
pprint(d)  # we see default precision used

decimal.getcontext().prec = 4
e = Decimal(1) / Decimal(11)
pprint(e)  # we see precision of change

pprint('http://www.python.{:s} {:s}'.format('tst', 'yes'))
