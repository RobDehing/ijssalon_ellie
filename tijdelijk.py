prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
aanbieding = prijzen["vanille"] * 0.8 # mijn output is slechts 1 decimaal 3.2
reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding:.2f}") # voor 2 decimalen :.2f toegevoegd
reclame_tekst2 = reclame_tekst[:63] # werkt als output aanbieding 3.20000000000000000000 is
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if len(el) > 4:
        print(el.upper())       
    else:
        print(el.lower())
