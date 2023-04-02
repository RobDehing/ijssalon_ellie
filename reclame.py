def aanbieding_1(smaak, prijs, korting): 
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs - (prijs * korting)} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = (sum(inkomsten) * btw/100)
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return uitvoer

def low_and_high(my_list):
    l_h = (min(my_list), max(my_list))
    output = list(l_h)
    return output

def gemiddelde(mijn_lijst):
    gem_waarde = sum(mijn_lijst) / len(mijn_lijst)
    return gem_waarde






print(aanbieding_1("aardbei", 4, 0.1))      # nog op 2 decimalen
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 9))
print(low_and_high([220, 430, 125, 160, 205, 90, 345]))
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))
