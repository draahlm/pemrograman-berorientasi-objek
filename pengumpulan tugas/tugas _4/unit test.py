import unittest
from unittest.mock import patch, MagicMock
import io
import sys

from makanan  import Makanan, get_daftar_makanan
from minuman  import Minuman, get_daftar_minuman
from keranjang import Keranjang
from kasir    import Kasir

# ==================================================
# TEST CASE 1: MENGUJI CLASS MAKANAN
# ==================================================
class TestMakanan(unittest.TestCase):

    def setUp(self):
        """Dipanggil otomatis sebelum setiap test."""
        self.item = Makanan("Nasi Rendang", 18000)

    def test_get_nama(self):
        """Memastikan nama item tersimpan dan bisa diambil dengan benar."""
        self.assertEqual(self.item.get_nama(), "Nasi Rendang")

    def test_get_harga(self):
        """Memastikan harga item tersimpan dan bisa diambil dengan benar."""
        self.assertEqual(self.item.get_harga(), 18000)

    def test_get_kategori(self):
        """Memastikan kategori mengembalikan 'Makanan'."""
        self.assertEqual(self.item.get_kategori(), "Makanan")

    def test_tampilkan_info(self):
        """Memastikan tampilkan_info() mengandung nama dan harga item."""
        info = self.item.tampilkan_info()
        self.assertIn("Nasi Rendang", info)
        self.assertIn("Makanan", info)

    def test_set_harga_valid(self):
        """Memastikan harga bisa diubah jika harga baru valid (> 0)."""
        self.item.set_harga(20000)
        self.assertEqual(self.item.get_harga(), 20000)

    def test_set_harga_tidak_valid(self):
        """Memastikan harga TIDAK berubah jika harga baru <= 0."""
        self.item.set_harga(-5000)
        self.assertEqual(self.item.get_harga(), 18000)

    def test_daftar_makanan_tidak_kosong(self):
        """Memastikan get_daftar_makanan() mengembalikan list yang tidak kosong."""
        daftar = get_daftar_makanan()
        self.assertGreater(len(daftar), 0)

    def test_semua_item_daftar_makanan_adalah_instance_makanan(self):
        """Memastikan semua item di daftar adalah instance class Makanan."""
        daftar = get_daftar_makanan()
        for item in daftar:
            self.assertIsInstance(item, Makanan)


# ==================================================
# TEST CASE 2: MENGUJI CLASS MINUMAN
# ==================================================
class TestMinuman(unittest.TestCase):

    def setUp(self):
        self.item = Minuman("Es Teh", 5000)

    def test_get_nama(self):
        """Memastikan nama minuman tersimpan dengan benar."""
        self.assertEqual(self.item.get_nama(), "Es Teh")

    def test_get_harga(self):
        """Memastikan harga minuman tersimpan dengan benar."""
        self.assertEqual(self.item.get_harga(), 5000)

    def test_get_kategori(self):
        """Memastikan kategori mengembalikan 'Minuman'."""
        self.assertEqual(self.item.get_kategori(), "Minuman")

    def test_tampilkan_info(self):
        """Memastikan tampilkan_info() mengandung nama dan kategori."""
        info = self.item.tampilkan_info()
        self.assertIn("Es Teh", info)
        self.assertIn("Minuman", info)

    def test_daftar_minuman_tidak_kosong(self):
        """Memastikan get_daftar_minuman() mengembalikan list yang tidak kosong."""
        daftar = get_daftar_minuman()
        self.assertGreater(len(daftar), 0)

    def test_semua_item_daftar_minuman_adalah_instance_minuman(self):
        """Memastikan semua item di daftar adalah instance class Minuman."""
        daftar = get_daftar_minuman()
        for item in daftar:
            self.assertIsInstance(item, Minuman)


