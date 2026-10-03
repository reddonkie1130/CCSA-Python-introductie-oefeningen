cover = input()
if cover == "kleur":
    kleur = input()
    omdraaien = input()

    if kleur == "rood" and omdraaien == "nee":
        print("Juist: kaarten met kleur rood moeten niet gedraaid worden.")
    elif kleur == "rood":
            print("Fout: kaarten met kleur rood moeten niet gedraaid worden.")
    elif kleur != "rood" and omdraaien == "ja":
         print(f"Juist: kaarten met kleur {kleur} moeten gedraaid worden.")
    else:
         print(f"Fout: kaarten met kleur {kleur} moeten gedraaid worden.")

else:
    nummer = int(input())
    omdraaien = input()

    if nummer % 2 !=  0 and omdraaien == "nee":
        print(f"Juist: kaarten met waarde {nummer} moeten niet gedraaid worden.")
    elif nummer % 2 !=  0:
            print(f"Fout: kaarten met waarde {nummer} moeten niet gedraaid worden.")
    elif nummer % 2 == 0 and omdraaien == "ja":
         print(f"Juist: kaarten met waarde {nummer} moeten gedraaid worden.")
    else:
         print(f"Fout: kaarten met waarde {nummer} moeten gedraaid worden.")


