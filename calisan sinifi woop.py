class Calisan():
    def __init__(self,isim,maas,departman):

        self.isim=isim
        self.maas=maas
        self.departman=departman

    def bilgileri_goster(self):
        print("Çalışan sınıfının bilgileri gösteriliyor...")
        print("İsim:",self.isim,"Maaş:",self.maas,"Departman:",self.departman)

    def maasa_zam(self,zam_miktarı):
        print("Maaşa zam yapıldı.")
        self.maas+=zam_miktarı
    def departman_degisikligi(self,yeni_departman):
        print("Departman değiştiriliyor...")
        self.departman=yeni_departman

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):

        super().__init__(isim,maas,departman)
        self.kisi_sayisi=kisi_sayisi

    def bilgileri_yazdir(self):
        print("Yöneticinin bilgileri gösteriliyor...")
        print("İsim:",self.isim,"Maaş:",self.maas,"Departman:",self.departman,"Şirketteki kişi sayısı:",self.kisi_sayisi)

    def kisi_sayisi_artır(self,yeni_kisi):
        print("Güncellenen kişi sayısı:")
        self.kisi_sayisi+=yeni_kisi


c1=Yonetici("Zeynep Besra Özden",80000,"Artifical İntelligence Enginner",145)
c1.bilgileri_yazdir()
c1.kisi_sayisi_artır(10)
c1.bilgileri_yazdir()