# ==================================================
# TEST CASE 3: MENGUJI CLASS KERANJANG (Enkapsulasi)
# ==================================================
class TestKeranjang(unittest.TestCase):

    def setUp(self):
        """Siapkan keranjang kosong dan beberapa item untuk testing."""
        self.keranjang = Keranjang()
        self.makanan   = Makanan("Nasi Ayam Pop", 12000)
        self.minuman   = Minuman("Es Jeruk", 5000)

    def test_keranjang_awal_kosong(self):
        """Memastikan keranjang baru selalu kosong."""
        self.assertTrue(self.keranjang.is_kosong())

    def test_tambah_item(self):
        """Memastikan item bisa ditambahkan ke keranjang."""
        self.keranjang.tambah_item(self.makanan, 1)
        self.assertFalse(self.keranjang.is_kosong())

    def test_tambah_item_qty(self):
        """Memastikan qty item tersimpan dengan benar."""
        self.keranjang.tambah_item(self.makanan, 3)
        items = self.keranjang.get_items()
        self.assertEqual(items[0][1], 3)

    def test_tambah_item_sama_bertambah_qty(self):
        """Memastikan menambah item yang sama akan menambah qty, bukan duplikat."""
        self.keranjang.tambah_item(self.makanan, 1)
        self.keranjang.tambah_item(self.makanan, 2)
        items = self.keranjang.get_items()
        # Harus tetap 1 baris, qty jadi 3
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0][1], 3)

    def test_hitung_total_satu_item(self):
        """Memastikan total dihitung dengan benar untuk satu item."""
        self.keranjang.tambah_item(self.makanan, 2)
        # 12000 x 2 = 24000
        self.assertEqual(self.keranjang.hitung_total(), 24000)

    def test_hitung_total_beberapa_item(self):
        """Memastikan total dihitung dengan benar untuk beberapa item."""
        self.keranjang.tambah_item(self.makanan, 1)  # 12000
        self.keranjang.tambah_item(self.minuman, 2)  # 10000
        # Total = 22000
        self.assertEqual(self.keranjang.hitung_total(), 22000)

    def test_kosongkan(self):
        """Memastikan keranjang kosong setelah dikosongkan."""
        self.keranjang.tambah_item(self.makanan, 1)
        self.keranjang.kosongkan()
        self.assertTrue(self.keranjang.is_kosong())

    def test_total_keranjang_kosong_adalah_nol(self):
        """Memastikan total keranjang kosong adalah 0."""
        self.assertEqual(self.keranjang.hitung_total(), 0)


# ==================================================
# TEST CASE 4: MENGUJI CLASS KASIR (Polimorfisme)
# ==================================================
class TestKasir(unittest.TestCase):

    def setUp(self):
        self.kasir     = Kasir()
        self.keranjang = Keranjang()
        self.keranjang.tambah_item(Makanan("Nasi Rendang", 18000), 1)
        self.keranjang.tambah_item(Minuman("Es Teh", 5000), 1)

    @patch('builtins.input', return_value='25000')
    def test_proses_pembayaran_uang_cukup(self, mock_input):
        """Memastikan pembayaran berhasil jika uang cukup."""
        uang_bayar, kembalian = self.kasir.proses_pembayaran(self.keranjang)
        # Total = 23000, bayar 25000, kembalian 2000
        self.assertEqual(uang_bayar, 25000)
        self.assertEqual(kembalian, 2000)

    @patch('builtins.input', side_effect=['10000', '25000'])
    def test_proses_pembayaran_uang_kurang_lalu_cukup(self, mock_input):
        """Memastikan sistem meminta ulang jika uang kurang."""
        uang_bayar, kembalian = self.kasir.proses_pembayaran(self.keranjang)
        # Input pertama (10000) ditolak, input kedua (25000) diterima
        self.assertEqual(uang_bayar, 25000)
        self.assertEqual(kembalian, 2000)

    @patch('builtins.input', return_value='23000')
    def test_kembalian_nol(self, mock_input):
        """Memastikan kembalian 0 jika bayar pas."""
        uang_bayar, kembalian = self.kasir.proses_pembayaran(self.keranjang)
        self.assertEqual(kembalian, 0)

    @patch('builtins.input', return_value='50000')
    def test_cetak_struk_mengandung_info_penting(self, mock_input):
        """
        POLIMORFISME in Action:
        Memastikan struk berisi nama item dari Makanan DAN Minuman
        meskipun keduanya dipanggil dengan cara yang sama.
        """
        uang_bayar, kembalian = self.kasir.proses_pembayaran(self.keranjang)
        # Tangkap output print ke string
        output = io.StringIO()
        sys.stdout = output
        self.kasir.cetak_struk(self.keranjang, uang_bayar, kembalian)
        sys.stdout = sys.__stdout__
        struk = output.getvalue()

        self.assertIn("Nasi Rendang", struk)
        self.assertIn("Es Teh", struk)
        self.assertIn("50,000", struk)


# ==================================================
# ENTRY POINT
# ==================================================
if __name__ == '__main__':
    unittest.main(verbosity=2)