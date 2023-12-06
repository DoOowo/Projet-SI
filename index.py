  


def RechercheEtudiant(f):
  nom = input("Entrer le nom de l'etudiant que vous voulez rechercher: ")  
  prenom = input("Entrer le prenom de l'etudiant que vous voulez rechercher: ")

  
  f.seek(0)
  lines = f.readlines()
  for line in lines:
    line = line.strip().split('\t')
    if line[1] == nom and line[2]== prenom: 
      print(line)




def AjouterEtudiant(f):
  matricule= input('matricule: ')
  nom = input('Nom: ')
  prenom = input('Prenom: ')
  Jour= input('Jour:')
  Mois= input('Mois:')
  Annee= input('Annee: ')
  Date_de_naissance = {
  "Jour": Jour,
  "Mois": Mois,
  "Annee": Annee
}
  Filiere= input('Filiere: ')
  f.write("{} \t {} \t {} \t {}/{}/{} \t {} \n ".format(matricule,nom,prenom, Date_de_naissance["Jour"], Date_de_naissance["Mois"], Date_de_naissance["Annee"], Filiere))


operation = int(input('Que voulez vous faire: (1)Ajouter des etudiants, (2)Rechercher un etudiant: '))
f = open("demofile2.txt", "a+")

if operation == 1:
  Num= int(input('Entrer le nombre de vos etudiants: '))
  for i in range(Num): 
    AjouterEtudiant(f)
elif operation == 2:
  RechercheEtudiant(f)



  


    


f.close()










