import random
import math

def keuze_m():
     keuze= int(input("Kies een van de opties:"'\n' 
          "1.spelen tegen de computer: "'\n'
          "2.computer tegen jou: ""\n"
          "Ik kies: "))
     if keuze==1:
        print('\r')
        return start()
     elif keuze==2:
         print('\r')
         return computer_guess()
     else:
         print("Voer een geldige keuze in !")
         print('\r')
         return keuze_m()

def start():
    print("---Mastermind game---")
    print("Kies uit de volgende kleuren: wit, rood, groen, geel, blauw en zwart. ")
    gok = []
    while len(gok) < 4:
        code_input=(input("Guess de kleuren: ")).lower()
        if code_input=="stop":
            print("Het spel is gestopt.")
            return gok
        else:
            gok.append(code_input)
    #gok = ["blauw", "zwart", "groen","rood"]
    secret_code = random_secret_code()
    count_aantal_pogingen =  0
    feedback(secret_code, gok, count_aantal_pogingen)

def random_secret_code():
    #kleuren= ["wit", "rood","groen", "geel", "blauw", "zwart"]
    #secret_code= random.sample(kleuren, 4 )
    #print(secret_code)
    secret_code = ["blauw", "zwart", "groen","rood"]
    return secret_code

def  vergelijking (gok, secret_code):
    if (gok==secret_code):
        return 0,4
    else:
        while(gok != secret_code):
            klopt_kleuren = 0 #wit
            klopt_positie= 0 #rood/ zwart 
            code_speler_list=[]
            code_list=[]
            for j in range(0, len(secret_code)): #zwart
                if (secret_code[j] == gok[j]):
                    klopt_positie+=1
                else:
                    code_speler_list.append(gok[j])
                    code_list.append(secret_code[j])
            for j in range(0, len(code_list)): #wit
                if (code_list[j] in code_speler_list):
                     klopt_kleuren+=1
                else:
                     continue
            return klopt_positie, klopt_kleuren

def feedback(secret_code, gok, count_aantal_pogingen):
    count_aantal_pogingen += 1

    klopt_kleuren, klopt_positie = vergelijking(secret_code, gok)
    if count_aantal_pogingen==10:
        print("Je hebt de maximale aantal pogingen bereikt. Probeert het opnieuw")
        exit()
    if klopt_positie == 4:
         print("Goed gedaan! Je bent een Mastermind!")
         print("Je hebt {} pogingen in totaal.".format(count_aantal_pogingen))
    else:
        print('\r')
        print("Het aantal zwart/rood pin(s) is {} \nHet aantal wit pin(s) is {}".
              format(klopt_positie, klopt_kleuren))
        print('\r')
        gok = []
        while len(gok) < 4:
            code_input = (input("Guess de kleuren : ")).lower()
            if code_input == "stop":
                print("Het spel is gestopt.")
                return gok
            else:
                gok.append(code_input)
        feedback(secret_code, gok, count_aantal_pogingen)

def computer_guess():
    print("Maak de secret code," '\n'
          "Kies uit de volgende kleuren: wit, rood, groen, geel, blauw en zwart. ")
    print('\r')
    secret_code = []
    while len(secret_code) < 4:
        code_input = (input("Geef me de kleuren: ")).lower()
        if code_input == "stop":
            print("Het spel is gestopt.")
            return secret_code
        else:
            secret_code.append(code_input)

    print("De gekozen secret code is " ,secret_code)
    return secret_code

def alle_mogelijk_gok():
    kleuren= ["wit", "rood","groen", "geel", "blauw", "zwart"]
    alle_mogelijkheden= []
    for i in kleuren:
        for k in kleuren:
            for c in kleuren:
                for g in kleuren:
                    alle_mogelijkheden.append([i , k ,c , g ])
    print(len(alle_mogelijkheden))
    return alle_mogelijkheden

def verwijder_onmogelijk_gok(alle_mogelijk_gok_combinaties, gok , klopt_positie ,klopt_kleuren):
   alle_mogelijk_gok_combinaties.remove(gok)
   definitief_lijst=[]
   for i in alle_mogelijk_gok_combinaties:
       if vergelijking(gok, i)== (klopt_positie, klopt_kleuren):
           definitief_lijst.append(i)
   print(definitief_lijst)
   return definitief_lijst


def gok_twee(alle_mogelijk_gok_combinaties):
    alle_feedback = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2),(3, 0), (3, 1), (4, 0)]

    for gok_in_mogelijkheden in alle_mogelijk_gok_combinaties:
        gok= gok_in_mogelijkheden
        lijst_te_rekenen= []
        for i in alle_feedback:
            tellenlist = []
            for gok_in_mogelijkheden in alle_mogelijk_gok_combinaties:
                if vergelijking(gok, gok_in_mogelijkheden) != i:
                    tellenlist.append(gok_in_mogelijkheden)
            te_rekenen = len(alle_mogelijk_gok_combinaties) - len(tellenlist)
            lijst_te_rekenen.append(te_rekenen)


alle_mogelijk_gok()

keuze_m()


kleuren_lijst= [ ]