import random
print("Välkommen till Mastermind!")
print()
print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.")
print("Du ska försöka gissa denna kods siffror på max 12 drag.")
print("Efter respektive gissning så kommer du att få en respons:")
print("För varje gissad korrekt siffra på korrekt plats i koden: ✔")
print("För varje gissad korrekt siffra på fel plats i koden: □")
print("För de siffror som inte finns med i koden ges ingen markering.")
print()
print("Exempel: om den slumpade koden är 2315")
print("och du gissar 3165")
print("så blir responsen ✔□□")
print()
print("Du får välja mellan två svårighetsnivåer:")
print("Lättare nivå: Alla siffror är garanterat olika")
print("Svårare nivå: Det kan finnas upprepningar av en eller flera siffror")
print()

attempts_svår = 12
attempts_lätt = 8

siffer_lista= ["1", "2", "3", "4", "5", "6"]

random_kod_lätt=random.sample(siffer_lista, k=4) 

random_kod_svår=random.choices(siffer_lista, k=4) 

print("Välkommen till Mastermind!")

print("1. Lätt")
print("2. Svår")
4
niva = input("Välj en svårighetsgrad: ")


if niva == "1" or  niva == "lätt":
    print("Du valde den lätta nivån") 
    for i in range (attempts_lätt):
        print("Du har " + str(attempts_lätt - i) + " försök kvar.")
        player_gissning = input("Gissa koden: ")  
        if player_gissning[0] == random_kod_lätt[0]:
            print("✔")
        if player_gissning[1] == random_kod_lätt[1]:
            print("✔")
        if player_gissning[2] == random_kod_lätt[2]:
            print("✔")
        if player_gissning[3] == random_kod_lätt[3]:
            print("✔")
        elif player_gissning[0] != random_kod_lätt[0]:
            print("□")
        elif player_gissning[1] != random_kod_lätt[1]:
            print("□")
        elif player_gissning[2] != random_kod_lätt[2]:
            print("□")
        elif player_gissning[3] != random_kod_lätt[3]:
            print("□")
    if player_gissning == random_kod_lätt:
        print("Grattis du gissade rätt på en siffra!")
    elif attempts_lätt == 0:
        print(f"Tyvärr du har inga försök kvar, koden var: {random_kod_lätt}")
else:
    print("Du valde den svåra nivån lycka till ")
    for i in range (attempts_svår):
        print("Du har " + str(attempts_svår - i) + " försök kvar.")
        player_gissning = input("Gissa koden: ")
        if player_gissning[0] == random_kod_svår[0]:
            print("✔")
        if player_gissning[1] == random_kod_svår[1]:
            print("✔")
        if player_gissning[2] == random_kod_svår[2]:
            print("✔")
        if player_gissning[3] == random_kod_svår[3]:
            print("✔")
        elif player_gissning[0] != random_kod_svår[0]:
            print("□")
        elif player_gissning[1] != random_kod_svår[1]:
            print("□")
        elif player_gissning[2] != random_kod_svår[2]:
            print("□")
        elif player_gissning[3] != random_kod_svår[3]:
            print("□")
    if player_gissning == random_kod_svår:
        print("Grattis du gissade rätt på en siffra!")
    elif attempts_svår == 0:
        print(f"Tyvärr du har inga försök kvar, koden var: {random_kod_svår}")
        
        
        


    
