def Penyusutan():
    print()
    print("======== Sistem Perhitungan Depresiasi Aktiva Tetap ========")
    print()
    while True:
        try:
            bp = int(input("Masukkan Biaya Perolehan        : Rp."))
            nr = int(input("Masukkan Nilai Residu           : Rp."))
            ue = int(input("Masukkan Umur Ekonomis (Tahun)  : "))
        except ValueError:
            print()
            print("XXXXX Nilai yang anda masukkan salah! XXXXX")
            print()
            continue

        print()
        print("=== Validasi Nilai Input ===")
        print()
        print("Biaya Perolehan  : Rp.",bp)
        print("Nilai Residu     : Rp.",nr)
        print("Umur Ekonomis    :",ue," Tahun")
        print()
        val = str(input("Apakah data yang anda masukkan sudah benar (ya/tidak)?:"))

        if val == "tidak":
            return Penyusutan()
        elif val == "ya":
            hasil = (bp-nr)/ue
            print()
            print("=== Hasil Perhitungan Depresiasi ===")
            print()
            print("Rp.", hasil)
            break
        else:
            print()
            print("XXXXX Inputan anda salah! XXXXX")
            print()
            continue
           
Penyusutan()
