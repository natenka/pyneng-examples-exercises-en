from datetime import datetime
import logging
import netmiko
import yaml


# this line indicates that paramiko log messages will be displayed
# only if their level is WARNING or higher
logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="%(threadName)s %(name)s %(levelname)s: %(message)s", level=logging.INFO
)


def send_show(device, show):
    start_msg = "===> {} Connection: {}"
    received_msg = "<=== {} Received:   {}"
    ip = device["ip"]
    logging.info(start_msg.format(datetime.now().time(), ip))

    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show)
        logging.info(received_msg.format(datetime.now().time(), ip))
    return result


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_show(dev, "sh clock"))
