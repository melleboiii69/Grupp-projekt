# Ett sten sax påse spel
import random
gissning=["sten", "sax", "påse"]
datorns_gissning=random.choice(gissning)
omgångar=int(input("Hur många omgångar vill du köra? Skriv i siffror annars fungerar det inte\n"))
player_name=input("Vad är ditt namn?\n")
for i in range(omgångar):
    datorns_gissning=random.choice(gissning)
    player_gissning=input(f"Hej {player_name}, välj sten, sax eller påse: ")
    while player_gissning not in gissning:
        player_gissning=input("Skriv sten, sax eller påse\n")
    if player_gissning == datorns_gissning:
        print("Oavgjort")
    elif (player_gissning == "sten" and datorns_gissning == "sax") or \
         (player_gissning == "sax" and datorns_gissning == "påse") or \
         (player_gissning == "påse" and datorns_gissning == "sten"):
        print(f"{player_name} vann")
    else:
        print(f"{player_name} förlorade")
        

    