import matplotlib.pyplot as plt
from data_init import km, price
import numpy as np

plt.plot(price, km, 'r+')

plt.axis([min(price) * 0.9, max(price) * 1.1, min(km) * 0.9, max(km) * 1.1])
plt.ylabel('km')
plt.xlabel('price')
plt.title('Price vs. km')



plt.show()