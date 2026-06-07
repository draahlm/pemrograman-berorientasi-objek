from makanan  import get_daftar_makanan
from minuman  import get_daftar_minuman
from keranjang import Keranjang
from kasir    import Kasir

# ==========================================
# FUNGSI TAMPIL MENU
# ==========================================
def tampilkan_menu(daftar_makanan, daftar_minuman):
    print("\n" + "=" * 50)
    print(f"  {'=== MENU RUMAH MAKAN DATUAK ANDAQIM ===':^48}")
    print("=" * 50)

    print("\n  ---- MAKANAN ----")
    for i, item in enumerate(daftar_makanan, 1):
        print(f"  {i:>2}. {item.get_nama():<28} Rp {item.get_harga():>7,.0f}")

    print(f"\n  ---- MINUMAN ----")
    offset = len(daftar_makanan)
    for i, item in enumerate(daftar_minuman, offset + 1):
        print(f"  {i:>2}. {item.get_nama():<28} Rp {item.get_harga():>7,.0f}")

    print("=" * 50)


def pilih_item(daftar_makanan, daftar_minuman):
    """Minta customer memilih nomor menu."""
    semua_item = daftar_makanan + daftar_minuman
    total_item = len(semua_item)

    while True:
        try:
            pilihan = input(f"\n  Pilih nomor menu (1-{total_item}): ")
            nomor   = int(pilihan)

            if 1 <= nomor <= total_item:
                return semua_item[nomor - 1]
            else:
                print(f"  Nomor tidak valid. Pilih antara 1 sampai {total_item}.")
        except ValueError:
            print("  Input tidak valid. Masukkan angka.")


def pilih_qty():
    """Minta customer memilih jumlah (qty) item."""
    while True:
        try:
            qty = int(input("  Jumlah pesanan: "))
            if qty > 0:
                return qty
            else:
                print("  Jumlah harus lebih dari 0.")
        except ValueError:
            print("  Input tidak valid. Masukkan angka.")


# ==========================================
# MAIN PROGRAM
# ==========================================
if __name__ == "__main__":

    daftar_makanan = get_daftar_makanan()
    daftar_minuman = get_daftar_minuman()
    keranjang      = Keranjang()
    kasir          = Kasir()

    print("\n" + "*" * 50)
    print(f"  {'Selamat Datang di Rumah Makan Datuak Andaqim':^48}")
    print("*" * 50)

    while True:
        # ---- LANGKAH 1: Tampilkan menu & pilih item ----
        tampilkan_menu(daftar_makanan, daftar_minuman)
        item_dipilih = pilih_item(daftar_makanan, daftar_minuman)
        qty          = pilih_qty()

        keranjang.tambah_item(item_dipilih, qty)
        print(f"\n  '{item_dipilih.get_nama()}' x{qty} ditambahkan ke keranjang!")

        # ---- LANGKAH 2: Tampilkan keranjang saat ini ----
        print("\n  === Keranjang Pesanan Kamu ===")
        keranjang.tampilkan_keranjang()

        # ---- LANGKAH 3: Pilih lanjut pesan atau bayar ----
        print("\n  Apa yang ingin kamu lakukan?")
        print("  1. Tambah pesanan lagi")
        print("  2. Bayar sekarang")

        while True:
            aksi = input("  Pilihan (1/2): ").strip()
            if aksi in ("1", "2"):
                break
            print("  Pilihan tidak valid. Masukkan 1 atau 2.")

        if aksi == "2":
            # ---- LANGKAH 4: Proses pembayaran & cetak struk ----
            uang_bayar, kembalian = kasir.proses_pembayaran(keranjang)
            kasir.cetak_struk(keranjang, uang_bayar, kembalian)

            keranjang.kosongkan()

            # Tanya mau pesan lagi atau keluar
            print("\n  Mau pesan lagi?")
            print("  1. Ya, pesan lagi")
            print("  2. Tidak, keluar")

            while True:
                lagi = input("  Pilihan (1/2): ").strip()
                if lagi in ("1", "2"):
                    break
                print("  Pilihan tidak valid.")

            if lagi == "2":
                print("\n" + "*" * 50)
                print(f"  {'Sampai jumpa! Terima kasih :)':^48}")
                print("*" * 50 + "\n")
                break
