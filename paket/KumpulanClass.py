import math

class Kotak(object):
    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    def hitungVolume(self):
        return self.panjang * self.lebar * \
               self.tinggi

class TekomC(object):
    def __init__(self, jp, jl):
        self.jumlahperempuan = jp
        self.jumlahlakilaki = jl
    def jumlahMahasiswa(self):
        return self.jumlahperempuan + self.jumlahlakilaki

class Bola(object):
    def __init__(self, r):
        self.jarijari = r
    def luaspermukaanBola(self):
        return 4 * math.pi * self.jarijari * self.jarijari
        
