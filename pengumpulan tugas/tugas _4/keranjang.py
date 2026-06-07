# ==========================================
# ENKAPSULASI - Class Keranjang
# ==========================================
class Keranjang:
    """
    Menyimpan semua item yang sudah dipesan oleh customer.
    Semua atribut bersifat private, hanya bisa diakses lewat method.
    """

    def __init__(self):
        # ENKAPSULASI: semua atribut private
        self.__items = []   # list of (MenuItem, qty)

    def tambah_item(self, menu_item, qty=1):
        """Tambah item ke keranjang. Jika sudah ada, tambah qty-nya."""
        for i, (item, jumlah) in enumerate(self.__items):
            if item.get_nama() == menu_item.get_nama():
                self.__items[i] = (item, jumlah + qty)
                return
        self.__items.append((menu_item, qty))

    def get_items(self):
        """Kembalikan salinan list items (tidak bisa diubah dari luar)."""
        return list(self.__items)

    def hitung_total(self):
        """Hitung total harga semua item di keranjang."""
        total = 0
        for item, qty in self.__items:
            total += item.get_harga() * qty
        return total

    def kosongkan(self):
        """Kosongkan keranjang setelah pembayaran selesai."""
        self.__items = []

    def is_kosong(self):
        return len(self.__items) == 0

    def tampilkan_keranjang(self):
        """Tampilkan semua item yang ada di keranjang."""
        if self.is_kosong():
            print("  Keranjang masih kosong.")
            return

        print(f"\n  {'No':<4} {'Item':<32} {'Qty':>4} {'Harga':>10} {'Subtotal':>12}")
        print("  " + "-" * 65)
        for i, (item, qty) in enumerate(self.__items, 1):
            subtotal = item.get_harga() * qty
            print(f"  {i:<4} {item.get_nama():<32} {qty:>4} "
                  f"Rp {item.get_harga():>7,.0f} Rp {subtotal:>9,.0f}")
        print("  " + "-" * 65)
        print(f"  {'TOTAL':>43} Rp {self.hitung_total():>9,.0f}")
