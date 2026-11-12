# Ett sten sax påse spel
import random
gissning=["sten", "sax", "påse"]
datorns_gissning=random.choice(gissning)
omgångar=int(input("Hur många omgångar vill du köra. Skriv i siffror annars funkar det inte\n"))
player_name=input(f"Vad är ditt namn\n")
for i in range(omgångar):
    player_gissning=input(f"Hej {player_name} bered dig själv på att förlora. Välj sten, sax eller påse ")
    if player_gissning==datorns_gissning:
        print("Oavgjort")
    elif player_gissning=="sten" and datorns_gissning=="sax":
        print(f"{player_name} vann")
    elif  player_gissning=="påse" and datorns_gissning=="sax":
        print(f"{player_name} förlorade")
    elif  player_gissning=="sax" and datorns_gissning=="sten":
        print(f"{player_name} förlorade")
    elif  player_gissning=="sax" and datorns_gissning=="påse":
        print(f"{player_name} vann")
        

    