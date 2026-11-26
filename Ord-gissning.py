# Ett spel där man ska gissa ordet
#Delar upp ordet i bokstäver och skriver ut det som **********
repeat = []
ordlista = ["äpple", "banan", "citron", "druva", "jordgubbe", "kiwi", "melon", "päron", "vindruva", "dator", "sigma", "sexigamän", "gabrielibikini", "vattenflaska", "rafaelmedstring", "alexmedöl", "katt", "hund", "fisk", "fågel", "orm", "sköldpadda", "kanin", "hamster", "marsvin", "råtta", "mus", "sork", "ekorre", "rådjur", "älg", "hjort", "ren", "varg", "björn", "lodjur"]
import random
print("Välkommen till ordgissningsspelet!\n" + "")
while True: 
    ord = random.choice(ordlista)
    mängden_bokstäver = len(ord)
    print("Ordet är " + str(mängden_bokstäver) + " bokstäver långt.\n" + "----------------------")
    gissning = input("Gissa en bokstav: ")
    list_of_wrong_letters = []
    erikärbäst = 9
    antal_gissningar = 1000
    gissade_bokstäver = ["*"] * len(ord)
    fel = 0
    for i in range(antal_gissningar):
        if gissning in list_of_wrong_letters:
            print("Du har redan gissat den bokstaven. Försök igen.\n" + "----------------------")

        elif gissning in ord:
            print("Rätt gissat!\n" + "----------------------")
            for index, bokstav in enumerate(ord):
                if bokstav == gissning:
                        gissade_bokstäver[index] = gissning
            print("Ordet: " + " ".join(gissade_bokstäver))
            if "*" not in gissade_bokstäver:
                print("Grattis! Du har gissat ordet: " + ord)
                break
        else:
            fel += 1
            list_of_wrong_letters.append(gissning)
            print("Du har:" + " " + str(9-fel) + " st felgissningar kvar.\n" + "----------------------")
            print("Felaktiga bokstäver: " + ", ".join(list_of_wrong_letters)+ "\n" + "----------------------")
            print("Ordet: " + " ".join(gissade_bokstäver))
        if fel == erikärbäst:
            print("Tyvärr, du har förlorat! Ordet var: " + ord)
            break
        gissning = input("Gissa en bokstav: ")


    spela_igen = input("Vill du spela igen? (y/n): ")
    if spela_igen.lower() == "y":
        continue 
    if spela_igen.lower() == "n":
        break  