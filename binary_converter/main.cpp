#include <iostream>
#include <cmath>

void convert_binary(std::string bin_number) {
    int number = 0;
    for (int i = bin_number.length() - 1; i >= 0; i--) {
        if (bin_number[i] == '1') {
            number += std::pow(2, (bin_number.length() - 1) - i);
        }
    }
    std::cout << "O número em binário " << bin_number << " em inteiro é: " << number << std::endl;
}

int main(int argc, char const *argv[])
{
    std::string number;

    std::cout << "Insira o número binário sem espaços: ";
    std::cin >> number;

    convert_binary(number);
    return 0;
}
