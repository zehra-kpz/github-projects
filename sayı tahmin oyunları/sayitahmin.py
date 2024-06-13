import random

def tahmin_oyunu():
    rastgele_sayi = random.randint(1, 100)
    tahmin = None

    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")

    while tahmin != rastgele_sayi:
        try:
            tahmin = int(input("Tahmininiz: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayı girin.")
        elif tahmin > rastgele_sayi:
            print("Daha küçük bir sayı girin.")
        else:
            print("Tebrikler! Doğru tahmin ettiniz.")

    input("Çıkmak için Enter tuşuna basın...")

tahmin_oyunu()
