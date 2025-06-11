import random
import time

# BAGIAN 1: MEMBUAT DATA PENJUALAN
def buat_data_penjualan():
    brand_hp = ["Samsung", "Apple", "Xiaomi", "OPPO", "Vivo","Realme", "Infinix", "Asus", "Advan", "Google"]
    data_penjualan = []
    
    for hari in range(1, 31):
        tanggal = f"2025-05-{hari:02d}"
        
        for brand in brand_hp:
            jumlah_terjual = random.randint(0, 50)
            data_satu_hari = {
                'tanggal': tanggal,
                'produk': brand,
                'jumlah_terjual': jumlah_terjual
            }
            data_penjualan.append(data_satu_hari)
    
    return data_penjualan

# BAGIAN 2: MENGHITUNG TOTAL PENJUALAN PER BRAND

def hitung_total_per_brand(data_penjualan):
    total_brand = {}

    for data in data_penjualan:
        brand = data['produk']
        jumlah = data['jumlah_terjual']
        if brand in total_brand:
            total_brand[brand] = total_brand[brand] + jumlah
        else:
            total_brand[brand] = jumlah
    list_brand = []
    for brand, total in total_brand.items():
        brand_data = {
            'produk': brand,
            'jumlah_terjual': total
        }
        list_brand.append(brand_data)
    
    return list_brand

# BAGIAN 3: ALGORITMA BUBBLE SORT
def bubble_sort(data):
    #Copy data
    data_copy = data.copy()
    
    jumlah_perbandingan = 0
    jumlah_pertukaran = 0
    
    n = len(data_copy)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            jumlah_perbandingan = jumlah_perbandingan + 1
            
            if data_copy[j]['jumlah_terjual'] < data_copy[j + 1]['jumlah_terjual']:
                temp = data_copy[j]
                data_copy[j] = data_copy[j + 1]
                data_copy[j + 1] = temp
                
                jumlah_pertukaran = jumlah_pertukaran + 1
    
    return data_copy, jumlah_perbandingan, jumlah_pertukaran

# BAGIAN 4: ALGORITMA INSERTION SORT

def insertion_sort(data):
    #Copy data
    data_copy = data.copy()
    
    jumlah_perbandingan = 0
    jumlah_pertukaran = 0
    
    for i in range(1, len(data_copy)):
        elemen_sekarang = data_copy[i]
        
        j = i - 1
        
        while j >= 0:
            jumlah_perbandingan = jumlah_perbandingan + 1
            
            if data_copy[j]['jumlah_terjual'] < elemen_sekarang['jumlah_terjual']:
                # Geser elemen ke kanan
                data_copy[j + 1] = data_copy[j]
                jumlah_pertukaran = jumlah_pertukaran + 1
                # Pindah ke kiri
                j = j - 1
            else:
                #udah bener
                break
        
        # Sisipkan elemen di posisi yang tepat
        data_copy[j + 1] = elemen_sekarang
    
    return data_copy, jumlah_perbandingan, jumlah_pertukaran

# BAGIAN 5: ALGORITMA MERGE SORT

#Variable global 
perbandingan_merge = 0
pertukaran_merge = 0

def merge_sort(data):

    #reset penghitungan
    global perbandingan_merge, pertukaran_merge
    perbandingan_merge = 0
    pertukaran_merge = 0
    
    data_copy = data.copy()
    
    merge_sort_rekursif(data_copy, 0, len(data_copy) - 1)
    
    return data_copy, perbandingan_merge, pertukaran_merge

def merge_sort_rekursif(data, kiri, kanan):

    # Jika masih ada elemen untuk dibagi
    if kiri < kanan:
        #titik tengah
        tengah = (kiri + kanan) // 2  # // artinya pembagian bulat
        
        # Bagi bagian kiri
        merge_sort_rekursif(data, kiri, tengah)
        
        # Bagi bagian kanan
        merge_sort_rekursif(data, tengah + 1, kanan)
        
        # Gabungkan kedua bagian
        gabung_data(data, kiri, tengah, kanan)

