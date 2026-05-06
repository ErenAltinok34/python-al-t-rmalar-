gun = int(input("Gün: "))
ay = int(input("Ay: "))
yil = int(input("Yıl: "))

if ay in [1, 3, 5, 7, 8, 10, 12]:
    ay_sonu = 31
elif ay in [4, 6, 9, 11]:
    ay_sonu = 30
else: # Şubat ayı
    ay_sonu = 28

gun = gun + 1

if gun > ay_sonu:
    gun = 1
    ay = ay + 1

if ay > 12:
    ay = 1
    yil = yil + 1

print("Ertesi günün tarihi:", gun, "/", ay, "/", yil)