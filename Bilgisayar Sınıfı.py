import random
import time

class Bilgisayar():

    def __init__(self,pc_durum = "Kapalı",pc_ses = 0,uzantı_listesi = ["Google"],uzantı = "Google"):

        self.pc_durum = pc_durum

        self.pc_ses = pc_ses

        self.uzantı_listesi = uzantı_listesi

        self.uzantı = uzantı

    def pc_ac(self):

        if (self.pc_durum == "Açık"):
            print("Bilgisayar Zaten Açık....")

        else:
            print("Bilgisayar Açılıyor...")
            self.pc_durum = "Açık"

    def pc_kapat(self):

        if(self.pc_durum == "Kapalı"):
            print("Bilgisayar Zaten Kapalı...")

        else:
            print("Bilgisayar Kapanıyor...")
            self.pc_durum = "Kapalı"

    def ses_ayarları(self):

        while True:

            cevap = input("Sesi Azalt: '-'\nSesi Azalt: '+'\nÇıkış: 'q'\nİşlem seçiniz: ")

            if (cevap == "-"):
                if(self.pc_ses != 0):

                    self.pc_ses -= 1
                    print("Ses: ",self.pc_ses)

            elif (cevap == "+"):
                if(self.pc_ses != 100):

                    self.pc_ses += 1
                    print("Ses: ",self.pc_ses)

            else:
                print("Ses Güncellendi: ",self.pc_ses)
                break

    def uzantı_ekle(self,uzantı_ismi):

        print("Uzantı Ekleniyor...")
        time.sleep(1)

        self.uzantı_listesi.append(uzantı_ismi)
        print("Uzantı EKlendi...")

    def rastgele_uzantı(self):

        rastgele = random.randint(0,len(self.uzantı_listesi)-1)

        self.uzantı = self.uzantı_listesi[rastgele]

        print("Şu anki Uzantı: ",self.uzantı)

    def __len__(self):

        return len(self.uzantı_listesi)

    def __str__(self):

        return "Pc Durumu: {}\nPc ses: {}\nUzantı Listesi: {}\nŞu anki Uzantı: {}\n".format(self.pc_durum,self.pc_ses,self.uzantı_listesi,self.uzantı)

bilgisayar = Bilgisayar ()

print("""

Bilgisayar Uygulaması 
    
1.Pc Aç

2.Pc Kapat

3.Pc Ses Ayarları

4.Uzantı Ekle

5.Uzantı Sayısını Öğrenme

6.Rastgele Uzantı Geçme

7.Bilgisayar Bilgileri

Çıkamak için 'q' ya basınız
""")

while True:

    işlem = input("İşlem Seçiniz: ")

    if(işlem == "q"):
        print("Program Sonlanrılıyor...")
        break

    elif (işlem == "1"):
        bilgisayar.pc_ac()

    elif(işlem == "2"):
        bilgisayar.pc_kapat()

    elif(işlem == "3"):
        bilgisayar.ses_ayarları()

    elif(işlem == "4"):
        uzantı_isimleri = input("Uzantı isimleri ',' ile ayırarak giriniz: ")

        uzantı_listesi = uzantı_isimleri.split(",")

        for eklenecekler in uzantı_listesi:
            bilgisayar.uzantı_ekle(eklenecekler)

    elif(işlem == "5"):
        print("Uzantı Sayısı: ",len(bilgisayar))

    elif(işlem == "6"):
        bilgisayar.rastgele_uzantı()

    elif(işlem == "7"):
        print(bilgisayar)

    else:
        print("Geçersiz İşlem")