"""
Code GarlaKowski
    Encoder par répetition de clé.
V1 - 01/2022
V1.1 - 03/2025
"""

##
Coder = input("Valeur à coder: ")
Cle = input("Clé: ")
##

resultat = []
testeur_cle = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Coder = Coder.lower()
Cle = Cle.lower()

Cle = [i for i in Cle]
Coder = [i for i in Coder]

for testeur_mot in range(len(Coder)):
    if not Coder[testeur_mot] == ' ':
        resultat.append(alphabet[alphabet.index(Cle[testeur_cle]) - alphabet.index(Coder[testeur_mot]) - 1])
        testeur_cle = testeur_cle + 1
    #else:
        #resultat.append(' ')
    if testeur_cle >= len(Cle):
        testeur_cle = 0

resultat = ''.join(resultat)


print(resultat)
print('Codage de', Coder, 'avec la clé:', Cle)