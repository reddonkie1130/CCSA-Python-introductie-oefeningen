som = 0

for i in range(10):
    getal = int(input())
    if(i != 9):
        som = som + (getal*(i+1))
    elif(som % 11 == getal):
        print("OK")
    else:
        print("FOUT")