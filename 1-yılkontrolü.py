yil = int(input("Yılı giriniz: "))

if yil % 400 == 0:
    print("Artık yıldır.")

elif yil % 100 == 0:
    print("Artık yıl değildir.")

elif yil % 4 == 0:
    print("Artık yıldır.")

else:
    print("Artık yıl değildir.")