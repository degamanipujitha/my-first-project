import matplotlib.pyplot as plt

x = [1, 2, 3, 6, 5, 9]
y = [2, 3, 6, 8, 10, 7]

plt.plot(x, y, marker='o', color='blue')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("X vs Y Graph")
plt.grid(True)

plt.show()
