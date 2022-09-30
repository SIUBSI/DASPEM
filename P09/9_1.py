# 9.1 - Mendefinisikan Fungsi (hal. 95-96)

'''
Berikut adalah sintaks yang digunakan untuk membuat fungsi:
def function_name(parameters):
    """function_docstring"""
    statement(s)

    return [expression]

Penjelasannya dari sintaks fungsi di atas:
1. Kata kunci def diikuti oleh function_name (nama fungsi), tanda kurung dan tanda titik dua 
(:) menandai header (kepala) fungsi.
2. Parameter / argumen adalah input dari luar yang akan diproses di dalam tubuh fungsi
3. "function_docstring" bersifat opsional, yaitu sebagai string yang digunakan untuk 
dokumentasi atau penjelasan fungsi. “function_doctring” diletakkan paling atas setelah 
baris def.
4. Setelah itu diletakkan baris – baris pernyataan (statements). Jangan lupa indentasi untuk 
menandai blok fungsi.
5. return bersifat opsional. Gunanya adalah untuk mengembalikan suatu nilai expression dari 
fungsi.
'''

print("> Contoh fungsi untuk menyapa seseorang")
def sapa(nama):
    """Fungsi ini untuk menyapa seseorang sesuai nama yang dimasukkan sebagai parameter"""
    print("Hi, " + nama + ". Apa kabar?")

# Pemanggilan fungsi
# Output: Hi, Daffy. Apa kabar?
sapa("Daffy")
