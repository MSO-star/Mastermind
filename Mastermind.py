import random


def keuzemenu():
    print("'\033[37m---Mastermind game---")
    while True:
        keuze = (input("Kies een van de opties:\n""1.Raad de code\n""2.Maak de code\n"
                       "3.Maak de code (met makkelijk algoritmen)\n""'\r"))
        if '1' in keuze:
            start_randen_optie()
            break
        elif '2' in keuze:
            print('\r')
            verwijder_gokken(computer_guess(), alle_mogelijk_gok())
            break
        elif '3' in keuze:
            algoritme_makkelijk(computer_guess(), alle_mogelijk_gok())
            break
        else:
            print('\033[31m' + "Voer een geldige keuze in !\r" + '\033[31m')


def gok_vragen():  # for player guess
    kleuren = ["wit", "rood", "groen", "geel", "blauw", "zwart"]
    gok = []
    while len(gok) < 4:
        code_input = (input("Guess de kleuren:")).lower()
        if code_input == "stop":
            print('\33[100m'"Het spel is gestopt."+'\33[100m')
            exit()
        if code_input not in kleuren:
            print('\033[91m' + "Voer een geldig kleur in!"+'\033[0m')
        else:
            gok.append(code_input)
    return gok


def start_randen_optie():
    print(" \nJe gaat de code raden, dus...\nKies uit de volgende kleuren: wit, rood, groen, geel, blauw en zwart. ")
    gok = gok_vragen()
    secret_code = random_secret_code()
    klopt_positie, klopt_kleuren = vergelijking(gok, secret_code)
    feedback_printen(klopt_positie, klopt_kleuren)


def random_secret_code():
    kleuren = ["wit", "rood", "groen", "geel", "blauw", "zwart"]
    secret_code_random = random.sample(kleuren, 4)
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
            for kleur_index in range(0, 4):  # zwart
                if gok[kleur_index] == secret_code[kleur_index]:
                    klopt_positie += 1
                else:
                    code_speler_list.append(gok[kleur_index])
                    code_list.append(secret_code[kleur_index])
            for items in code_speler_list:  # wit
                for items2 in code_list:
                    if items == items2:
                        klopt_kleuren += 1
                        code_list.remove(items2)
                        break
                else:
                    continue
            return klopt_positie, klopt_kleuren


def feedback_printen(klopt_positie, klopt_kleuren):
    count_aantal_pogingen = 1
    while klopt_positie != 10:
        if count_aantal_pogingen == 10:
            print('\033[91m' + "Je hebt de maximale aantal pogingen bereikt. Probeert het opnieuw" + '\033[91m')
            exit()
        elif klopt_positie == 4:
            print('\33[4m' + "Goed gedaan! Je bent een Mastermind!" + '\33[4m')
            print("Je hebt het binnen {} pogingen in gedaan.".format(count_aantal_pogingen))
        else:
            print("\r\033[33mHet aantal zwart pin(s) is {}"
                  "\nHet aantal wit pin(s) is {}\r\033[33m".format(klopt_positie, klopt_kleuren))
            gok_vragen()
        count_aantal_pogingen += 1


def computer_guess():  # voor computer guess

    print("Maak de secret code,\n" 
          "Kies uit de volgende kleuren: \33[34m'wit, rood, groen, geel, blauw en zwart.\n'\33[33m")
    kleuren = ["wit", "rood", "groen", "geel", "blauw", "zwart"]
    secret_code = []
    while len(secret_code) < 4:
        code_input = (input("Geef me de kleuren:")).lower()
        if code_input == "stop":
            print('\33[100m'"Het spel is gestopt."+'\33[100m')
            exit()
        if code_input not in kleuren:
            print('\033[91m' + "Voer een geldig kleur in!"+'\033[0m')
        else:
            secret_code.append(code_input)
    print("De gekozen secret code is: {} ".format(secret_code))
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


def verwijder_gokken(secret_code, alle_mogelijkheden):   # combinatie van de simple strategy en de expected size,
    teller = 0
    while True:  # Bron for using the while loop : Iwan
        if teller == 0:
            gok1 = ['wit', 'wit', 'rood', 'groen']  # vaste gok, het beste gok volgens de Expected Size Strategy
            teller = 1
        else:
            gok1 = alle_mogelijkheden[0]
        lijst_return = []
        print(gok1)
        if secret_code == gok1:
            print("De computer heeft je secret code binnen {} keer geraden !".format(teller))
            break
        feedback1 = vergelijking(gok1, secret_code)
        for item in alle_mogelijkheden:
            a = vergelijking(gok1, item)
            if a == feedback1:
                lijst_return.append(item)
        alle_mogelijkheden = lijst_return
        teller += 1


def algoritme_makkelijk(secret_code, alle_mogelijkheden):  # eigen algoritmen
    teller = 0
    while True:
        gok = alle_mogelijkheden[0]
        if gok == secret_code:
            print(gok)
            print("De algoritme heeft je secret code binnen {} keer geraden!".format(teller))
            break
        else:
            alle_mogelijkheden.remove(gok)
            teller += 1


keuzemenu()
