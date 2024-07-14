""" Loads project configuration options and environment variable attributes """

import os
from dotenv import load_dotenv, find_dotenv
import sys
from pathlib import Path

configuration = dict()
try:
    # Automatically fetch .env in project tree
    dotenv_path = find_dotenv()
    if not dotenv_path:
        raise FileNotFoundError("Could not find .env secrets configuration file.")
    with open(dotenv_path) as env_file:
        configuration.update(
            {item.split("=")[0]: item.split("=")[1] for item in env_file.readlines()}
        )
    load_dotenv(dotenv_path)


except FileNotFoundError as err:
    print(err)
    sys.exit(0)
