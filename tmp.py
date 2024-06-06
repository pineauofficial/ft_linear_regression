import matplotlib.pyplot as plt

plt.plot([0, 1, 2, 3, 4, 5, 6, 7], [2, 4, 6, 8, 10, 12, 14, 16], 'r+')

plt.axis((0, 10, 0, 20))
plt.ylabel('axe y')
plt.xlabel('axe x')

plt.show()