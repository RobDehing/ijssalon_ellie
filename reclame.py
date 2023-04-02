from algemene_functies import mijn_functie_2


def aanbieding_1(smaak, prijs, korting): 
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {prijs - (prijs * korting):.2f} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = (sum(inkomsten) * btw/100)
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return uitvoer

def laag_en_hoog(mijn_lijst):
    l_h = (min(mijn_lijst), max(mijn_lijst))
    uitvoer = list(l_h)
    return uitvoer

def gemiddelde(mijn_lijst):
    gem_waarde = sum(mijn_lijst) / len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gem_waarde:.2f} euro."
    return uitvoer

def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(mijn_lijst = invoer_lijst)   
    return uitvoer
    


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer





print(aanbieding_1("aardbei", 4, 0.1))      # nog op 2 decimalen
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 9))
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))
print(meervoudig([10,5,3,2,1,2,9]))
print(combinatie([2,10,5,8]))