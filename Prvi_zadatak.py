devojka_iz_petnice = "Da je ljubav nauka\ndobio bih Nobela\nA da je ljubav knjiga\nuzeo bih NIN-a\n\nDevojke iz Petnice\nredom su pametnice\nA jedna među njima\nsad moje srce ima\n\nŽelim da sam projekat\ni da sam joj u mislima\nmrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima\nDevojka iz Petnice\nona meni znači sve\ni kada me se seti\nja hoću da poletim\n\nDevojka iz Petnice\nu koju sam zaljubljen\nsad uči tamo negde\nDa li pamti mene?\n\nHoću da sam tema\nU nečemu što sprema\nMrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima"
mala_slova =devojka_iz_petnice.lower()
lista_stihova= mala_slova.split("\n")
prazna_lista= []
for stih in lista_stihova:
    lista_reči= stih.split(" ")
    for reč in lista_reči:
        prazna_lista.append(reč)
        lista_reči=[]
print (len(prazna_lista))
lista_unikata = []
for reč in prazna_lista:
    if reč not in lista_unikata:
        lista_unikata.append(reč)
print(len(lista_unikata))
