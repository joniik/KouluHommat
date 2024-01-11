import keyboard
import time

numero = 00000000
numerolista = []

asti = input("Mihin asti?: ")
start = time.time()

while numero <= int(asti):
    numerolista.append(numero)
    print(numero)
    numero += 1
    
file = open("numerot.txt","w")
file.write(str(numerolista))
file.close()
end = time.time()
aika = end - start

print("%.3f" % aika , "sec")