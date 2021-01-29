import sys

while True: #sets infinite loop
    try:
        print('Please enter a starting value (integers only)')
        startingValue = int(input())

        print('Please enter an ending value (integers only)')
        endingValue = int(input()) + 1

        if startingValue >= endingValue:
            raise Exception #raising own error if startingValue >= endingValue

    except ValueError:
        print('Error: You did not enter an integer') #when input != integer
        continue
    except Exception:
        print('Starting value must be greater than ending value.')  #if startingValue >= endingValue
        continue
    else:
        for num in range(startingValue, endingValue):
           if num > 1:
                for i in range(2, num):
                    if (num % i) == 0: 
                        break #break avoids the else statement and brings program back to initial for loop
                else: #else statement is activated if break statement is never met (when a prime number)
                    print(num)

    while True:
        try:
            print('Do you want to try again? Y for yes, N for no.') 
            reset = input()
            if reset != 'Y' and reset != 'N':
                raise ValueError #rasing own error if input is not Y or N
        except ValueError:
            print('Error: Invalid input')
            continue
        else:
            if reset == 'Y':
                break
            else:
                print('Thank you for playing!')
                sys.exit()

    continue

    