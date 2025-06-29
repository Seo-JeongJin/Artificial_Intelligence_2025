
import matplotlib.pyplot as plt

x = range(-10, 11)
y1 = [2 * val for val in x]
y2 = [4 * val for val in x]
y3 = [8 * val for val in x]

plt.plot(x, y1, label="2x", color="red")
plt.plot(x, y2, label="4x", marker="o")
plt.plot(x, y3, label="8x", marker="x")

plt.legend()
plt.title("A graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)

plt.show()