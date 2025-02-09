import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
yeni_sifre = ""

sifre = int(input("Kaç karakterli bir şifre istersiniz?"))
for i in range(sifre):
    karakter = random.choice(karakterler)
    yeni_sifre += karakter
print(yeni_sifre)
