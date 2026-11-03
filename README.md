## PROJECT AKHIR DASAR PEMROGRAMAN; SISTEM DONASI ONLINE.

### Kelompok A1 (DONIFY) :
|**Nama**|**Kontribusi**|**Bagian**|
|---|---|---|
|AWANG FARID AL BUHARI (2609116003)|Konsep, Coding|	1.	Referensi konsep program<br> 2.	Coding |
|MUHAMMAD IHSAN (2609116009)|Coding, Pengecekan|	1.	Coding Halaman Utama,   dan User<br> 2.	Pengecekan Bug dan Error|
|JIHANUN SYAM NAFI'AH (2609116017)|Laporan|	1.	Konsep dan penyusunan Laporan |
|MUTHIARA MAY LISTA (2609116020)|Flowchart, Pengecekan|	1.	 Penyusun Alur Flowchart<br> 2.	Pengecekan Laporan|
<br>


## 📝 Deskripsi Proyek Akhir Dasar Pemrograman
**DONIFY** adalah sebuah sistem atau platform manajemen donasi digital berbasis CLI/aplikasi yang dirancang untuk mempermudah proses penggalangan dana, penyaluran, serta transparansi laporan keuangan donasi kepada masyarakat luas. Aplikasi ini dibangun untuk menghubungkan para **Donatur** (masyarakat/dermawan) yang ingin menyisihkan sebagian rezekinya dengan **Admin/Pengelola** yang bertugas memverifikasi, mengelola kampanye sosial (campaign), serta mencatat seluruh transaksi masuk dan keluar secara akurat.

## ⭐ Tujuan Proyek Akhir Dasar Pemrograman

1. **Meningkatkan Transparansi:** Menyediakan sistem pencatatan donasi yang transparan dan akuntabel sehingga setiap dana yang masuk terpapar jelas.
2. **Mempermudah Akses Berdonasi:** Memberikan kemudahan bagi donatur untuk memilih kampanye sosial yang ingin didukung secara cepat dan efisien.
3. **Efisiensi Pengelolaan Admin:** Membantu pihak pengelola dalam memvalidasi bukti transfer, mengelola data kampanye, serta menghasilkan laporan rekapitulasi dana secara otomatis.


## 👨‍💻Fitur untuk Admin:
1. Login Admin – Masuk ke sistem menggunakan akun admin.
2. CRUD Kampanye – Melihat, menambahkan, mengubah, dan menghapus kampanye donasi.
3. Riwayat Transaksi – Melihat seluruh riwayat transaksi donasi dari semua donatur.
4. Laporan Donasi – Menampilkan total donasi masuk, jumlah transaksi, dan kampanye unggulan.


## 🙇‍♀️Fitur untuk Donatur (User):
1. Registrasi dan Login – Membuat akun baru dan masuk ke sistem menggunakan username dan password.
2. Lihat Kampanye – Melihat daftar kampanye donasi yang tersedia beserta target dan persentase dana terkumpul.
3. Cek Saldo – Melihat jumlah saldo yang dimiliki.
4. Top Up Saldo – Menambahkan saldo sesuai pilihan nominal yang ada.
5. Donasi – Menyalurkan donasi ke kampanye yang tersedia menggunakan saldo akun.
6. Invoice Donasi – Mendapatkan bukti transaksi.
7. Riwayat Donasi – Melihat daftar transaksi donasi yang pernah dilakukan.


## 💻Tools & Library:
1. Python – Bahasa pemrograman utama.
2. JSON – Tempat penyimpanan database akun pengguna, kampanye, dan transaksi.
3. PrettyTable – Menampilkan data kampanye dan riwayat transaksi dalam tabel yang rapi.
4. pwinput – Menyembunyikan input password saat proses registrasi dan login.
5. os – Mengelola tampilan terminal, termasuk membersihkan layar.
6. time – Mengatur jeda program dan mencatat waktu transaksi donasi.
7. try-except – Menangani kesalahan seperti file tidak ditemukan, input tidak valid, dan pembagian dengan nol.
8. Dictionary dan List – Mengelola data pengguna, kampanye, serta transaksi.
9. Function – Membagi program menjadi beberapa fungsi agar lebih terstruktur.
<br>


## A. Flowchart

**1. Flowchart Menu Utama**

<img width="6144" height="4932" alt="Fc_MenuUtama" src="https://github.com/user-attachments/assets/bf5d1768-5ffe-4a18-a173-7977dd35eab5" /><br>
Penjelasan:<br>
Program dimulai dari Start, lalu sistem menampilkan Menu Utama yang berisi pilihan Login, Registrasi, dan Keluar. Jika memilih Login, pengguna memasukkan username, password, dan role untuk dicocokkan dengan data pada users.json, kemudian diarhkan ke Menu Admin atau Menu User sesuai rolenya. Jika memilih Registrasi, pengguna membuat akun baru yang disimpan ke file JSON, lalu sistem kembali ke Menu Utama. Pilihan Keluar akan mengakhiri program, sedangkan input yang kosong atau tidak valid akan ditolak dan pengguna dikembalikan ke Menu Utama.
<br>

