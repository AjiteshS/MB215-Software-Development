nGrade = float(input("Enter your numeric grade: "))
if nGrade >= 90:
    iGrade = "A+"
    print(f"Your letter grade is {iGrade}")
elif nGrade in range (80,89):
    oGrade = "A" 
    print(f"Your grade is {oGrade}")
elif nGrade in range (70, 79): 
    pGrade = "B"
    print(f"Your grade is {pGrade}")
elif nGrade in range (60,69): 
    aGrade = "C"
    print(f"Your grade is {aGrade}")
elif nGrade in range (50,59):   
    sGrade = "D"
    print (f"Your grade is {sGrade}")
else:
    rGrade = "F"
    print (f"Your grade is {rGrade}")