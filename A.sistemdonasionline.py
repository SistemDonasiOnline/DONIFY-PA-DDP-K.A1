import json
import os
import time
from prettytable import PrettyTable
import pwinput

file_login = "login.json"
file_kampanye = "kampanye.json"
file_transaksi = "transaksi.json"

pilihan_top_up = (10000, 50000, 100000, 500000)

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def jeda():
    input("Tekan Enter untuk melanjutkan...")

def baca_file(nama_file):
    try:
        file = open(nama_file, "r")
        data = json.load(file)
        file.close()
        return data
    except FileNotFoundError:
        print("file", nama_file, "tidak ditemukan, membuat file baru...")
        return []

def simpan_file(nama_file, data):
    file = open(nama_file, "w")
    json.dump(data, file, indent=4)
    file.close()

def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Input tidak boleh kosong, silakan ulangi.")
        else:
            return teks

def input_angka(pesan):
    try:
        angka = int(input(pesan))
        return angka
    except ValueError:
        print("harus berupa angka!")
        return 0

def cari_user(data_user, username):
    for user in data_user:
        if user["username"] == username:
            return user
    return None

def registrasi(data_user):
    print("=== REGISTRASI USER BARU ===")
    username = input("Masukkan username: ")
    if len(username) < 4:
        print("Username harus memiliki minimal 4 karakter.")
        return False
    if cari_user(data_user, username) != None:
        print("Username sudah digunakan.")
        return False

    password = pwinput.pwinput("Masukkan password: ")
    if len(password) < 6:
        print("Password harus memiliki minimal 6 karakter.")
        return False

    user_baru = {"username": username, "password": password, "role": "user", "saldo": 0}
    data_user.append(user_baru)
    simpan_file(file_login, data_user)
    print("Registrasi berhasil. Silakan login.")
    return True

def login(data_user):
    percobaan = 0
    while percobaan < 3:
        print("=== LOGIN ===")
        username = input("Masukkan username: ")
        password = pwinput.pwinput("Masukkan password: ")

        user = cari_user(data_user, username)
        if user != None and user["password"] == password:
            print("Login berhasil. Selamat datang,", username)
            return user

        percobaan += 1
        print("Gagal, Sisa percobaan:", 3 - percobaan)

    print("Gagal login sudah 3x")
    return None

def cari_kampanye(data_kampanye, id_kampanye):
    for k in data_kampanye:
        if k["id"] == id_kampanye:
            return k
    return None

def tampil_kampanye(data_kampanye):
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Kategori", "Target", "Terkumpul", "Persen"]
    for k in data_kampanye:
        try:
            persen = k["terkumpul"] / k["target"] * 100
        except ZeroDivisionError:
            persen = 0
        tabel.add_row([k["id"], k["nama"], k["kategori"], k["target"], k["terkumpul"], str(round(persen, 1)) + "%"])
    print(tabel)
    
def tambah_kampanye(data_kampanye):
    print("===TAMBAH KAMPANYE BARU===")
    nama = input("Masukkan nama kampanye: ")
    kategori = input("masukkan kategori kampanye: ")
    target = input_angka("Masukkan target donasi: ")
    if nama == "" or target <= 0:
        print("Judul dan target tidak boleh kosong atau nol.")
        return data_kampanye

    id_baru = 1
    for k in data_kampanye:
        if k["id"] >= id_baru:
            id_baru = k["id"] + 1

    kampanye_baru = {
        "id": id_baru, 
        "nama": nama, 
        "kategori": kategori,
        "target": target, 
        "terkumpul": 0
        }
    data_kampanye.append(kampanye_baru)
    simpan_file(file_kampanye, data_kampanye)
    print("Kampanye berhasil ditambahkan.")
    return data_kampanye

def ubah_kampanye(data_kampanye):
    tampil_kampanye(data_kampanye)
    id_kampanye = input_angka("Masukkan ID kampanye yang ingin diubah: ")
    k = cari_kampanye(data_kampanye, id_kampanye)
    if k == None:
        print("Kampanye tidak ditemukan.")
        return data_kampanye

    diubah = False
    nama_baru = input("Masukkan nama kampanye baru (kosongkan jika tidak ingin mengubah): ").strip()
    if nama_baru != "":
        k["nama"] = nama_baru
        diubah = True

    target_baru = input_angka("Masukkan target donasi baru (0 jika tidak ingin mengubah): ")
    if target_baru > 0:
        if target_baru < k["terkumpul"]:
            print("Target baru tidak boleh kurang dari jumlah terkumpul.")
        else:
            k["target"] = target_baru
            diubah = True

    if diubah:
        simpan_file(file_kampanye, data_kampanye)
        print("Kampanye berhasil diubah.")
    else:
        print("Tidak ada perubahan yang disimpan.")
    
    return data_kampanye

