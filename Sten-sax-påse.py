# Ett sten sax påse spel
import random
gissning=["sten", "sax", "påse"]
wincon={
    "sten":"sax",
    "sax":"påse",
    "påse":"sten"}

score=[]
<<<<<<< HEAD


omgångar=(input("hur många omgångar vill du sköra.\n"))

=======
datorns_gissning=random.choice(gissning)
omgångar=(input("hur många omgångar vill du köra.\n"))
>>>>>>> f11c1e9ccf35081cc3edf5c01f5e5aef10e5de55
while not omgångar.isdigit():
    print("Fel! Du får bara skriva i siffror")
    omgångar = input("Försök igen: ")

omgångar = int(omgångar)
<<<<<<< HEAD
player_name=input(f"så vad heter du low key type shit\n")

=======
player_name=input(f"Vad heter du?\n")
>>>>>>> f11c1e9ccf35081cc3edf5c01f5e5aef10e5de55
for i in range(omgångar):
    player_gissning=input(f"hej {player_name} förbered dig själv på att förlora. \n välj sten sax eller påse: ")
    while player_gissning not in gissning:
       player_gissning=input("skriv faktiskt sten sax eller påse\n")

    datorns_gissning=random.choice(gissning)
    
    if wincon [player_gissning]==datorns_gissning:
<<<<<<< HEAD
        print("du och datorn valde samma sak")

    elif wincon[player_gissning]>datorns_gissning:
        score.append(1)
        score=[sum(score)]
        print("du vann")
=======
        print("Oavgjort")
    elif wincon[player_gissning]>datorns_gissning:
        score.append(1)
        score=[sum(score)]
        print(f"{player_name} vann")
>>>>>>> f11c1e9ccf35081cc3edf5c01f5e5aef10e5de55
        print(score)

    else:
        score.append(-1)
        score=[sum(score)]
        print("du förlora")
        print(score)
    print(f"så här mycket poäng har du {score}")
        

    
