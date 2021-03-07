# -*- coding: utf-8 -*-
"""
Task 15.2a

Create a convert_to_dict function that expects two arguments:
* list with field names
* list of tuples with values

The function returns a list of dictionaries, where the keys are taken
from the first list, and the values from the second.

For example, if you pass the headers list and the list
[('R1', '12.4(24)T1', 'Cisco 3825'),
 ('R2', '15.2(2)T1', 'Cisco 2911')]

The function should return a list of dictionaries:
[{'hostname': 'R1', 'ios': '12.4(24)T1', 'platform': 'Cisco 3825'},
 {'hostname': 'R2', 'ios': '15.2(2)T1', 'platform': 'Cisco 2911'}]

The function should not be tied to specific data or the number
of headers/data in tuples.

Check function operation:
* the first argument is the headers list
* the second argument is the data list

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

headers = ["hostname", "ios", "platform"]

data = [
    ("R1", "12.4(24)T1", "Cisco 3825"),
    ("R2", "15.2(2)T1", "Cisco 2911"),
    ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
]
