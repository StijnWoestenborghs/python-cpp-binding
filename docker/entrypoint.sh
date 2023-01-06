#!/bin/bash
set -e

# run executble
/opt/binding_cpp_root/build/bin/binding

# run python binding
cd /opt
python3 /opt/src/main.py