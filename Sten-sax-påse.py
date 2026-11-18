# Ett sten sax påse spel
import random
gissning = ["sten", "sax", "påse"]
wincon={
    "sten":"sax",
    "sax":"påse",
    "påse":"sten"}

player_name = input(f"Vad heter du? -> ")
omgångar = (input("Hur många omgångar vill du köra -> "))

datorn_score = 0
player_score = 0
datorns_namn=("Python311")
datorns_gissning=random.choice(gissning)


while not omgångar.isdigit():
    print("Fel! Du får bara skriva i siffror")
    omgångar = input("Försök igen: ")

omgångar = int(omgångar)

loopcount = 1

for i in range(omgångar):#här är en for loop där längden bestämms av hur många omgångar man vill köra. 

    player_gissning = input(f"\nHej {player_name}, dags för en ny runda. Förbered dig själv på att förlora. \n\nSpelomgång {loopcount} \n------------------------ \nVälj 'Sten', 'Sax' eller 'Påse': ")

    while player_gissning not in gissning:
        print("Fel! Du kan bara skriva 'Sten', 'Sax' eller 'Påse'")
        player_gissning = input("Prova igen --> ")

    datorns_gissning = random.choice(gissning)
    
    if wincon [player_gissning] == datorns_gissning:
        print("Du och datorn valde samma sak")
        print(f"{player_name} spelar: {player_gissning}\nDatorn spelar: {datorns_gissning}")
        print(f"Vinnare av spelomgång {loopcount} är oavgjort")
        loopcount = loopcount+1

    elif wincon[player_gissning] > datorns_gissning:
        player_score += 1
        print(f"{player_name} spelar: {player_gissning}\n{datorns_namn} spelar: {datorns_gissning}")
        print(f"Vinnare i spel omgång {loopcount}: är {player_name}")
        loopcount = loopcount+1

    else:
        datorn_score += 1
        print(f"{player_name} spelar: {player_gissning}\n{datorns_namn} spelar: {datorns_gissning}\nVinnare i spelomgång {loopcount}: {datorns_namn}\n")
        loopcount = loopcount+1

if player_score > datorn_score: 
    print(f"\nSLUTRESULTAT\n===================\n{player_name}: {player_score}\n{datorns_namn}: {datorn_score}\nVinnare: {player_name}!\n\nProgrammet avslutades normalt")
if datorn_score > player_score:
    print(f"\nSLUTRESULTAT\n===================\n{player_name}: {player_score}\n{datorns_namn}: {datorn_score}\nVinnare: {datorns_namn}!\n\nProgrammet avslutades normalt")
if datorn_score == player_score:
    print(f"\nSLUTRESULTAT\n===================\n{player_name}: {player_score}\n{datorns_namn}: {datorn_score}\nVinnare: Oavgjort!\n\nProgrammet avslutades normalt")