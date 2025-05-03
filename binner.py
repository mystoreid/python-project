import time
from colorama import init, Fore, Back, Style
import os

# Inisialisasi colorama
init(autoreset=True)

def clear_screen():
    """Membersihkan layar konsol"""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.05):
    """Animasi ketik teks"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def text_to_binary(text):
    """Konversi teks ke biner"""
    return ' '.join([bin(ord(char))[2:].zfill(8) for char in text])

def binary_to_text(binary_str):
    """Konversi biner ke teks"""
    try:
        binary_list = binary_str.split() if ' ' in binary_str else \
                     [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        return ''.join([chr(int(bin_char, 2)) for bin_char in binary_list])
    except:
        return None

def show_binary_table():
    """Menampilkan tabel ASCII dengan animasi"""
    clear_screen()
    print(Fore.YELLOW + "⎻"*60)
    animate_text(Fore.CYAN + "       TABEL INFORMASI HURUF (STANDARD ASCII)", 0.01)
    print(Fore.YELLOW + "⎻"*60)
    print(Fore.MAGENTA + "| Huruf | Desimal |   Biner    |  Hex  |  Oktal  |")
    print(Fore.YELLOW + "⎻"*60)
    
    for char in range(32, 127):
        time.sleep(0.005)  # Animasi loading
        print(Fore.WHITE + f"|  {chr(char):<3}  |   {char:<4}  | {bin(char)[2:].zfill(8)} | {hex(char)[2:].zfill(2)}  | {oct(char)[2:].zfill(3)}    |")
    print(Fore.YELLOW + "⎻"*60)
    input("\nTekan Enter untuk kembali ke menu...")

def loading_animation():
    """Animasi loading sederhana"""
    for i in range(3):
        for char in '⣾⣽⣻⢿⡿⣟⣯⣷':
            print(Fore.GREEN + f"\rMemproses {char}", end='', flush=True)
            time.sleep(0.1)

def main():
    while True:
        clear_screen()
        print(Fore.BLUE + Style.BRIGHT + "✧"*60)
        animate_text(Fore.CYAN + "       KONVERTER TEKS & BINER ADVANCED", 0.02)
        print(Fore.BLUE + Style.BRIGHT + "✧"*60)
        print(Fore.YELLOW + Style.BRIGHT + "\nPILIH MENU:")
        print(Fore.GREEN + "1. Teks → Biner")
        print(Fore.GREEN + "2. Biner → Teks")
        print(Fore.CYAN + "3. Tabel Informasi Lengkap")
        print(Fore.RED + "0. Keluar")
        print(Style.RESET_ALL)
        
        choice = input(Fore.WHITE + "➤ Masukkan pilihan (1/2/3/0): ").strip()
        
        if choice == '1':
            clear_screen()
            print(Fore.BLUE + "⎻"*60)
            animate_text(Fore.CYAN + "       MODE TEKS KE BINER", 0.02)
            print(Fore.BLUE + "⎻"*60)
            text = input("\nMasukkan teks: ")
            loading_animation()
            print(Fore.GREEN + f"\n\nHasil konversi:\n{text_to_binary(text)}")
            input("\nTekan Enter untuk melanjutkan...")
        
        elif choice == '2':
            clear_screen()
            print(Fore.BLUE + "⎻"*60)
            animate_text(Fore.CYAN + "       MODE BINER KE TEKS", 0.02)
            print(Fore.BLUE + "⎻"*60)
            binary = input("\nMasukkan biner (contoh: 01000001 atau 01000001 01000010): ")
            loading_animation()
            result = binary_to_text(binary)
            if result:
                print(Fore.GREEN + f"\n\nHasil konversi:\n{result}")
            else:
                print(Fore.RED + "\n\nError: Format biner tidak valid!")
            input("\nTekan Enter untuk melanjutkan...")
        
        elif choice == '3':
            show_binary_table()
        
        elif choice == '0':
            clear_screen()
            animate_text(Fore.RED + "\nKeluar dari program...", 0.05)
            animate_text(Fore.YELLOW + "Terima kasih telah menggunakan konverter ini!", 0.05)
            time.sleep(1)
            break
        
        else:
            print(Fore.RED + "\nPilihan tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    main()