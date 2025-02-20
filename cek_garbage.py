import gc
import time
import os
import sys
from colorama import Fore,Style

# -------------------------- CLEAR TERMINAL DAN ANIMASI-------------------------- #
def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def loading(durasi):
    for _ in range(durasi):
        sys.stdout.write("🔄 ")
        sys.stdout.flush()
        time.sleep(1)
    print()
    return
# -------------------------- CLEAR TERMINAL DAN ANIMASI-------------------------- #

# -------------------------- CEK PANJANG TERMINAL (OPSIONAL) -------------------------- #
# lenght = os.get_terminal_size()
# print(lenght)
# -------------------------- CEK PANJANG TERMINAL (OPSIONAL) -------------------------- #



# -------------------------- JUDUL PROGRAM -------------------------- #
clear_terminal()
judul = "❤️ 🤍 Efisiensi Object 🤍❤️ ".upper()
print(judul.center(100,"🔹"))
# -------------------------- JUDUL PROGRAM -------------------------- #



# -------------------------- SEBELUM GC BERJALAN -------------------------- #
gc.disable() # menonaktifkan sementara
total_object_sebelum = len(gc.get_objects()) # melihat object terpakai
object_nonefisien_sebelum = sum(gc.get_count()) # ter-tracking di gc

print("Sebelum object terfilter: ", total_object_sebelum) # total object
print("Sebelum efisiensi object dijalankan: ",gc.get_count(),object_nonefisien_sebelum,"object terdeteksi  perlu di efisiensi") # tracking useless object
# -------------------------- SEBELUM GC BERJALAN -------------------------- #



# -------------------------- GC Berjalan -------------------------- #
start = time.perf_counter()
gc.enable() # aktifkan garbage collection
gc.collect() # efisiensi object berjalan
gc.set_threshold(70,10,5) # mengatur pembagian filter
loading(5)
end = time.perf_counter()
print(Fore.GREEN + f"GC selesai dalam {end - start:.2f} detik\n" + Style.RESET_ALL,end="-"*100)

total_object_sesudah = len(gc.get_objects()) # melihat object terpakai setelah efisiensi object
object_nonefisien_sesudah = sum(gc.get_count()) # tracking gc yang tidak efisien setelah efisiensi

print("\nSetelah object terfilter: ",total_object_sesudah)
print("Setelah efisiensi berjalan: ",gc.get_count(),object_nonefisien_sesudah, "Object")
# -------------------------- GC Berjalan -------------------------- #



# -------------------------- TRANSPARANSI EFISIENSI -------------------------- #
total_dibersihkan = total_object_sebelum - total_object_sesudah
print(total_dibersihkan,"Berhasil di efisiensi")
print(object_nonefisien_sebelum - total_dibersihkan,"Object masih diperlukan\n",end="-"*100)

print("\n📊 Statistik GC 📊")
stats = gc.get_stats()
for i, gen in enumerate(stats):
    print(f"Generasi {i}: {gen['collections']} kali GC, {gen['collected']} objek dibersihkan, {gen['uncollectable']} objek tidak bisa dibersihkan")
# -------------------------- TRANSPARANSI EFISIENSI -------------------------- #

# -------------------------- JIKA INGIN MELIHAT OBJECT YANG DIPAKAI (OPSIONAL) -------------------------- #
# terpakai = gc.get_objects()

# for i in terpakai: = # (len(gc.get_objects() jika transparan)
#     print(i)
# -------------------------- JIKA INGIN MELIHAT OBJECT YANG DIPAKAI (OPSIONAL) -------------------------- #