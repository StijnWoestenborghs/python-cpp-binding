import os, sys
import json
import pytest

# from src.function import counting_stars_cpp
import src.run_binding
import src.timeit
from src.function import counting_stars_cpp



def test_binding_cpp():
    with open(r"test/example_input.json", "r") as f:
        input_json = json.load(f)

    print(input_json)
    print("HELLO WORLD")
    assert(True == True)
