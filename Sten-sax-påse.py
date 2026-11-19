# Ett sten sax påse spel
import random
gissning = ["sten", "sax", "påse"]
# Visar vad som vinner mot vad
wincon={
    "sten":"sax",
    "sax":"påse",
    "påse":"sten"} #detta är ett lexikon av gissningars matchupps. så om man väljer t.e.x sten så checkar programmet om datorn valde sax. Om deatorn gjorde det så printas det ut att spelaren vann. 

player_name = input(f"Vad heter du? -> ")
omgångar = (input("Hur många omgångar vill du köra -> "))

# Startar båda poängen på 0
datorn_score = 0
player_score = 0
datorns_namn=("Python311")
datorns_gissning=random.choice(gissning)

# Kräver att antal omgångar är en siffra
while not omgångar.isdigit():
    print("Fel! Du får bara skriva i siffror")
    omgångar = input("Försök igen: ")

# Gör om texten till ett heltal
omgångar = int(omgångar)

loopcount = 1

# Kör så många rundor som spelaren valt
for i in range(omgångar):

    player_gissning = input(f"\nHej {player_name}, dags för en ny runda. Förbered dig själv på att förlora. \n\nSpelomgång {loopcount} \n------------------------ \nVälj 'Sten', 'Sax' eller 'Påse': ")
    
 # Fortsätter fråga tills spelaren skriver rätt
    while player_gissning not in gissning: 
        print("Fel! Du kan bara skriva 'Sten', 'Sax' eller 'Påse'")
        player_gissning = input("Prova igen --> ")
# Datorn väljer slumpmässigt varje runda
    datorns_gissning = random.choice(gissning)
# Samma val ger oavgjort och inga poäng
    if player_gissning == datorns_gissning:
        print("Du och datorn valde samma sak")
        print(f"{player_name} spelar: {player_gissning}\nDatorn spelar: {datorns_gissning}")
        print(f"Vinnare av spelomgång {loopcount} är oavgjort")
        loopcount = loopcount+1
# Kollar i wincon om spelaren slår datorn
    elif wincon[player_gissning] == datorns_gissning:
        player_score += 1
        print(f"{player_name} spelar: {player_gissning}\n{datorns_namn} spelar: {datorns_gissning}")
        print(f"Vinnare i spel omgång {loopcount}: är {player_name}")
        loopcount = loopcount+1
# Annars får datorn ett poäng
    else:
        datorn_score += 1
        print(f"{player_name} spelar: {player_gissning}\n{datorns_namn} spelar: {datorns_gissning}\nVinnare i spelomgång {loopcount}: {datorns_namn}\n")
        loopcount = loopcount+1
# Jämför poängen och skriver ut slutresultatet
if player_score > datorn_score: 
    print(f"\nSLUTRESULTAT\n===================\n{player_name}: {player_score}\n{datorns_namn}: {datorn_score}\nVinnare: {player_name}!\n\nProgrammet avslutades normalt")
if datorn_score > player_score:
    print(f"\nSLUTRESULTAT\n===================\n{player_name}: {player_score}\n{datorns_namn}: {datorn_score}\nVinnare: {datorns_namn}!\n\nProgrammet avslutades normalt")
if datorn_score == player_score:
    print(f"\nSLUTRESULTAT\n===================\n{player_name}: {player_score}\n{datorns_namn}: {datorn_score}\nVinnare: Oavgjort!\n\nProgrammet avslutades normalt")
