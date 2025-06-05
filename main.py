import random
import time

# ===============================================
# BAGIAN 1: MEMBUAT DATA PENJUALAN
# ===============================================

def buat_data_penjualan():
    """
    Fungsi untuk membuat data penjualan smartphone
    Return: list berisi data penjualan
    """
    # Daftar nama brand smartphone Indonesia
    brand_hp = ["Samsung", "Apple", "Xiaomi", "OPPO", "Vivo","Realme", "Infinix", "Asus", "Advan", "Google"]
    
    # List kosong untuk menyimpan semua data penjualan
    data_penjualan = []
    
    # Loop untuk 30 hari
    for hari in range(1, 31):  # 1 sampai 30
        # Format tanggal (contoh: 2025-05-01)
        tanggal = f"2025-05-{hari:02d}"  # :02d artinya 2 digit (01, 02, dst)
        
        # Loop untuk setiap brand HP
        for brand in brand_hp:
            # Buat angka acak untuk jumlah terjual (0-50)
            jumlah_terjual = random.randint(0, 50)
            
            # Buat dictionary untk menyimpan data
            data_satu_hari = {
                'tanggal': tanggal,
                'produk': brand,
                'jumlah_terjual': jumlah_terjual
            }
            
            # Tambahkan ke list data_penjualan
            data_penjualan.append(data_satu_hari)
    
    return data_penjualan

# ===============================================
# BAGIAN 2: MENGHITUNG TOTAL PENJUALAN PER BRAND
# ===============================================

def hitung_total_per_brand(data_penjualan):
    """
    Fungsi untuk menghitung total penjualan setiap brand
    Input: data_penjualan (list)
    Return: list berisi total penjualan per brand
    """
    # Dictionary untuk menyimpan total setiap brand
    total_brand = {}
    
    # Loop semua data penjualan
    for data in data_penjualan:
        brand = data['produk']           # Ambil nama brand
        jumlah = data['jumlah_terjual']  # Ambil jumlah terjual
        
        # Jika brand sudah ada di dictionary, tambahkan
        if brand in total_brand:
            total_brand[brand] = total_brand[brand] + jumlah
        # Jika brand belum ada, buat baru
        else:
            total_brand[brand] = jumlah
    
    # Ubah dictionary menjadi list untuk mudah diurutkan
    list_brand = []
    for brand, total in total_brand.items():
        brand_data = {
            'produk': brand,
            'jumlah_terjual': total
        }
        list_brand.append(brand_data)
    
    return list_brand

# ===============================================
# BAGIAN 3: ALGORITMA BUBBLE SORT
# ===============================================

def bubble_sort(data):
    """
    Algoritma Bubble Sort - Mengurutkan dari terbesar ke terkecil
    Input: data (list)
    Return: data yang sudah diurutkan, jumlah perbandingan, jumlah pertukaran
    """
    # Buat copy data agar data asli tidak berubah
    data_copy = data.copy()
    
    # Variable untuk menghitung operasi
    jumlah_perbandingan = 0
    jumlah_pertukaran = 0
    
    # Jumlah data
    n = len(data_copy)
    
    # Loop luar: sebanyak n kali
    for i in range(n):
        # Loop dalam: membandingkan data yang berdekatan
        for j in range(0, n - i - 1):
            # Tambah counter perbandingan
            jumlah_perbandingan = jumlah_perbandingan + 1
            
            # Bandingkan: jika data kiri lebih kecil dari data kanan
            if data_copy[j]['jumlah_terjual'] < data_copy[j + 1]['jumlah_terjual']:
                # Tukar posisi (swap)
                temp = data_copy[j]                    # Simpan data kiri
                data_copy[j] = data_copy[j + 1]       # Pindahkan data kanan ke kiri
                data_copy[j + 1] = temp               # Pindahkan data kiri ke kanan
                
                # Tambah counter pertukaran
                jumlah_pertukaran = jumlah_pertukaran + 1
    
    return data_copy, jumlah_perbandingan, jumlah_pertukaran

