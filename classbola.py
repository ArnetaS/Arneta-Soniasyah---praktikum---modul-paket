from KumpulanClass import Bola as b

def main():
    print("MENGHITUNG LUAS PERMUKAAN BOLA")
    r = float(input("Masukkan Jari - Jari: "))

    obj = b (r)
    lpb = obj.luaspermukaanBola()
    
    print("Luas Permukaan Bola= ", lpb)

if __name__ == "__main__":
    main()
