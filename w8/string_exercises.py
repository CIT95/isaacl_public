"""
# pynative question 1 (hard)
def mid_3_char(string):
    middle_string_index = int(len(string) / 2)
    new_string = string[middle_string_index - 1: middle_string_index +2]
    print('Orginal: %s\nNew: %s' % (string, new_string))


str_1 = 'JhonDipPeta'
str_2 = 'JaSonAy'
mid_3_char(str_1)
mid_3_char(str_2)

# I was able to solve this without help.
"""


"""
# pynative question 2 (medium)
def append_mid(str_1, str_2):
    str_1_mid = int(len(str_1) / 2)
    str_1_left = str_1[:str_1_mid]
    str_1_right = str_1[str_1_mid:]
    print(str_1_left + str_2 + str_1_right)

s1 = 'Ault'
s2 = 'Kelly'
append_mid(s1, s2)

# I was able to solve without help. Note, this only works if len(s1) is even
"""


"""
# pynative question 4 (medium)
def lower_first(string):
    lowercase = ''
    uppercase = ''
    for index in string:
        if index.islower():
            lowercase += index
        else:
            uppercase += index

    lower_first_str = lowercase + uppercase
    print(lower_first_str)


str1 = 'PyNaTive'
lower_first(str1)

# I was able to solve this without help.
"""


"""
# pynative question 5 (easy)
def count_char_type(string):
    lower_chars = 0
    upper_chars = 0
    digits = 0
    symbols = 0
    for index in string:
        if index.isupper():
            upper_chars += 1
        elif index.islower():
            lower_chars += 1
        elif index.isdecimal():
            digits += 1
        elif index in ('!', '@', '#', '$', '%', '^', '&', '*'):
            symbols += 1

    print('Lower Chracters = ' + str(lower_chars))
    print('Upper Characters = ' + str(upper_chars))
    print('Digits = ' + str(digits))
    print('Symbols = ' + str(symbols))

str1 = 'P@#yn26at^&i5ve'
count_char_type(str1)

# I was able to solve this without help.
"""


"""
# pynative question 18 (hard)
def replace_str(string):
    char = '/*@&!'
    for c in char:
        string = string.replace(c, '#')
    print(string)


str1 = '/*Jon is @developer & musician!!'
replace_str(str1)

# I was able to solve this with some googling. Reference: https://stackoverflow.com/questions/3411771/best-way-to-replace-multiple-characters-in-a-string
"""


"""
# w3resource question 1 (easy)
def str_len_calulator(string):
    string_length = len(string)
    print(f'String length = {string_length}')


str = 'Hello world! It is a beautiful day, lets have a picnic'
str_len_calulator(str)
"""


"""
# w3resouces question 2 (easy)
from collections import Counter


def char_counter(string):
    num_char = dict(Counter(string))
    print(num_char)


str = 'google.com'
char_counter(str)

# I was able to do this without help. I previous learned about the
# Counter module during the week we learned about dictionaries.
"""


"""
# w3resource question 3 (medium)
def mod_str(string):
    str_len = len(string)
    if str_len < 2:
        print('')
    else:
        split_str = []
        split_str.append(string[:2])
        split_str.append(string[-2:])
        new_str = ''.join(split_str)
        print(new_str)

str = 'w3resource'
str2 = 'w3'
str3 = 'w'
mod_str(str)
mod_str(str2)
mod_str(str3)
"""


"""
# w3resources question 7 (hard)
def replace_not_poor(string):
    not_index = string.find('not')
    poor_index = string.find('poor')

    if not_index < poor_index and not_index > 0 and poor_index > 0:
        new_string = string.replace(string[not_index: (poor_index + 4)], 'good')
        print(new_string)
    else:
        print(string)


str = 'The lyrics is not that poor'
str2 = 'The lyrics is poor'
replace_not_poor(str)
replace_not_poor(str2)

# I had trouble with this one. I had too look up the find method.
"""


"""
# w3resouces question 9 (medium)
def remove_char(string, index=0):
    new_string = string.replace(string[index], '')
    print(new_string)


str = 'Hello my name is Frank and I like ice cream.'
remove_char(str, 6)

# I was able to solve this one without help.
"""
