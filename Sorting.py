import time

# Implementasi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Tukar elemen jika tidak berurutan
                swapped = True
        if not swapped:  # Jika tidak ada pertukaran, berhenti
            break

# Implementasi Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:  # Jika elemen hanya 1 atau kosong, kembalikan array
        return arr
    pivot = arr[len(arr) // 2]  # Pilih elemen tengah sebagai pivot
    left = [x for x in arr if x < pivot]  # Elemen yang lebih kecil dari pivot
    middle = [x for x in arr if x == pivot]  # Elemen yang sama dengan pivot
    right = [x for x in arr if x > pivot]  # Elemen yang lebih besar dari pivot
    return quick_sort(left) + middle + quick_sort(right)

# Daftar uji
A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # Daftar terbalik
B = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]  # Daftar hampir terurut

# Mengukur waktu Bubble Sort untuk A
start_time = time.perf_counter()
bubble_sort(A.copy())  # Gunakan salinan agar daftar asli tidak berubah
end_time = time.perf_counter()
bubble_sort_time_A = end_time - start_time

# Mengukur waktu Bubble Sort untuk B
start_time = time.perf_counter()
bubble_sort(B.copy())
end_time = time.perf_counter()
bubble_sort_time_B = end_time - start_time

# Mengukur waktu Quick Sort untuk A
start_time = time.perf_counter()
quick_sort(A.copy())
end_time = time.perf_counter()
quick_sort_time_A = end_time - start_time

# Mengukur waktu Quick Sort untuk B
start_time = time.perf_counter()
quick_sort(B.copy())
end_time = time.perf_counter()
quick_sort_time_B = end_time - start_time

# Menampilkan waktu eksekusi
print(f"Waktu Bubble Sort untuk A: {bubble_sort_time_A:.10f} detik")
print(f"Waktu Bubble Sort untuk B: {bubble_sort_time_B:.10f} detik")
print(f"Waktu Quick Sort untuk A: {quick_sort_time_A:.10f} detik")
print(f"Waktu Quick Sort untuk B: {quick_sort_time_B:.10f} detik")

# JAWABAN NO 2
# Pada kasus A : Ternyata penerapan Quick Sort lebih cocok dan lebih efektif karena kompleksitasnya lebih rendah dibanding Bubble Short.
# Pada kasus B : Ternyata Penerapan Bubble Short lebih efektif.