# Familiar functions

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True
# Print out type of var1
print(type(var1))
# Print out length of var1
print(len(var1))
# Convert var2 to an integer: out2
out2 = int(var2)



# Multiple arguments

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

Use + to merge the contents of first and second into a new list: full.

# Paste together first and second: full
full = first + second
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)
# Print out full_sorted
print(full_sorted)




# String Methods

# string to experiment with: place
place = "poolhouse"
# Use upper() on place: place_up
place_up = place.upper()
# Print out place and place_up
print(place, place_up)
# Print out the number of o's in place
print(place.count('o'))


 
# List Methods

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)
# Print out areas
print(areas)
# Reverse the orders of the elements in areas
areas.reverse()
# Print out areas
print(areas)



# Import package


# Definition of radius
r = 0.43
# Import the math package
import math
# Calculate C
C = 2 * math.pi * r
# Calculate A
A = math.pi * r*r
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))



# Selective import


# Definition of radius
r = 192500
# Import radians function of math package
from math import radians
# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)
# Print out dist
print(dist)


# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))