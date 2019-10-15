from KumpulanClass import TekomC as c

def main():
    jp = 15
    jl = 16

    obj = c (jp, jl)
    jumlah = obj.jumlahMahasiswa()

    print("MAHASISWA TEKOM C")
    print("Jumlah Perempuan\t: ", jp)
    print("Jumlah Laki-Laki\t: ", jl)
    print("Jumlah Mahasiswa\t: ", jumlah)


if __name__ == "__main__":
    main()
    
