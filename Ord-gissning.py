# Ett spel där man ska gissa ordet
#Delar upp ordet i bokstäver och skriver ut det som **********
ordlista = ["äpple", "banan", "citron", "druva", "jordgubbe", "kiwi", "melon", "päron", "vindruva", "dator", "sigma", "sexigamän", "gabrielibikini", "vattenflaska", "rafaelmedgstring", "alexmedöl", "katt", "hund", "fisk", "fågel", "orm", "sköldpadda", "kanin", "hamster", "marsvin", "råtta", "mus", "sork", "ekorre", "rådjur", "älg", "hjort", "ren", "varg", "björn", "lodjur"]
import random
antal_gissningar = 9
if antal_gissningar > 0:
    print("Du har " + str(antal_gissningar) + " gissningar kvar.")  
ord = random.choice(ordlista)
mängden_bokstäver = len(ord)
print("Välkommen till ordgissningsspelet!. Ordet är " + str(mängden_bokstäver) + " bokstäver långt.")
print("Mängden bokstäver i ordet är: " + str(len(ord)))
gissade_bokstäver = []
for bokstav in ord:
        gissade_bokstäver.append("*")   
print("Gissade bokstäver: " + " ".join(gissade_bokstäver))
svar = input("Gissa en bokstav: ")
while svar != ord:
    if svar in ord:
        print("Rätt bokstav!")
        for i in range(len(ord)):
            if ord[i] == svar:
                gissade_bokstäver[i] = svar
        print("Gissade bokstäver: " + " ".join(gissade_bokstäver))
    else:
        print("Gissningar kvar: " + " ".join(gissade_bokstäver))
    svar = input("Gissa en bokstav: ")
    print("Alla gissade bokstäver: " + " ".join(gissade_bokstäver))

