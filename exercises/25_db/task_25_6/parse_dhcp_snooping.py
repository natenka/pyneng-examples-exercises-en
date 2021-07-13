#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import parse_dhcp_snooping_functions as pds

# Default values:
DFLT_DB_NAME = "dhcp_snooping.db"
DFLT_DB_SCHEMA = "dhcp_snooping_schema.sql"


def create(args):
    print("Creating a {} database with {} schema".format(args.name, args.schema))
    pds.create_db(args.name, args.schema)


def add(args):
    if args.sw_true:
        print("Adding switch data")
        pds.add_data_switches(args.db_file, args.filename)
    else:
        print("Adding information from files\n{}".format(", ".join(args.filename)))
        print("\nAdding data on DHCP records to {}".format(args.db_file))
        pds.add_data(args.db_file, args.filename)


def get(args):
    if args.key and args.value:
        print("Data from the database: {}".format(args.db_file))
        print(
            "Information about devices with the following parameters:",
            args.key,
            args.value,
        )
        pds.get_data(args.db_file, args.key, args.value)
    elif args.key or args.value:
        print("Please enter two or zero arguments\n")
        print(show_subparser_help("get"))
    else:
        print("The dhcp table has the following entries:")
        pds.get_all_data(args.db_file)


def show_subparser_help(subparser_name):
    """
    Function returns help message for subparser
    """
    subparsers_actions = [
        action
        for action in parser._actions
        if isinstance(action, argparse._SubParsersAction)
    ]
    return subparsers_actions[0].choices[subparser_name].format_help()


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(
    title="subcommands", description="commands", help="additional info"
)

create_parser = subparsers.add_parser("create_db", help="create new database")
create_parser.add_argument(
    "-n", dest="name", default=DFLT_DB_NAME, help="database name"
)
create_parser.add_argument(
    "-s", dest="schema", default=DFLT_DB_SCHEMA, help="database schema"
)
create_parser.set_defaults(func=create)

add_parser = subparsers.add_parser("add", help="add data to database")
add_parser.add_argument("filename", nargs="+", help="file(s) to add")
add_parser.add_argument(
    "--db", dest="db_file", default=DFLT_DB_NAME, help="database name"
)
add_parser.add_argument(
    "-s",
    dest="sw_true",
    action="store_true",
    help=("if the flag is set, add switch data, otherwise " "add DHCP records"),
)
add_parser.set_defaults(func=add)

get_parser = subparsers.add_parser("get", help="show database records")
get_parser.add_argument(
    "--db", dest="db_file", default=DFLT_DB_NAME, help="database name"
)
get_parser.add_argument(
    "-k",
    dest="key",
    choices=["mac", "ip", "vlan", "interface", "switch"],
    help="parameter for searching records",
)
get_parser.add_argument("-v", dest="value", help="parameter value")
get_parser.add_argument("-a", action="store_true", help="show all database content")
get_parser.set_defaults(func=get)

if __name__ == "__main__":
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
