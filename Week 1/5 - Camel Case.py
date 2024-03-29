import re

def convert_Camel(input_str):
    sep_type, data_type, content = input_str.split(";")

    # Desired Action is Seperation
    if sep_type == "S":
        # Create matches checking for lower case first word or proceeding (or starting) words
        # starting with upper case and followed by lower including check for numbers
        # NOTE - Python variables may not start with a number
        matches = re.findall(r"([a-z]+)|([A-Z][a-z]+)?|([0-9])", content)

        final_word = ""
        
        # search through match tuples, recombing words into single string seperated with spaces
        for val_tup in matches:
            for val in val_tup:
                if val != "":
                    final_word += " " + val.lower()

        # remove potential trailing whitespace
        print(final_word.strip())

    else:
        # Desired Action is combine

        recombine = ""
        
        # seperate content into words list
        content_list = content.split()
        
        # for classes, set start_index for capitalization from first word
        if data_type == "C":
            start_index = 0
        else:
            # methods and variables, set capitalization from second word
            # and add first, lower case word to string
            start_index = 1
            recombine += content_list[0]
        
        # recombine words into string and capitalize words
        for i in range(start_index, len(content_list)):
            recombine += content_list[i].capitalize()
        
        # add parenthesis for methods
        if data_type == "M":
            recombine += "()"

        print(recombine)

s = input()
convert_Camel(s)