def hapus_kampanye(data_kampanye):
    tampil_kampanye(data_kampanye)
    id_kampanye = input_angka("ID kampanye yang dihapus: ")
    k = cari_kampanye(data_kampanye, id_kampanye)
    if k == None:
        print("ID tidak ditemukan")
        return data_kampanye

    yakin = input("Yakin hapus "+ k["nama"] + "? (y/n): ")
    if yakin == "y":
        data_kampanye.remove(k)
        simpan_file(file_kampanye, data_kampanye)
        print("Kampanye dihapus.")
    else:
        print("Batal dihapus.")
    return data_kampanye

def laporan_ringkas(data_transaksi):
    print("=== LAPORAN RINGKAS ===")
    if len(data_transaksi) == 0:
        print("BELUM ADA TRANSAKSI!!!")
        return None

    try:
        total = 0
        nominal_per_kampanye = {}
        jumlah_per_kampanye = {}
        nama_kampanye = {}
        for t in  data_transaksi:
            id_k = t["id_kampanye"]
            nominal = int(t["nominal"])
            total += nominal
            nominal_per_kampanye[id_k] = nominal_per_kampanye.get(id_k, 0) + nominal
            jumlah_per_kampanye[id_k] = jumlah_per_kampanye.get(id_k, 0) + 1
            nama_kampanye[id_k] = t["nama_kampanye"]

        id_unggulan = max(nominal_per_kampanye, key=nominal_per_kampanye.get)

    except KeyError as e:
        print("Data Transaksi Tidak Lengkap, field", e, "TIDAK DITEMUKAN.")
        return None
    except(ValueError, TypeError):
        print("Data Transaksi Tidak valid, NOMINAL HARUS BERUPA ANGKA!!!")
        return None

    print("Total donasi masuk :", "Rp", total)
    print("Jumlah transaksi   :", len(data_transaksi))
    print("Kampanye unggulan  :", nama_kampanye[id_unggulan],
        "(Rp " + str(nominal_per_kampanye[id_unggulan]) + ", " + str(jumlah_per_kampanye[id_unggulan]) + "x donasi)")
    return total, len(data_transaksi), nama_kampanye[id_unggulan]


def top_up(user, data_user):
    print("=== TOP UP SALDO ===")
    print("Saldo kamu: Rp", user["saldo"])
    for i in range(len(pilihan_top_up)):
        print(str(i + 1) + ". Rp", pilihan_top_up[i])
    print("0. Batal")

    pilih = input_angka("Pilih nominal: ")
    if pilih == 0:
        print("Top up dibatalkan.")
        return False
    if pilih < 1 or pilih > len(pilihan_top_up):
        print("Pilihan tidak valid.")
        return False

    nominal = pilihan_top_up[pilih - 1]
    user["saldo"] += nominal
    simpan_file(file_login, data_user)
    print("Top up berhasil. Saldo sekarang: Rp", user["saldo"])
    return True

def cetak_invoice(transaksi, nama_kampanye, sisa_saldo):
    print("\n===== INVOICE DONASI =====")
    print("Waktu     :", transaksi["waktu"])
    print("Kode      :", transaksi["kode"])
    print("Donatur   :", transaksi["username"])
    print("Kampanye  :", nama_kampanye)
    print("Nominal   : Rp", transaksi["nominal"])
    print("Sisa saldo: Rp", sisa_saldo)
    print("==========================")

