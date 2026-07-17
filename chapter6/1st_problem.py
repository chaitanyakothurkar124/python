marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))   
marks3 = int(input("Enter marks of subject 3: "))   
marks4 = int(input("Enter marks of subject 4: "))   

totalpercentage = (100 * (marks1 + marks2 + marks3 + marks4)) / 400
print("Total percentage:", totalpercentage)
if (totalpercentage >= 40):
    print("passed")
elif (totalpercentage < 40):
    print("try again next time")

totalsubjectpercentage1 = (100 * marks1) / 100
totalsubjectpercentage2 = (100 * marks2) / 100
totalsubjectpercentage3 = (100 * marks3) / 100
totalsubjectpercentage4 = (100 * marks4) / 100
print("Subject 1 percentage:", totalsubjectpercentage1)
print("Subject 2 percentage:", totalsubjectpercentage2)
print("Subject 3 percentage:", totalsubjectpercentage3) 
print("Subject 4 percentage:", totalsubjectpercentage4)

if (totalsubjectpercentage1 >= 33):
    print("Subject 1 passed")
else:    print("Subject 1 failed")  
if (totalsubjectpercentage2 >= 33):
    print("Subject 2 passed")
else:    print("Subject 2 failed")
if (totalsubjectpercentage3 >= 33):
    print("Subject 3 passed")
else:    print("Subject 3 failed")
if (totalsubjectpercentage4 >= 33):
    print("Subject 4 passed")
else:    print("Subject 4 failed")