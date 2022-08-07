import os, sys
import ctypes
from ctypes import *
from timeit import timeit

libc = CDLL("binding_cpp_root/build/lib/binding.so")
run_binding_external = libc.run_binding_external
run_binding_external.argtypes = [c_char_p, c_int, POINTER(c_char_p), POINTER(c_int)]
run_binding_external.restype = c_int

delete_c_return = libc.delete_c_return
delete_c_return.argtypes = [c_char_p]
delete_c_return.restype = None


@timeit
def run_binding(input_string):
    s_return = c_char_p()
    length_return = c_int()
    code = run_binding_external(input_string, len(input_string), pointer(s_return), pointer(length_return))
    if code == 0:
        result = string_at(s_return, length_return)
        delete_c_return(s_return)
        return result
    else:
        raise Exception('Error in binding')
