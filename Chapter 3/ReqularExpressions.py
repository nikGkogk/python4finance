import re
from pprint import pprint
from datetime import datetime

series = """
'01/18/2014 13:00:00', 100, '1st';
'01/18/2014 13:30:00', 110, '2nd';
'01/18/2014 14:00:00', 120, '3rd'
"""

# datetime regular expression
dt = re.compile("'[0-9/:\s]+'")
dates = []
for item in dt.findall(series):
    item = item.replace("'", "")  # strip extra single quote
    dates.append(
        datetime.strptime(  # convert to date object
            item,
            '%m/%d/%Y %H:%M:%S'
        )
    )

pprint(dates)
