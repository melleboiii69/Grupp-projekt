# Ett sten sax påse spel
import random
gissning = ["sten", "sax", "påse"]
wincon={
    "sten":"sax",
    "sax":"påse",
    "påse":"sten"}

score=[]

datorns_gissning = random.choice(gissning)
omgångar = (input("Hur många omgångar vill du köra?\n"))

while not omgångar.isdigit():
    print("Fel! Du får bara skriva i siffror")
    omgångar = input("Försök igen: ")

omgångar = int(omgångar)
player_name = input(f"Vad heter du? --> ")

for i in range(omgångar):
    player_gissning = input(f"Hej {player_name}, förbered dig själv på att förlora.\nVälj 'Sten', 'Sax' eller 'Påse': ")
    while player_gissning not in gissning:
        print("Fel! Du kan bara skriva 'Sten', 'Sax' eller 'Påse'")
        player_gissning = input("Prova igen --> ")

    datorns_gissning=random.choice(gissning)
    
    if wincon [player_gissning]==datorns_gissning:
        print("Du och datorn valde samma sak")

    elif wincon[player_gissning]>datorns_gissning:
        score.append(1)
        score = [sum(score)]
        print("Du vann!")
        print(score)

    else:
        score.append(-1)
        score=[sum(score)]
        print("Du förlorade!")
        print(score)
    print(f"Dina poäng {score}")
        

    
