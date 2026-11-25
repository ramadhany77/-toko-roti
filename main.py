from roti_tawar import RotiTawar
from roti_manis import RotiManis
from penjualan import Penjualan

daftar_roti = []
daftar_penjualan = []

daftar_roti.append(RotiTawar("R001", "Roti Tawar Gandum", 15000, 20, "Gandum", True, 3))
daftar_roti.append(RotiTawar("R002", "Roti Tawar Putih", 12000, 8, "Terigu", False, 2))
daftar_roti.append(RotiManis("R003", "Roti Coklat", 10000, 15, "Coklat", "Meses", 5))
daftar_roti.append(RotiManis("R004", "Roti Keju", 12000, 0, "Keju", "Keju Parut", 3))

def cari_roti(kode):
    for r in daftar_roti:
        if r.get_id_produk() == kode:
            return r
    return None

def main():
    while True:
        print("\n===== APLIKASI PRODUKSI TOKO ROTI =====")
        print("1. Tambah Data Roti")
        print("2. Tampilkan Data Roti")
        print("3. Cari Data Roti")
        print("4. Ubah Data Roti")
        print("5. Hapus Data Roti")
        print("6. Cek Status Data Roti")
        print("7. Buat Penjualan")
        print("8. Tampilkan Penjualan")
        print("0. Keluar")
        print("========================================")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            jenis = input("Jenis (1=Tawar, 2=Manis): ")
            kode = input("Kode: ")
            nama = input("Nama: ")
            harga = int(input("Harga: "))
            stok = int(input("Stok: "))
            if jenis == "1":
                tepung = input("Jenis Tepung: ")
                kulit = input("Tanpa Kulit? (y/n): ").lower() == "y"
                tahan = int(input("Daya Tahan (hari): "))
                daftar_roti.append(RotiTawar(kode, nama, harga, stok, tepung, kulit, tahan))
            else:
                rasa = input("Varian Rasa: ")
                topping = input("Topping: ")
                manis = int(input("Level Manis (1-5): "))
                daftar_roti.append(RotiManis(kode, nama, harga, stok, rasa, topping, manis))
            print("Data berhasil ditambah!")

        elif pilih == "2":
            print("\n-- Daftar Roti --")
            for r in daftar_roti:
                r.tampilkan_info()
                print("---")

        elif pilih == "3":
            kode = input("Kode yang dicari: ")
            r = cari_roti(kode)
            if r:
                r.tampilkan_info()
            else:
                print("Data tidak ditemukan!")

        elif pilih == "4":
            kode = input("Kode yang mau diubah: ")
            r = cari_roti(kode)
            if r:
                harga_baru = int(input(f"Harga baru (lama Rp{r.get_harga()}): "))
                stok_baru = int(input(f"Stok baru (lama {r.get_stok()}): "))
                r.ubah_harga(harga_baru)
                selisih = stok_baru - r.get_stok()
                if selisih > 0:
                    r.tambah_stok(selisih)
                elif selisih < 0:
                    r.kurangi_stok(-selisih)
                print("Data berhasil diubah!")
            else:
                print("Data tidak ditemukan!")

        elif pilih == "5":
            kode = input("Kode yang mau dihapus: ")
            r = cari_roti(kode)
            if r:
                daftar_roti.remove(r)
                print("Data berhasil dihapus!")
            else:
                print("Data tidak ditemukan!")

        elif pilih == "6":
            for r in daftar_roti:
                print(f"{r.get_nama()} -> Stok: {r.get_stok()} | Status: {r.cek_status()}")

        elif pilih == "7":
            id_jual = f"P{len(daftar_penjualan)+1:03d}"
            pembeli = input("Nama Pembeli: ")
            pj = Penjualan(id_jual, pembeli)
            while True:
                kode = input("Kode Roti (ketik 'selesai' untuk akhiri): ")
                if kode.lower() == "selesai":
                    break
                r = cari_roti(kode)
                if not r:
                    print("Roti tidak ditemukan!")
                    continue
                jml = int(input(f"Jumlah {r.get_nama()}: "))
                if pj.tambah_produk(r, jml):
                    print("Ditambahkan!")
                else:
                    print("Stok tidak cukup!")
            daftar_penjualan.append(pj)
            pj.tampilkan_struk()

        elif pilih == "8":
            for pj in daftar_penjualan:
                pj.tampilkan_struk()

        elif pilih == "0":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()