
# programul va numara cati bani ii vom datora Profesorului,
# astfel: pentru fiecare ora de Python plata se face in Euro, 20/0ra.
# pentru: fiecare ora de Mate, plata se face in Lei, 100/Lei
# pentru fiecare ora de lupte... plata se face in natura. (teribil!)
# banii se vireaza intr-un cont comun, de lei, la schimbul zilei +1.
# aparatul nu da rest.
# pentru clietii fideli (mai mult de 50 ore investite), pretul orelor se reduce cu 20%.
# conditia de incetare a contractului este cand fiecare client intelege ce are de facut (bani de platit).

tarif_ora_de_Python = 20
tarif_ora_de_Mate = 100

fara_ramburs = True

cursul_zilei = 5.5
euro = cursul_zilei + 1.15

client_Elevul = [0, 0, 0, True] # lista de valori
stop_Elevul = 1 # valoare pentru a opri

while (stop_Elevul == 1):
    client_Elevul[0] += int(input("Nr de ore de Python pentru Elevul: ")) # apelam prima valoare
    client_Elevul[1] += int(input("Nr de ore de Mate pentru Elevul: ")) # apelam a doua valoare
    client_Elevul[2] += int(input("Plata pentru orele de lupta: "))  # apelam a treia valoare
    client_Elevul[3] = bool(input("True = fara ramburs, False = cu ramburs: "))  # apelam a patra valoare
    stop_Elevul = int(input("1 = mai adauga ore sau 0 = nu mai adauga ore: "))

if (client_Elevul[2] > 0):
    raspuns = input("Cine bate pe cine la plata in natura? ")
else:
    raspuns = "Nimicul tocmai s-a manifestat prin ceata ce-a lasat."

print(raspuns)

client_Elevul[2] = (client_Elevul[0] * tarif_ora_de_Python * euro) + (client_Elevul[1] * tarif_ora_de_Mate)
print("Datoria avuta este de " + str(client_Elevul[2]) + " lei.")
