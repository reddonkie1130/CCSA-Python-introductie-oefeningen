
def berekenPrijsPerBoek(aantal):
    korting = 0.4
    prijs = 24.95
    verzenkost = 3

    resultaat = (prijs - (prijs * korting)) * aantal

    for i in range(aantal):
        if(i > 0):
            verzenkost = 0.75
        resultaat += verzenkost

    return resultaat


print(berekenPrijsPerBoek(60))
