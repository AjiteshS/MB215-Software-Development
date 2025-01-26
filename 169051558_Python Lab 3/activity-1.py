# Describe the program 
print("Hello user, this program will convert a number from KM to MPH ")
# Ask the user to input their value 
KILOMETER = float(input("Enter a number to represent KM: "))
# Using a general multiplier, calculate the vlaue in miles 
MILES = KILOMETER * 0.621371 
# Display the result in a sentence 
print (f"{KILOMETER}KM is {(round(MILES,2))}MPH ") 