#Angelina Febriani Madesen_F55123084
#Kelas: Informatika C

import numpy as np
import random
import time

# Mengatur seed nya
random.seed(42)
start_time_total = time.perf_counter()
 
angka_acak = random.sample(range(1, 101), 50)
print("Angka acak yang dihasilkan:", angka_acak)

# Mengimplementasikan Bubble Sort dengan metode divide and conquer
def urut_bubble_divide(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        kiri = urut_bubble_divide(arr[:mid])
        kanan = urut_bubble_divide(arr[mid:])
        
         
        return gabungkan_bubble(kiri, kanan)

def gabungkan_bubble(kiri, kanan):
    hasil = []
    while kiri and kanan:
        if kiri[0] < kanan[0]:
            hasil.append(kiri.pop(0))
        else:
            hasil.append(kanan.pop(0))
    hasil.extend(kiri)
    hasil.extend(kanan)
    return hasil

# Mengimplementasikan Quick Sort dengan metode divide and conquer
def urut_quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    kiri = [x for x in arr if x < pivot]
    tengah = [x for x in arr if x == pivot]
    kanan = [x for x in arr if x > pivot]
    return urut_quick(kiri) + tengah + urut_quick(kanan)

 
waktu_mulai_bubble = time.perf_counter()
hasil_urut_bubble = urut_bubble_divide(angka_acak.copy())
waktu_selesai_bubble = time.perf_counter()
hasilwaktububble = waktu_selesai_bubble - waktu_mulai_bubble
print("Hasil Bubble Sort (Divide and Conquer):", hasil_urut_bubble)
print("Waktu eksekusi Bubble Sort:",  hasilwaktububble, "detik")

waktu_mulai_quick = time.perf_counter()
hasil_urut_quick = urut_quick(angka_acak.copy())
waktu_selesai_quick = time.perf_counter()
hasilwaktuquick = waktu_selesai_quick - waktu_mulai_quick
print("Hasil Quick Sort:", hasil_urut_quick)
print("Waktu eksekusi Quick Sort:", hasilwaktuquick, "detik")

end_time_total = time.perf_counter()
print("Waktu eksekusi keseluruhan:", end_time_total - start_time_total, "detik")