from produksi import Produk

class RotiTawar(Produk):
    def __init__(self, id_produk, nama, harga, stok, jenis_tepung, tanpa_kulit, daya_tahan_hari):
        super().__init__(id_produk, nama, harga, stok)
        self.__jenis_tepung = jenis_tepung
        self.__tanpa_kulit = tanpa_kulit
        self.__daya_tahan_hari = daya_tahan_hari

    def get_jenis_tepung(self):
        return self.__jenis_tepung

    def hitung_harga_diskon(self):
        if self.__daya_tahan_hari <= 1:
            return self.get_harga() * 0.9
        return self.get_harga()

    def cek_kadaluarsa(self):
        if self.__daya_tahan_hari <= 0:
            return "KADALUARSA"
        return f"Tahan {self.__daya_tahan_hari} hari lagi"

    def tampilkan_info(self):
        super().tampilkan_info()
        print("jenis: Roti Tawar")
        print("tepung:", self.__jenis_tepung)
        print("kadaluarsa:", self.cek_kadaluarsa())