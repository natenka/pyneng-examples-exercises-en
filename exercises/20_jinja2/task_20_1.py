# -*- coding: utf-8 -*-
"""
Task 20.1

Create generate_config function.

Function parameters:
* template - path to the template file (for example, "templates/for.txt")
* data_dict - a dictionary with values to be substituted into the template

The function should return the generated configuration string.

Check the operation of the function on the templates/for.txt template
and data from the data_files/for.yml file.

"""
import yaml


# this is how a function call should look
if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))
