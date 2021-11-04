import secrets
import hashlib
import random

givere = ["Bob", "Alice", "Peder Aas", "Marte Kirkerud"]

mottakere = givere.copy()

random.shuffle(givere) #rister i hatten
random.shuffle(mottakere)

paringer = []

for giv in givere: #trekker giver-mottaker-par
    mottaker = secrets.choice(mottakere)
    while mottaker == giv:
        mottaker = secrets.choice(mottakere)
    mottakere.remove(mottaker)
    par = [giv, mottaker]
    paringer.append(par)

hemmeligOrd = "HEMMELIG_ORD" #kombineres med trukket navn og kjøres gjennom en krytografisk enveisfunksjon

for i in range(len(paringer)):
    mottaker = paringer[i][1]
    mottakerHash = mottaker + hemmeligOrd
    print(paringer[i][0], "trakk: ", end="")
    encoded = hashlib.md5(mottakerHash.encode()) #Sjekksummen deles offentlig for etterettelighet
    f = open("{0}.txt".format(paringer[i][0]), "w")
    f.write("Gratulerer, {0}! Du trakk {1} som din hemmelige gavemottaker!\n\n".format(paringer[i][0], mottaker))
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
    f.write("Sjekksum for din trekning (skal vaere identisk til den som ble delt offentlig): {0}".format(
        encoded.hexdigest()))
    f.close()
    print(encoded.hexdigest())