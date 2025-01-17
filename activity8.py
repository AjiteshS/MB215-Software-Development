# this is a simple python code to calculate gross pay 
hours = float(input("Input your number of hours worked: "))
# by using float values for the hours and rate we will be able to accomodate for irrational hours or pay 
rate = float(input("Input your hourly pay rate: "))
print(f"Your gross pay is {hours * rate}")
