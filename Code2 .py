import Code1 as fl

def computer_guess():
   print("Geef me 4 kleuren om te raden," '\n'
         "Kies uit de volgende kleuren: wit, rood, groen, geel, blauw, zwart en paars. ")
   secret_code= []
   while len(secret_code) < 4:
       secret_code.append(input("Guess de kleuren : "))
   print("Please type: 1 als mijn  gok fout is"
         "           : 2 als mijn gok goed is  ")
   humanFeedback= input("Dus had ik het goed?")
   if 1< humanFeedback >2 :
       print("Voer een geldig keuze in:")
fl.feedback()
