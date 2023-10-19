"""
- you must be maximum of 6 and minimum of 2
- all numbers must be at the end
- first number cannot be a zero
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    is_alpha = s[0:2].isalpha()
    if is_alpha and 2 <= len(s) <= 6 and search_of_punctuation(s) and search_of_numbers(s):
        return True
    else:
        return False


def search_of_punctuation(punctuation_s):
    __list = ["!", ".", ";", ":", "'", "-", " "]
    for i in __list:
        if punctuation_s.find(i) == -1:
            # valid
            continue  # because we need to continue check
        else:
            return False
    return True


def search_of_numbers(numbers_s):
    __list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    __int_piece = 0
    if search_of_punctuation(numbers_s):
        for u in numbers_s:
            if u in __list:
                __int_piece = numbers_s.index(u)
                __str_piece = numbers_s[__int_piece:]
                for j in __str_piece:
                    if j not in __list:
                        return False
                if int(__str_piece[0]) != 0 and type(__str_piece[-1] != str):
                        return True
                else:
                    return False
            elif u not in __list:
                continue
        return True
        
        


main()
