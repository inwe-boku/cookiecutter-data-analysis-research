"""This file contains functions to load files from the data folder. This comes in handy to avoid
hard coding file paths in scripts and Jupyter notebooks. It is also a good place to implement
parsing of input files and conerting them to objects which can easily be used in the rest of the
code (e.g. xarray Dataarray or Pandas DataFrame objects)."""

import json


def load_some_input_data():
    """"This is just a dummy function to demonstrate how to load input data from a file.

    Returns
    -------
    dict

    """
    # Load some input data
    with open('data/input_data.json') as f:
        input_data = json.load(f)

    return input_data
