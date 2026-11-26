import random

def rättning_lätt(player_gissning, random_kod_lätt):
    for i in range(4):
        if player_gissning[i] == random_kod_lätt[i]:
            print("✔")
        elif player_gissning[i] != random_kod_lätt[i]:
            print("□")
    return rättning_lätt

#def rättning_lätt(player_gissning, random_kod_lätt):
    #i=0
    #feedback=""
    #remaining=[]
    #for bokstav in player_gissning:
        #remaining.append(bokstav)
    #while i <= 4:
        #if player_gissning[i] == random_kod_lätt[i]:
            #feedback+="✔"
            #remaining.remove(player_gissning[i])
        #elif player_gissning[i] != random_kod_lätt[i]:
            #feedback+="□"
            #remaining.remove(player_gissning[i])
        #elif player_gissning[i] not in random_kod_lätt:
           # feedback+=""
            #remaining.remove(player_gissning[i])
        #i += 1
    #return feedback



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


attempts_svår = 12
attempts_lätt = 12

siffer_lista= [1, 2, 3, 4, 5, 6]

random_kod_lätt=random.sample(siffer_lista, k=4) 

random_kod_svår=random.choices(siffer_lista, k=4) 

print("Välkommen till Mastermind!")

print("1. Lätt")
print("2. Svår")

niva = input("Välj en svårighetsgrad: ")
if niva == "1" or  niva == "lätt":
    for i in range (attempts_lätt, 0, -1):
        
        player_gissning = input(f"Du valde den lätta nivån. dags att gissa koden! Du har {attempts_lätt} försök på dig att gissa koden. Lycka till!\n drag#        drag       feedback\n------------------------------------\n{attempts_lätt-i}: ")
        print(f"{rättning_lätt(player_gissning, random_kod_lätt)}")
        x=x-1







#if niva == "1" or  niva == "lätt":
    #print("Du valde den lätta nivån") 
    #for i in range (attempts_lätt):
       # print("Du har " + str(attempts_lätt - i) + " försök kvar.")
        #player_gissning = input("Gissa koden: ")  
        #if player_gissning[0] == random_kod_lätt[0]:
            #print("✔")
        #if player_gissning[1] == random_kod_lätt[1]:
            #print("✔")
        #if player_gissning[2] == random_kod_lätt[2]:
            #print("✔")
        #if player_gissning[3] == random_kod_lätt[3]:
            #print("✔")
        #elif player_gissning[0] != random_kod_lätt[0]:
            #print("□")
        #elif player_gissning[1] != random_kod_lätt[1]:
            #print("□")
        #elif player_gissning[2] != random_kod_lätt[2]:
            #print("□")
        #elif player_gissning[3] != random_kod_lätt[3]:
            #print("□")
    #if player_gissning == random_kod_lätt:
        #print("Grattis du gissade rätt på en siffra!")
    #elif attempts_lätt == 0:
        #print(f"Tyvärr du har inga försök kvar, koden var: {random_kod_lätt}")
#else:
    #print("Du valde den svåra nivån lycka till ")
    #for i in range (attempts_svår):
        #print("Du har " + str(attempts_svår - i) + " försök kvar.")
        #player_gissning = input("Gissa koden: ")
        #if player_gissning[0] == random_kod_svår[0]:
            #print("✔")
        #if player_gissning[1] == random_kod_svår[1]:
            #print("✔")
        #if player_gissning[2] == random_kod_svår[2]:
            #print("✔")
        #if player_gissning[3] == random_kod_svår[3]:
            #print("✔")
        #elif player_gissning[0] != random_kod_svår[0]:
            #print("□")
        #elif player_gissning[1] != random_kod_svår[1]:
            #print("□")
        #elif player_gissning[2] != random_kod_svår[2]:
            #print("□")
        #elif player_gissning[3] != random_kod_svår[3]:
            #print("□")
    #if player_gissning == random_kod_svår:
        #print("Grattis du gissade rätt på en siffra!")
    #elif attempts_svår == 0:
        #print(f"Tyvärr du har inga försök kvar, koden var: {random_kod_svår}")