import random

random.seed(random.randint(0, 999999999))

def Luolista(n):
    return list(range(1, n + 1))

def sekoitalista(L):
    Sekoitettulista = L.copy()
    for i in range(len(Sekoitettulista)):
        indeksi = random.randint(0, len(Sekoitettulista) - 1)
        Sekoitettulista[i], Sekoitettulista[indeksi] = Sekoitettulista[indeksi], Sekoitettulista[i]
    return Sekoitettulista

def sortattu(L, kerrat):
    print(L)
    kerrat += 1
    return all(L[i] <= L[i + 1] for i in range(len(L) - 1)), kerrat

def Bubblesort(L, kerrat):
    n = len(L)
    while not sortattu(L, kerrat)[0]:
        laskuri = 0
        while laskuri < n - 1:
            if L[laskuri] > L[laskuri + 1]:
                L[laskuri], L[laskuri + 1] = L[laskuri + 1], L[laskuri]
            laskuri += 1
        kerrat += 1
    return L, kerrat


luolista_result = Luolista(50)
sekoitettu_result = sekoitalista(luolista_result)

print("Luolista:", luolista_result)
print("Sekoitettu lista:", sekoitettu_result)

sorted_result, kerrat = Bubblesort(sekoitettu_result, 0)
print("Järjestetty lista:", sorted_result)
print("Kerrat:", kerrat, "Kpl")
