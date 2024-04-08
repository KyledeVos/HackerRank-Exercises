
import re

def pangrams(s):
    # Write your code here
    
    alpha_dict = {}
    letter_count = 0
    for char in s:
        if re.match("[a-zA-z]", char):
            if alpha_dict.get(char.lower(), 0) == 0:
                alpha_dict[char.lower()] = 1
                letter_count +=1
    print(letter_count)
    if letter_count == 26:
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':


    s = input()

    result = pangrams(s)

    print(result)
