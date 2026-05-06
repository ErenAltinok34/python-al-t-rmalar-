sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

toplam = 0
sayac = 0

while sayac < sayi2:
    toplam = toplam + sayi1
    sayac = sayac + 1

print("Sonuç:", toplam)