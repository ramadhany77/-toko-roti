from datetime import date

class Penjualan:
    def __init__(self, id_penjualan, nama_pembeli):
        self.__id_penjualan = id_penjualan
        self.__nama_pembeli = nama_pembeli
        self.__tanggal = str(date.today())
        self.__daftar_produk = []

    def get_id_penjualan(self):
        return self.__id_penjualan

    def get_nama_pembeli(self):
        return self.__nama_pembeli

    def get_tanggal(self):
        return self.__tanggal

    def get_daftar_produk(self):
        return self.__daftar_produk

    def tambah_produk(self, produk, jumlah):
        if produk.kurangi_stok(jumlah):
            self.__daftar_produk.append((produk, jumlah))
            return True
        return False

    def hitung_total(self):
        total = 0
        for produk, jumlah in self.__daftar_produk:
            total += produk.hitung_total_harga(jumlah)
        return total

    def cek_status(self):
        if len(self.__daftar_produk) == 0:
            return "BELUM ADA ITEM"
        return f"SELESAI - {len(self.__daftar_produk)} item"

    def tampilkan_struk(self):
        print(f"\n=== STRUK {self.__id_penjualan} ===")
        print("pembeli:", self.__nama_pembeli)
        print("tanggal:", self.__tanggal)
        for produk, jumlah in self.__daftar_produk:
            print(f"- {produk.get_nama()} x{jumlah} = Rp{produk.hitung_total_harga(jumlah)}")
        print("total:", self.hitung_total())
        print("status:", self.cek_status())
        print("="*35)