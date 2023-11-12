
cuvantul_de_ghicit = "alandala"
cuvantul_introdus = ""
numarul_de_variante = 3 # = 3  Varianta pentru verificare in incrementare

while cuvantul_introdus != cuvantul_de_ghicit and numarul_de_variante >= 1 : # < 3  :  Varianta pentru verificare in incrementare
    cuvantul_introdus = input ("Introdu alt cuvant: ")
    numarul_de_variante -=1 # += 1  Varianta pentru verificare in incrementare

if numarul_de_variante == 0 and cuvantul_introdus != cuvantul_de_ghicit : # > 3:  Varianta pentru verificare in incrementare
    print("Ai pierdut!")
else:
    print("Ai castigat!")
