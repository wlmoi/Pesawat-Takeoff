    P S E U D O C O D E
1. Mulai
2. Import library matplotlib.pyplot sebagai plt
3. Import library numpy sebagai np

4. Inisialisasi variabel CekDataApakahSiap dengan nilai False

5. Selama CekDataApakahSiap bernilai False, lakukan langkah-langkah berikut:
   1. Minta pengguna untuk memasukkan titikdata, jamterbang, CL, dan CD
   2. Jika titikdata, jamterbang, CL, dan CD semuanya lebih besar dari 0, ubah nilai CekDataApakahSiap menjadi True
   3. Jika tidak, tampilkan pesan "Cek ulang data yang telah dimasukkan."

6. Setelah data valid diterima dari pengguna, buat array waktu dari 0 hingga jamterbang dengan jumlah elemen sebanyak titikdata

7. Hitung ketinggian pesawat selama takeoff dengan rumus (10000) * (waktu/(jamterbang/6))**2
8. Jika waktu > jamterbang/6 jam, set ketinggian pesawat menjadi 10000 meter
9. Buat array ketinggian pesawat selama terbang dengan nilai konstan 10000
10. Jika waktu < jamterbang/6 jam, set ketinggian pesawat sama dengan fase takeoff
11. Tambahkan variasi acak ke ketinggian selama fase terbang hanya pada interval waktu tertentu dengan mempengaruhi np.random.normal dengan CL dan CD
12. Hitung ketinggian pesawat selama landing dengan rumus (10000) * ((jamterbang-waktu)/(jamterbang/6))**2
13. Hitung ketinggian pesawat selama landing dengan rumus (10000) * ((jamterbang-waktu)/(jamterbang/6))**2
14. Jika waktu kurang dari jamterbang*5/6, set ketinggian pesawat sama dengan fase terbang

15. Definisikan fungsi plot_graph dengan parameter waktu dan Landing:
   1. Buat figur baru dengan ukuran 5x3
   2. Buat plot dengan waktu sebagai sumbu x dan Landing sebagai sumbu y
   3. Beri judul plot 'Grafik Ketinggian Pesawat Saat Penerbangan'
   4. Beri label sumbu x 'Waktu (jam)'
   5. Beri label sumbu y 'Ketinggian atas tanah (kilometer)'
   6. Tambahkan grid ke plot
   7. Tampilkan plot

16. Panggil fungsi plot_graph dengan parameter waktu dan Landing

17. Selesai



#    ALUR KERJA PROGRAM
1. **Impor library**: Kode ini mengimpor dua library Python, yaitu matplotlib.pyplot (untuk membuat grafik) dan numpy (untuk operasi matematika dan array).

2. **Input pengguna**: Kode ini meminta pengguna untuk memasukkan jumlah titik data yang akan digunakan dalam grafik, durasi penerbangan dalam jam, koefisien lift, dan koefisien drag. Jika data yang dimasukkan tidak valid (misalnya, jika salah satu nilai kurang dari atau sama dengan 0), kode ini akan meminta pengguna untuk memeriksa kembali data yang telah dimasukkan.

3. **Pembuatan array waktu**: Setelah menerima input yang valid dari pengguna, kode ini membuat array waktu dari 0 hingga jamterbang dengan jumlah elemen sebanyak titikdata.

4. **Menghitung ketinggian selama takeoff**: Kode ini menghitung ketinggian pesawat selama takeoff dengan asumsi percepatan konstan dan waktu takeoff adalah 1/6 dari waktu perjalanan. Setelah waktu lebih dari 1/6 jamterbang, ketinggian pesawat tetap di 10000 meter.

5. **Menghitung ketinggian selama terbang**: Setelah takeoff, pesawat terbang pada ketinggian konstan. Sebelum waktu lebih dari 1/6 jamterbang, ketinggian pesawat sama dengan fase takeoff.

6. **Modifikasi ketinggian dengan CL dan CD**: Bagian ini menambahkan variasi acak ke ketinggian selama fase terbang hanya pada interval waktu tertentu dengan mempengaruhi np.random.normal dengan CL dan CD. Variasi ini mewakili guncangan pada pesawat.

