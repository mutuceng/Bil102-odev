class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satis_tutari = 0

    def __str__(self):
        return f"Mağaza Adı: {self.__magaza_adi}, Satıcı Adı: {self.__satici_adi}, Satıcı Cinsi: {self.__satici_cinsi}, Satış Tutarı: {self.__satis_tutari}"

    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi

    def get_satis_tutari(self):
        return self.__satis_tutari

    def set_satis_tutari(self, satis_tutari):
        self.__satis_tutari = satis_tutari

    def magaza_satis_tutar(self, magaza_adi=None, satici_adi=None, satici_cinsi=None):
        if magaza_adi is not None and magaza_adi != self.__magaza_adi:
            return 0

        if satici_adi is not None and satici_adi != self.__satici_adi:
            return 0

        if satici_cinsi is not None and satici_cinsi != self.__satici_cinsi:
            return 0

        return self.__satis_tutari

satislar = []
while True:
    magaza_adi = input("Mağaza Adı: ")
    if not magaza_adi:
        break

    satici_adi = input("Satıcı Adı: ")
    satici_cinsi = input("Satıcı Cinsi (tv, bilgisayar, beyaz eşya, diğer): ")
    satis_tutari = int(input("Satış Tutarı: "))

    satis = {"magaza_adi": magaza_adi, "satici_adi": satici_adi,
             "satici_cinsi": satici_cinsi, "satis_tutari": satis_tutari}

    satislar.append(satis)

    devam_et = input("\nDevam etmek istiyor musunuz? (E/H): ").lower()
    if devam_et == "h":
        break
    elif devam_et != "e":
        print("Geçersiz seçim, işleme devam ediliyor...")

    print("\n")

magazalar = {}
for satis in satislar:
    magaza_adi = satis["magaza_adi"]
    satici_adi = satis["satici_adi"]
    satici_cinsi = satis["satici_cinsi"]
    satis_tutari = satis["satis_tutari"]

    if magaza_adi not in magazalar:
        magazalar[magaza_adi] = {}

    if satici_adi not in magazalar[magaza_adi]:
        magazalar[magaza_adi][satici_adi] = {"satis_tutari": 0}

    magazalar[magaza_adi][satici_adi]["satis_tutari"] += satis_tutari

for magaza_adi, magaza in magazalar.items():
    print(magaza_adi.upper())
    for satici_adi, satici in magaza.items():
        print(f"\t{satici_adi}: {satici['satis_tutari']} TL")
