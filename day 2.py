# Day 2: 30 Days of python programming
import math

# Level 1:

# Declare a first name variable and assign a value to it
first_name = "Dinh Nguyen"

# Declare a last name variable and assign a value to it
last_name = "Son Tung"

# Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name

# Declare a country variable and assign a value to it
country = "United States"

# Declare a city variable and assign a value to it
city = "New York"

# Declare an age variable and assign a value to it
age = 23

# Declare a year variable and assign a value to it
year = 2023

# Declare a variable is_married and assign a value to it
is_married = True

# Declare a variable is_true and assign a value to it
is_true = False

# Declare a variable is_light_on and assign a value to it
is_light_on = True

# Declare multiple variables on one line
variable1, variable2, variable3 = 1, 2, 3

# Level 2
# Compare the length of your first name and your last name
if len(first_name) > len(last_name):
    print(f"My first name: {first_name} - {len(first_name)} is longer > "
          f"than my last name: {last_name} - {len(last_name)}")
else:
    print(f"My first name: {first_name} - {len(first_name)} is shorter <"
          f" than my last name: {last_name} - {len(last_name)}")

# The radius of a circle is 30 meters.
radius = 30
area_of_circle = math.pi*(radius**2)
circum_of_circle = 2*math.pi*radius
print(area_of_circle)
print(circum_of_circle)

while radius == 30:
    radius = int(input("Type in the rad of your circle: "))
    area_of_circle = math.pi * (radius ** 2)
    circum_of_circle = 2 * math.pi * radius
    print(area_of_circle)
    print(circum_of_circle)

print("End of Day 2")

