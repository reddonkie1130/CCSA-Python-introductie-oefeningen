# Invoer
uur1 = int(input())
min1 = int(input())
uur2 = int(input())
min2 = int(input())

# Omzetten naar totale minuten
start = uur1 * 60 + min1
einde = uur2 * 60 + min2

# Grenzen
MIN_START = 18 * 60
MAX_EINDE = 24 * 60
GRENSTARIEF = 21 * 60 + 30

LAAG = 2
HOOG = 4

# Ongeldige invoer controleren
if start < MIN_START or einde > MAX_EINDE or einde <= start:
    print("ongeldige invoer")
else:
    # Volledig laag tarief
    if einde <= GRENSTARIEF:
        totaal = (einde - start) / 60 * LAAG

    # Volledig hoog tarief
    elif start >= GRENSTARIEF:
        totaal = (einde - start) / 60 * HOOG

    # Gemengd tarief
    else:
        laag_deel = (GRENSTARIEF - start) / 60 * LAAG
        hoog_deel = (einde - GRENSTARIEF) / 60 * HOOG
        totaal = laag_deel + hoog_deel

    print(totaal)
