import random
def keuze_m():
     keuze= int(input("Kies een van de opties:"'\n' 
          "1.spelen tegen de computer: "'\n'
          "2.computer tegen jou: ""\n"
          "Ik kies: "))
     if keuze==1:
        return start()
     if keuze==2:
        return computer_guess()
def start():
    print("---Mastermind game---")
    print("Kies uit de volgende kleuren: wit, rood, groen, geel, blauw, zwart en paars. ")
    code_speler = []
    while len(code_speler) < 4:
        code_speler.append(input("Guess de kleuren : "))
    #code_speler = ["blauw", "zwart", "groen","rood"]
    code = secret_code()
    count_aantal_pogingen = 0
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
                     print(klopt_positie)
                     print(klopt_kleuren)
                else:
                     continue
            return klopt_kleuren, klopt_positie

def feedback(code, code_speler, count_aantal_pogingen):
    count_aantal_pogingen += 1
    klopt_kleuren, klopt_positie = vergelijking(code, code_speler)
    if klopt_positie == 4:
         print("Goed gedaan! Je bent een Mastermind!")
         print("Je hebt" + str(count_aantal_pogingen) + "  pogingen in totaal.")
    else:
        print("Het aantal goede posities is {}, het aantal goede kleuren op de verkeerde positie is {}".
              format(klopt_positie, klopt_kleuren))
        code_speler = []
        while len(code_speler) < 4:
            code_speler.append(input("Guess de kleuren : "))
        feedback(code, code_speler, count_aantal_pogingen)

keuze_m()

def computer_guess():
    secret_code= input("Geef een secret code: ")
