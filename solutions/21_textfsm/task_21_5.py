# -*- coding: utf-8 -*-

from task_21_4 import send_and_parse_show_command
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import os
import yaml


def send_and_parse_command_parallel(devices, command, path, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result_all = [
            executor.submit(send_and_parse_show_command, device, command, path)
            for device in devices
        ]
        output = [f.result() for f in as_completed(result_all)]
    return output


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    command = "sh ip int br"
    path_dir = f"{os.getcwd()}/templates"
    pprint(send_and_parse_command_parallel(devices, command, path_dir))
