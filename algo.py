import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd

sys.dont_write_bytecode = True

data = pd.read_csv('data.csv')
km = data['km']
price = data['price']

learningRate = 0.1
T0 = 0
T1 = 0
m = len(km)
km_value = int(sys.argv[1])

def normalize(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = []
    for x in data:
        normalized_value = (x - min_val) / (max_val - min_val)
        normalized_data.append(normalized_value)
    return normalized_data

def sumError():
	sum = 0
	for i in range(m):
		sum += (T0 + T1 * km_normalized[i]) - price_normalized[i]
	return sum

def tmpTheta0():
	return learningRate * (1/m) * sumError()

def tmpTheta1():
	sum = 0
	for i in range(m):
		sum += ((T0 + T1 * km_normalized[i]) - price_normalized[i]) * km_normalized[i]
	return learningRate * (1/m) * sum

def display_graph():
	plt.plot(km, y_hat, 'b-', label='linear regression')
	plt.plot(km, price, 'r+', label='Data Points')
	plt.plot(km_value, predicted_price, 'ro', label='Prediction')

	plt.axis([min(km) * 0.9, max(km) * 1.1, min(price) * 0.9, max(price) * 1.1])
	plt.xlabel('km')
	plt.ylabel('price')
	plt.title('Price vs. km')
	plt.legend()

km_normalized = normalize(km)
price_normalized = normalize(price)

iteration = 1000
for i in range(iteration):
    tmp_T0 = tmpTheta0()
    tmp_T1 = tmpTheta1()
    
    T0 -= tmp_T0
    T1 -= tmp_T1

    km_value_normalized = (km_value - min(km)) / (max(km) - min(km))
    predicted_price_normalized = T0 + T1 * km_value_normalized

    min_price = min(price)
    max_price = max(price)
    predicted_price = predicted_price_normalized * (max_price - min_price) + min_price
    y_hat = []
    for i in range(len(km)):
        y_hat.append((T0 + T1 * km_normalized[i]) * (max_price - min_price) + min_price)


print("y = ", predicted_price, "pour km = " + sys.argv[1])
display_graph()
plt.show()


#-- = pointilles