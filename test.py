# Importer les bibliothèques nécessaires
import numpy as np

# Données
km = np.array([240000, 139800, 150500])
price = np.array([3650, 3800, 4400])

# Normaliser les données
km_mean = np.mean(km) # me donne la moyenne
km_std = np.std(km) # me donne l'ecarttype
km_normalized = (km - km_mean) / km_std # normalisation des données
print("Données normalisées:", km_normalized)

# Paramètres
learningRate = 0.01  # Taux d'apprentissage ajusté
T0 = 0.0
T1 = 0.0
m = len(km)

# Fonction pour calculer la somme des erreurs pour T0
def compute_gradient_T0(T0, T1):
    return np.sum((T0 + T1 * km_normalized) - price) / m

# Fonction pour calculer la somme des erreurs pour T1
def compute_gradient_T1(T0, T1):
    return np.sum(((T0 + T1 * km_normalized) - price) * km_normalized) / m

# Fonction de coût pour vérifier la convergence
def compute_cost(T0, T1):
    return np.sum(((T0 + T1 * km_normalized) - price) ** 2) / (2 * m)

# Gradient descent
iterations = 1000
for iteration in range(iterations):
    tempT0 = learningRate * compute_gradient_T0(T0, T1)
    tempT1 = learningRate * compute_gradient_T1(T0, T1)
    
    T0 -= tempT0
    T1 -= tempT1
    
    if iteration % 100 == 0:  # Afficher les valeurs toutes les 100 itérations
        cost = compute_cost(T0, T1)
        print(f"Iteration {iteration}: Cost = {cost}, T0 = {T0}, T1 = {T1}")

# Affichage final
print("Paramètres finaux:")
print("T0:", T0)
print("T1:", T1)
print("Equation finale: y = ", T0, " + ", T1, " * (x - ", km_mean, ") / ", km_std)

# Prédiction pour 240000 km
y_pred = T0 + T1 * (240000 - km_mean) / km_std
print("Prédiction pour 240000 km:", y_pred)
