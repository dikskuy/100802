# class alattulis (object):
#     def __init__(self,nama):
#         self.nama = nama
    
#     def barang (self, pensil, pulpen, penggaris, hargapensil, hargapulpen, hargapenggaris):
#         self.__hargapensil = hargapensil
#         self.__hargapulpen = hargapulpen
#         self.__hargapenggaris = hargapenggaris

#         self.__pensil = pensil
#         self.__pulpen = pulpen
#         self.__penggaris = penggaris
    
#     def cekbarang (self) :
#         print("-"*5,"Jumlah Barang","-"*5)
#         print(f"Pensil = {self.__pensil}") 
#         print(f"Pensil = {self.__pulpen}") 
#         print(f"Pensil = {self.__penggaris}") 
    
#     def cekharga (self) :
#         print("-"*5,"Harga Barang","-"*5)
#         print(f"Harga Pensil = {self.__hargapulpen}")
#         print(f"Harga Pensil = {self.__hargapenggaris}")
#         print(f"Harga Pensil = {self.__hargapensil}")
    
#     def __total (self) :
#         self.__totalpensil = self.__pensil * self.__hargapensil
#         self.__totalpulpen = self.__pulpen * self.__hargapulpen
#         self.__totalpenggaris = self.__penggaris * self.__hargapenggaris
#         self.__totalbarang = self.__pensil + self.__pulpen + self.__penggaris
#         self.__totalharga = self.__totalpensil + self.__totalpulpen + self.__totalpenggaris

#     def cekakhir (self):
#         self.__total()
#         print("-"*5,"Total","-"*5)
#         print(f"Total harga = {self.__totalharga}")
#         print(f"Total barang = {self.__totalbarang}")

# if __name__== "__main__":
#     Andika = alattulis("Andika")
#     Andika.barang(5, 5, 2, 1500, 2000, 5000)
#     Andika.cekbarang()
#     Andika.cekharga()
#     Andika.cekakhir()

