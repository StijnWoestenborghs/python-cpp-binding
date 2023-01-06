#include <iostream>

#include "function.h"
#include "timer.h"


int main(){
    std::cout << "[EXECUTABLE] Counting stars as C++ executable " << std::endl;

    ExampleInputStruct input;
    input.value = 0;
    input.n = 1000000000;
    
    ExampleOutputStruct output;
    {
        Timer timer;
        output = counting_stars(input);
    } 

    std::cout << "\t Done: " << output.done << std::endl;
    std::cout << "\t Value out: " << output.value_out << std::endl;
}