**2. Flowchart Menu Admin**

<img width="9060" height="7004" alt="Fc_MenuAdmin" src="https://github.com/user-attachments/assets/df7539bc-1fac-4759-a7a7-93bfa1401746" /><br>
Penjelasan:<br>
Setelah masuk ke Menu Admin, sistem menampilkan tujuh pilihan menu, yaitu Lihat Kampanye, Tambah Kampanye, Ubah Kampanye, Hapus Kampanye, Riwayat Transaksi, Laporan Singkat, dan Logout. Pada Lihat Kampanye, sistem memuat data dari file kampanye.json dan menampilkannya kepada admin. Pada Tambah Kampanye, admin memasukkan nama serta target donasi yang akan divalidasi terlebih dahulu agar tidak kosong, lalu data kampanye baru disimpan ke file JSON. Pada Ubah Kampanye, admin memilih kampanye berdasarkan ID dan memasukkan data baru yang mengantikan data lama, sedangkan pada Hapus Kampanye, admin memasukkan ID kampanye dan sistem meminta konfirmasi sebelum data dihapus dari file JSON. Riwayat Transaksi menampilkan data dari file transaksi.json, sementara Laporan Singkat menyajikan total donasi masuk, jumlah transaksi, dan kampanye unggulan. Pilihan Logout mengembalikan admin ke Menu Utama, dan setiap proses yang telah selesai akan kembali ke Menu Admin, sedangkan input yang tdak valiid atau kosong akan ditolak dan admin diminta memilih ulang.
<br>

**3. Flowchart Menu User**

<img width="8252" height="7172" alt="Fc_MenuUser" src="https://github.com/user-attachments/assets/25e27b15-ba2b-4b3d-a575-917f53cecf83" /><br>
Penjelasan:<br>
Setelah masuk ke Menu User, sistem menampilkan pilihan menu yang terdiri dari Lihat Kampanye, Cek Saldo, Top Up Saldo, Donasi, Invoice, dan Logout. Pada pilihan Lihat Kampanye, sistem memuat data dari file kampanye.json lalu menampilkannya kepada pengguna, sedangkan pada pilihan Cek Saldo, sistem memuat data akun dari Login.json dan menampilkan saldo yang dimiliki. Selanjutnya, pada pilihan Top Up Saldo, pengguna memilih nominal yang tersedia, lalu sistem memvalidasinya dan menambahkan saldo ke data akun jika input benar. Pada pilihan Donasi, pengguna memilih kampanye berdasarkan ID dan memasukkan nominal donasi, kemudian sistem memeriksa apakah saldo cukup serta nominalnya valid sebelum mencatat transaksi ke transaksi.json. Pilihan Invoice berfungsi menampilkan bukti transaksi yang telah dilakukan, sedangkan Logout mengembalikan pengguna ke Menu Utama. Setiap proses yang selesai akan kembali ke Menu User, di mana input yang kosong atau tidak valid akan ditolak sehingga pengguna diminta untuk memilih ulang.
<br>


## B. Output Program

<img width="214" height="105" alt="1menuutama" src="https://github.com/user-attachments/assets/c9760eaf-3719-4cbc-bccd-45beae98b8eb" />

Di atas merupakan output pertama sistem yang menampilkan menu pilihan dimana akan menentukan login sebagai User atau Admin 

**Admin DONIFY**

1. Login DONIFY
<img width="223" height="85" alt="loginadmin" src="https://github.com/user-attachments/assets/424d1c60-37c8-4556-9cfa-47aa0079c867" />

Ini merupakan tampilan ketika memilih menu 1 yaitu Login, disini login sebagai Admin. Ketika login akan diminta memasukan username dan password, jika password benar maka akan diarahkan ke output selanjutnya namun jika password salah akan diminta memasukkan password lagi dengan kesempatan percobaan tersisa 2 kali.

2. Menu Admin
<img width="211" height="170" alt="2menuadmin" src="https://github.com/user-attachments/assets/5d3df7ec-cec4-45eb-802e-9ac28ae70415" />

Berikut adalah tampilan menu admin ketika berhasil menginput password dengan benar.  Disini sistem menampilkan pilhan menu kepada admin dan admin diminta memasukkan pilihan.

3. Lihat Kampanye
<img width="642" height="240" alt="3adminuserlihat" src="https://github.com/user-attachments/assets/865b38a0-b41f-4a1a-bc9c-8b458a6d3677" />

Ini tampilan menu Lihat Kampanye dimana output sistem kali ini menampilkan data kampanye yang sekarang atau yang sudah ada dengan menggunakan tabel rapi.

4. Tambah Kampanye
<img width="355" height="132" alt="4tambahadmin" src="https://github.com/user-attachments/assets/e0f7df0e-cd59-4130-a13b-91c556aaa0e2" />

