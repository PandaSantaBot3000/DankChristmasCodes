import secrets
import hashlib
import random

givere = ["Bob", "Alice", "Peder Aas", "Marte Kirkerud"]

mottakere = givere.copy()

random.shuffle(givere)        #rister i hatten med loddene
random.shuffle(mottakere)

paringer = []

for giv in givere: #trekker gavepar
    mottaker = secrets.choice(mottakere)
    while mottaker == giv:
        mottaker = secrets.choice(mottakere)
    mottakere.remove(mottaker)
    par = [giv, mottaker]
    paringer.append(par)

hemmeligOrd = "HEMMELIG"

for i in range(len(paringer)):
    mottaker = paringer[i][1]
    mottakerHash = mottaker + hemmeligOrd
    print(paringer[i][0], "trakk: ", end="")
    encoded = hashlib.md5(mottakerHash.encode()) #kryptografisk enveisfunsksjon som deles offentlig for etterettelighet
    f = open(paringer[i][0] + ".txt", "w")
    f.write("Gratulerer, " + paringer[i][0] +"! Du trakk " + mottaker + " som din hemmelige gavemottaker!\n\n")
    f.write("""       
            ,,,         ,,,
          ;"   ^;     ;'   ",
          ;    s$$$$$$$s     ;
          ,  ss$$$$$$$$$$s  ,'
          ;s$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$
         $$$$P""Y$$$Y""W$$$$$
         $$$$  p"$$$"q  $$$$$
         $$$$  .$$$$$.  $$$$
          $$DcaU$$$$$$$$$$
            "Y$$$"*"$$$Y"    
               "$b.$$"     """)
    f.write("\n"*2)
    f.write("Sjekksum for din trekning (skal vaere identisk til den som ble delt offentlig): " + encoded.hexdigest())
    f.close()
    print(encoded.hexdigest())