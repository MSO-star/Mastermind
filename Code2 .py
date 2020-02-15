import Code1 as fl

def computer_guess():
   print("Geef me 4 kleuren om te raden," '\n'
         "Kies uit de volgende kleuren: wit, rood, groen, geel, blauw, zwart en paars. ")
   secret_code= []
   while len(secret_code) < 4:
       code_input = (input("Geef me de kleuren : ")).lower()
       if code_input == "stop":
           exit()
       else:
           secret_code.append(code_input)
       print(secret_code)
   print("Please type: 1 als mijn gok fout is"'\n'
         "           : 2 als mijn gok goed is")
   humanFeedback= input("Dus had ik het goed?")

   fl.keuze_m()
   fl.vergelijking( )
fl.keuze_m()