def gabung_data(data, kiri, tengah, kanan):

    global perbandingan_merge, pertukaran_merge
    
    #Copy untuk bagian kiri dan kanan
    bagian_kiri = data[kiri:tengah + 1].copy()
    bagian_kanan = data[tengah + 1:kanan + 1].copy()
    
    # Index untuk bagian kiri, kanan, dan data utama
    i = 0  # Index bagian_kiri
    j = 0  # Index bagian_kanan
    k = kiri  # Index untuk data utama
    
    # Gabungkan kedua bagian dengan membandingkan
    while i < len(bagian_kiri) and j < len(bagian_kanan):
        perbandingan_merge = perbandingan_merge + 1
        
        if bagian_kiri[i]['jumlah_terjual'] >= bagian_kanan[j]['jumlah_terjual']:
            data[k] = bagian_kiri[i]
            i = i + 1
        else:
            data[k] = bagian_kanan[j]
            j = j + 1
        pertukaran_merge = pertukaran_merge + 1
        k = k + 1
    
    # Menambahakan sisa elemen dari bagian kiri (jika ada)
    while i < len(bagian_kiri):
        data[k] = bagian_kiri[i]
        i = i + 1
        k = k + 1
        pertukaran_merge = pertukaran_merge + 1
    
    # Menambahakan  sisa elemen dari bagian kanan (jika ada)
    while j < len(bagian_kanan):
        data[k] = bagian_kanan[j]
        j = j + 1
        k = k + 1
        pertukaran_merge = pertukaran_merge + 1

# BAGIAN 6: FUNGSI UNTUK MENAMPILKAN RANKING

def tampilkan_ranking_penjualan(data_terurut):
    print("\n" + "=" * 45)
    print(f"|{' ' * 8}ORDER OF SMARTPHONE SALES{' ' * 9}|")
    print("=" * 45)
    print(f"|{'Order':<6}|{'Brand':<15}|{'Total Sales':<19}|")
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


# BAGIAN 7: FUNGSI UNTUK MENAMPILKAN HASIL
def tampilkan_hasil(hasil_sorting):
    print("\n"+"=" * 60)
    print(f"|{' ' * 12}SMARTPHONE SALES ANALYSIS RESULTS{' ' * 13}|")
    print("=" * 60)
    
    data_terurut = hasil_sorting[0]['data_terurut']
    
    # Brand dengan penjualan tertinggi dan terendah
    brand_tertinggi = data_terurut[0]
    brand_terendah = data_terurut[-1]
    
    # Tampilkan informasi penjualan
    print(f"{'|' + ' ' * 58 + '|'}")
    print(f"|{' ' * 21}SMARTPHONE SALES{' ' * 21}|")
    print(f"|{' ' * 58}|")
    print(f"| Highest: {brand_tertinggi['produk']:<15} ({brand_tertinggi['jumlah_terjual']:>3} unit) {' ' * 21}|")
    print(f"| Lowest : {brand_terendah['produk']:<15} ({brand_terendah['jumlah_terjual']:>3} unit) {' ' * 21}|")
    print(f"|{'_' * 58}|")
    
    tampilkan_ranking_penjualan(data_terurut)
    
    print(f"\n{'=' * 60}")
    print(f"|{'COMPARISON OF SORTING ALGORITHMS':<58}|")
    print(f"{'=' * 60}")
    print(f"|{'Algorithm':<15}|{'Time (ms)':<12}|{'Iterasi':<15}|{'Swap':<13}|")
    print(f"{'=' * 60}")
    
    for hasil in hasil_sorting:
        nama_algo = hasil['nama_algoritma']
        waktu = f"{hasil['waktu_eksekusi']:.4f}"
        perbandingan = hasil['jumlah_perbandingan']
        pertukaran = hasil['jumlah_pertukaran']
        
        print(f"|{nama_algo:<15}|{waktu:<12}|{perbandingan:<15}|{pertukaran:<13}|")
    
    print(f"{'=' * 60}")

# BAGIAN 8: FUNGSI UTAMA PROGRAM

def main():

    print("MULAI ANALISIS PENJUALAN SMARTPHONE")
    print("=" * 50)
    
    # pertukaran 1: Buat data penjualan
    print("Generating sales data...")
    data_penjualan = buat_data_penjualan()
    print("Generated 300 sales records")
    
    # pertukaran 2: Hitung total per brand
    print("Analyzing 10 smartphone brands")
    data_brand = hitung_total_per_brand(data_penjualan)
    
    # pertukaran 3: Test ketiga algoritma sorting
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
    
    #hasil bubble sort
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
    
    #Hasil insertion sort
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
    
    #Hasil merge sort
    hasil_merge = {
        'nama_algoritma': 'Merge Sort',
        'waktu_eksekusi': waktu_merge,
        'jumlah_perbandingan': perbandingan_merge_result,
        'jumlah_pertukaran': pertukaran_merge_result,
        'data_terurut': data_merge
    }
    hasil_semua_algoritma.append(hasil_merge)
    
    #Tampilkan hasil
    tampilkan_hasil(hasil_semua_algoritma)
    
    print(f"\nAnalysis completed successfully!")

# MENJALANKAN PROGRAM

if __name__ == "__main__":
    main()