# ===============================================
# BAGIAN 4: ALGORITMA INSERTION SORT
# ===============================================

def insertion_sort(data):
    """
    Algoritma Insertion Sort - Mengurutkan dari terbesar ke terkecil
    Input: data (list)
    Return: data yang sudah diurutkan, jumlah perbandingan, jumlah pertukaran
    """
    # Buat copy data agar data asli tidak berubah
    data_copy = data.copy()
    
    # Variable untuk menghitung operasi
    jumlah_perbandingan = 0
    jumlah_pertukaran = 0
    
    # Loop mulai dari elemen kedua (index 1)
    for i in range(1, len(data_copy)):
        # Ambil elemen yang akan disisipkan
        elemen_sekarang = data_copy[i]
        
        # Mulai dari posisi sebelum elemen sekarang
        j = i - 1
        
        # Cari posisi yang tepat untuk menyisipkan
        while j >= 0:
            # Tambah counter perbandingan
            jumlah_perbandingan = jumlah_perbandingan + 1
            
            # Jika elemen di kiri lebih kecil dari elemen sekarang
            if data_copy[j]['jumlah_terjual'] < elemen_sekarang['jumlah_terjual']:
                # Geser elemen ke kanan
                data_copy[j + 1] = data_copy[j]
                # Tambah counter pertukaran
                jumlah_pertukaran = jumlah_pertukaran + 1
                # Pindah ke kiri
                j = j - 1
            else:
                # Sudah menemukan posisi yang tepat
                break
        
        # Sisipkan elemen di posisi yang tepat
        data_copy[j + 1] = elemen_sekarang
    
    return data_copy, jumlah_perbandingan, jumlah_pertukaran

# ===============================================
# BAGIAN 5: ALGORITMA MERGE SORT
# ===============================================

# Variable global untuk menghitung operasi merge sort
perbandingan_merge = 0
pertukaran_merge = 0

def merge_sort(data):
    """
    Algoritma Merge Sort - Mengurutkan dari terbesar ke terkecil
    Input: data (list)
    Return: data yang sudah diurutkan, jumlah perbandingan, jumlah pertukaran
    """
    # Reset counter
    global perbandingan_merge, pertukaran_merge
    perbandingan_merge = 0
    pertukaran_merge = 0
    
    # Buat copy data agar data asli tidak berubah
    data_copy = data.copy()
    
    # Panggil fungsi rekursif merge sort
    merge_sort_rekursif(data_copy, 0, len(data_copy) - 1)
    
    return data_copy, perbandingan_merge, pertukaran_merge

def merge_sort_rekursif(data, kiri, kanan):
    """
    Fungsi rekursif untuk merge sort
    Input: data, index kiri, index kanan
    """
    # Jika masih ada elemen untuk dibagi
    if kiri < kanan:
        # Cari titik tengah
        tengah = (kiri + kanan) // 2  # // artinya pembagian bulat
        
        # Bagi bagian kiri
        merge_sort_rekursif(data, kiri, tengah)
        
        # Bagi bagian kanan
        merge_sort_rekursif(data, tengah + 1, kanan)
        
        # Gabungkan kedua bagian
        gabung_data(data, kiri, tengah, kanan)

def gabung_data(data, kiri, tengah, kanan):
    """
    Fungsi untuk menggabungkan dua bagian yang sudah terurut
    Input: data, index kiri, tengah, kanan
    """
    global perbandingan_merge, pertukaran_merge
    
    # Buat copy untuk bagian kiri dan kanan
    bagian_kiri = data[kiri:tengah + 1].copy()
    bagian_kanan = data[tengah + 1:kanan + 1].copy()
    
    # Index untuk bagian kiri, kanan, dan data utama
    i = 0  # Index untuk bagian_kiri
    j = 0  # Index untuk bagian_kanan
    k = kiri  # Index untuk data utama
    
    # Gabungkan kedua bagian dengan membandingkan
    while i < len(bagian_kiri) and j < len(bagian_kanan):
        # Tambah counter perbandingan
        perbandingan_merge = perbandingan_merge + 1
        
        # Jika elemen kiri lebih besar atau sama
        if bagian_kiri[i]['jumlah_terjual'] >= bagian_kanan[j]['jumlah_terjual']:
            data[k] = bagian_kiri[i]
            i = i + 1
        else:
            data[k] = bagian_kanan[j]
            j = j + 1
        
        # Tambah counter pertukaran
        pertukaran_merge = pertukaran_merge + 1
        k = k + 1
    
    # Masukkan sisa elemen dari bagian kiri (jika ada)
    while i < len(bagian_kiri):
        data[k] = bagian_kiri[i]
        i = i + 1
        k = k + 1
        pertukaran_merge = pertukaran_merge + 1
    
    # Masukkan sisa elemen dari bagian kanan (jika ada)
    while j < len(bagian_kanan):
        data[k] = bagian_kanan[j]
        j = j + 1
        k = k + 1
        pertukaran_merge = pertukaran_merge + 1

