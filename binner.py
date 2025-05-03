# ======================================
# KONVERTER TEKS-BINER DENGAN 4 OPSI
# ======================================

def text_to_binary(text):
    """Konversi teks ke biner (per karakter dipisah spasi)"""
    return ' '.join([bin(ord(char))[2:].zfill(8) for char in text])

def binary_to_text(binary_str):
    """Konversi biner ke teks (dengan/spasi tanpa spasi)"""
    try:
        binary_list = binary_str.split() if ' ' in binary_str else \
                     [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        return ''.join([chr(int(bin_char, 2)) for bin_char in binary_list])
    except:
        return "⚠ Error: Format biner tidak valid!"

def show_binary_table():
    """Tampilkan tabel informasi huruf-biner"""
    print("\nTABEL INFORMASI HURUF (ASCII):")
    print("="*40)
    print("| Huruf | Desimal | Biner      |")
    print("="*40)
    for char in range(32, 127):  # Karakter printable ASCII
        print(f"| {chr(char):<5} | {char:<7} | {bin(char)[2:].zfill(8)} |")
    print("="*40)

def main():
    while True:
        print("\n" + "="*30)
        print("  KONVERTER TEKS-BINER  ")
        print("="*30)
        print("1. Teks → Biner")
        print("2. Biner → Teks")
        print("3. Tabel Informasi Huruf")
        print("0. Exit")
        
        choice = input("Pilih opsi (1/2/3/0): ").strip()
        
        if choice == '1':
            text = input("Masukkan teks: ")
            print(f"\n🔹 Hasil Konversi:\n{text_to_binary(text)}")
        elif choice == '2':
            binary = input("Masukkan biner (contoh: 01000001 atau 01000001 01000010): ")
            print(f"\n🔹 Hasil Konversi:\n{binary_to_text(binary)}")
        elif choice == '3':
            show_binary_table()
        elif choice == '0':
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\n⛔ Opsi tidak valid! Silakan pilih 1, 2, 3, atau 0.")

if __name__ == "__main__":
    main()