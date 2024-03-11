#!/usr/bin/python3.11

# Becareful ! Up to 5000 and your computer begin to slow down

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
			return True
		i -= 1

prime_nb_list = []
chiffre_max = int(input("Your maximum number to calculate to : "))
print("Prime numbers list from : ", chiffre_max, "to 2 :")
while(chiffre_max >= 2):
	if(isfirst(chiffre_max) is not True):
		#print(chiffre_max, "is prime")
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
