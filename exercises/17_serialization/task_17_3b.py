# -*- coding: utf-8 -*-
"""
Task 17.3b

Create a transform_topology function that converts the topology to a format
suitable for the draw_topology function.

The function expects a YAML filename as an argument in which the topology is stored.

The function must read data from the YAML file, transform it accordingly,
so that the function returns a dictionary of the following form:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

The transform_topology function should not only change the format of the topology
representation, but also remove the "duplicate" connections (they are best seen
in the diagram that the draw_topology function generates from
the draw_network_graph.py file).
"Duplicate" connections are connections of this kind:
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

Due to the fact that the same link is described twice, there will be extra
connections on the diagram. The task is to leave only one of these links
in the final dictionary, does not matter which one.

Check the operation of the function on the topology.yaml file (must be created
in task 17.3a). Based on the resulting dictionary, you need to generate a topology
image using the draw_topology function.
Do not copy draw_topology function code from draw_network_graph.py file.

The result should look the same as the diagram in the task_17_3b_topology.svg file:
* Interfaces must be written with a space Fa 0/0
* The arrangement of devices on the diagram may be different
* Connections must match the diagram
* There should be no "duplicate" links on the diagram


> To complete this task, graphviz must be installed:
> apt-get install graphviz

> And a python module to work with graphviz:
> pip install graphviz
"""
