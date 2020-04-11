import numpy as np 
first = int(input("enter first number: "))
second = int(input("enter second number: "))
third = int(input("enter third number: "))
fourth = int(input("enter fourth number: "))

a = np.array([[1,1,0,0], [1,0,1,0], [0,0,1,-1],[0,1,0,1]])

b = np.array([first,second,third,fourth])

print("solution is",np.linalg.solve(a,b))
print(np.linalg.solve(a,b))