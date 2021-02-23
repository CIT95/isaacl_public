# My dd is modeling the number of hours I was productive on the week of
# 02/15/2021 - 02/19/2021. The values of the dd are in total minutes.


def average():
    # This takes the sorted_productivity_dd_list and outputs the average number
    # of minutes worked each day.
    minutes_list = []
    for index in sorted_productivity_dd_list:
        minutes_list.append(index[1])

    # Average = total min / number of days
    average_productivity = sum(minutes_list) / len(minutes_list)

    print(f'The average number of minutues worked per day is \
{average_productivity}.')


def total():
    # This prints the total number of hours worked.
    minutes_list = []
    for index in sorted_productivity_dd_list:
        minutes_list.append(index[1])

    print(f'The total number of hours worked is {sum(minutes_list)}.')


productivity_dd = {
    'Mon': 100,
    'Tue': 220,
    'Wed': 85,
    'Thu': 125,
    'Fri': 250
}

# How I sorted my dd is by assigning a key in the sorted method that targets
# the index[1] in each tuple nested in the list created by the .items() method.
# This sorts and filters the dd based on values.
# Here is a reference to what I did: https://careerkarma.com/blog/python-sort-a-dictionary-by-value/#:~:text=To%20sort%20a%20dictionary%20by%20value%20in%20Python%20you%20can,Dictionaries%20are%20unordered%20data%20structures.
sorted_productivity_dd_list = sorted(productivity_dd.items(), key=lambda x: x[1])

print('My productive days in ascending order are:')
# This for loop grabs each list item in sorted_productivity_dd, which is now
# in ascending order, and prints the key(date) followed by the value(mins).
# This also iterates the dd using a for loop.
for index in sorted_productivity_dd_list:
    print(index[0], index[1])

# This checks if the user input is an exisiting key.
while True:
    print('Input key to check if it exisit:')
    key_check = input()
    if key_check in productivity_dd.keys():
        print(key_check + ' ' + str(productivity_dd.get(key_check, 'none')))
    else:
        print(f'{key_check} does not exisit.')

    # Giving the option to check another key.
    print('Check another key? Y for yes.')
    check_again = input()
    if check_again.upper() == 'Y':
        continue
    else:
        break

total()
average()
