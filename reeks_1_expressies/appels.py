capaciteit_kist = 20
caciteit_pallet = 35 * capaciteit_kist

aantalAppels = int(input())

aantalPaletten = aantalAppels//caciteit_pallet
print(aantalPaletten)
rest = aantalAppels % caciteit_pallet
aantalKisten = rest//capaciteit_kist
print(aantalKisten)
rest = rest%capaciteit_kist
print(rest)

