#include "binding_export.h"
#include "simpleson.h"

#include "function.h"


int run_binding_external(char* c, int length, char** c_return, int* length_return) {
    // Deserialize input_string to json
    std::string input_string = std::string(c, length);
    json::jobject input_json = json::jobject::parse(input_string);

    // Copy input json into Binding struct
    ExampleInputStruct example_input;
    example_input.value = (int)input_json["value"];
    example_input.n = (int)input_json["n"];

    // Call cppFunction
    ExampleOutputStruct example_output;
    try {
        example_output = counting_stars(example_input);
    
    } catch(...) {
        printf("cppFunction crashed\n");
        return -1;
    }

    // Create output json
    json::jobject output_json;
   
    output_json["value_out"] = example_output.value_out;
    output_json["done"] = example_output.done;

    // Serialize output_json to string
    std::string output_string = (std::string)output_json;

    // Copy output to the output variables
    *c_return = new char[output_string.length()];
    std::copy(output_string.c_str(), output_string.c_str() + output_string.length(), *c_return);
    *length_return = output_string.length();

    return 0;
}

void delete_c_return(char* c_return) {
    delete c_return;
}
