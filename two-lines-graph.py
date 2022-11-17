import matplotlib.pyplot as plt

#defining first points
x1 = [1, 5, 3]
y1 = [5, 10, 7]

#Ploting the first points
plt.plot(x1, y1, label = 'line 1')

#defining second points
x2 = [3,4,5]
y2 = [3,2,1]

#Ploting the second points
plt.plot(x2, y2,  label = 'line 2')

plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("two lines")
plt.legend()
plt.show()
