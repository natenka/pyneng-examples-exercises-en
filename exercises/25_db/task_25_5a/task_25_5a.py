# -*- coding: utf-8 -*-
"""
Task 25.5a

There are no tests for the tasks of the 25th chapter!

After completing task 25.5, the dhcp table has a new last_active field.

Update the add_data.py script so that it removes all records that were active
more than 7 days ago.
In order to get such records, you can manually update the last_active field
in some records and set the time to 7 or more days.

The task file shows an example of working with objects of the datetime module.
Shows how to get the date 7 days ago. It will be necessary to compare
the last_active time with this date.

Please note that date strings that are written to the database can be compared
with each other.

"""

from datetime import timedelta, datetime

now = datetime.today().replace(microsecond=0)
week_ago = now - timedelta(days=7)

# print(now)
# print(week_ago)
# print(now > week_ago)
# print(str(now) > str(week_ago))
