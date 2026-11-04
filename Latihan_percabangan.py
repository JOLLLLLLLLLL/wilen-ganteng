jml = int(input("Masukkan Jumlah Mahasiswa : "))

if 5 <= jml <= 10:
    tot = 0
    for i in range(jml):
        tot += int(input("Masukkan Nilai Mahasiswa : "))
    
    avg = tot / jml
    print(f"nilai rata-ratanya : {avg}")

    if avg >= 90: print("sangat bagus")
    elif avg >= 80: print("bagus")
    elif avg >= 70: print("cukup")
    else: print("remedial")
else:
    print("Jumlah mahasiswa harus antara 5 sampai 10!")