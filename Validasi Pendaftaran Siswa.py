nama = input("Masukkan Nama Siswa : ")
umur = int(input("Masukkan Umur : "))
nilai = float(input("Masukkan Nilai Ujian : "))

#Validasi nama 
if nama =="":
    print("Nama tidak boleh kosong")

# Validasi umur
elif umur < 15:
    print("Umur belum memenuhi syarat (minimal 15 tahun)")

# Validasi nilai
elif nilai < 0 or nilai > 100:
    print("Nilai tidak valid (harus antara 0 - 100)")

# Jika semua valid
else:
    print("Data valid")

    if nilai >= 75:
        print("Status: LULUS")
    else:
        print("Status: TIDAK LULUS")