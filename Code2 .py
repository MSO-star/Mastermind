import Code1 as fl

def computer_guess():
    print("Geef me 4 kleuren om te raden," '\n'
          "Kies uit de volgende kleuren: wit, rood, groen, geel, blauw en zwart . ")
    print('\r')
    secret_code = []
    while len(secret_code) < 4:
        code_input = (input("Geef me de kleuren: ")).lower()
        if code_input == "stop":
            print("Het spel is gestopt.")
            exit()
        else:
            secret_code.append(code_input)

    print(secret_code)
    return secret_code

    #print("Please type: 1 als mijn gok fout is" '\n'
          #"           : 2 als mijn gok goed is")

    #humanFeedback = input("Dus had ik het goed?")
def  vergelijking (secret_code_input, gok1):
    if (gok1==secret_code_input):
        return 0,4
    else:
        while(gok1 != secret_code_input):
            #klopt kleuren= wit
            #klopt positie= zwart
            klopt_kleuren = 0
            klopt_positie= 0
            code_speler_list=[]
            code_list=[]
            #wit
            for j in range(0, len(secret_code_input)):
                if (secret_code_input[j] == gok1[j]):
                    klopt_positie+=1
                else:
                    code_speler_list.append(gok1[j])
                    code_list.append(secret_code_input[j])
            #zwart
            for j in range(0, len(code_list)):
                if (code_list[j] in code_speler_list):
                     klopt_kleuren+=1

                else:
                     continue

            return klopt_kleuren, klopt_positie
def vergelijk_codes(gok1, secret_code_input):
    gok1= fl.random_secret_code()
    secret_code_input= computer_guess()
    return gok1
    return secret_code_input




def mogelijk_gok():
    kleuren= ["wit", "rood","groen", "geel", "blauw", "zwart"]
    alle_mogelijkheden= []
    for i in kleuren:
        for k in kleuren:
            for c in kleuren:
                for g in kleuren:
                    alle_mogelijkheden.append([i , k ,c , g ])

    return alle_mogelijkheden


    keuze_m()

mogelijk_gok()
