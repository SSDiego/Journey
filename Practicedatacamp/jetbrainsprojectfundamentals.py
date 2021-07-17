# Python Enhancement Proposal

# The length of a line

# Avoid extra spaces
        
# Avoid extra spaces within parentheses.
        
print('Hello!') # Good 
        
print( 'Hello!' ) # Bad
        
# Avoid an extra space before an open parenthesis.
        
print('some text') # Good
        
print ('some text') # Bad
        
# Quotes
        
print("It's a good string!") # Good
        
print('It\'s a bad string!') # Bad
        


# More practice    
    
    
word = word.replace("\u0301", "")  # delete stress symbols from the word

# print(1 + 2 + 3 + 6)
print(1 + 3 + 3)
# print(1 + 2 + 3)

print(type('int'))
print(type(394))
print(type(2.71))

print('"""')
print('THIS IS A STRING')
print('"""')



# Taking Input

#1
user_name = input()
print('Hello, ' + user_name)

#2
user_name = input('Please, enter your name: ')
print('Hello, ' + user_name)

#3
print('Enter your name: ')
user_name = input()
print('Hello, ' + user_name)

#4 Numbers to be number
print("What's your favorite number?")
value = int(input())  # now value keeps an integer number

#5.1
day = int(input())  # 4
month = input()     # October

#5.2
print('Cinnamon roll day is celebrated on', month, day)
# Cinnamon roll day is celebrated on October 4

number1 = float(input())
number2 = float(input())
print(number1 + number2)




# String Formating

# dividing 11 by 3
print(11 / 3)  # 3.6666666666666665
print('%.3f' % (11/3))  # 3.667
print('%.2f' % (11/3))  # 3.67

# now The str. format() method
print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))

print('The {film} at {theatre} was {adjective}!'.format(film='Lord of the Rings',
                                                        adjective='incredible',
                                                        theatre='BFI IMAX'))

print('The {0} was {adjective}!'.format('Lord of the Rings', adjective='incredible'))
# The Lord of the Rings was incredible!

print('The {0} was {adjective}!'.format(adjective='incredible', 'Lord of the Rings'))
# SyntaxError: positional argument follows keyword argument


name = 'Elizabeth II'
title = 'Queen of the United Kingdom and the other Commonwealth realms'
reign = 'the longest-lived and longest-reigning British monarch'
f'{name}, the {title}, is {reign}.'


hundred_percent_number = 1823
needed_percent = 16
needed_percent_number = hundred_percent_number * needed_percent / 100

print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
# 16% from 1823 is 291.68

print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
# Rounding 291.68 to 1 decimal place is 291.7


pi = 3.141592653589793
print(f'{pi:.5f}')



#Sample Input 1:

#raybeam
#cereal-killer
#Sample Output 1:

#http://example.com/raybeam/desirable/cereal-killer/profile
#Sample Input 2:

#AnnMelon
#bodybuilder
#Sample Output 2:

#http://example.com/AnnMelon/desirable/bodybuilder/profile

nickname = input()
profession = input()
print(f'http://example.com/{nickname}/desirable/{profession}/profile')


# Write a program that gets information about a movie from the input and presents in the following format:

# movie (dir. director) came out in year

# The input format:

# 3 lines: first the title of the movie, then the name of the director and then the year of its release.

# Report a typo
# Sample Input 1:

#Fight Club
#David Fincher
#1999

# Sample Output 1:

#Fight Club (dir. David Fincher) came out in 1999


var1 = input()
var2 = input()
var3 = int(input())
print(f'{var1} (dir. {var2}) came out in {var3}')
