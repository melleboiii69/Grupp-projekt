# Ett sten sax påse spel
import random
gissning=["sten", "sax", "påse"]
wincon={
    "sten":"sax",
    "sax":"påse",
    "påse":"sten"}
score=[]
datorns_gissning=random.choice(gissning)
omgångar=(input("hur många omgångar vill du köra.\n"))
while not omgångar.isdigit():
    print("Fel! Du får bara skriva i siffror")
    omgångar = input("Försök igen: ")
omgångar = int(omgångar)
player_name=input(f"Vad heter du?\n")
for i in range(omgångar):
    player_gissning=input(f"hej {player_name} förbered dig själv på att förlora. \n välj sten sax eller påse: ")
    while player_gissning not in gissning:
       player_gissning=input("skriv faktiskt sten sax eller påse\n")
    
    if wincon [player_gissning]==datorns_gissning:
        print("Oavgjort")
    elif wincon[player_gissning]>datorns_gissning:
        score.append(1)
        score=[sum(score)]
        print(f"{player_name} vann")
        print(score)
    else:
        score.append(-1)
        score=[sum(score)]
        print("du förlora")
        print(score)
    print(f"så här mycket poäng fick du {score}")
        





    #if player_gissning == datorns_gissning or redo==datorns_gissning:
        #print("oavgjort")
   # elif (player_gissning == "sten" and datorns_gissning == "sax") or \
         #(player_gissning == "sax" and datorns_gissning == "påse") or \
         #(player_gissning == "påse" and datorns_gissning == "sten")or \
            #(redo == "sten" and datorns_gissning == "sax") or \
         #(redo == "sax" and datorns_gissning == "påse") or \
         #(redo== "påse" and datorns_gissning == "sten"):
        #print(f"{player_name} low key vann")
    #else:
        #print(f"{player_name} low key förlorade")
        

    
