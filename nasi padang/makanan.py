from menu_item import MenuItem

# ==========================================
# PEWARISAN (Inheritance) - Child class Makanan
# ==========================================
class Makanan(MenuItem):
    """Class turunan dari MenuItem untuk kategori Makanan."""

    def __init__(self, nama, harga):
        # Memanggil constructor parent class
        super().__init__(nama, harga)

    def get_kategori(self):
        return "Makanan"

    # POLIMORFISME: implementasi tampilkan_info() berbeda dari Minuman
    def tampilkan_info(self):
        return f"[Makanan] {self.get_nama():<30} Rp {self.get_harga():>7,.0f}"


# ==========================================
# DATA MENU MAKANAN
# ==========================================
def get_daftar_makanan():
    return [
        # --- Ayam ---
        Makanan("Nasi Ayam Pop",           12000),
        Makanan("Nasi Ayam Cabe",          12000),
        Makanan("Nasi Ayam Kecap",         12000),
        Makanan("Nasi Ayam Rendang",       12000),
        Makanan("Nasi Ayam Gulai",         12000),
        Makanan("Nasi Ayam Bakar",         12000),
        # --- Ikan ---
        Makanan("Nasi Ikan Bakar Nila",    15000),
        Makanan("Nasi Ikan Lele Goreng",   15000),
        Makanan("Nasi Ikan Kakap Bakar",   17000),
        # --- Spesial ---
        Makanan("Nasi Rendang",            18000),
        Makanan("Nasi Dendeng",            18000),
        Makanan("Nasi Kikil",              18000),
        Makanan("Nasi tambah",              2000),
    ]
