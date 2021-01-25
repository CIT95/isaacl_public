#Function to calculate birth year based off current age
def yearBorn(age=0):
    while True:
        print('Has your birthday occured in 2021 yet? Y for yes, N for no.')
        birthdayOccurrence = input()
        if birthdayOccurrence == 'Y':
            return(2021 - age)
            
        elif birthdayOccurrence == 'N':
            return(2020 - age)
            
        else:
            print('Invalid reponse. Please try again.')
            continue


#Function to determine zodiac animal based off birth year
def chineseZodiacAnimal(birthYear):
    if (2021%birthYear)%12 == 0: #divide most recent zodiac year by birth year. If the remainder/12 = 0 then they are the zodiac of the year stated. One zodiac occurs every 12 years
        return ('Ox')
    elif (2020%birthYear)%12 == 0:
        return ('Rat')
    elif (2019%birthYear)%12 == 0:
        return ('Pig')
    elif (2018%birthYear)%12 == 0:
        return ('Dog')
    elif (2017%birthYear)%12 == 0:
        return ('Rooster')
    elif (2016%birthYear)%12 == 0:
        return ('Monkey')
    elif (2015%birthYear)%12 == 0:
        return ('Sheep')
    elif (2014%birthYear)%12 == 0:
        return ('Horse')
    elif (2013%birthYear)%12 == 0:
        return ('Snake')
    elif (2012%birthYear)%12 == 0:
        return ('Dragon')
    elif (2011%birthYear)%12 == 0:
        return ('Rabit')
    elif (2010%birthYear)%12 == 0:
        return ('Tiger')


print('How old are you?')
year = yearBorn(int(input()))
print('You were born in '+str(year)+ ' and your chinese zodiac is the '+chineseZodiacAnimal(year)+'.')




    
    




