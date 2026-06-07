from abc import ABC, abstractmethod

# ==========================================
# ABSTRAKSI (Abstract Base Class)
# ==========================================
class MenuItem(ABC):
    """
    Class Abstrak: Tidak bisa di-instansiasi langsung.
    Ini adalah 'kontrak' untuk setiap jenis item menu.
    """

    def __init__(self, nama, harga):
        # ENKAPSULASI: atribut dibuat private dengan __
        self.__nama = nama
        self.__harga = harga

    # Getter untuk nama (akses ke atribut private)
    def get_nama(self):
        return self.__nama

    # Getter untuk harga (akses ke atribut private)
    def get_harga(self):
        return self.__harga

    # Setter untuk harga (kalau suatu saat harga berubah)
    def set_harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga = harga_baru

    @abstractmethod
    def get_kategori(self):
        """Setiap class turunan WAJIB mengimplementasikan ini."""
        pass

    @abstractmethod
    def tampilkan_info(self):
        """Setiap class turunan WAJIB mengimplementasikan ini."""
        pass
