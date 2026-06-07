class gameCharacter:
    def __init__(self, nama, level):
        self.__nama = nama
        self.__level = level

    def get_name(self):
        return self.__nama
    
    def get_level(self):
        return self.__level

    def set_level(self, level):
        if level > 0:
            self.__level = level
        else:
            print("level tidak valid")

    def tampil_status(self):
        print(f"nama: {self.__nama}")
        print(f"level {self.__level}")

char1 = gameCharacter("sova", 10)

char1.tampil_status()
char1.set_level(15)
char1.tampil_status()

print("level:", char1.get_level())
print("nama :", char1.get_name())

