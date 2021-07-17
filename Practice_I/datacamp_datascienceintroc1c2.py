

#Importing Python modules

# Use an import statement to import statsmodels
import statsmodels


# Import statsmodels under the alias sm
import statsmodels as sm


# Use an import statement to import seaborn with alias sns
import seaborn as sns


#Correcting a broken import

# Fix the import of numpy to run without errors
import NumPy as np


import numpy as np

(Python is case-sensitive, so numpy must be all lowercase)



# Creating a float


# Fill in Bayes' age (4.0)
bayes_age = 4.0

# Display the variable bayes_age
print(bayes_age)



# Creating strings

# Bayes' favorite toy
favorite_toy = 'Mr. Squeaky'

# Bayes' owner
owner = 'DataCamp'

# Display variables
print(favorite_toy)
print(owner)



Correcting string errors

# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors

birthday = "2017-07-14'
case_id = 'DATACAMP!123-456?

birthday = "2017-07-14"
case_id = 'DATACAMP!123-456?'


# Load a DataFrame

Use pd.read_csv to load data from a CSV file called ransom.csv. This file represents the frequency of each letter in the ransom note for Bayes.

# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)



# Correcting a function error

# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors

# Plot a graph
plt.plot(x_values y_values)

# Display the graph
plt.show()

# Plot a graph
plt.plot(x_values, y_values)



# Snooping for suspects

# Define plate to represent a plate beginning with FRQ

# Use * to represent the missing four letters
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

# Call lookup_plate() with the keyword argument for color
lookup_plate(plate, color='Green')


# Loading a DataFrame

# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv('credit_records.csv')

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())


# Inspecting a DataFrame

# Use .info() to inspect the DataFrame credit_records
print(credit_records.info())


# Two methods for selecting columns

# Select the column item from credit_records

# Use brackets and string notation
items = credit_records[item]


items = credit_records['item']


# Display the results
print(items)


# Select the column item from credit_records

# Use dot notation
items = credit_records.item

# Display the results
print(items)


# Correcting column selection errors

# One or more lines of code contain errors.
# Fix the errors so that the code runs.
# Select the location column in credit_records
location = credit_records[location]
# Select the item column in credit_records
items = credit_records."item"
# Display results
print(location)

# One or more lines of code contain errors.
# Fix the errors so that the code runs.
# Select the location column in credit_records
location = credit_records['location']
# Select the item column in credit_records
items = credit_records.item
# Display results
print(location)


# More column selection mistakes

# Use info() to inspect mpr
print(mpr.info())

# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors
# Select column "Dog Name" from mpr
name = mpr.Dog Name
# Select column "Missing?" from mpr
is_missing = mpr.Missing?
# Display the columns
print(name)
print(is_missing)

# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors
# Select column "Dog Name" from mpr
name = mpr['Dog Name']
# Select column "Missing?" from mpr
is_missing = mpr['Missing?']
# Display the columns
print(name)
print(is_missing)


# Logical testing


# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")

# Is fur_color not equal to "brown"?
print(fur_color != "brown")


# Selecting missing puppies

# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)
# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == 'Still Missing']
print(still_missing)
# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)







Narrowing the list of suspects


# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.location == 'Pet Paradise']

# Display
print(purchase)