7. **Menghitung ketinggian selama landing**: Untuk landing, pesawat akan turun dengan perlambatan konstan. Sebelum waktu lebih dari 5/6 jamterbang, ketinggian pesawat sama dengan fase terbang.

8. **Membuat dan menampilkan grafik**: Bagian terakhir kode ini membuat grafik ketinggian terhadap waktu menggunakan matplotlib, memberikan judul dan label sumbu, menambahkan grid, dan menampilkan grafik.


    ! PERLU DIINGAT !

AND tidak dapat menggantikan & pada kode diatas.
Karena AND digunakan untuk kondisional (IF/ELSE DLL) sedangkan bitwise “&” dalam Python melakukan operasi AND pada representasi bit dari angka (010) pada matlab dll. Umpamanya gini, Operator “&” bekerja seperti kata “dan” dalam mtk, tetapi pada setiap bit dari angka. Misalnya, jika kamu punya dua angka 5 dan 3, dalam biner ditulis 101 dan 011. Operator “&” membandingkan setiap bit: jika kedua bitnya 1, hasilnya 1; jika tidak, hasilnya 0. Jadi, 101 & 011 menjadi 001, atau 1 dalam desimal.


______________________________________________________________________
Lalu,
Dalam kode ini, ekspresi (waktu/jamterbang/6) digunakan untuk menskalakan waktu selama fase takeoff pesawat.

Dalam konteks ini, asumsi yang dibuat adalah bahwa waktu takeoff adalah 1/6 dari total waktu penerbangan (jamterbang). Oleh karena itu, ekspresi (waktu/jamterbang/6) akan menghasilkan nilai antara 0 dan 1 selama fase takeoff, dan nilai lebih besar dari 1 setelah fase takeoff.

Nilai ini kemudian dikuadratkan dan dikalikan dengan 10000 untuk menghitung ketinggian pesawat selama takeoff. Dengan kata lain, ketinggian pesawat selama takeoff diasumsikan meningkat secara kuadratik dengan waktu, mencapai 10000 meter pada akhir fase takeoff. (kuadratrik == kurva)





