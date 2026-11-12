# Ett sten sax påse spel
import random
gissning=["sten", "sax", "påse"]
wincon={
    "sten":"sax",
    "sax":"påse",
    "påse":"sten"}

score=0


datorns_gissning=random.choice(gissning)
omgångar=(input("hur många omgångar vill du köra.\n"))

while not omgångar.isdigit():
    print("Fel! Du får bara skriva i siffror")
    omgångar = input("Försök igen: ")

omgångar = int(omgångar)
player_name=input(f"så vad heter du low key type shit\n")

for i in range(omgångar):
    player_gissning=input(f"hej {player_name} daks för runda förbered dig själv på att förlora. \n  spel omgång 1 \n------------------------ \n välj sten sax eller påse: ")
    while player_gissning not in gissning:
       player_gissning=input("skriv faktiskt sten sax eller påse\n")

    datorns_gissning=random.choice(gissning)
    
    if wincon [player_gissning]==datorns_gissning:
        print("du och datorn valde samma sak")

    elif wincon[player_gissning]>datorns_gissning:
        score+=1
        print("du vann")
        print(score)

    else:
        score-=1
        print("du förlora")
        print(score)
    print(f"så här mycket poäng har du {score}")
        

    
