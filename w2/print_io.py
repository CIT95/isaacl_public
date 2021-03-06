import sys

while True: #sets infinite loop
    print('Please enter a starting value (integers only)') #asks for first value
    startingValue = int(input())

    print('Please enter an ending value (integers only)') #asks for second value
    endingValue = int(input()) + 1

    if startingValue < endingValue: #if startingValue is greater than endingValue will print all numbers from start to end
        for num in range(startingValue, endingValue):
           if num > 1:
                for i in range(2, num):
                    if (num % i) == 0: 
                        break #break avoids the else statement and brings program back to initial for loop
                else: #else statement is activated if break statement is never met (when a prime number)
                    print(num)
    else:
        print('Try again.') #restarts loop if start is not greater than end value
        continue

    print('Do you want to try again? Y for yes, N for no.') 
    reset = input()
    if reset == 'Y': 
        continue #restarts loop if Y is entered
    elif reset == 'N':
        break #breaks loop if N is entered
    else:
        print('Wrong input, but thanks for playing!')
        sys.exit() #includes texts and ends program if neither Y or N is entered

print('Have a great day!')
    