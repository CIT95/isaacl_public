#lookupError
list = ['cat', 'frog', 'dog',]

while True:
    try:
        print('Please enter index number to look up list item')
        listItem = list[int(input())]
    except LookupError: #when index value does not exist
        print('Error: list item tied to that index does not exist') 
        continue
    except ValueError: #when integer is not inputed
        print('Error: must enter integer')
        continue
    else:
        print(str(listItem))
        break
