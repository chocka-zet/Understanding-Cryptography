#include <iostream>
#include <string>
#include <numeric> 
#include <cctype>  
using namespace std; 

int letter_to_number(char letter) {
    return (toupper(letter) - 65);
}

char number_to_letter(int y) {
    return (char)(y + 65);
}

char shift_cipher(char letter, int k) {
    int y = (letter_to_number(letter) + k) % 26;
    return number_to_letter(y);
}

char affine_cipher(char letter, int a, int b) {
    if (std::gcd(a, 26) == 1) {
        int x = letter_to_number(letter);
        int y = ((a * x) + b) % 26;
        return number_to_letter(y);
    } else {
        return char('@'); 
    }
}
