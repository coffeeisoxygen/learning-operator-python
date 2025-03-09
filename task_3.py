"""
Demonstrasi Operator Bitwise dan Presedensi Operator di Python
"""

# ===================== DEFINISI VARIABEL =====================
x = 100  # 0b01100100
y = 10  # 0b00001010
z = 68  # 0b01000100


# ===================== FUNGSI UTILITAS =====================
def to_binary(n):
    """Mengonversi angka ke biner dalam format 8-bit"""
    return bin(n & 0xFF)[2:].zfill(8)  # Mengambil hanya 8-bit terakhir


def interpret_signed(n):
    """Mengonversi unsigned 8-bit ke signed integer"""
    return n if n < 128 else n - 256  # Mengonversi ke signed jika > 127


# ===================== HEADER PROGRAM =====================
print("=" * 60)
print("=== EVALUASI BERDASARKAN PRESEDENSI OPERATOR PYTHON ===".center(60))
print("=" * 60)

# Tampilkan nilai awal variabel
print("NILAI AWAL:")
print(f"x = {x} (binary: {to_binary(x)})")
print(f"y = {y} (binary: {to_binary(y)})")
print(f"z = {z} (binary: {to_binary(z)})")
print("-" * 60)


# ===================== SOAL A =====================
print("SOAL A: Bitwise AND dengan tiga operand (x & y & z)")
print("-" * 60)

# Evaluasi dari kiri ke kanan
expr_a = x & y & z
print(f"Hasil: {expr_a} (binary: {to_binary(expr_a)})")

# Tampilkan langkah-langkah evaluasi
print("Langkah evaluasi:")
step1_result = x & y
print(
    f"1. x & y = {step1_result} ({to_binary(x)} & {to_binary(y)} = {to_binary(step1_result)})"
)
print(
    f"2. (x & y) & z = {expr_a} ({to_binary(step1_result)} & {to_binary(z)} = {to_binary(expr_a)})"
)
print("-" * 60)


# ===================== SOAL B1 =====================
print("SOAL B1: Kombinasi operator bitwise tanpa kurung eksplisit")
print("Ekspresi: x ^ y << 5 >> 2")
print("-" * 60)

# Presedensi: shift, XOR, shift
expr_b_no_parens = x ^ y << 5 >> 2
print(f"Hasil: {expr_b_no_parens} (binary: {to_binary(expr_b_no_parens)})")

# Tampilkan langkah-langkah evaluasi berdasarkan presedensi
print("Langkah evaluasi berdasarkan presedensi Python:")
step1_b1 = y << 5
print(f"1. y << 5 = {step1_b1} ({to_binary(y)} << 5 = {to_binary(step1_b1)})")

step2_b1 = x ^ step1_b1
print(
    f"2. x ^ (y << 5) = {step2_b1} ({to_binary(x)} ^ {to_binary(step1_b1)} = {to_binary(step2_b1)})"
)

print(
    f"3. (x ^ (y << 5)) >> 2 = {expr_b_no_parens} ({to_binary(step2_b1)} >> 2 = {to_binary(expr_b_no_parens)})"
)
print("-" * 60)


# ===================== SOAL B2 =====================
print("SOAL B2: Kombinasi operator bitwise dengan kurung eksplisit")
print("Ekspresi: x ^ (y << 5) >> 2")
print("-" * 60)

# Langkah-langkah eksplisit
y_shift = y << 5  # Geser y ke kiri 5 bit
xor_result = x ^ y_shift  # XOR dengan x
expr_b_parens = xor_result >> 2  # Geser hasil XOR ke kanan 2 bit

print(f"Hasil: {expr_b_parens} (binary: {to_binary(expr_b_parens)})")

# Tampilkan langkah-langkah evaluasi dengan kurung eksplisit
print("Langkah evaluasi dengan kurung eksplisit:")
print(f"1. y << 5 = {y_shift} ({to_binary(y)} << 5 = {to_binary(y_shift)})")
print(
    f"2. x ^ (y << 5) = {xor_result} ({to_binary(x)} ^ {to_binary(y_shift)} = {to_binary(xor_result)})"
)
print(
    f"3. (x ^ (y << 5)) >> 2 = {expr_b_parens} ({to_binary(xor_result)} >> 2 = {to_binary(expr_b_parens)})"
)
print("-" * 60)


# ===================== SOAL C =====================
print("SOAL C: Kombinasi bitwise NOT, AND, dan OR")
print("Ekspresi: ~x & ~y | ~z")
print("-" * 60)

# Negasi bitwise (dalam batas 8-bit)
not_x = ~x & 0xFF
not_y = ~y & 0xFF
not_z = ~z & 0xFF

# Evaluasi berdasarkan presedensi
expr_c = (not_x & not_y) | not_z

# Interpretasi hasil
result_signed = interpret_signed(expr_c)
print(f"Hasil signed: {result_signed} (binary: {to_binary(expr_c)})")
print(f"Hasil unsigned: {expr_c} (binary: {to_binary(expr_c)})")

# Tampilkan langkah-langkah evaluasi
print("Langkah evaluasi:")
print(f"1. ~x = {not_x} (binary: {to_binary(not_x)})")
print(f"2. ~y = {not_y} (binary: {to_binary(not_y)})")
print(f"3. ~z = {not_z} (binary: {to_binary(not_z)})")

step4_c = not_x & not_y
print(
    f"4. ~x & ~y = {step4_c} ({to_binary(not_x)} & {to_binary(not_y)} = {to_binary(step4_c)})"
)
print(
    f"5. (~x & ~y) | ~z = {expr_c} ({to_binary(step4_c)} | {to_binary(not_z)} = {to_binary(expr_c)})"
)
print("=" * 60)
