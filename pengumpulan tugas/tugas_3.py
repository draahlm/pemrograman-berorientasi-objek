from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def get_harga(self):
        pass


class Makanan(Menu):
    def get_harga(self):
        return 15000


class Minuman(Menu):
    def get_harga(self):
        return 5000


class Pesanan:
    def __init__(self, menu):
        self.menu = menu

    def hitung_total(self):
        return self.menu.get_harga()

    def tampilkan(self):
        print(f"Total harga : {self.hitung_total()}")


makan1 = Makanan()
minum1 = Minuman()

pesan1 = Pesanan(makan1)
pesan2 = Pesanan(minum1)

pesan1.tampilkan()
pesan2.tampilkan()