# Ett sten sax påse spel
import random
gissning = ["sten", "sax", "påse"]
wincon={
    "sten":"sax",
    "sax":"påse",
    "påse":"sten"}

<<<<<<< HEAD
score=[]

datorns_gissning = random.choice(gissning)
omgångar = (input("Hur många omgångar vill du köra?\n"))
=======
score=0


datorns_gissning=random.choice(gissning)
omgångar=(input("hur många omgångar vill du köra.\n"))
>>>>>>> e5f739e2447fde002e38f0133bb844fe073e5c1b

while not omgångar.isdigit():
    print("Fel! Du får bara skriva i siffror")
    omgångar = input("Försök igen: ")

omgångar = int(omgångar)
player_name = input(f"Vad heter du? --> ")

for i in range(omgångar):
<<<<<<< HEAD
    player_gissning = input(f"Hej {player_name}, förbered dig själv på att förlora.\nVälj 'Sten', 'Sax' eller 'Påse': ")
=======
    player_gissning=input(f"hej {player_name} daks för runda förbered dig själv på att förlora. \n  spel omgång 1 \n------------------------ \n välj sten sax eller påse: ")
>>>>>>> e5f739e2447fde002e38f0133bb844fe073e5c1b
    while player_gissning not in gissning:
        print("Fel! Du kan bara skriva 'Sten', 'Sax' eller 'Påse'")
        player_gissning = input("Prova igen --> ")

    datorns_gissning=random.choice(gissning)
    
    if wincon [player_gissning]==datorns_gissning:
        print("Du och datorn valde samma sak")

    elif wincon[player_gissning]>datorns_gissning:
<<<<<<< HEAD
        score.append(1)
        score = [sum(score)]
        print("Du vann!")
        print(score)

    else:
        score.append(-1)
        score=[sum(score)]
        print("Du förlorade!")
=======
        score+=1
        print("du vann")
        print(score)

    else:
        score-=1
        print("du förlora")
>>>>>>> e5f739e2447fde002e38f0133bb844fe073e5c1b
        print(score)
    print(f"Dina poäng {score}")
        

    
