import matplotlib.pyplot as plt
from data_init import km, price
import numpy as np

plt.plot(km, price, 'r+')

plt.axis([min(km) * 0.9, max(km) * 1.1, min(price) * 0.9, max(price) * 1.1])
plt.xlabel('km')
plt.ylabel('price')
plt.title('Price vs. km')

plt.show()