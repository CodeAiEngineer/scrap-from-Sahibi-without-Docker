# -*- coding: utf-8 -*-
from aracCek import AracCek
from sendMail import SendMail
from mailVerisi import MailVerisi
from url import Url


# Kullanıcıdan filtreleme bilgisi almadan direkt filtre.ini dosyasını okur. Eğer önce kullanıcıdan veri almak isteniyorsa
# önce user_input.py çalıştırılmalıdır.

class ArabaFiltresi:
    def __init__(self):
        self.sayfaDevam = True
        self.emailAlindi = True
        

    def run(self):
        # Sayfa değişkeni her döngüde 20 arttırılıyor çünkü sahibinden.com'dan veri okunurken 2. sayfayı okumak için 20 arttırmak gerekiyor.
        sayfa=1
        # numarator değişkeni mail içeriğinde n. araç bilgileri kısmının düzenlenmesi için tanımlandı
        numarator= 0
        while self.sayfaDevam:
            
            # Bu değişken son sayfada olup olmadığımızı anlamak için kontrol amacıyla tanımlandı
            aracListesiStrEski = ""
            aracListesi = []
            lists = Url().url_cek(sayfa)        
            toplamListelenenAracSayisi=0

            aracListesi, toplamListelenenAracSayisi = AracCek().aracCek(lists, toplamListelenenAracSayisi, aracListesi)
            if toplamListelenenAracSayisi==0:
                print("Araç bulunamadı")
                self.sayfaDevam = False
                
            if toplamListelenenAracSayisi != 0:

                if self.emailAlindi:
                    print('*******************************************************************************')
                    email = input("Gönderilecek e-posta adresini girin: ")
                    print('*******************************************************************************')
                    self.emailAlindi = False

                aracListesiStr,numarator = MailVerisi().mailVerisi(aracListesi,numarator)
                sendmail = SendMail()
                sendmail.send_email(aracListesiStr, email)
                if aracListesiStr != aracListesiStrEski:
                    aracListesiStrEski = aracListesiStr
                else:
                    print('*******************************************************************************')
                    print("Son sayfaya ulaştınız")
                    print('*******************************************************************************')
                    self.sayfaDevam=False
                if toplamListelenenAracSayisi > 19:
                    print('*******************************************************************************')
                    devam = input(str(toplamListelenenAracSayisi)+" adet gönderdik. Diğer sayfayı gönderelim mi? Y/N: ")
                    print('*******************************************************************************')
                    if devam=="Y" or devam=="y":
                        self.sayfaDevam=True 
                        sayfa += 20
                    else:
                        print('*******************************************************************************')
                        print("İşlem Sonlanıyor")        
                        print('*******************************************************************************')
                        self.sayfaDevam=False
                else:
                    if numarator !=  0:
                        print('*******************************************************************************')
                        print(str(numarator)+" tane gönderdik. Başka araç bulunamadı. İşlem sonlanıyor.")
                        print('*******************************************************************************')
                        self.sayfaDevam = False

if __name__ == "__main__":
    arabafiltresi = ArabaFiltresi()
    arabafiltresi.run()

    