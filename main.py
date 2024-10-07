from components.codecaesar import chiffrement, dechiffrement

action = input ("Voulez vous (1) chiffrer ou (2) dechiffrer un texte ? 1 ou 2 :")

texte = input("Entrez votre texte : ")

while True :
    try:
        cle = int(input('Entrer la clè de chiffrement( un entier) : '))
        break
    except ValueError:
        print("la clé doit être un entier")
        

if action =='1':
    texte_chiffre= chiffrement(texte, cle)
    print(f"Texte chiffré : {texte_chiffre}")
elif action =='2':
    texte_dechiffre = dechiffrement(texte, cle)
    print(f"Texte dechiffré : {texte_dechiffre}")
else: 
    print("Action non valide, veuillez choisir 1 ou 2")