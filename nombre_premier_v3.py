#!/usr/bin/python3.11

# la condition pour Premier : uniquement divisible par lui meme et par 1
# Attention ! Au dela du nombre 5000, l'ordinateur ralentit (et l'un des core tourne a 100%)

def isfirst(chiffre_max):
	i = chiffre_max
	while(i > 2):
		res = chiffre_max/(i-1)
		#print(chiffre_max, " / ", i-1, " = ", res)
		x = str(res)
		cpt = 0
		position_point = 0
		for ele in x:
			if(ele == "."):
				position_point = cpt
			cpt += 1

		if(int(x[position_point+1:]) == 0):
			# le chiffre n'est pas premier vu qu'il a un autre diviseur
			#print(chiffre_max, " n'est pas premier")
			return True
		i -= 1

prime_nb_list = []
chiffre_max = int(input("Vous voulez la liste de tous les chiffres premier jusqu'a quel nombre ? : "))
print("Liste des nombres premiers de", chiffre_max, "a 2 :")
while(chiffre_max >= 2):
	if(isfirst(chiffre_max) is not True):
		#print(chiffre_max, "est premier")
		prime_nb_list.append(chiffre_max)
	chiffre_max -= 1

print(prime_nb_list)
j = 0
while(j <= len(prime_nb_list)-1):
	try:
		print(prime_nb_list[j], prime_nb_list[j+1], prime_nb_list[j+2], prime_nb_list[j+3])
		j += 4
	except:
		pass