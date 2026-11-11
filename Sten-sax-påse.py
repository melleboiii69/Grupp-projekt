# Ett sten sax påse spel
import random
gissning="sten, sax, påse"
datorns_gissning=random.choice(gissning)
omgångar=input("hur många omgångar vill du sköra")
player_name=input(f"så vad heter du low key type shit\n")
for i in range(omgångar):
    player_gissning=input(f"hej {player_name} bered dig skjälv på att förlora. välj sten sax eller påse ")
    if player_gissning==datorns_gissning:
        print("o avgjort")
    