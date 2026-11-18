# Ett sten sax påse spel
import random
gissning = ["sten", "sax", "påse"]
wincon={
    "sten":"sax",
    "sax":"påse",
    "påse":"sten"}

score=0

datorns_gissning=random.choice(gissning)
omgångar = (input("Hur många omgångar vill du köra? "))

while not omgångar.isdigit():
    print("Fel! Du får bara skriva i siffror")
    omgångar = input("Försök igen: ")

omgångar = int(omgångar)
player_name = input(f"Vad heter du? --> ")

loopcount = 1

for i in range(omgångar):

    player_gissning = input(f"\n Hej {player_name}, dags för en ny runda. Förbered dig själv på att förlora. \n  Spelomgång {loopcount} \n------------------------ \n Välj 'Sten', 'Sax' eller 'Påse': ")

    while player_gissning not in gissning:
        print("Fel! Du kan bara skriva 'Sten', 'Sax' eller 'Påse'")
        player_gissning = input("Prova igen --> ")

    datorns_gissning = random.choice(gissning)
    
    if wincon [player_gissning] == datorns_gissning:
        print("Du och datorn valde samma sak")
        print(f"{player_name} spelar: {player_gissning}\nDatorn spelar: {datorns_gissning}\n")
        print(f"Vinnare av spelomgång {loopcount} är oavgjort")
        loopcount += loopcount

    elif wincon[player_gissning] > datorns_gissning:
        score += 1
        print(f"{player_name} spelar: {player_gissning}\nDatorn spelar: {datorns_gissning}\n")
        print(f"Vinnare i spel omgång {loopcount}: ")
        loopcount += loopcount

    else:
        score -= 1
        print("Du förlorade!")
    print(f"Dina poäng {score}")
    loopcount += loopcount
        
print(score)
    
