import random

#def start():
print("Mstermind game")
Kies_soort_spel= input("Kies soort spel: ")# moet nog vinden hoe je het met keeuzes gaat meken, geldt voor alle inputs
Kies_aantaal_kleuren= int(input("Hoeveel kleuren mogen er in zitten?: "))

Welke_kleuren= input("Welke kleuren mogen er in komen?: ")#optie voor easy spel
code_speler= input("Guess de kleuren : ")
def functions():
    def secret_code():

         code= random.sample(["wit", "rood","groen", "geel", "blauw", "zwart"], Kies_aantaal_kleuren )
         code_raden= code
         print(code_raden)

    def  vergelijking ():


         if (code_speler==secret_code()):
             print("Great! Je hebt alle kleuren goed geraden.You're a Mastermind!")
         else:
            count_aantaal_pogingen=0

            while(code_speler!=secret_code()):
                count_aantaal_pogingen+=1
                if count_aantaal_pogingen == 10:
                     print("Je hebt de maximum aantaal poginen bereikt.")
                break
                for j in range(0,Kies_aantaal_kleuren):
                    klopt_kleuren = 0
                    if (code_speler[j] in secret_code([j])):
                        klopt_kleuren+=1
                    else:
                         continue


    def feedback():


        if (vergelijking(klopt_kleuren) < 4) and (vergelijking(klopt_kleuren) != 0):
            print("Het klopt niet helemaal, maar je hebt "+ str(klopt_kleuren)+ "kleuren op een verkerde positie goed geraden")
            code_speler = input("Guess de kleuren: ")


        elif (klopt_kleuren == 0):
            print("Niets van de kleuren klopt")
            code_speler = input("Guess de kleuren: ")

        if code_speler == code_raden:
            print("Goed gedaan! Je bent een Mastermind!")
            print("Je hebt"+ str(count_aantaal_pogingen)+ "pogingen in totaal gehad.")

functions()


