# Melakukan import library untuk memudahkan kita
import numpy as np # Untuk Operasi Hitung nya (Determinan, mengubah array ke matrix, dan cek kemiripan float dengan 0)
from scipy.linalg import null_space# Untuk cetakan rumus nya (Eliminasi Gauss dalam kasus ini)

# Membuat fungsi untuk R3
def span_r3(a,b,c):
    # Membuat matrix dari vector list
    matrixR3 = np.column_stack((a,b,c))

    # Cek apakah determinan matrix = 0
    det_matrix = np.linalg.det(matrixR3)

    # Cek apakah Independen atau Dependen
    if np.isclose(det_matrix,0,atol=1e-8): # Toleransi abosolut nya 10 pangkat -8
        print(f"Himpunan vektor kemungkinan besar merupakan Dependen: determinan Matrix = {det_matrix}")
        
        # Cek null_space
        null_vector = null_space(matrixR3)
        
        # Output
        if null_vector.size > 0:
            # Normalisasi
            null_vector = null_vector / np.abs(null_vector).max()
            # Mengambil nilai kontanta
            print(f"Nilai C (Konstanta) dari tiap-tiap vector menggunakan \"Linear Combination\" yang memenuhi Ac = 0 adalah:")
            c1, c2, c3 = null_vector.flatten()
            print(f"c1: {c1:.2f}, c2: {c2:.2f}, c3: {c3:.2f}")
        else:
            print("Tidak ada konstanta Cn yang memenuhi")
    else:
        # Output
        print(f"Himpunan vektor adalah Independen: determinan Matrix = {det_matrix}")
        print(f"Tidak ada konstanta yang memenuhi kecuali c1 = c2 = c3 = 0")

def span_r2(a,b):
    # Membuat matrix dari vector list
    matrixR2 = np.column_stack((a,b))

    # Cek apakah determinan matrix = 0
    det_matrix = np.linalg.det(matrixR2)

    if np.isclose(det_matrix,0):
        print("Kemungkinan besar ini adalah Matrix Dependen:")

        # Mengambil nilai null
        null_vector = null_space(matrixR2)

        # Cek apakah ada Cn yang memenuhi
        if null_vector.size > 0:
            # Normalisasi
            null_vector = null_vector / np.abs(null_vector).max()

            # Ubah ke bentuk array 2D
            c1, c2 = null_vector.flatten()
            print(f"Nilai C (Konstanta) dari tiap-tiap vector menggunakan \"Linear Combination\" yang memenuhi Ac = 0 adalah:")
            print(f"c1: {c1:.2f}, c2: {c2:.2f}")
        else:
            print("Tidak ada konstanta Cn yang memenuhi") 
    else:
        # Output
        print(f"Himpunan vektor adalah Independen: determinan Matrix = {det_matrix}")
        print(f"Tidak ada konstanta yang memenuhi kecuali c1 = c2 = c3 = 0")


def main():
    # Contoh 1: Vektor independen
    a = [1, 2, 3]
    b = [4, 5, 0]
    c = [7, 8, 11]
    print("Contoh 1 (Independen):")
    span_r3(a, b, c)

    # Contoh 2: Vektor dependen (c = a + b)
    a = [1, 0, 0]
    b = [0, 1, 0]
    c = [1, 1, 0]
    print("\nContoh 2 (Dependen):")
    span_r3(a, b, c)

    # Contoh 3: Vektor dependen (c = a + b)
    print("\nContoh 3 (Dependen di R²):")
    a = [1, 2]
    b = [2, 4]
    span_r2(a, b)

if __name__ == "__main__":
    main()