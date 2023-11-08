import pickle

filename = 'betalinger.pk'

fodboldtur ={}

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    for item in fodboldtur.items():
        print(item)
    menu()


#def indbetal():
    #pass()
    #Indtast  navn
    #indtast ønsket beløb



def menu():
    print("MENU")
    print("1: Print liste")
    print("2: indbetal")
    print("3: Afslut program")
    valg = input("Indtast dit valg:")
    if (valg == '1'):
        printliste()
    #if (valg == '2'):
        #indbetal()
    if (valg == '3'):
        afslut()

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()
'''
Pseudokode --> Overblik over de indbetalte beløb(OB) *opfyldningaf 2.krav
Når der trykkes på OB:
    vælg mellem værdierne 1 og 2
        Hvis valgt værdi = 1
            vis printliste 1
        Hvis valgt værdi = 2
            vis printliste 1



Pseudokode --> Registrere modtagelse af betalinger
Indtast betalingbeløb;
    Indsend beløb;
        Gokend beløb/fremvisning af bon

'''