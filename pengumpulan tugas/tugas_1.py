class RentalMotor:

    def __init__(self, nama_penyewa, jenis_motor, lama_sewa, harga_per_hari):
        self.nama_penyewa = nama_penyewa
        self.jenis_motor = jenis_motor
        self.lama_sewa = lama_sewa
        self.harga_per_hari = harga_per_hari
        self.total_biaya = 0

    def hitung_total(self):
        self.total_biaya = self.lama_sewa * self.harga_per_hari
        return self.total_biaya


    def tampilkan_data(self):
        print("===== DATA RENTAL MOTOR =====")
        print("Nama Penyewa   :", self.nama_penyewa)
        print("Jenis Motor    :", self.jenis_motor)
        print("Lama Sewa      :", self.lama_sewa, "hari")
        print("Harga per Hari :", self.harga_per_hari)
        print("Total Biaya    :", self.total_biaya)


    def kembalikan_motor(self):
        print(self.nama_penyewa, "telah mengembalikan motor", self.jenis_motor)



rental1 = RentalMotor("Andra Ahlam", "Honda Vario", 3, 100000)


rental1.hitung_total()
rental1.tampilkan_data()
rental1.kembalikan_motor()