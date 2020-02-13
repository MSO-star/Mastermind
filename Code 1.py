import random

def start():
    print("---Mastermind game---")
    code_speler = []
    while len(code_speler) < 4:
        code_speler.append(input("Guess de kleuren : "))
    code = secret_code()
    count_aantal_pogingen = 0
    feedback(code, code_speler, count_aantal_pogingen)

def secret_code():
    kleuren= ["wit", "rood","groen", "geel", "blauw", "zwart", "paars"]
    code= random.sample(kleuren, 4 )
    #print(code)
    return code

def  vergelijking (code, code_speler):
    if (code_speler==code):
        print("Great! Je hebt alle kleuren goed geraden.You're a Mastermind!")
    else:
        while(code_speler!=code):
            klopt_kleuren = 0
            for j in range(0, len(code_speler)):
                #print(code_speler[j])
                if (code_speler[j] in code):
                    klopt_kleuren+=1
                else:
                    continue
           # print(klopt_kleuren)
            return klopt_kleuren

def feedback(code, code_speler, count_aantaal_pogingen):
    count_aantaal_pogingen += 1
    klopt_kleuren = vergelijking(code, code_speler)
    if (klopt_kleuren < 4) and (klopt_kleuren != 0):
        print("Het klopt niet, maar je hebt "+ str(klopt_kleuren)+ " kleuren op een verkerde positie goed geraden!")
        code_speler = []
        while len(code_speler) < 4:
            code_speler.append(input("Guess de kleuren : "))


    elif (klopt_kleuren == 0):
        print("Niets van de kleuren klopt")
        code_speler = []
        while len(code_speler) < 4:
            code_speler.append(input("Guess de kleuren : "))

    if code_speler == code:
         print("Goed gedaan! Je bent een Mastermind!")
         print("Je hebt"+ str(count_aantaal_pogingen)+ "pogingen in totaal gehad.")




start()