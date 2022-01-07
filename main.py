"""principal file."""
from manage import run, dict_config

from utils.clean_data import clean_data
from utils.handle_file import ReadFile
from utils.transform_data import transform_data

from loadbalance.loadbalancer import LoadBalancer

import os


if __name__ == "__main__":
    """fuction to execute system."""
    run()
    data = ReadFile().list_content()
    data_clean = clean_data(data)
    data_transform = transform_data(data_clean)
    ttask = data_transform[0]
    umax = data_transform[1]
    users = data_transform[2:]
    if os.path.exists(dict_config["OUTPUT_FILE"]):
        os.remove(dict_config["OUTPUT_FILE"])
    LoadBalancer(umax, users).balancer(ttask)
