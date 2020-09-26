# -*- coding: utf-8 -*-
from pprint import pprint
import sqlite3
import create_sw_inventory_ver2_functions as dbf

# sw7 MAC address sw7 address is the same as sw3 MAC address
data2 = [
    ("0055.AAAA.CCCC", "sw5", "Cisco 3750", "London, Green Str"),
    ("0066.BBBB.CCCC", "sw6", "Cisco 3780", "London, Green Str"),
    ("0000.AAAA.DDDD", "sw7", "Cisco 2960", "London, Green Str"),
    ("0088.AAAA.CCCC", "sw8", "Cisco 3750", "London, Green Str"),
]


def write_rows_to_db(connection, query, data, verbose=False):
    """
    Function expects arguments:
      * connection - connection to the database
      * query - the query to be executed
      * data - data to be written as a list of tuples

    Function tries to write all data from the data list.
    If the data was written successfully, the changes are saved to the database
    and the function returns True.
    If an error occurs during the write process, the transaction is rolled back
    and the function returns False.

    The verbose flag controls whether messages are displayed on stdout.
    """
    for row in data:
        try:
            with connection:
                connection.execute(query, row)
        except sqlite3.IntegrityError as e:
            if verbose:
                print(
                    "An error occurred while writing data '{}'".format(", ".join(row), e)
                )
        else:
            if verbose:
                print("Data '{}' written successfully".format(", ".join(row)))


con = dbf.create_connection("sw_inventory3.db")

query_insert = "INSERT into switch values (?, ?, ?, ?)"
query_get_all = "SELECT * from switch"

print("\nDatabase contents")
pprint(dbf.get_all_from_db(con, query_get_all))

print("-" * 60)
print("Writing data with duplicate MAC address:")
pprint(data2)
write_rows_to_db(con, query_insert, data2, verbose=True)
print("\nDatabase contents")
pprint(dbf.get_all_from_db(con, query_get_all))

con.close()