Di menu kali ini Admin bisa menambah data kampanye baru namun sistem meminta Admin untuk menginput nama kampanye, kategori kampanye, dan target donasi, Apabila semua data kampanye baru sudah di input oleh admin, maka sistem akan menampilkan Kampanye berhasil ditambahkan dan kembali ke menu.

5. Ubah Kampanye
<img width="732" height="321" alt="5ubahadmin" src="https://github.com/user-attachments/assets/3000fcac-6083-4881-afe4-e4d55caab7c5" />

Pada menu ini Admin bisa mengubah data kampanye dengan sistem menampilkan data kampanye terbaru lalu admin diminta untuk memasukkan ID Kampanye yang ingin diubah, nama kampanye baru, dan target donasi baru. Jika semua data yang diminta sistem di input dengan sesuai maka sistem Kampanye berhasil diubah dan data akan terubah juga.

6. Hapus Kampanye
<img width="653" height="303" alt="6hapusadmin" src="https://github.com/user-attachments/assets/814f35af-00ab-43fb-a4b2-5db9113a019f" />

Sesuai namanya, di menu ini Admin bisa menghapus data kampanye yang tersedia dan data kampanye ditampilkan disini oleh karena itu Admin bisa memilih data yang dihapus. Sistem meminta Admin menginput ID Kampanye yang ingin dihapus, lalu sistem akan menanyakan apakah yakin ingin menghapus, jika "y" data berhasil dihapus dan sistem menampilkan Kampanye dihapus.

7. Riwayat Semua Transaksi
<img width="623" height="305" alt="7riwayatadmin" src="https://github.com/user-attachments/assets/ff994a98-116e-4c6b-8f88-b98358d61ff7" />

Di menu ini sistem menampilkan semnua Riwayat Transaksi yang dilakukan dengan menggunakan PrettyTable sehingga table yang ditampilkan di output rapi dan bagus

8. Laporan Ringkas
<img width="551" height="112" alt="8laporanadmin" src="https://github.com/user-attachments/assets/d84409e0-ead4-4469-940c-db63a0d3a47a" />

Pada menu 6 ini sistem menampilkan Laporan Ringkas dari data kampanye yang terdiri dari Total donasi masuk, jumlah transaksi, dan kampanye unggulan.


**User DONIFY**

Disini akan membahas pilihan menu jika login sebagai User

1. Registrasi Akun Baru (menu ke-2)
<img width="262" height="115" alt="14menuregis" src="https://github.com/user-attachments/assets/6343a2df-0e89-49ee-b3ed-9e435bf82f13" />

Menu registrasi akun baru ini hanya ada di menu User yaitu di pilihan menu ke 2 dimana disini user akan diminta untuk menginput username dan password. Jika sudah maka registrasi berhasil dan sistem meminta User untuk Login.

2. Login DONIFY
<img width="242" height="73" alt="login" src="https://github.com/user-attachments/assets/125bc184-e495-4e0c-9318-3ed63cc40ebc" />

Di menu Login, User diminta menginput Username dan Password yang sudah tersimpan di data. Jika Username dan Password yang diinput tidak tersedia di data maka User harus registrasi akun baru. Karena menu Login hanya bisa di akses dengan menggunakan Username dan Password dari data yang tersimpan.

3. Menu Donatur
<img width="253" height="150" alt="9menuuser" src="https://github.com/user-attachments/assets/8af853c5-4854-454a-8aa0-3ab2b6a00afe" />

Jika sudah berhasil Login, sistem menampilkan menu pilihan User atau Donatur, dimana menu Donatur ini terdiri dari Lihat Kampanye, Cek Saldo, Top Up Saldo, Donasi, Riwayat Donasi Saya, dan Logout. Sistem diminta unbtuk memasukkan pilihan menu yang ingin di akses.

4. Lihat Kampanye
<img width="642" height="240" alt="3adminuserlihat" src="https://github.com/user-attachments/assets/802d1415-e1e1-4a4e-9a4b-6bbce41e74fd" />

Menu pertama yaitu Lihat Kampanye, disini 

5. Cek Saldo
<img width="250" height="57" alt="10ceksaldo" src="https://github.com/user-attachments/assets/86e8ff98-6401-434f-a24d-2b668506e9ec" />

6. Top Up Saldo
<img width="323" height="205" alt="11topup" src="https://github.com/user-attachments/assets/13ecb13d-96b5-4377-923a-ded6b52f4575" />

7. Donasi Kampanye
<img width="332" height="237" alt="12donasi" src="https://github.com/user-attachments/assets/f10df0f5-73ba-457c-8d16-0a6c84f1b472" />

8. Riwayat Donasi
<img width="568" height="187" alt="13riwayatdonasi" src="https://github.com/user-attachments/assets/3febf29f-29ef-41de-9449-9523804f4078" />

0. Log Out
<img width="256" height="110" alt="15logout" src="https://github.com/user-attachments/assets/f12830f6-840f-4b4f-962e-f5a61a7d4b80" />
