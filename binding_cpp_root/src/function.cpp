#include "binding_interfaces.h"

ExampleOutputStruct counting_stars(ExampleInputStruct input){
    int value = input.value;

    for (int i=0; i<input.n; i++) {
        value++;
    }
    
    ExampleOutputStruct output;
    output.value_out = value;
    output.done = true;

    return output;
}