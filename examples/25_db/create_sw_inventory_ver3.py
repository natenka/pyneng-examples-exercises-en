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

con = dbf.create_connection("sw_inventory3.db")

query_insert = "INSERT into switch values (?, ?, ?, ?)"
query_get_all = "SELECT * from switch"

print("\nDatabase contents")
pprint(dbf.get_all_from_db(con, query_get_all))

print("-" * 60)
print("Writing data with duplicate MAC address:")
pprint(data2)
dbf.write_data_to_db(con, query_insert, data2)
print("\nDatabase contents")
pprint(dbf.get_all_from_db(con, query_get_all))

con.close()
