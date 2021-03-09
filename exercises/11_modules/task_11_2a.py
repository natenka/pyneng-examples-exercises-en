# -*- coding: utf-8 -*-
"""
Task 11.2a

> To complete this task, graphviz must be installed:
> apt-get install graphviz

> And a python module to work with graphviz:
> pip install graphviz

Use the create_network_map function from task 11.2 to create the topology dict
for files:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

Using the draw_topology function from the draw_network_graph.py file, draw
schema for the topology dict received with create_network_map function.
You need to figure out how to work with the draw_topology function on your own,
by reading the function description in the draw_network_graph.py file.
The resulting scheme will be written to the svg file - it can be opened with a browser.


With the current topology dictionary, extra connections are drawn on the diagram. They
occur because one CDP file (sh_cdp_n_r1.txt) describes connection
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")

and another (sh_cdp_n_sw1.txt) describes connection
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

In this task, you need to create a new function unique_network_map, which of these
two connections will leave only one, for correct drawing of the schema.
In this case, it does not matter which of the connections to leave.

The unique_network_map function must have one topology_dict parameter,
which expects a dictionary as an argument.
It should be a dictionary resulting from the create_network_map function call.

Dict example:
{
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
}


The function should return a dictionary that describes the connections between
devices. In the dictionary, you need to get rid of "duplicate" connections and
leave only one of them.

The structure of the final dict is the same as in task 11.2:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

After creating the function, try drawing the topology again,
now for the dictionary returned by the unique_network_map function.

The result should look the same as the diagram in task_11_2a_topology.svg

Wherein:
* The arrangement of devices on the diagram may be different
* Connections must match the diagram

Do not copy the code of the create_network_map and draw_topology functions.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]
