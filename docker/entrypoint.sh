#!/bin/bash
set -e

# build executable
g++ -std=c++20 -o /opt/binding_cpp_root/build/bin/binding -I /opt/binding_cpp_root/include/binding /opt/binding_cpp_root/src/*.cpp &

# build shared object
g++ -std=c++20 -o /opt/binding_cpp_root/build/lib/binding.so -fpic -shared -I /opt/binding_cpp_root/include/binding /opt/binding_cpp_root/src/*.cpp

# run executble
/opt/binding_cpp_root/build/bin/binding

# run python binding
echo "Starting python binding ..."
cd /opt
python3 /opt/src/main.py