print("Hello user, this program will calculate multiple aspects of a cylinder")
DIAMETER =  float(input("Input the diameter of your cylinder: "))
HEIGHT =  float(input("Input the height of the cylinder: "))
PI = 3.141592 
RADIUS = DIAMETER / 2 
VOLUME = (round (PI,2)) * RADIUS * HEIGHT
print(f"The volume of your cylinder is 5{round(VOLUME,2)}CM squared")