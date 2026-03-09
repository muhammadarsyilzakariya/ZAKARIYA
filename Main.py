# ==========================
# Login Masuk Museum Lukis 
# LOGIN + MENU CRUD SYSTEM 

username_benar = "Lukis123"
parssword_benar = "Mahal466"

data_pengunjung = []

#--------LOGIN------
def login():
    print("====LOGIN SISTEM====")
    while True:
        user = input("Username: ")
        pw = input("Password: ")

        if user == username_benar and pw == parssword_benar:
            print("Login Berhasil!! Welcome!!!\n")
            
            break

        else:
            print("Username atau Password salah\n")

login()

# -----Tambah Data----
def tambah_data():
    nama = input("Nama Pengunjung: ")
    umur = input("Umur Pengunjung: ")
    waktu = input("Tanggal dan Wakktu Pengunjung Masuk Museum Lukis: ")

    pengunjung = {
        "nama":nama,
        "umur":umur,
        "waktu":waktu
    }

    data_pengunjung.append(pengunjung)
    print("Data Pengunjung Berhasil di tambahkan")

# -----Lihat Data-----
def lihat_data():
    if len(data_pengunjung) == 0:
        print("Belum ada data pengunjung!!!")
    else:
        print("\n====DATA PENGUNJUNG MUSEUM LUKIS====")
        for i,s in enumerate(data_pengunjung,start=1):
            print(f"{i}.{s['nama']} - {s['umur']} - {s['waktu']}")

# -----Edit Data-----
def edit_data():
    lihat_data()
    if len(data_pengunjung) > 0 :
        nomor = int(input("Pilih nomor data: ")) -1
        if nomor <len(data_pengunjung):
            nama = input("Masukan nama pengunjung baru: ")
            umur = input("Masukan umur pengunjung baru: ")
            waktu = input("Masukan Tanggal dan waktu Baru: ")

            data_pengunjung[nomor]["nama"] = nama
            data_pengunjung[nomor]["umur"] = umur
            data_pengunjung[nomor]["waktu"] = waktu
            print("Data berhasill di perbarui!!!!")

#-----Hapus Data-----
def hapus_data():
    lihat_data()
    if len(data_pengunjung) > 0:
        nomor = int(input("pilih nomor yang ingin dihapus!!"))-1
        if nomor<len(data_pengunjung):
            data_pengunjung.pop(nomor)
            print("Data berhasil dihapus!!")
#-----MENU-----
def menu():
    while True:
        print("\n=====MENU UTAMA =====")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Logout/Keluar")
        
        pilih = input("Pilih Menu: ")

        if pilih == "1":
           tambah_data()
        elif pilih == "2":
           lihat_data()
        elif pilih == "3":
           edit_data()
        elif pilih == "4":
           hapus_data()
        elif pilih == "5":
           print("Berhasil logout!!!.")
           break
    
    
        else:
           print("Menu tidak tersedia!!")

#-----PROGRAM UTAMA-----

menu()

print("Program Selesai.")

    

