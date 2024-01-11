import random

#Seedin rändömisointi
random.seed(random.randint(0, 999999999))

#Luo annetunarvon pituisen listan
def Luolista(n):
    return list(range(1, n + 1))

#Sekoittaa listan
def sekoitalista(L):
    Sekoitettulista = L.copy()
    for i in range(len(Sekoitettulista)):
        indeksi = random.randint(0, len(Sekoitettulista) - 1)
        Sekoitettulista[i], Sekoitettulista[indeksi] = Sekoitettulista[indeksi], Sekoitettulista[i]
    return Sekoitettulista

#Returnaa valmiin listan
def sortattu(L):
    print (L)
    return all(L[i] <= L[i + 1] for i in range(len(L) - 1))

#Sorttaa listan Bogo
def sortti(L):
    laskuri = 0
    while not sortattu(L):
        random.shuffle(L)
        laskuri += 1
    return L, laskuri


luolista_result = Luolista(13)
sekoitettu_result = sekoitalista(luolista_result)

print("Luolista:", luolista_result)
print("Sekoitettu lista:", sekoitettu_result)

sorted_result, laskuri = sortti(sekoitettu_result)
print("sortattu:", sorted_result)
print("yrityksia:", laskuri , "Kpl")

