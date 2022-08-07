import json
import pytest


def test_binding_cpp():
    with open("test//example_input.json", "r") as f:
        input_json = json.load(f)

    print(input_json)
    assert(True == True)
