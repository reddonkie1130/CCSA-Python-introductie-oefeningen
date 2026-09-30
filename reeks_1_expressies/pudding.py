aantal = int(input())
prijs = float(input())
aantalBarcodes = int(input())
aantalMijlen = int(input())


print(f"Phillips spendeerde ${aantal * prijs} voor {int(aantal/aantalBarcodes) * aantalMijlen} frequent flyer mijlen.")