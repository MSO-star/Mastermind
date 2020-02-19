import Code1 as fl
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

def verwijder_onmogelijk_gok(alle_mogelijk_gok_combinaties, code_speler , klopt_positie ,klopt_kleuren):
   alle_mogelijk_gok_combinaties.remove(secret_code)
   definitief_lijst=[]
   for i in alle_mogelijk_gok_combinaties:
       if vergelijking(code_speler, i)== (klopt_positie, klopt_kleuren):
           definitief_lijst.append(i)
   print(definitief_lijst)
   return definitief_lijst


def gok_twee(alle_mogelijk_gok_combinaties):
    """
    :param alle_mogelijk_gok_combinaties:
    :return:
    """
    for gok in alle_mogelijk_gok_combinaties:
        code_speler= gok
        lijst_te_rekenen= []
        alle_feedback= [ (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),(1, 0), (1, 1), (1, 2), (1, 3),(2, 0), (2, 1), (2, 2),(3, 0),(3,1), (4, 0)]
        for i in alle_feedback:
            tellenlist=[]
            for alle_gokken in alle_mogelijk_gok_combinaties:
                if vergelijking(code_speler,alle_gokken)!= i:
                    tellenlist.append(alle_gokken)
            te_rekenen= len(alle_mogelijk_gok_combinaties)- len(tellenlist)
            lijst_te_rekenen.append(te_rekenen)




 alle_mogelijk_gok_combinaties.remove(gok)
   definitief_lijst=[]
   for i in alle_mogelijk_gok_combinaties:
       if vergelijking(gok, i)== (klopt_positie_teller, klopt_kleuren_teller):
           definitief_lijst.append(i)
   return definitief_lijst
