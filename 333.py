import random


def keuze_m():
    print("---Mastermind game---")
    while True:
        keuze = (input("Kies een van de opties:\n"
                          "1.Raad de code\n"
                          "2.Maak de code \n"
                          "3.Maak de code met makkelijk algoritmen\n""'\r"))
        if '1' in keuze:
            start()
            break
        elif '2' in keuze:
            print('\r')
            verwijder_gokken(computer_guess_m(), alle_mogelijk_gok())
            break
        elif '3' in keuze:
            algoritme_makkelijk(computer_guess_m(), alle_mogelijk_gok())
            break
        else:
            print("Voer een geldige keuze in !\r")


def input_vragen():  # voor player guess
    kleuren = ["wit", "rood", "groen", "geel", "blauw", "zwart"]
    gok = []
    while len(gok) < 4:
        code_input = (input("Guess de kleuren:")).lower()
        if code_input == "stop":
            print("Het spel is gestopt.")
            exit()
        if code_input not in kleuren:
            print("Voer een geldig kleur in!")
        else:
            gok.append(code_input)
    return gok


def player_secretcode_pc():  # voor computer guess
    kleuren = ["wit", "rood", "groen", "geel", "blauw", "zwart"]
    secret_code = []
    while len(secret_code) < 4:
        code_input = (input("Geef me de kleuren:")).lower()
        if code_input not in kleuren:
            print("voer een geldig kleur in!")
        elif code_input == "stop":
            print("Het spel is gestopt.")
            return secret_code
        else:
            secret_code.append(code_input)
    print("De gekozen secret code is: {} ".format(secret_code))
    return secret_code


def start():
    print(" \nJe gaat de code raden, dus...\nKies uit de volgende kleuren: wit, rood, groen, geel, blauw en zwart. ")
    gok = input_vragen()
    secret_code = random_secret_code()
    count_aantal_pogingen = 0
    klopt_positie, klopt_kleuren = vergelijking(gok, secret_code)
    feedback(secret_code, gok, count_aantal_pogingen, klopt_positie, klopt_kleuren)


def computer_guess_m():
    secret_code = player_secretcode_pc()
    print("Maak de secret code,\n" 
          "Kies uit de volgende kleuren: wit, rood, groen, geel, blauw en zwart. \r")
    return secret_code


def alle_mogelijk_gok():
    kleuren = ["wit", "rood", "groen", "geel", "blauw", "zwart"]
    alle_mogelijkheden = []
    for i in kleuren:
        for k in kleuren:
            for c in kleuren:
                for g in kleuren:
                    alle_mogelijkheden.append([i, k, c, g])
                    alle_mogelijkheden.sort()
    return alle_mogelijkheden


def verwijder_gokken(secret_code, alle_mogelijkheden):     # Bron for the while loop : Iwan
    eerstekeer = 0
    while True:
        if eerstekeer == 0:
            gok1 = ['wit', 'wit', 'rood', 'groen']
            eerstekeer = 1
        else:
            gok1 = alle_mogelijkheden[0]
        lijst_return=[]
        print(gok1)
        if secret_code == gok1:
            print("De computer heeft je secret code binnen {} keer geraden !".format(eerstekeer))
            break
        feedback1 = vergelijking(gok1, secret_code)
        for item in alle_mogelijkheden:
            a = vergelijking(gok1, item)
            if a == feedback1:
                lijst_return.append(item)
        alle_mogelijkheden = lijst_return
        eerstekeer += 1


def algoritme_makkelijk(secret_code, alle_mogelijkheden):
    teller= 0
    while True:
        gok = alle_mogelijkheden[0]
        if gok == secret_code:
            print(gok)
            print("De algoritme heeft je secret code binnen {} keer geraden!".format(teller))
            break
        else:
            alle_mogelijkheden.remove(gok)
            teller+=1

def eigen_algoritme():
    secret_code = computer_guess_m()
    alle_mogelijkheden = alle_mogelijk_gok()
    teller= 0
    mogelijkheden_2= []

    while True:
        gok1 = ['wit', 'wit', 'rood', 'groen']
        gok2= ["wit", 'rood', 'groen', 'geel']
        if secret_code == gok1:
            print(gok1)
            print("De computer heeft je secret code binnen 1 stap geraden!")
            break
        elif secret_code == gok2:
            print(gok2)
            print("De computer heeft je secret code binnen 2 stappen geraden !")
            break
        else:
            a = vergelijking(gok1, secret_code)
            b = vergelijking(gok2, secret_code)
            if str(a) == str(b) or str(a) > str(b):
                for item in alle_mogelijkheden:
                    c = vergelijking(gok1,item)
                    if a == c :
                        mogelijkheden_2.append(item)
            elif str(b)<str(a):
                for item in alle_mogelijkheden:
                    d=vergelijking(gok2, item)
                    if b == d :
                         mogelijkheden_2.append(item)
            else:
                gok3 = mogelijkheden_2[0]
                print(gok3)
        alle_mogelijkheden = mogelijkheden_2
        teller += 1
        print(len(mogelijkheden_2))




def random_secret_code():
    kleuren= ["wit", "rood","groen", "geel", "blauw", "zwart"]
    secret_code_random= random.sample(kleuren, 4 )
    return secret_code_random


def vergelijking(gok, secret_code):  # Bron: Adam (de twee lijsten methode)
    if gok == secret_code:
        return 4, 0
    else:
        while gok != secret_code:
            klopt_kleuren = 0  # wit
            klopt_positie = 0  # zwart
            code_speler_list = []
            code_list = []
            for kleur_index in range(0,4):  # zwart
                if gok[kleur_index] == secret_code[kleur_index]:
                    klopt_positie += 1
                else:
                    code_speler_list.append(gok[kleur_index])
                    code_list.append(secret_code[kleur_index])
            for items in code_speler_list:  # wit
                for items2 in code_list:
                    if items == items2:
                     klopt_kleuren +=1
                     code_list.remove(items2)
                     break
                else:
                     continue
            return  klopt_positie, klopt_kleuren


def feedback(secret_code, gok, count_aantal_pogingen, klopt_positie, klopt_kleuren):
    count_aantal_pogingen += 1
    klopt_positie, klopt_kleuren = vergelijking(secret_code, gok)
    if count_aantal_pogingen == 10:
        print("Je hebt de maximale aantal pogingen bereikt. Probeert het opnieuw")
        exit()
    if klopt_positie == 4:
         print("Goed gedaan! Je bent een Mastermind!")
         print("Je hebt het binnen {} pogingen in gedaan.".format(count_aantal_pogingen))
    else:
        print("\rHet aantal zwart pin(s) is {} \nHet aantal wit pin(s) is {}\r".format(klopt_positie, klopt_kleuren))
        input_vragen()



keuze_m()
