# Ett sten sax påse spel
import random
gissning=["sten", "sax", "påse"]
datorns_gissning=random.choice(gissning)
omgångar=int(input("hur många omgångar vill du sköra. skriv i siffror annars funkar det inte\n"))
player_name=input(f"så vad heter du low key type shit\n")
for i in range(omgångar):
    player_gissning=input(f"hej {player_name} bered dig skjälv på att förlora. välj sten sax eller påse ")
    if player_gissning==datorns_gissning:
        print("oavgjort")
    elif player_gissning=="sten" and datorns_gissning=="sax":
        print(f"{player_name} vann")
    elif  player_gissning=="påse" and datorns_gissning=="sax":
        print(f"{player_name} low key fölorade")
    elif  player_gissning=="sax" and datorns_gissning=="sten":
        print(f"{player_name} low key förlorade")
    elif  player_gissning=="sax" and datorns_gissning=="påse":
        print(f"{player_name}low key vann")
        

    