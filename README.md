PROJECT AKHIR DASAR PEMROGRAMAN; SISTEM DONASI ONLINE.

Kelompok A1 (DONIFY):
1. Awang Farid Al Buhari (2609116003)
2. Muhammad Ihsan (2609116009)
3. Jihanun Syam Nafi'ah (2609116017)
4. Muthiara May Lista (2609116020)
<br>


👨‍💻Fitur untuk Admin:
1. Login Admin – Masuk ke sistem menggunakan akun admin.
2. Kelola Kampanye – Menambahkan, mengubah, dan menghapus kampanye donasi.
3. Lihat Kampanye – Melihat daftar kampanye.
4. Riwayat Transaksi – Melihat seluruh riwayat transaksi donasi dari semua donatur.
5. Laporan Donasi – Menampilkan total donasi masuk, jumlah transaksi, dan kampanye unggulan.
<br>


🙇‍♀️Fitur untuk Donatur (User):
1. Registrasi dan Login – Membuat akun baru dan masuk ke sistem menggunakan username dan password.
2. Lihat Kampanye – Melihat daftar kampanye donasi yang tersedia beserta target dan persentase dana terkumpul.
3. Cek Saldo – Melihat jumlah saldo yang dimiliki.
4. Top Up Saldo – Menambahkan saldo sesuai pilihan nominal yang ada.
5. Donasi – Menyalurkan donasi ke kampanye yang tersedia menggunakan saldo akun.
6. Invoice Donasi – Mendapatkan bukti transaksi.
7. Riwayat Donasi – Melihat daftar transaksi donasi yang pernah dilakukan.
<br>


💻Tools:
1. Python – Bahasa pemrograman utama.
2. JSON – Tempat penyimpanan data akun pengguna, kampanye, dan transaksi.
3. PrettyTable – Menampilkan data kampanye dan riwayat transaksi dalam tabel yang rapi.
4. pwinput – Menyembunyikan input password saat proses registrasi dan login.
5. os – Mengelola tampilan terminal, termasuk membersihkan layar.
6. time – Mengatur jeda program dan mencatat waktu transaksi donasi.
7. try-except – Menangani kesalahan seperti file tidak ditemukan, input tidak valid, dan pembagian dengan nol.
8. Dictionary dan List – Mengelola data pengguna, kampanye, serta transaksi.
9. Function – Membagi program menjadi beberapa fungsi agar lebih terstruktur.
<br>



A. Flowchart

1. Flowchart Menu Utama
<img width="6144" height="4932" alt="Fc_MenuUtama" src="https://github.com/user-attachments/assets/bf5d1768-5ffe-4a18-a173-7977dd35eab5" /><br>
Penjelasan:<br>
Program dimulai dari Start, lalu sistem menampilkan Menu Utama yang berisi pilihan Login, Registrasi, dan Keluar. Jika memilih Login, pengguna memasukkan username, password, dan role untuk dicocokkan dengan data pada users.json, kemudian diarhkan ke Menu Admin atau Menu User sesuai rolenya. Jika memilih Registrasi, pengguna membuat akun baru yang disimpan ke file JSON, lalu sistem kembali ke Menu Utama. Pilihan Keluar akan mengakhiri program, sedangkan input yang kosong atau tidak valid akan ditolak dan pengguna dikembalikan ke Menu Utama.
<br>

2. Flowchart Menu Admin
<img width="9060" height="7004" alt="Fc_MenuAdmin" src="https://github.com/user-attachments/assets/df7539bc-1fac-4759-a7a7-93bfa1401746" /><br>
Penjelasan:<br>
Setelah masuk ke Menu Admin, sistem menampilkan tujuh pilihan menu, yaitu Lihat Kampanye, Tambah Kampanye, Ubah Kampanye, Hapus Kampanye, Riwayat Transaksi, Laporan Singkat, dan Logout. Pada Lihat Kampanye, sistem memuat data dari file kampanye.json dan menampilkannya kepada admin. Pada Tambah Kampanye, admin memasukkan nama serta target donasi yang akan divalidasi terlebih dahulu agar tidak kosong, lalu data kampanye baru disimpan ke file JSON. Pada Ubah Kampanye, admin memilih kampanye berdasarkan ID dan memasukkan data baru yang mengantikan data lama, sedangkan pada Hapus Kampanye, admin memasukkan ID kampanye dan sistem meminta konfirmasi sebelum data dihapus dari file JSON. Riwayat Transaksi menampilkan data dari file transaksi.json, sementara Laporan Singkat menyajikan total donasi masuk, jumlah transaksi, dan kampanye unggulan. Pilihan Logout mengembalikan admin ke Menu Utama, dan setiap proses yang telah selesai akan kembali ke Menu Admin, sedangkan input yang tdak valiid atau kosong akan ditolak dan admin diminta memilih ulang.
<br>

3. Flowchart Menu User
<img width="8252" height="7172" alt="Fc_MenuUser" src="https://github.com/user-attachments/assets/25e27b15-ba2b-4b3d-a575-917f53cecf83" /><br>
Penjelasan:<br>
Setelah masuk ke Menu User, sistem menampilkan pilihan menu yang terdiri dari Lihat Kampanye, Cek Saldo, Top Up Saldo, Donasi, Invoice, dan Logout. Pada pilihan Lihat Kampanye, sistem memuat data dari file kampanye.json lalu menampilkannya kepada pengguna, sedangkan pada pilihan Cek Saldo, sistem memuat data akun dari Login.json dan menampilkan saldo yang dimiliki. Selanjutnya, pada pilihan Top Up Saldo, pengguna memilih nominal yang tersedia, lalu sistem memvalidasinya dan menambahkan saldo ke data akun jika input benar. Pada pilihan Donasi, pengguna memilih kampanye berdasarkan ID dan memasukkan nominal donasi, kemudian sistem memeriksa apakah saldo cukup serta nominalnya valid sebelum mencatat transaksi ke transaksi.json. Pilihan Invoice berfungsi menampilkan bukti transaksi yang telah dilakukan, sedangkan Logout mengembalikan pengguna ke Menu Utama. Setiap proses yang selesai akan kembali ke Menu User, di mana input yang kosong atau tidak valid akan ditolak sehingga pengguna diminta untuk memilih ulang.
<br>

