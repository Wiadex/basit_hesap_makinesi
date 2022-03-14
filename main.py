#       Python Öğrenme Sürecimde Basit bir hesap makinesi yazmak istedim ve bunu da sizinle paylaşmak istedim                                                             
giriş = """
                                                               

(1) Toplama İşlemleri
(2) Çıkarma İşlemleri
(3) Çarpma İşlemleri
(4) Bölme İşlemleri
(5) Karesini Hesaplama
(6) Karekök Hesaplama
"""

print(giriş)

anahtar = 1

while anahtar:
    soru = input("Yapmak İstediğiniz İşlemi Seçin (Çıkış Yapmak İçin q):")
    if soru == "q":
        print("Çıkış Yapılıyor...")
        anahtar = 0

    elif soru== "1":
        sayı_1 = int(input("Lütfen Toplama İşlemi İçin İlk Sayıyı Girin :"))
        sayı_2 = int(input("Lütfen Toplama İşlemi İçin İkinci Sayıyı Girin :"))
        print("İşlem Sonucu :",sayı_1, "+", sayı_2, "=", sayı_1 + sayı_2)

    elif soru== "2":
        sayı_3 = int(input("Lütfen Çıkarma İşlemi İçin İlk Sayıyı Girin :"))
        sayı_4 = int(input("Lütfen Çıkarma İşlemi İçin İkinci Sayıyı Girin :"))
        print("İşlem Sonucu :", sayı_3, "-", sayı_4, "=", sayı_3 - sayı_4)

    elif soru== "3":
        sayı_5 = int(input("Lütfen Çarpma İşlemi İçin İlk Sayıyı Girin :"))
        sayı_6 = int(input("Lütfen Çarpma İşlemi İçin İkinci Sayıyı Girin :"))
        print("İşlem Sonucu :", sayı_5, "x", sayı_6, "=", sayı_5 * sayı_6)

    elif soru== "4":
        sayı_7 = int(input("Lütfen Bölme İşlemi İçin İlk Sayıyı Girin :"))
        sayı_8 = int(input("Lütfen Bölme İşlemi İçin İkinci Sayıyı Girin :"))
        print("İşlem Sonucu :", sayı_7, "/", sayı_8, "=", sayı_7 / sayı_8)

    elif soru== "5":
        sayı_9 = int(input("Lütfen Karesini Hesaplamak İstediğiniz Sayıyı Girin :"))
        print("İşlem Sonucu :", sayı_9, "Sayısının Karesi", "=", sayı_9 ** 2)

    elif soru== "6":
        sayı_10 = int(input("Lütfen Karekökünü Hesaplamak İstediğiniz Sayıyı Girin :"))
        print("İşlem Sonucu :", sayı_10, "sayısının karekökü =", sayı_10 ** 0.5)

    else:
        print("Geçersiz İşlem !")
        print("Aşağıdaki Seçeneklerden Birini Giriniz :", giriş)