# ===============================================
# BAGIAN 6: FUNGSI UNTUK MENAMPILKAN RANKING
# ===============================================

def tampilkan_ranking_penjualan(data_terurut):
    """
    Fungsi untuk menampilkan ranking penjualan smartphone
    Input: data_terurut (list berisi data yang sudah diurutkan)
    """
    print("\n" + "=" * 45)
    print(f"|{' ' * 8}RANKING PENJUALAN SMARTPHONE{' ' * 8}|")
    print("=" * 45)
    print(f"|{'Rank':<6}|{'Brand':<15}|{'Total Penjualan':<19}|")
    print("=" * 45)
    
    # Hitung total keseluruhan penjualan
    total_keseluruhan = sum(item['jumlah_terjual'] for item in data_terurut)
    
    # Tampilkan setiap brand dengan rankingnya
    for i, brand_data in enumerate(data_terurut, 1):
        nama_brand = brand_data['produk']
        total_penjualan = brand_data['jumlah_terjual']
        
        print(f"|{i:<6}|{nama_brand:<15}|{total_penjualan:<19}|")
    
    print("=" * 45)
    print(f"|{'TOTAL':<22}|{total_keseluruhan:<19}|")
    print("=" * 45)

# ===============================================
# BAGIAN 7: FUNGSI UNTUK MENAMPILKAN HASIL
# ===============================================

def tampilkan_hasil(hasil_sorting):
    """
    Fungsi untuk menampilkan hasil dalam bentuk tabel
    Input: hasil_sorting (list berisi hasil dari 3 algoritma)
    """
    print("\n"+"=" * 60)
    print(f"|{' ' * 12}HASIL ANALISIS PENJUALAN SMARTPHONE{' ' * 11}|")
    print("=" * 60)
    
    # Ambil data yang sudah diurutkan (semua algoritma hasilnya sama)
    data_terurut = hasil_sorting[0]['data_terurut']
    
    # Brand dengan penjualan tertinggi dan terendah
    brand_tertinggi = data_terurut[0]  # Elemen pertama = tertinggi
    brand_terendah = data_terurut[-1]  # Elemen terakhir = terendah
    
    # Tampilkan informasi penjualan
    print(f"{'|' + ' ' * 58 + '|'}")
    print(f"|{' ' * 19}PENJUALAN SMARTPHONE{' ' * 19}|")
    print(f"|{' ' * 58}|")
    print(f"| Tertinggi: {brand_tertinggi['produk']:<15} ({brand_tertinggi['jumlah_terjual']:>3} unit) {' ' * 19}|")
    print(f"| Terendah:  {brand_terendah['produk']:<15} ({brand_terendah['jumlah_terjual']:>3} unit) {' ' * 19}|")
    print(f"|{'_' * 58}|")
    
    # Tampilkan ranking lengkap penjualan smartphone
    tampilkan_ranking_penjualan(data_terurut)
    
    # Tampilkan tabel perbandingan algoritma
    print(f"\n{'=' * 60}")
    print(f"|{'PERBANDINGAN ALGORITMA SORTING':<58}|")
    print(f"{'=' * 60}")
    print(f"|{'Algoritma':<15}|{'Waktu (ms)':<12}|{'Perbandingan':<15}|{'Langkah':<13}|")
    print(f"{'=' * 60}")
    
    for hasil in hasil_sorting:
        nama_algo = hasil['nama_algoritma']
        waktu = f"{hasil['waktu_eksekusi']:.4f}"
        perbandingan = hasil['jumlah_perbandingan']
        langkah = hasil['jumlah_pertukaran']
        
        print(f"|{nama_algo:<15}|{waktu:<12}|{perbandingan:<15}|{langkah:<13}|")
    
    print(f"{'=' * 60}")

