"""Demonstrasi Operasi Aritmatika pada Bilangan Biner"""

# Mendefinisikan variabel biner dengan komentar desimal
x = 0b1100100  # 100 dalam desimal
y = 0b110010  # 50 dalam desimal
z = 0b101  # 5 dalam desimal

print("=== NILAI AWAL VARIABEL ===")
print(f"x = {x} (biner: {bin(x)})")
print(f"y = {y} (biner: {bin(y)})")
print(f"z = {z} (biner: {bin(z)})")
print("-" * 50)


# Fungsi untuk mengonversi desimal ke biner
def to_binary(n):
    if n == 0:
        return "0b0"
    is_negative = n < 0
    if is_negative:
        n = -n  # Ubah ke positif untuk konversi
    binary = bin(n)[2:]  # Hilangkan prefiks '0b'
    return "-0b" + binary if is_negative else "0b" + binary


# ========= EKSPRESI A: (x - y) / z =========
print("\n=== EKSPRESI A: (x - y) / z ===")
print("Langkah-langkah perhitungan:")

# Langkah 1: Kurangkan y dari x
a_numerator = x - y
print(f"1. x - y = {x} - {y} = {a_numerator}")
print(f"   Dalam biner: {bin(x)} - {bin(y)} = {bin(a_numerator)}")

# Langkah 2: Bagi hasil dengan z
a_result = a_numerator / z
print(f"2. (x - y) / z = {a_numerator} / {z} = {a_result}")

# Tampilkan hasil pembulatan dan konversi ke biner
a_rounded = round(a_result)
a_int = int(a_result)

print("\nHasil Ekspresi a:")
print(f"Desimal (tidak dibulatkan): {a_result}")
print(f"Desimal (dibulatkan ke integer terdekat): {a_rounded}")
print(f"Desimal (dikonversi ke integer): {a_int}")
print(f"Biner (dari konversi ke integer): {to_binary(a_int)}")
print(
    f"Apakah hasil adalah bilangan bulat? {'Ya' if a_result.is_integer() else 'Tidak'}"
)


# ========= EKSPRESI B: ((x * z) + y) / (x - z + z) =========
print("\n=== EKSPRESI B: ((x * z) + y) / (x - z + z) ===")
print("Langkah-langkah perhitungan:")

# Langkah 1: Kalikan x dengan z
b_step1 = x * z
print(f"1. x * z = {x} * {z} = {b_step1}")
print(f"   Dalam biner: {bin(x)} * {bin(z)} = {bin(b_step1)}")

# Langkah 2: Tambahkan y ke hasil
b_numerator = b_step1 + y
print(f"2. (x * z) + y = {b_step1} + {y} = {b_numerator}")
print(f"   Dalam biner: {bin(b_step1)} + {bin(y)} = {bin(b_numerator)}")

# Langkah 3: Hitung penyebut (x - z + z)
b_step3_sub = x - z
print(f"3a. x - z = {x} - {z} = {b_step3_sub}")
print(f"    Dalam biner: {bin(x)} - {bin(z)} = {bin(b_step3_sub)}")

b_denominator = b_step3_sub + z
print(f"3b. (x - z) + z = {b_step3_sub} + {z} = {b_denominator}")
print(f"    Dalam biner: {bin(b_step3_sub)} + {bin(z)} = {bin(b_denominator)}")
print(f"    Catatan: x - z + z disederhanakan menjadi x (yaitu {x})")

# Langkah 4: Bagi
b_result = b_numerator / b_denominator
print(f"4. ((x * z) + y) / (x - z + z) = {b_numerator} / {b_denominator} = {b_result}")

# Tampilkan hasil pembulatan dan konversi ke biner
b_rounded = round(b_result)
b_int = int(b_result)

print("\nHasil Ekspresi b:")
print(f"Desimal (tidak dibulatkan): {b_result}")
print(f"Desimal (dibulatkan ke integer terdekat): {b_rounded}")
print(f"Desimal (dikonversi ke integer): {b_int}")
print(f"Biner (dari konversi ke integer): {to_binary(b_int)}")
print(
    f"Apakah hasil adalah bilangan bulat? {'Ya' if b_result.is_integer() else 'Tidak'}"
)

# Perhatikan bahwa (x - z + z) = x, sehingga ekspresi b menjadi ((x * z) + y) / x
print("\n=== CATATAN PENTING ===")
print("Dalam Ekspresi B: ((x * z) + y) / (x - z + z)")
print(
    "Perhatikan bahwa (x - z + z) = x, sehingga ekspresi dapat disederhanakan menjadi:"
)
print("((x * z) + y) / x")
simplified_result = ((x * z) + y) / x
print(f"Hasil: ((x * z) + y) / x = {simplified_result}")
print(f"Yang sama dengan hasil sebelumnya: {b_result}")
