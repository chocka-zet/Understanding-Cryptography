import math

#letter to numbers
def letter_to_number(letter):
    return (ord(letter.upper())) - 65  

#number to letter
def number_to_letter(y):
    return chr(y+65)


#Shift cipher
def shift_cipher(letter, k):
    y=(letter_to_number(letter) + k) % 26
    cipher_letter=number_to_letter(y)
    return cipher_letter

#Affine cipher
def affine_cipher(letter, a, b):
    if math.gcd(a, 26) == 1:
        x=letter_to_number(letter)
        y=((a*x) + b) % 26
        cipher_letter=number_to_letter(y)
        return cipher_letter
    else:
        return "You have chosen value for 'a' that is not co-prime to 26. Please use Euclidean Algorithm to compute a proper 'a' value."
