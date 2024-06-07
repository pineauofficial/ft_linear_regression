import numpy as np
import matplotlib.pyplot as plt

#from data_init import km, price
km = [240000, 139800, 150500]
price = [3650, 3800, 4400]
learningRate = 0.01
T0 = 0
T1 = 0
m = len(km)

#calcul de la somme des erreurs
def sumError():
	sum = 0
	for i in range(m):
		sum += (T0 + T1 * km[i]) - price[i]
	return sum

#calcul de tmpT0
def tmpTheta0():
	return learningRate * (1/m) * sumError()

#calcul de tmpT1
def tmpTheta1():
	sum = 0
	for i in range(m):
		sum += ((T0 + T1 * km[i]) - price[i]) * km[i]
	return learningRate * (1/m) * sum

iteration = 10
for i in range(iteration):
	T0 = T0 - tmpTheta0()
	T1 = T1 - tmpTheta1()
	print("sumError:", sumError())
	print("tmpTheta0:", tmpTheta0())
	print("tmpTheta1:", tmpTheta1())
	print("y = ", T0 + T1 * 240000)

