from paket.KumpulanClass import Kotak as k

def main():
    print("MENGHITUNG VOLUME KOTAK")
    p = float(input("Masukkan Panjang: "))
    l = float(input("Masukkan Lebar  : "))
    t = float(input("Masukkan Tinggi : "))

    obj = k (p, l, t)
    volume = obj.hitungVolume()
    
    print("Volume: ", volume)

if __name__ == "__main__":
    main()
