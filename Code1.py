import random
import
def keuze_m():
     keuze= int(input("Kies een van de opties:"'\n' 
          "1.spelen tegen de computer: "'\n'
          "2.computer tegen jou: ""\n"
          "Ik kies: "))
     if keuze==1:
        print('\r')
        return start()
     if keuze==2:
         print('\r')
         return computer_guess()
     else:
         print("Voer een geldige keuze in !")
         print('\r')
         return keuze_m()

def start():
    print("---Mastermind game---")
    print("Kies uit de volgende kleuren: wit, rood, groen, geel, blauw, zwart en paars. ")
    code_speler = []
    while len(code_speler) < 4:
        code_input=(input("Guess de kleuren : ")).lower()
        if code_input=="stop":
            exit()
        else:
            code_speler.append()
    #code_speler = ["blauw", "zwart", "groen","rood"]
    code = secret_code()
    count_aantal_pogingen =  0
    feedback(code, code_speler, count_aantal_pogingen)

def secret_code():
    #kleuren= ["wit", "rood","groen", "geel", "blauw", "zwart", "paars"]
    #code= random.sample(kleuren, 4 )
    #print(code)
    code = ["blauw", "zwart", "groen","rood"]
    return code

def  vergelijking (code, code_speler):
    if (code_speler==code):
        return 0,4
    else:
        while(code_speler!=code):
            #klopt kleuren= wit
            #klopt positie= zwart
            klopt_kleuren = 0
            klopt_positie= 0
            code_speler_list=[]
            code_list=[]
            #wit
            for j in range(0, len(code)):
                if (code[j] == code_speler[j]):
                    klopt_positie+=1
                else:
                    code_speler_list.append(code_speler[j])
                    code_list.append(code[j])
            #zwart
            for j in range(0, len(code_list)):
                if (code_list[j] in code_speler_list):
                     klopt_kleuren+=1

                else:
                     continue
            return klopt_kleuren, klopt_positie

def feedback(code, code_speler, count_aantal_pogingen):
    count_aantal_pogingen += 1
    klopt_kleuren, klopt_positie = vergelijking(code, code_speler)
    if klopt_positie == 4:
         print("Goed gedaan! Je bent een Mastermind!")
         print("Je hebt {} pogingen in totaal.".format(count_aantal_pogingen))
    else:
        print("Het aantal goede posities is {}, het aantal goede kleuren op de verkeerde positie is {}".
              format(klopt_positie, klopt_kleuren))
        code_speler = []
        while len(code_speler) < 4:
            code_input = (input("Guess de kleuren : ")).lower()
            if code_input == "stop":
                exit()
            else:
                code_speler.append(code_input)
        feedback(code, code_speler, count_aantal_pogingen)

keuze_m()

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

#feedback(code, code_speler, count_aantal_pogingen)