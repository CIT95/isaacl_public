# My thoughts on how I can implment regex for dev_1

import re

# Method 1
# Using regex to search large amounts of text for certain keywords

# This searches this txt file
interview_txt_file = open('isaacl_public/w10/interview_trans.txt')
text = interview_txt_file.read()

keyword_regex = re.compile(r'like', re.IGNORECASE)
like_list = keyword_regex.findall(text)
num_of_likes = len(like_list)
print(f'The word "like" appears {num_of_likes} times.')


# Method 2
# Replace keywords with user input

mailing_placeholders = '''
NAME
ADDRESS
CITY, STATE ZIPCODE
PHONE
EMAIL
'''

mail_regex = re.compile(r'NAME|ADDRESS|CITY|STATE|ZIPCODE|PHONE|EMAIL')
# Create a list for all found strings
mail_keywords_list = mail_regex.findall(mailing_placeholders)

# For loop to replace all placeholders
placeholder_replace = []
for i in range(len(mail_keywords_list)):
    print(mail_keywords_list[i] + ':')
    replacement = input()
    placeholder_replace.append(replacement)
placeholder_replace_tuple = tuple(placeholder_replace)  # convert to tuple

# Subs all placeholders with '%s'
mailing_filled = mail_regex.sub('%s', mailing_placeholders)

# Fill '%s' with user inputs
complete_mailing_form = mailing_filled % placeholder_replace_tuple

print(complete_mailing_form)
