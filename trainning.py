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
---> y = θ0 + θ1 * x      /      y = θ1 * x + θ0
	---> y est le prix estimé
	---> x est le kilométrage

x sera le meme pour les points connu et ceux de la droite
R = a la difference entre le y de la droite et le y du point connu au carre
S = somme de tous les R residus (nombre qui devra etre le plus petit possible) 


Voiture	Kilométrage 	Prix
1			20			21000
2			40			20000
3			60			19000
defninition arbitraire : learningRate = 0.01, θ0 = 0, θ1 = 0


voiture 1 --> prix estimer = 0 + (0 * 20) = 0
              erreur = 0 - 21000 = -21000
voiture 2 --> prix estimer = 0 + (0 * 40) = 0
			  erreur = 0 - 20000 = -20000
voiture 3 --> prix estimer = 0 + (0 * 60) = 0
			  erreur = 0 - 19000 = -19000

tmpθ0 = 0.01 * (1/3) * (-21000 - 20000 - 19000) = -200
tmpθ1 = 0.01 * (1/3) * ((-21000 * 20) + (-20000 * 40) + (-19000 * 60)) = -7866

θ0 = 0 - (-200) = 200
θ1 = 0 - (-7866) = 7866
y = b + ax
y = 200 + 7866 * x
voiture 1 --> prix estimer = 200 + (7866 * 20) = 200 + 157320 = 157520
voiture 2 --> prix estimer = 200 + (7866 * 40) = 200 + 314640 = 314840
voiture 3 --> prix estimer = 200 + (7866 * 60) = 200 + 472960 = 473160

2eme tour
voiture 1 --> prix estimer = 200 + (7866 * 20) = 200 + 157320 = 157520
			  erreur = 157520 - 21000 = 136520
voiture 2 --> prix estimer = 200 + (7866 * 40) = 200 + 314640 = 314840
			  erreur = 314840 - 20000 = 294840
voiture 3 --> prix estimer = 200 + (7866 * 60) = 200 + 472960 = 473160
			  erreur = 473160 - 19000 = 454160

tmpθ0 = 0.01 * (1/3) * (136520 + 294840 + 454160) = 2951
tmpθ1 = 0.01 * (1/3) * ((136520 * 20) + (294840 * 40) + (454160 * 60)) = 109202

θ0 = 200 - 2951 = -2751
θ1 = 7866 - 109202 = -101336
y = -2751 + (-101336 * x)
voiture 1 --> prix estimer = -2751 + (-101336 * 20) = -2751 + (-2026720) = -2039471
voiture 2 --> prix estimer = -2751 + (-101336 * 40) = -2751 + (-4053440) = -4056191
voiture 3 --> prix estimer = -2751 + (-101336 * 60) = -2751 + (-6070160) = -6072911

