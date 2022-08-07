import json

from timeit import timeit
from typing import Any, TypedDict, Optional, Callable, Tuple, List
from run_binding import run_binding


@timeit
def counting_stars_python(value: int, n: int) -> Tuple[int, bool]:
    for i in range(n):
        value += 1
    
    done = True
    return (value, done)


def counting_stars_cpp(value: int, n: int) -> Tuple[int, bool]:
    # Serialize input
    input_json = json.dumps({
        "value": value,
        "n": n,
    })

    # call python-cpp binding
    result = run_binding(input_json.encode('utf-8'))

    # Deserialize output
    output_json = json.loads(result.decode('utf-8'))
    value_out = output_json["value_out"]
    done = output_json["done"]

    return (value_out, done)

