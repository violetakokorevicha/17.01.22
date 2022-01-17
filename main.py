teksts = input('Ievadi ciparu virkni:')


def Countnumbers(teksts):
 summa = 0
 for simbols in teksts:
   summa = summa + int(simbols)
 print(summa)
 return summa
Countnumbers(teksts)