class Taksi():
    sefer_taksisayisi = 0
    toplam_yolcusayisi= 0


    def __init__(self, surucu_adi , yol_km, yer, ucret, yolcu_sayisi):
        self.surucu_adi = surucu_adi
        self.yol_km = yol_km
        self.yer = yer
        self.ucret = ucret
        self.yolcu_sayisi = yolcu_sayisi
        Taksi.sefer_taksisayisi += 1
        Taksi.toplam_yolcusayisi = self.yolcu_sayisi + self.toplam_yolcusayisi



    def kmorani(self):
        return self.ucret / self.yol_km

    @classmethod
    def taksi_sayisi(cls):
        return cls.sefer_taksisayisi

    @classmethod
    def ortalamayolcu(cls):
        return cls.toplam_yolcusayisi / cls.sefer_taksisayisi






birinci = Taksi(surucu_adi= "Berke", yol_km= 100, yer= "Istanbul", ucret=50, yolcu_sayisi=4)
ikinci = Taksi("Bora", 100, "Izmir", 30, 2)
ucuncu = Taksi("Osman aga", 200, "Istanbul", 150, 2)
print(Taksi.sefer_taksisayisi)
dorduncu= Taksi("Sinan", 10, "Istanbul", 50, 4)
print(birinci.kmorani())
print(Taksi.toplam_yolcusayisi)
print(Taksi.sefer_taksisayisi)
print(Taksi.taksi_sayisi())
print(Taksi.ortalamayolcu())
print(dorduncu.yer)





