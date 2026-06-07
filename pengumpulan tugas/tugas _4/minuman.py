from menu_item import MenuItem

# ==========================================
# PEWARISAN (Inheritance) - Child class Minuman
# ==========================================
class Minuman(MenuItem):
    """Class turunan dari MenuItem untuk kategori Minuman."""

    def __init__(self, nama, harga):
        # Memanggil constructor parent class
        super().__init__(nama, harga)

    def get_kategori(self):
        return "Minuman"

    # POLIMORFISME: implementasi tampilkan_info() berbeda dari Makanan
    def tampilkan_info(self):
        return f"[Minuman] {self.get_nama():<30} Rp {self.get_harga():>7,.0f}"


# ==========================================
# DATA MENU MINUMAN
# ==========================================
def get_daftar_minuman():
    return [
        Minuman("Es Kosong",              1000),
        Minuman("Es Teh",                 5000),
        Minuman("Es Jeruk",               5000),
        Minuman("Es Milo",                5000),
        Minuman("Es Cappucino Cincau",    5000),
        Minuman("Jus Alpokat",            6000),
        Minuman("Jus Mangga",             6000),
    ]
