# encoding:utf-8
from abc import ABC, abstractmethod 
import datetime

class Bilgi(ABC):  # Soyut sınıf
    @abstractmethod
    def bilgi_goster(self):
        pass

class KisiselBilgi(Bilgi):
    # Özellikler (Attributes)
    def __init__(self, isim, kimlikNo, cinsiyet, yas, dogumTarihi, telefonNo):
        self.isim = isim
        self._kimlikNo = kimlikNo  # protected
        self.cinsiyet = cinsiyet
        self.yas = yas
        self.dogumTarihi = dogumTarihi
        self.telefonNo = telefonNo  # setter ile private set edilir
     
    #Getter metodu
    @property
    def telefonNo(self):
        return self.__telefonNo

    @telefonNo.setter
    def telefonNo(self, telefonNo):
        if telefonNo.isdigit() and len(telefonNo) == 10:  # Telefon numarası sadece rakamlardan oluşmalı ve 10 haneli olmalı 
            self.__telefonNo = telefonNo
        else:
            raise ValueError("Geçersiz telefon numarası!")
            

    # Metotlar (Methods)
    def bilgi_goster(self):
        return f"------------------------------------\nİsim: {self.isim}\nKimlik Numarası: {self._kimlikNo}\nCinsiyet: {self.cinsiyet}\nYaş: {self.yas}\nDoğum Tarihi: {self.dogumTarihi}\nTelefon Numarası: {self.__telefonNo}"


class SaglikBilgi(KisiselBilgi,Bilgi):
    # Özellikler (Attributes)
    def __init__(self, kanGrubu, alerji, alinanIlac, hastalikBilgisi, isim, kimlikNo, cinsiyet, yas, dogumTarihi, telefonNo):
        KisiselBilgi.__init__(self,isim, kimlikNo, cinsiyet, yas, dogumTarihi, telefonNo)  # KisiselBilgi'yi çağır,tekli kalıtım örneği
        self.kanGrubu = kanGrubu
        self.alerji = alerji
        self.alinanIlac = alinanIlac
        self.hastalikBilgisi = hastalikBilgisi
    
    # Metotlar (Methods)
    def bilgi_goster(self):
        return f"------------------------------------\nKan Grubu: {self.kanGrubu}\nAlerjiler: {self.alerji}\nAlınan İlaçlar: {self.alinanIlac}\nHastalıklar: {self.hastalikBilgisi}"


# Kişisel Bilgiler için kullanıcıdan veri al
print("\nKullanıcının Bilgileri:")
isim=input("------------------------------------\nİsim (ad-soyad): ")
kimlikNo=input("Kimlik Numarası : ")
cinsiyet=input("Cinsiyet (Kadın, Erkek): ")
yas=input("Yaş: ")
dogumTarihi=input("Doğum Tarihi (gg.aa.yy): ")
telefonNo=input("Telefon Numarası (0'la başlamayınız!): ")

# KisiselBilgi nesnesi oluştur
kisiselbilgi = KisiselBilgi(isim, kimlikNo, cinsiyet, yas, dogumTarihi, telefonNo)

# Sağlık bilgileri için kullanıcıdan veri al
kanGrubu = input("\nKan Grubu: ")
alerji = input("Alerjiler (yoksa yok yazın): ")
alinanIlac = input("Alınan İlaçlar (yoksa yok yazın): ")
hastalikBilgisi = input("Hastalıklar (hastalığınız yoksa yok yazın): ")

# SaglikBilgi nesnesi oluştur
saglikbilgi = SaglikBilgi(kanGrubu, alerji, alinanIlac, hastalikBilgisi, isim, kimlikNo, cinsiyet, yas, dogumTarihi, telefonNo)

#Acil durum kişileri
class AcilKisiler(Bilgi):
    # Özellikler (Attributes)
    def __init__(self,yakinlikDerecesi,isim,telefonNo):
        self.yakinlikDerecesi = yakinlikDerecesi
        self.isim = isim 
        self.__telefonNo = telefonNo  # private

    # Metotlar (Methods)
    def bilgi_goster(self):
        return f"------------------------------------\nİsim: {self.isim}\nYakınlık Derecesi: {self.yakinlikDerecesi}\nTelefon Numarası: {self.__telefonNo}"

    #Acil durum kişisi ekler
    @classmethod
    def acil_kisi_ekle(cls,yakinlikDerecesi, isim, telefonNo):
        return cls(yakinlikDerecesi, isim, telefonNo)

    #Acil durum kişilerini yazdırır
    @staticmethod
    def acil_kisileri_getir(kisiler_listesi):
        for kisi in kisiler_listesi:
            print(kisi.bilgi_goster())

# Acil durum kişilerini saklayacak liste
acil_kisiler_listesi = []

# Kullanıcıdan üç acil durum kişisi bilgisi al
for i in range(3):
    print(f"\nAcil Durum Kişisi {i + 1}")
    isim = input("İsim (ad-soyad): ")
    yakinlikDerecesi = input("Yakınlık Derecesi: ")
    telefonNo = input("Telefon Numarası(0'la başlamayınız!): ")
    

    acil_kisi = AcilKisiler.acil_kisi_ekle(yakinlikDerecesi, isim, telefonNo)
    acil_kisiler_listesi.append(acil_kisi)
    
# Konum Sınıfı
class Konum(Bilgi):
    def __init__(self):
        self.enlem = None
        self.boylam = None
        self.zaman = None

    def konumAl(self):
        self.enlem = 38.334217  # Örnek: İnönü Üniversitesi enlemi
        self.boylam = 38.438061  # Örnek: İnönü Üniversitesi boylamı
        self.zaman = datetime.datetime.now()
        print(f"\nKonum alındı: {self}")
        
    def bilgi_goster(self): 
        return f"Konum: Enlem: {self.enlem}, Boylam: {self.boylam}, Zaman: {self.zaman}"

    def bilgiGonder(self):
        if self.enlem and self.boylam:
            print(f"Konum gönderiliyor: {self}")
        else:
            print("Konum bilgisi eksik. Önce konum alınmalıdır.")

    def __str__(self):
        return f"Enlem: {self.enlem}, Boylam: {self.boylam}, Zaman: {self.zaman}"


# Bilgileri yazdır
print("\nKullanıcı Bilgileri:")
print(kisiselbilgi.bilgi_goster())
print(saglikbilgi.bilgi_goster())
print("\nAcil Durum Kişileri Bilgileri:")
AcilKisiler.acil_kisileri_getir(acil_kisiler_listesi)
konum = Konum()
konum.konumAl()
print("\n\nAcil Yardım Talebinde Bulunuldu!!!")
konum.bilgiGonder()

# Polimorfik bilgi gösterme fonksiyonu
def genel_bilgi_goster(nesneler):
    for nesne in nesneler:
        print(nesne.bilgi_goster())  # Tüm nesnelerin bilgi_goster metodu çağrılır

nesneler = [kisiselbilgi, saglikbilgi, acil_kisi, konum]

# Polimorfik bilgi gösterimi
print("\nTüm Bilgiler Polimorfizm Prensibiyle Gösteriliyor:")
genel_bilgi_goster(nesneler)

