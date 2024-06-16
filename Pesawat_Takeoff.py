# KAMUS
# titikdata   = int        : Jumlah titik data yang digunakan pada grafik
# jamterbang  = int        : Durasi pesawat bekerja dalam jam
# CL          = float      : Koefisien lift
# CD          = float      : Koefisien drag
# CekDataApakahSiap = boolean : Pembuat algoritma pengecekan
# waktu       = np.array   : list of float : Array waktu dari 0 hingga jamterbang dengan titikdata
# Takeoff     = np.array   : list of float : Array ketinggian pesawat selama takeoff
# Flying      = np.array   : list of float : Array ketinggian pesawat selama terbang
# Landing     = np.array   : list of float : Array ketinggian pesawat selama landing
# Program ini menggunakan if/else, while loop, Array dari numpy (Numpy membuat Array yang digunakan lebih efisien prosesnya dan fleksibel operasinya), dan fungsi def

# ALGORITMA
import matplotlib.pyplot as plt   # Impor library matplotlib.pyplot sebagai plt
import numpy as np                # Impor library numpy sebagai np

# Input data dari pengguna (titikdata, jamterbang, CL, CD harus >0), waktu input sekaligus melakukan pengecekan...
# CekDataApakahSiap
CekDataApakahSiap = False #Dia belum siap
while CekDataApakahSiap == False:
  titikdata = int(input("Jumlah titik data digunakan pada grafik (Bilangan Bulat): ")) # Menerima input titik data dari pengguna (Umumnya ratusan cth. 300)
  jamterbang = int(input("Durasi pesawat bekerja (jam): "))        # Menerima input waktu dari pengguna          (Asumsikan pesawat harus lebih dari 1)
  CL = float(input("Lift Coffiecient: "))                          # Menerima input koefisien lift dari pengguna (Umumnya 0.0-1.0)
  CD = float(input("Drag Coffiecient: "))                          # Menerima input koefisien drag dari pengguna (Umumnya 0.0-1.0)
  if titikdata>0 and jamterbang>0 and CL>=0 and CD>=0:
    CekDataApakahSiap = True # Dia sudah siap untuk dibuat plot/grafik nya
  else:
    print("Cek ulang data yang telah dimasukkan.")

# Waktu dalam jam
waktu = np.linspace(0, jamterbang, titikdata)        # Membuat array waktu dari 0 hingga jamterbang dengan titikdata

# Ketinggian dalam kilometer, asumsikan percepatan konstan dan waktu takeoff itu 1/6 dari waktu perjalanan
Takeoff = (10000) * (waktu/(jamterbang/6))**2  # Menghitung ketinggian pesawat selama takeoff
Takeoff[waktu > jamterbang/6] = 10000          # Setelah waktu > jamterbang/6 jam, ketinggian pesawat tetap di 10000 meter

# Setelah takeoff, pesawat terbang pada ketinggian konstan
Flying = np.full_like(waktu, 10000)                           # Membuat array dengan nilai konstan (np.full_like) 10000 (Letak dia selama terbang)
Flying[waktu < jamterbang/6] = Takeoff[waktu < jamterbang/6]  # Sebelum waktu > jamterbang/6 jam, ketinggian pesawat sama dengan fase takeoff

# Modifikasi bagian ini untuk mempengaruhi ketinggian dengan CL dan CD
Flying[(waktu >= jamterbang/8) & (waktu <= jamterbang*7/8)] += np.random.normal(0, 20*(1 + CL)**3, size=len(waktu[(waktu >= jamterbang/8) & (waktu <= jamterbang*7/8)]))
Flying[(waktu >= jamterbang/8) & (waktu <= jamterbang*7/8)] -= np.random.normal(0, 20*(1 + CD)**3, size=len(waktu[(waktu >= jamterbang/8) & (waktu <= jamterbang*7/8)]))
# Menambahkan variasi acak (ibaratnya letak pesawat berguncang) ke ketinggian selama fase terbang hanya pada interval waktu jamterbang/8 sampai jamterbang*7/8
# 20*(1 + CL atau 1 + CD)**3 bekerja sebagai penentu titik pesawat saat dia dipengaruhi koefisien

# Untuk landing, pesawat akan turun dengan perlambatan konstan
Landing = (10000) * ((jamterbang-waktu)/(jamterbang/6))**2          # Menghitung ketinggian pesawat selama landing
Landing[waktu < jamterbang*5/6] = Flying[waktu < jamterbang*5/6]    # Sebelum waktu >jamterbang*5/6 jam, ketinggian pesawat sama dengan fase terbang

def plot_graph(waktu, Landing):
    # Fungsi plot_graph
    # Membuat dan menampilkan plot ketinggian terhadap waktu menggunakan matplotlib.pyplot (Disetel manual oleh programmernya)
    plt.figure(figsize=(5,3))                                 # Membuat tempat kita bisa isi dengan grafik (5 x 3)
    plt.plot(waktu, Landing)                                  # Membuat grafik ketinggian terhadap waktu (x,y)
    plt.title('Grafik Ketinggian Pesawat Saat Penerbangan')   # Memberi judul grafik
    plt.xlabel('Waktu (jam)')                         # Memberi nama sumbu x di grafik
    plt.ylabel('Ketinggian atas tanah (kilometer)')   # Memberi nama sumbu y di grafik
    plt.grid(True)    #       Menambahkan grid pada grafik (Biar rapi)
    plt.show()        #       Menampilkan plot kita (Tunjukkin grafik)

#Menerapkan fungsi plot_graph
plot_graph(waktu,Landing)
