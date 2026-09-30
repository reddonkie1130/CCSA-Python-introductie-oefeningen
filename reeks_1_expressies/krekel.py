def berekenTemperatuur(tjirpsPer15sec):
    tjirpsPer15sec = int(tjirpsPer15sec)

    fahrenheit = 40 + (tjirpsPer15sec / 4)
    celsius = 4.285714285714286 + (tjirpsPer15sec / 7)

    print(f"temperatuur (Fahrenheit): {fahrenheit}")
    print(f"temperatuur (Celsius): {celsius}")


# Lees invoer van de gebruiker
tjirps = input()
berekenTemperatuur(tjirps)
