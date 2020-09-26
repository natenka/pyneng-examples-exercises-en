# -*- coding: utf-8 -*-
from pprint import pprint
import sqlite3


data = [
    ("0000.AAAA.CCCC", "sw1", "Cisco 3750", "London, Green Str"),
    ("0000.BBBB.CCCC", "sw2", "Cisco 3780", "London, Green Str"),
    ("0000.AAAA.DDDD", "sw3", "Cisco 2960", "London, Green Str"),
    ("0011.AAAA.CCCC", "sw4", "Cisco 3750", "London, Green Str"),
]


def create_connection(db_name):
    """
    Function creates a connection  to the database db_name
    and returns Connection object
    """
    connection = sqlite3.connect(db_name)
    return connection


def write_data_to_db(connection, query, data):
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
    """
    try:
        with connection:
            connection.executemany(query, data)
    except sqlite3.IntegrityError as e:
        print("Error occured: ", e)
        return False
    else:
        print("Data written successfully")
        return True


def get_all_from_db(connection, query):
    """
    Function expects arguments:
      * connection - connection to the database
      * query - the query to be executed

    Function returns data received from the database.
    """
    result = [row for row in connection.execute(query)]
    return result


if __name__ == "__main__":
    con = create_connection("sw_inventory3.db")

    print("Creating table...")
    schema = """create table switch
                (mac text primary key, hostname text, model text, location text)"""
    con.execute(schema)

    query_insert = "INSERT into switch values (?, ?, ?, ?)"
    query_get_all = "SELECT * from switch"

    print("Writing data to the database:")
    pprint(data)
    write_data_to_db(con, query_insert, data)
    print("\nDatabase contents")
    pprint(get_all_from_db(con, query_get_all))

    con.close()
