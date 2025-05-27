
import matplotlib.pyplot as plt
from matplotlib import rc

x = [val for val in range(0, 21)]
y = [val**2 for val in x]

print(x)
print(y)

plt.scatter(x,y, color="red", marker="*")

plt.xlabel("X Line")
plt.ylabel("Y Line")
plt.title("Graph")
plt.grid(True)

plt.show()

import sys
print(sys.executable)