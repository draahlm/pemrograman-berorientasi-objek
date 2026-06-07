from datetime import datetime

# ==========================================
# CLASS KASIR - Proses Pembayaran & Struk
# ==========================================
class Kasir:
    """
    Menangani proses pembayaran dan mencetak struk.
    POLIMORFISME: method cetak_struk() bisa menampilkan
    info item secara berbeda (Makanan vs Minuman) lewat tampilkan_info().
    """

    def __init__(self, nama_restoran="RUMAH MAKAN DATUAK ANDAQIM"):
        self.__nama_restoran = nama_restoran
        self.__no_transaksi   = 1

    def proses_pembayaran(self, keranjang):
        """Minta input uang bayar dan hitung kembalian."""

        total = keranjang.hitung_total()

        print(f"\n  Total yang harus dibayar: Rp {total:,.0f}")
        print("  " + "-" * 40)

        while True:
            try:
                bayar_str = input("  Masukkan uang bayar (Rp): ")
                uang_bayar = int(bayar_str.replace(".", "").replace(",", ""))

                if uang_bayar < total:
                    print(f"  Uang kurang! Minimal Rp {total:,.0f}")
                else:
                    break
            except ValueError:
                print("  Input tidak valid. Masukkan angka saja.")

        kembalian = uang_bayar - total
        return uang_bayar, kembalian

    def cetak_struk(self, keranjang, uang_bayar, kembalian):
        """
        POLIMORFISME in Action:
        Saat memanggil item.tampilkan_info(), Python secara otomatis
        akan memanggil versi Makanan atau Minuman sesuai tipe objeknya.
        """

        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print("\n")
        print("  " + "=" * 45)
        print(f"  {'** ' + self.__nama_restoran + ' **':^45}")
        print(f"  {'Jl. rantau perapat No. 88, Pekanbaru':^45}")
        print("  " + "=" * 45)
        print(f"  No. Transaksi : #{self.__no_transaksi:04d}")
        print(f"  Tanggal       : {now}")
        print("  " + "-" * 45)
        print(f"  {'ITEM':<33} {'SUBTOTAL':>10}")
        print("  " + "-" * 45)

        for item, qty in keranjang.get_items():
            subtotal = item.get_harga() * qty
            # POLIMORFISME: tampilkan_info() dipanggil tanpa tahu tipe aslinya
            nama_display = f"{item.get_nama()} (x{qty})"
            print(f"  {nama_display:<33} Rp {subtotal:>7,.0f}")

        print("  " + "-" * 45)
        print(f"  {'TOTAL':<33} Rp {keranjang.hitung_total():>7,.0f}")
        print(f"  {'Bayar':<33} Rp {uang_bayar:>7,.0f}")
        print(f"  {'Kembalian':<33} Rp {kembalian:>7,.0f}")
        print("  " + "=" * 45)
        print(f"  {'Terima kasih sudah memesan!':^45}")
        print(f"  {'Selamat menikmati :)':^45}")
        print("  " + "=" * 45)

        self.__no_transaksi += 1
