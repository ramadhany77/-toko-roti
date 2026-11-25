class Produk:
    def __init__(self, id_produk, nama, harga, stok):
        if harga < 0 or stok < 0:
            raise ValueError("harga/stok tidak valid")
        self.__id_produk = id_produk
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    def get_id_produk(self):
        return self.__id_produk

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def ubah_harga(self, harga_baru):
        if harga_baru < 0:
            return False
        self.__harga = harga_baru
        return True

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            return False
        self.__stok += jumlah
        return True

    def kurangi_stok(self, jumlah):
        if jumlah < 0 or jumlah > self.__stok:
            return False
        self.__stok -= jumlah
        return True

    def hitung_nilai_stok(self):
        return self.__harga * self.__stok

    def hitung_total_harga(self, jumlah):
        return self.__harga * jumlah

    def cek_status(self):
        if self.__stok == 0:
            return "HABIS"
        elif self.__stok < 5:
            return "HAMPIR HABIS"
        else:
            return "TERSEDIA"

    def tampilkan_info(self):
        print("kode:", self.__id_produk)
        print("nama:", self.__nama)
        print("harga:", self.get_harga())
        print("stok:", self.get_stok())
        print("nilai stok:", self.hitung_nilai_stok())
        print("status:", self.cek_status())

