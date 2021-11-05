import matplotlib.pyplot as plt
import numpy as np

print("Generate a random normal distribution of size m 1-D array.")
m = 100
s = np.random.normal(0,1,m)
print(s)
print("mean 平均")
print(np.mean(s))
print("standard deviation標準差")
print(np.std(s))
print("Visualization of Normal Distribution of this 1-D array (plot a figure)")
plt.hist(s, m)
plt.show()
print("Reshape this 1-D array to nxn array and print")
b = s.reshape(10,10)
print(b)
print("Determinant value")
Dv = np.linalg.det(b)
print(Dv)
if Dv != 0 :
    print("Find the inverse of a matrix and print.")
    y = np.linalg.inv(b)
    print(y)
    print("Give a nx1 b constant array.")
    # ● b will be given
    b = 10
    ed = np.random.rand(b)
    print(ed)
    print("Solve the nxn linear equations and print the result.")
    r = np.linalg.solve(b,ed)
    print(r)