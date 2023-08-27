#for this program we use monte carlo simulation to approximate pie.
#The large number of dots you enter, the better the approximation is
import random
import math

flag = True
while flag == True:
    all_dots = int(input("Enter the dots to approximate pie:"))
    dots_inside_circle = 0
    radius = 1
    
    for i in range(all_dots):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if x**2 + y**2 <= radius**2:
            dots_inside_circle += 1 
        pie_approximation = 4*(dots_inside_circle/all_dots)
        
    print()
    print("The approximation of pie at ",i+1,"is:",pie_approximation)
    pie_value = math.pi
    error_percentage = ((pie_value - pie_approximation)/pie_approximation)*100
    print()
    print("The real value of pie is:",pie_value)
    print()
    print("The error percentage is :", error_percentage)
