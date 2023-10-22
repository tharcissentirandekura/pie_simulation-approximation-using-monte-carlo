import math
import time
import random
import matplotlib.pyplot as plt

ax,fig = plt.subplots()
# ax.set_facecolor("black")

all_dots = int(input("Enter the dots to approximate pie:"))
dots_inside_circle = 0
radius = 1
current_pi = []


start_time = time.time() 

for trialNum in range(1,all_dots):
    x = random.uniform(-radius,radius)
    y = random.uniform(-radius,radius)
    if x**2 + y**2 <= radius**2:
        dots_inside_circle += 1
    current_pi.append(4*dots_inside_circle/trialNum)

# plt.plot(current_pi, color = "red", linewidth = 4)
    
end_time = time.time()

print("The approximation of pi is:",current_pi[-1])

error_percentage = ((math.pi - current_pi[-1])/math.pi)*100
print()
print("The real value of pi is:",math.pi)
print()
print("The error percentage is :", error_percentage)
print()
time_taken = end_time - start_time
print("The time it took to run on a sample of " ,all_dots," dots is :",time_taken,"secs")



fig.set_facecolor("black" )
plt.plot(current_pi, color = "red", linewidth = 2)
plt.title("Instantenous pi approximation", size = 14, color = "blue")
plt.ylabel("Pi_approximation value", color = "green",size = 14)
plt.xlabel("Samples of dots used", color = "green", size = 14)
plt.grid()

plt.show()