def donasi(user, data_user, data_kampanye, data_transaksi):
    tampil_kampanye(data_kampanye)
    id_kampanye = input_angka("ID kampanye yang ingin didonasi: ")
    k = cari_kampanye(data_kampanye, id_kampanye)
    if k == None:
        print("ID tidak ditemukan!")
        return False

    sisa_target = k["target"] - k["terkumpul"]
    if sisa_target == 0:
        print("Target kampanye ini sudah tercapai.")
        return False

    print("Saldo kamu: Rp", user["saldo"])
    nominal = input_angka("Nominal donasi: ")

    if nominal <= 0:
        print("Nominal harus lebih dari 0!")
        return False
    elif nominal > user["saldo"]:
        print("Saldo tidak cukup, silakan top up dulu.")
        return False
    elif nominal > sisa_target:
        print("Melebihi sisa target! Maksimal: Rp", sisa_target)
        return False

    user["saldo"] -= nominal
    k["terkumpul"] += nominal

    transaksi = {
        "username": user["username"],
        "kode": "TRX-" + str(len(data_transaksi) + 1),
        "nama_kampanye": k["nama"],
        "id_kampanye": k["id"],
        "nominal": nominal,
        "waktu": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    data_transaksi.append(transaksi)

    simpan_file(file_login, data_user)
    simpan_file(file_kampanye, data_kampanye)
    simpan_file(file_transaksi, data_transaksi)

    cetak_invoice(transaksi, k["nama"], user["saldo"])
    return True

def tampil_riwayat(data_transaksi, user):
    tabel = PrettyTable()
    if user["role"] == "admin":
        print("=== RIWAYAT SEMUA TRANSAKSI ===")
        tabel.field_names = ["kode", "Waktu", "Donatur", "Kampanye", "Nominal"]
    else:
        print("=== RIWAYAT DONASI SAYA ===")
        tabel.field_names = ["kode", "Waktu", "Kampanye", "Nominal"]

    ada = False
    for t in data_transaksi:
        if user["role"] == "admin":
            tabel.add_row([t["kode"], t["waktu"], t["username"], t["nama_kampanye"], t["nominal"]])
            ada = True
        elif t["username"] == user["username"]:
            tabel.add_row([t["kode"], t["waktu"], t["nama_kampanye"], t["nominal"]])
            ada = True

    if ada:
        print(tabel)
    else:
        print("Belum ada transaksi.")

def menu_admin(user, data_kampanye, data_transaksi):
    while True:
        bersihkan_layar()
        print("=== MENU ADMIN ===")
        print("1. Lihat Kampanye")
        print("2. Tambah Kampanye")
        print("3. Ubah Kampanye")
        print("4. Hapus Kampanye")
        print("5. Riwayat Semua Transaksi")
        print("6. Laporan Ringkas")
        print("0. Logout")
        pilih = input("Pilih: ")

        if pilih == "1":
            tampil_kampanye(data_kampanye)
        elif pilih == "2":
            data_kampanye = tambah_kampanye(data_kampanye)
        elif pilih == "3":
            data_kampanye = ubah_kampanye(data_kampanye)
        elif pilih == "4":
            data_kampanye = hapus_kampanye(data_kampanye)
        elif pilih == "5":
            tampil_riwayat(data_transaksi, user)
        elif pilih == "6":
            laporan_ringkas(data_transaksi)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")
        jeda()

def menu_user(user, data_user, data_kampanye, data_transaksi):
    while True:
        bersihkan_layar()
        print("=== MENU DONATUR ===", user["username"])
        print("1. Lihat Kampanye")
        print("2. Cek Saldo")
        print("3. Top Up Saldo")
        print("4. Donasi")
        print("5. Riwayat Donasi Saya")
        print("0. Logout")
        pilih = input("Pilih: ")

        if pilih == "1":
            tampil_kampanye(data_kampanye)
        elif pilih == "2":
            print("Saldo kamu: Rp", user["saldo"])
        elif pilih == "3":
            top_up(user, data_user)
        elif pilih == "4":
            donasi(user, data_user, data_kampanye, data_transaksi)
        elif pilih == "5":
            tampil_riwayat(data_transaksi, user)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")
        jeda()

def main():
    data_user = baca_file(file_login)
    data_kampanye = baca_file(file_kampanye)
    data_transaksi = baca_file(file_transaksi)
    if len(data_user) == 0:
        data_user = [{"username": "admin", "password": "admin123", "role": "admin", "saldo": 0}]
        simpan_file(file_login, data_user)

    while True:
        try:
            bersihkan_layar()
            print("Selamat datang di DONIFY!")
            print("1. Login")
            print("2. Registrasi")
            print("3. Keluar")
            pilih = input_teks("Pilih menu anda (1-3): ")

            if pilih == "1":
                user = login(data_user)
                if user != None:
                    if user["role"] == "admin":
                        menu_admin(user, data_kampanye, data_transaksi)
                    else:
                        menu_user(user, data_user, data_kampanye, data_transaksi)
                else:
                    jeda()
            elif pilih == "2":
                registrasi(data_user)
                jeda()
            elif pilih == "3":
                print("Terima kasih telah support Donify!")
                break
            else:
                print("Pilihan tidak valid.")
                time.sleep(1)

        except (KeyboardInterrupt, EOFError):
            print("\nKembali ke menu awal...")
            time.sleep(1)

main()