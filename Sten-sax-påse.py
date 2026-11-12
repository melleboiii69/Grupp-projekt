# Ett sten sax påse spel
import random
gissning=["sten", "sax", "påse"]
datorns_gissning=random.choice(gissning)
omgångar=int(input("hur många omgångar vill du sköra.\n"))
player_name=input(f"så vad heter du low key type shit\n")
for i in range(omgångar):
    player_gissning=input(f"hej {player_name} bered dig skjälv på att förlora. välj sten sax eller påse ")
    if player_gissning not in gissning:
        redo=input("skriv faktiskt sten sax eller påse\n")
    if player_gissning == datorns_gissning or redo==datorns_gissning:
        print("oavgjort")
    elif (player_gissning == "sten" and datorns_gissning == "sax") or \
         (player_gissning == "sax" and datorns_gissning == "påse") or \
         (player_gissning == "påse" and datorns_gissning == "sten")or \
            (redo == "sten" and datorns_gissning == "sax") or \
         (redo == "sax" and datorns_gissning == "påse") or \
         (redo== "påse" and datorns_gissning == "sten"):
        print(f"{player_name} low key vann")
    else:
        print(f"{player_name} low key förlorade")
        

    