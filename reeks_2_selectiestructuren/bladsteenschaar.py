s1 = input()
s2 = input()


# de code werkt maar er is verbetering mogelijk.
# probeer eerst te controleren of er een gelijkspel is zodat er neit perongelijk een speler kan winnen...
if s1 == s2:
    print("gelijkspel")
elif s1 == "schaar" and s2 in ["blad", "hagedis"] or s1 == "blad" and s2 in ["steen", "spock"] or s1 == "steen" and s2 in ["hagedis", "schaar"] or s1 == "hagedis" and s2 in ["Spock", "blad"] or s1 == "spock" and s2 in ["schaar", "steen"]:
    print("speler1 wint")
else:
    print("speler2 wint")

