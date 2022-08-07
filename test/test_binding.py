import os, sys
import json
import pytest

from function import counting_stars_cpp
from function import counting_stars_python


def test_binding_cpp():
    with open(r"test/example_input.json", "r") as f:
        input_json = json.load(f)

    value = input_json["value"]
    n = input_json["n"]

    # call binding
    value_out, done = counting_stars_cpp(value, n)

    with open(r"test/example_output.json", "r") as f:
        output_json = json.load(f)

    assert(value_out == output_json["value_out"])
    assert(done == output_json["done"])


def test_python_cpp_output():
    value = 0
    n = 1000

    value_out_python, done_python = counting_stars_python(value, n)
    value_out_cpp, done_cpp = counting_stars_cpp(value, n)

    assert(value_out_python == value_out_cpp)
    assert(done_python == done_cpp)