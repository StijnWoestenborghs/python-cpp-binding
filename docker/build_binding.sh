#!/bin/bash
set -e

# build executable
echo "Building executable ..."
g++ -std=c++20 -o /opt/binding_cpp_root/build/bin/binding -I /opt/binding_cpp_root/include/binding /opt/binding_cpp_root/src/*.cpp

# build shared object
echo "Building shared object ..."
g++ -std=c++20 -o /opt/binding_cpp_root/build/lib/binding.so -fpic -shared -I /opt/binding_cpp_root/include/binding /opt/binding_cpp_root/src/*.cpp
