tmpθ0=learningRate×(m1​)×∑(estimatedPrice−price)
tmpθ1=learningRate×(m1)×∑((estimatedPrice−price)×km)

- learningRate est le taux d'apprentissage (ou pas de gradient),
- estimatedPrice est le prix estimé par le modèle,
- price est le prix réel,
- km est le kilométrage de la voiture,
- m est le nombre total d'exemples de données (ou le nombre total de paires de km et price).

tmpθ0 = learningRate * (1 / m) * estimatedPrice(km - price)
tmpθ1 = learningRate * (1 / m) * (estimatedPrice(km - price) * km)

---> θ0 et θ1 sont les led parametres de la regression lineaire
---> y = θ0 + θ1 * x
	---> y est le prix estimé
	---> x est le kilométrage