# ==============================
# KONVERTER TEKS <> BINER
# ==============================
# Fungsi: Teks -> Biner (per karakter)
def text_to_binary(text):
    binary_result = []
    for char in text:
        # Konversi karakter ke ASCII, lalu ke biner 8-bit
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_result.append(binary_char)
    return ' '.join(binary_result)

# Fungsi: Biner -> Teks
def binary_to_text(binary_str):
    try:
        # Handle input dengan/spasi tanpa spasi
        binary_list = binary_str.split() if ' ' in binary_str else \
                     [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        text = ''.join([chr(int(bin_char, 2)) for bin_char in binary_list])
        return text
    except ValueError:
        return "ERROR: Format biner tidak valid!"

# Menu utama
def main():
    print("\n" + "="*30)
    print(" KONVERTER TEKS <> BINER ")
    print("="*30)
    
    while True:
        print("\nPilih mode:")
        print("1. Teks -> Biner")
        print("2. Biner -> Teks")
        print("3. Keluar")
        choice = input("Pilihan (1/2/3): ").strip()
        
        if choice == '1':
            text = input("Masukkan teks: ")
            print(f"\nHasil konversi:\n{text_to_binary(text)}")
        elif choice == '2':
            binary = input("Masukkan biner (contoh: 01000001 atau 01000001 01000010): ")
            print(f"\nHasil konversi:\n{binary_to_text(binary)}")
        elif choice == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    main()