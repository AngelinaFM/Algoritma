#Angelina Febriani Madesen_F55123084
#Kelas : Informatika C

import numpy as np
import random
import time

# Mengatur seed nya  
random.seed(42)

start_time_total = time.perf_counter()

random_numbers = random.sample(range(1, 101), 50)
print("Angka acak yang dihasilkan:", random_numbers)

# Bagian ini untuk mempersiapkan data untuk Naive Bayes
X = np.array(random_numbers).reshape(-1, 1)  # Fitur
y = np.array([1 if x % 2 == 0 else 0 for x in random_numbers])  # 1 untuk genap, 0 untuk ganjil

# untuk mengimplementasi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# untuk mengimplementasi Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


start_time_bubble = time.perf_counter()
sorted_bubble = bubble_sort(random_numbers.copy())
end_time_bubble = time.perf_counter()
print("Hasil Bubble Sort:", sorted_bubble)
print("Waktu eksekusi Bubble Sort:", end_time_bubble - start_time_bubble, "detik")

start_time_quick = time.perf_counter()
sorted_quick = quick_sort(random_numbers.copy())
end_time_quick = time.perf_counter()

print("Hasil Quick Sort:", sorted_quick)
print("Waktu eksekusi Quick Sort:", end_time_quick - start_time_quick, "detik")
print("Klasifikasi (0: ganjil, 1: genap):", y)

end_time_total = time.perf_counter()
print("Waktu eksekusi keseluruhan:", end_time_total - start_time_total, "detik")