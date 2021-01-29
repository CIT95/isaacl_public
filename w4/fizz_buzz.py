def fizz_buzz(x):
    if x%15 == 0:
        print('FizzBuzz')
    elif x%5 == 0:
        print('Buzz')
    elif x%3 == 0:
        print('Fizz')
    else:
        print(x)


while True:
    try:
        fizz_buzz(int(input('Please enter an integer: ')))
    except ValueError:
        print('Error: must enter an integer') #error when input is not an integer
        continue
    else:
        break #breaks out of loop if no error is encountered


