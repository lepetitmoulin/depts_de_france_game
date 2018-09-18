#This version allows the user to choose whether (s)he wants to identify a department by its name or by its number (INSEE code)

import random

dept_names = ["Ain", "Aisne", "Allier", "Alpes-de-Haute-Provence", "Hautes-Alpes", "Alpes-Maritimes", "Ardèche", "Ardennes", "Ariège", "Aube", "Aude", "Aveyron", "Bouches-du-Rhône", "Calvados", "Cantal", "Charente", "Charente-Maritime", "Cher", "Corrèze", "Corse-du-Sud", "Haute-Corse", "Côte-d'Or", "Côtes-d'Armor", "Creuse", "Dordogne", "Doubs", "Drôme", "Eure", "Eure-et-Loir", "Finistère", "Gard", "Haute-Garonne", "Gers", "Gironde", "Hérault", "Ille-et-Vilaine", "Indre", "Indre-et-Loire", "Isère", "Jura", "Landes", "Loir-et-Cher", "Loire", "Haute-Loire", "Loire-Atlantique", "Loiret", "Lot", "Lot-et-Garonne", "Lozère", "Maine-et-Loire", "Manche", "Marne", "Haute-Marne", "Mayenne", "Meurthe-et-Moselle", "Meuse", "Morbihan", "Moselle", "Nièvre", "Nord", "Oise", "Orne", "Pas-de-Calais", "Puy-de-Dôme", "Pyrénées-Atlantiques", "Hautes-Pyrénées", "Pyrénées-Orientales", "Bas-Rhin", "Haut-Rhin", "Rhône", "Haute-Saône", "Saône-et-Loire", "Sarthe", "Savoie", "Haute-Savoie", "Paris", "Seine-Maritime", "Seine-et-Marne", "Yvelines", "Deux-Sèvres", "Somme", "Tarn", "Tarn-et-Garonne", "Var", "Vaucluse", "Vendée", "Vienne", "Haute-Vienne", "Vosges", "Yonne", "Territoire de Belfort", "Essonne", "Hauts-de-Seine", "Seine-Saint-Denis", "Val-de-Marne", "Val-d'Oise", "Guadeloupe", "Martinique", "Guyane", "La Réunion", "Mayotte"]
dept_nums = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "2A", "2B", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "971", "972", "973", "974", "976"]

def dept_de_france_par_numéro(numéro):

	print("Bienvenue au plus beau jeu du monde ! Vous avez l'occasion de tester votre connaissance des départements de France !")
	print("Je vais vous présenter un numéro et vous allez identifier le nom du départment auquel il correspond. Simple, non ?")
	print("Je réflechis . . . ")
	print("Le voilà !")
	print(numéro)

	depts_essayes = []
	count = 3
	
	while True:
		
		guess = str(input("Dites-moi : quel est le nom du département indiqué par ce numéro-là ? (" + (numéro) + ") "))
		
		if count<=0:
			print("Vous n'avez plus de chances ! Quel pauvre con ! C'était " + secret_dept_name)
			break
		elif guess in depts_essayes:
			print("Vous avez déjà tenté ce nom-là ! Pour ça, vous perdez un point. Prenez ça ! Arrêtez de déconner.")
			count-=1
		elif guess not in dept_names:
			print("Soit ça n'existe pas, soit vous avez mal écrit. L'orthographe, ça compte !")
			count-=1
		elif dept_names.index(guess) == dept_nums.index(numéro):
			print("Youpi ! Vous êtes trop fort ! Vous connaissez bien la France !")
			print("Ça vaut " + str(count * 100) + " points !")
			break
		else:
			print("Non, c'est pas ça. Essayez encore !")
			count-=1
		depts_essayes.append(guess)

def dept_de_france_par_nom(nom):

	print("Bienvenue au plus beau jeu du monde ! Vous avez l'occasion de tester votre connaissance des départements de France !")
	print("Je vais vous présenter un nom et vous allez identifier le numéro du départment auquel il correspond. Simple, non ?")
	print("Je réflechis . . . ")
	print("Le voilà !")
	print(nom)

	numéros_essayes = []
	count = 3
	
	while True:

		guess = str(input("Dites-moi : quel est le numéro du département indiqué par ce nom-là ? (" + (nom) + ") "))

		if count<=0:
			print("Vous n'avez plus de chances ! Quel(le) pauvre con(ne) ! C'était " + secret_numéro)
			break
		elif guess in numéros_essayes:
			print("Vous avez déjà tenté ce nom-là ! Pour ça, vous perdez un point. Prenez ça ! Arrêtez de déconner.")
			count-=1
		elif guess not in dept_nums:
			print("Soit ça n'existe pas, soit vous avez mal écrit. L'orthographe, ça compte !")
			count-=1
		elif dept_nums.index(guess) == dept_names.index(nom):
			print("Youpi ! Vous êtes trop fort(e) ! Vous connaissez bien la France !")
			print("Ça vaut " + str(count * 100) + " points !")
			break
		else:
			print("Non, c'est pas ça. Essayez encore !")
			count-=1
		numéros_essayes.append(guess)


x = str(input("Comment voulez-vous jouer ? Par nom ou par numéro ? ")).lower()
print(x)

if x == "par numéro" or x=="numéro":
	numéro = random.choice(dept_nums)
	secret_dept_name = dept_names[dept_nums.index(numéro)]
	dept_de_france_par_numéro(numéro)
elif x == "par nom" or x=="nom":
	nom = random.choice(dept_names)
	secret_numéro = dept_nums[dept_names.index(nom)]
	dept_de_france_par_nom(nom)
else:
	print("Vous ne savez pas jouer. Au revoir.")
