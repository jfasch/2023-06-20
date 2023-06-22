#include <iostream>
#include <string>

int main()
{
    // char c = 'ö';   // <--- multibyte char? (!!!)

    const char* my_c_string = "ö";
    std::string my_cpp_string = my_c_string;
    std::cout << my_cpp_string << ", size: " << my_cpp_string.size() << std::endl;
    return 0;
}
