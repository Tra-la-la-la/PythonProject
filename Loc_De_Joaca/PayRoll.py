
# Presupunem ca un birou solicita un program pentru a executa platasalariului
# in aceasta firma sunt cateva persoane angajate. ei muncesc orele cu regularitate, iar uneori extra-timp.
# Sarcina este de a executa plata pentru fiecare angajat, cat si
# o sarcina totala cu repartizarea in functie de intervalul orar muncit.
# .
# Algorithm: PayRoll
# repetam urmatorul ciclu "while" atat timp cat este mai multa informatie:
# "get" date pentru fiecare persoana angajat
# "calculeaza" plata pentru fiecare individ din datele introduse
# si, "actualizeaza" plata cumulativa distributa pana acum
# "print" plata pentru fiecare individ
# "print" plata totala.
plata_pe_ora = 15 # minimul pe economie plentru plata pe ora
munca_partiala = 100
munca_intreaga = 40 * 4.5 # 40 ore/saptamana * 4,5 ca zile de munca sa rezulte media de 21 zile lucratoare
Sambata = 25 # plus 25 la %
Duminica = 50 # plus 50 la %
Sarbatoare_Legala = 175 # plus 175 la %
Bonificatie = "Craciun", "Paste", "Ziua_Nationala", "Celebrare"

prima_marire = plata_pe_ora + 0.25 # bonificatie de vechime in munca +0.25 per ora de munca (15.00+0.25/ora)
a_doua_marire = prima_marire + 0.50 # bonificatie in vechimea in munca la plata de la prima marire plus 0.50 per ora de munca (15.25+0.50/ora)
a_treia_marire = a_doua_marire + 0.75 # bonificatie in vechimea in munca la plata de la a 2-a marire plus 0.75 per ora de munca (15.75+0.75/ora)
a_patra_marire = a_treia_marire + 1.00 # bonificatie in vechimea in munca la plata de la a 3-a marire plus 1.00 per ora de munca (16.50+1/ora)
a_cincia_marire = a_patra_marire + 1.25 # bonificatie in vechimea in munca la plata de la a 4-a marire plus 1.25 per ora de munca (17.50+1.25/ora)




def Percentage(part, whole):
    Percentage = 100 * float(part) / float(whole)
  #  return str(Percentage)+“%”
