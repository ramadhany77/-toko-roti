from produksi import Produk

class RotiManis(Produk):
    def __init__(self, id_produk, nama, harga, stok, varian_rasa, topping, level_manis):
        super().__init__(id_produk, nama, harga, stok)
        self.__varian_rasa = varian_rasa
        self.__topping = topping
        self.__level_manis = level_manis

    def get_varian_rasa(self):
        return self.__varian_rasa

    def hitung_harga_diskon(self):
        if self.__level_manis >= 4:
            return self.get_harga() * 0.85
        return self.get_harga()

    def rekomendasi_penyajian(self):
        if self.__level_manis >= 4:
            return "Disajikan Hangat + Teh Tawar"
        return "Disajikan Suhu Ruang"

    def tampilkan_info(self):
        super().tampilkan_info()
        print("jenis: Roti Manis")
        print("rasa:", self.__varian_rasa)
        print("topping:", self.__topping)
        print("penyajian:", self.rekomendasi_penyajian())