```
`# This is formatted as code`
```

  #               TAHAPAN BERPIKIR KOMPUTASI

1. Modularisasi: Kode ini dibagi menjadi beberapa bagian atau modul yang berfungsi secara independen. Misalnya, bagian yang menghitung ketinggian selama takeoff, terbang, dan landing adalah modul (algoritma) yang berbeda.

2. Pengenalan Pola: Kode ini mengidentifikasi pola dalam data dan menggunakan pola tersebut untuk membuat simulasi. Misalnya, kode ini mengasumsikan bahwa pesawat akan terbang pada ketinggian konstan setelah takeoff dan sebelum landing, dan bahwa waktu takeoff dan landing adalah 1/6 dari total waktu penerbangan.

3. Abstraksi: Kode ini menggunakan abstraksi untuk menyederhanakan masalah. Misalnya, kode ini mengabstraksikan proses penerbangan pesawat menjadi tiga fase: takeoff, terbang, dan landing. Selain itu, kode ini juga mengabstraksikan pengaruh koefisien lift dan drag pada ketinggian pesawat selama penerbangan.

4. Algoritma: Kode ini menggunakan algoritma untuk menghitung ketinggian pesawat selama setiap fase penerbangan. Misalnya, kode ini menggunakan rumus fisika dasar (percepatan waktu kuadrat dll) untuk menghitung ketinggian pesawat selama takeoff dan landing (dengan asumsi percepatan konstan), dan menambahkan variasi acak ke ketinggian pesawat selama penerbangan untuk mensimulasikan efek dari koefisien lift dan drag

    __________________________________________________________


Penjelasan fungsi murni dari `np` dan `plt` yang digunakan dalam kode ini:

- `np.linspace(0, jamterbang, titikdata)`: Fungsi ini menghasilkan array yang berisi `titikdata` jumlah angka yang merata dari 0 hingga `jamterbang`.
Jadi dengan ini dapat menjelaskan bagaimana array waktu bisa dibuat:

    Array waktu dibuat menggunakan fungsi linspace dari library numpy. Fungsi ini menghasilkan array berisi sejumlah titik data yang merata dari nilai awal hingga nilai akhir.
    Dalam kode ini, nilai awal adalah 0 dan nilai akhir adalah jamterbang, yang merupakan durasi penerbangan dalam jam. Jumlah titik data yang dihasilkan adalah titikdata, yang merupakan jumlah titik data yang akan digunakan dalam grafik. Intinya... array waktu akan berisi titikdata jumlah nilai yang merata dari 0 hingga jamterbang. Misalnya, jika jamterbang adalah 6 dan titikdata adalah 3, maka array waktu pasti akan berisi [0, 3, 6]. (Dipisah berdasarkan titik data)


- `np.full_like(waktu, 10000)`: Fungsi ini menghasilkan array baru dengan dimensi dan tipe yang sama seperti array `waktu`, tetapi semua elemennya diisi dengan angka 10000.
- `np.random.normal(0, 20*(1 + CL)**3, size=len(waktu[(waktu >= jamterbang/8) & (waktu <= jamterbang*7/8)]))`: Fungsi ini menghasilkan array acak yang diambil dari distribusi normal dengan rata-rata 0 dan standar deviasi `20*(1 + CL)**3`. Ukuran array ditentukan oleh panjang array waktu pada interval tertentu.

Untuk fungsi `plt`:
- `plt.figure(figsize=(5,3))`: Fungsi ini membuat figur baru dengan ukuran 5x3 (lebar x tinggi dalam inci).
- `plt.plot(waktu, Landing)`: Fungsi ini membuat plot pada figur saat ini menggunakan array `waktu` sebagai sumbu x dan array `Landing` sebagai sumbu y.
- `plt.title('Grafik Ketinggian Pesawat Saat Penerbangan')`: Fungsi ini menetapkan judul untuk plot saat ini.
- `plt.xlabel('Waktu (jam)')` dan `plt.ylabel('Ketinggian atas tanah (kilometer)')`: Fungsi-fungsi ini menetapkan label untuk sumbu x dan y plot saat ini.
- `plt.grid(True)`: Fungsi ini menambahkan grid ke plot saat ini.
- `plt.show()`: Fungsi ini menampilkan plot saat ini. Jika tidak gunakan fungsi ini, plot tidak akan ditampilkan.


    ALUR PRESENTASI
1. **Pembukaan (1 menit)**
    - Salam pembuka
    - Perkenalan Anggota Kelompok (Jangan lupa NIM)
    - Tujuan presentasi: Membahas kode simulasi penerbangan pesawat tubes

2. **Isi Presentasi (7 menit)**
    - Bagian 1: Memahami Kode (2 menit)
        - Penjelasan tentang library yang digunakan: matplotlib.pyplot dan numpy
        - Penjelasan tentang input yang diperlukan: titik data, durasi penerbangan, koefisien lift, dan koefisien drag
    - Bagian 2: Proses Simulasi (3 menit)
        - Penjelasan tentang bagaimana array waktu dibuat (Numpy array!)
        - Jelaskan tentang bagaimana ketinggian selama takeoff, terbang, dan landing dihitung (Menggunakan rumus kuadrat, dll)
        - Jelaskan tentang bagaimana koefisien lift dan drag mempengaruhi ketinggian selama penerbangan (Dipengaruhi pada plot randomnya)
    - Bagian 3: Visualisasi Data (2 menit)
        - Penjelasan tentang bagaimana grafik ketinggian terhadap waktu dibuat dan ditampilkan

4. **Kesimpulan (1 menit)**
    - Lesson Learned (Jelasin inti dari program, merupakan pemanfaatan dari hal yang dipelajari baik dalam kelas (cth. if/else, while/for, array, dan def) maupun terkandung dalam library (array yang digunakan ialah numpy dan untuk membuat grafik pakai matplot), baru buat hikmah Bahwa Pemrograman sangat bermanfaat dalam kehidupan sehari-hari serta penerapannya dapat diilustrasikan dari projek sederhana ini)

5. **Tanya Jawab (20 detik)**
    - Membuka kesempatan untuk pertanyaan dari teman-teman (mungkin dari dosen tapi umumnya sunyi)

6. **Penutup (20 detik)**
    - Ucapan terima kasih kepada Dosen dan teman-teman sudah memperhatikan