# ===============================================
# BAGIAN 8: FUNGSI UTAMA PROGRAM
# ===============================================

def main():
    """
    Fungsi utama yang menjalankan seluruh program
    """
    print("MULAI ANALISIS PENJUALAN SMARTPHONE")
    print("=" * 50)
    
    # Langkah 1: Buat data penjualan
    print("Generating sales data...")
    data_penjualan = buat_data_penjualan()
    print("Generated 300 sales records")
    
    # Langkah 2: Hitung total per brand
    print("Analyzing 10 smartphone brands")
    data_brand = hitung_total_per_brand(data_penjualan)
    
    # Langkah 3: Test ketiga algoritma sorting
    print("Testing Bubble Sort...")
    print("Testing Insertion Sort...")
    print("Testing Merge Sort...")
    
    # List untuk menyimpan hasil semua algoritma
    hasil_semua_algoritma = []
    
    # Test Bubble Sort
    waktu_mulai = time.perf_counter()  # Catat waktu mulai
    data_bubble, perbandingan_bubble, pertukaran_bubble = bubble_sort(data_brand)
    waktu_selesai = time.perf_counter()  # Catat waktu selesai
    waktu_bubble = (waktu_selesai - waktu_mulai) * 1000  # Konversi ke milidetik
    
    # Simpan hasil bubble sort
    hasil_bubble = {
        'nama_algoritma': 'Bubble Sort',
        'waktu_eksekusi': waktu_bubble,
        'jumlah_perbandingan': perbandingan_bubble,
        'jumlah_pertukaran': pertukaran_bubble,
        'data_terurut': data_bubble
    }
    hasil_semua_algoritma.append(hasil_bubble)
    
    # Test Insertion Sort
    waktu_mulai = time.perf_counter()
    data_insertion, perbandingan_insertion, pertukaran_insertion = insertion_sort(data_brand)
    waktu_selesai = time.perf_counter()
    waktu_insertion = (waktu_selesai - waktu_mulai) * 1000
    
    # Simpan hasil insertion sort
    hasil_insertion = {
        'nama_algoritma': 'Insertion Sort',
        'waktu_eksekusi': waktu_insertion,
        'jumlah_perbandingan': perbandingan_insertion,
        'jumlah_pertukaran': pertukaran_insertion,
        'data_terurut': data_insertion
    }
    hasil_semua_algoritma.append(hasil_insertion)
    
    # Test Merge Sort
    waktu_mulai = time.perf_counter()
    data_merge, perbandingan_merge_result, pertukaran_merge_result = merge_sort(data_brand)
    waktu_selesai = time.perf_counter()
    waktu_merge = (waktu_selesai - waktu_mulai) * 1000
    
    # Simpan hasil merge sort
    hasil_merge = {
        'nama_algoritma': 'Merge Sort',
        'waktu_eksekusi': waktu_merge,
        'jumlah_perbandingan': perbandingan_merge_result,
        'jumlah_pertukaran': pertukaran_merge_result,
        'data_terurut': data_merge
    }
    hasil_semua_algoritma.append(hasil_merge)
    
    # Langkah 4: Tampilkan hasil
    tampilkan_hasil(hasil_semua_algoritma)
    
    print(f"\nAnalysis completed successfully!")

# ===============================================
# MENJALANKAN PROGRAM
# ===============================================

# Cek apakah file ini dijalankan langsung (bukan di-import)
if __name__ == "__main__":
    main()  # Jalankan fungsi utama