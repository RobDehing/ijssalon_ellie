def presenteer(mijn_dict, totaal):
    totaal_dictionary = 0
    for key, value in mijn_dict:
        totaal_dictionary += value
    return totaal_dictionary









mijn_dict = {'vis': 10, 'vlees': 25, 'overig': 15}
totaal = 50

print(presenteer(mijn_dict, totaal))