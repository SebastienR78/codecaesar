def chiffrement(texte,cle):
    resultat=[]
    for caractere in texte:
        if caractere.isalpha():
            ascii_debut=ord('A')if caractere.isupper() else ord('a')
            nouvelle_position= (ord(caractere) - ascii_debut + cle )% 26 + ascii_debut
            resultat.append(chr(nouvelle_position))
        else:
            resultat.append(caractere)
    return ''.join(resultat)

def dechiffrement(texte,cle):
    return chiffrement(texte, -cle)