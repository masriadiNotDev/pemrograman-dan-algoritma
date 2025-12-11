# masriadi
#tuple 
Warna = ("merah",
        "kuning",
        "hijau")
print("list tuple  : ", Warna)
print("lem 1:", Warna[0]) #mncoba mngakses indks ke-1 , tupple tak bisa di ubah karena nilai tetap maka akan error
# ================= LIST =============== 
#List
hewan = ["beruk",
         "monyet",
         "orangutan"] # list bisa diubah hampir sama dgn dict tapi tak mempunyai simbol siku "["
print("Sebelum diubah:", hewan)

hewan[1] = "monyet"     # mengubah isi berdasarkan index atau posisi "[1]"
hewan.append("kucing")  # menambah nilai atau bisa juga mnggunakan input
print("setelah diubah:", hewan) # setelah append maka di nilai "kucing" ada 
#perbedaan tuple dan list adalah tuple tidak bisa di ubah sedangkan list bisa di ubah
