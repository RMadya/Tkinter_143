import tkinter as tk
from tkinter import messagebox

#Mendefinisikan fungsi yang akan dijalankan ketika tombol "Hasil Prediksi" ditekan. Fungsi ini bertanggung jawab untuk memvalidasi input dan menampilkan prediksi.
def prediksi_prodi():
     # Mengabaikan input nilai, selalu menampilkan "Teknologi Informasi"
    try: # Try except block memulai try untuk menangkap kesalahan yang mungkin terjadi saat proses input
        for entry in nilai_entries:
            #Mengonversi teks yang diambil menjadi integer.
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0-100.") #memriksa apakah nilai dalam rentang 0-100. jika tidak akan menampilkan error atau memicu 'valueError' dan menampillkan pesan yang sesuai.
        
        # Jika semua nilai valid, menampilkan hasil prediksi atau Jika semua nilai valid, mengatur nilai dari StringVar hasil untuk menampilkan "Prediksi prodi: Teknologi Informasi".
        hasil.set("Prediksi prodi: Teknologi Informasi")
    except ValueError as ve: #jika 'ValueError', menampilkan kotak pesan kesalahan dengan judul 'input error' dan pesan yang menjalankan input harus berupa angka 0-100
        messagebox.showerror("Input error", "Pastikan semua input adalah angka 0-100.")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")#membuat  judul jendela apk

# Memberikan Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10) #mengatur posisi dalam grid. dan menunjukkan posisi serta menunjukkan label mengambil dua kolom dan memberikan jarak vertikal

# Membuat input nilai mata pelajaran.membuat daftar kosong untuk menyimpan label dan entry. Kemudian loop untuk mengulangi 1-10 untuk membuat label dan entry untuk nilai mata pelajaran
#label untuk membuat label untuk setiap mapel dg teks yang sesuai dan menempatkannya di grid
#entry untuk membuat entry(input) untuk setiap mapel dan menampatkannya di grid
nilai_labels = []
nilai_entries = []
for i in range(1, 11):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i}:")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    nilai_labels.append(label)
    nilai_entries.append(entry)

# Memberikan Tombol untuk menghasilkan prediksi.'command' mengaitkan tombol dg fungsi presiksi_prodi, sehingga ketika tombol ditekan, fungsi ini akan dijalankan
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil prediksi
hasil = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil, font=("Arial", 12))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()