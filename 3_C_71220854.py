#c. Test case 1:
import math
p = int(input("Masukan panjang :"))
l = int (input("Masukan lebar : "))
r = int (input("Masukan jari-jari :"))
Llingkaran=float(((math.pi)*(r**2)/2))
luasspp=float(p*1)
jumlahkaleng=float(((Llingkaran + luasspp)/15))
print("Area tersebut membutuhkan",math.ceil(jumlahkaleng),"kaleng cat")