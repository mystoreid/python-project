import time
from colorama import init, Fore, Back, Style
import os
import platform

# Inisialisasi colorama
init(autoreset=True)

# Variabel global
history = []

def clear_screen():
    """Membersihkan layar konsol"""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_text(text, delay=0.03):
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

def analyze_password(password):
    """Analisis kekuatan password (Fitur 5)"""
    strength = 0
    if len(password) >= 12: strength += 1
    if any(c.isupper() for c in password): strength += 1
    if any(c.isdigit() for c in password): strength += 1
    if any(c in '!@#$%^&*()' for c in password): strength += 1
    
    tips = []
    if len(password) < 8:
        tips.append("Gunakan minimal 8 karakter")
    if not any(c.isupper() for c in password):
        tips.append("Tambahkan huruf kapital")
    if not any(c.isdigit() for c in password):
        tips.append("Tambahkan angka")
    if not any(c in '!@#$%^&*()' for c in password):
        tips.append("Tambahkan simbol")
    
    return {
        "strength": ["Sangat Lemah", "Lemah", "Sedang", "Kuat", "Sangat Kuat"][strength],
        "score": strength * 25,
        "tips": tips
    }

def binary_calculator():
    """Kalkulator operasi biner (Fitur 7)"""
    print(Fore.CYAN + "\nOperasi yang tersedia:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    
    try:
        op_choice = input("Pilih operasi (1-4): ")
        ops = {'1': '+', '2': '-', '3': '*', '4': '/'}
        a = input("Masukkan bilangan biner pertama: ").replace(" ", "")
        b = input("Masukkan bilangan biner kedua: ").replace(" ", "")
        
        result = eval(f"{int(a, 2)} {ops[op_choice]} {int(b, 2)}")
        binary_result = bin(result)[2:]
        
        print(Fore.GREEN + f"\nHasil dalam biner: {binary_result}")
        print(Fore.GREEN + f"Hasil dalam desimal: {result}")
        return binary_result
    except:
        print(Fore.RED + "Input tidak valid!")
        return None

def show_history():
    """Menampilkan riwayat konversi (Fitur 8)"""
    clear_screen()
    print(Fore.YELLOW + "⎻"*60)
    animate_text(Fore.CYAN + "       RIWAYAT KONVERSI", 0.01)
    print(Fore.YELLOW + "⎻"*60)
    
    if not history:
        print(Fore.RED + "Belum ada riwayat konversi")
    else:
        for idx, entry in enumerate(history, 1):
            print(Fore.MAGENTA + f"\n[{idx}] {entry['timestamp']}")
            print(Fore.WHITE + f"Mode: {entry['mode']}")
            print(f"Input: {entry['input'][:50]}...")
            print(f"Output: {entry['output'][:50]}...")
    
    input("\nTekan Enter untuk kembali...")

def add_to_history(input_text, result, mode):
    """Menambahkan entri ke riwayat"""
    history.append({
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
        'input': input_text,
        'output': result,
        'mode': mode
    })

def show_banner():
    """Menampilkan banner judul"""
    clear_screen()
    print(Fore.BLUE + Style.BRIGHT + "✧"*60)
    animate_text(Fore.CYAN + "       SUPER BINARY CONVERTER PRO", 0.02)
    print(Fore.BLUE + Style.BRIGHT + "✧"*60)
    print(Fore.YELLOW + " " + platform.system() + " " + platform.release() + 
          " " * 30 + time.strftime("%H:%M:%S"))
    print(Fore.BLUE + "⎻"*60)

def main():
    while True:
        show_banner()
        print(Fore.YELLOW + Style.BRIGHT + "\nMENU UTAMA:")
        print(Fore.GREEN + "1. Teks → Biner")
        print(Fore.GREEN + "2. Biner → Teks")
        print(Fore.CYAN + "5. Analisis Kekuatan Password")
        print(Fore.CYAN + "6. Tabel Informasi Lengkap")
        print(Fore.MAGENTA + "7. Kalkulator Biner")
        print(Fore.MAGENTA + "8. Lihat Riwayat")
        print(Fore.RED + "0. Keluar")
        print(Style.RESET_ALL)
        
        choice = input(Fore.WHITE + "➤ Masukkan pilihan: ").strip()
        
        if choice == '1':
            show_banner()
            print(Fore.CYAN + "\nMODE TEKS → BINER")
            text = input("\nMasukkan teks: ")
            result = text_to_binary(text)
            print(Fore.GREEN + f"\nHasil konversi:\n{result}")
            add_to_history(text, result, "Teks ke Biner")
            input("\nTekan Enter untuk melanjutkan...")
        
        elif choice == '2':
            show_banner()
            print(Fore.CYAN + "\nMODE BINER → TEKS")
            binary = input("\nMasukkan biner (contoh: 01000001 atau 01000001 01000010): ")
            result = binary_to_text(binary)
            if result:
                print(Fore.GREEN + f"\nHasil konversi:\n{result}")
                add_to_history(binary, result, "Biner ke Teks")
            else:
                print(Fore.RED + "\nError: Format biner tidak valid!")
            input("\nTekan Enter untuk melanjutkan...")
        
        elif choice == '5':
            show_banner()
            print(Fore.CYAN + "\nANALISIS KEKUATAN PASSWORD")
            password = input("\nMasukkan password untuk dianalisis: ")
            analysis = analyze_password(password)
            
            print(Fore.YELLOW + "\n⎻"*40)
            print(Fore.CYAN + "   HASIL ANALISIS")
            print(Fore.YELLOW + "⎻"*40)
            print(Fore.WHITE + f"Kekuatan: {analysis['strength']}")
            print(f"Skor: {analysis['score']}/100")
            
            if analysis['tips']:
                print(Fore.RED + "\nTips untuk meningkatkan:")
                for tip in analysis['tips']:
                    print(f"- {tip}")
            
            add_to_history(password, str(analysis), "Analisis Password")
            input("\nTekan Enter untuk melanjutkan...")
        
        elif choice == '6':
            show_banner()
            print(Fore.CYAN + "\nTABEL INFORMASI LENGKAP")
            print(Fore.YELLOW + "\n⎻"*60)
            print(Fore.MAGENTA + "| Huruf | Desimal |   Biner    |  Hex  |  Oktal  |")
            print(Fore.YELLOW + "⎻"*60)
            
            for char in range(32, 127):
                time.sleep(0.002)
                print(Fore.WHITE + f"|  {chr(char):<3}  |   {char:<4}  | {bin(char)[2:].zfill(8)} | {hex(char)[2:].zfill(2)}  | {oct(char)[2:].zfill(3)}    |")
            
            print(Fore.YELLOW + "⎻"*60)
            add_to_history("Tabel ASCII", "Ditampilkan", "Lihat Tabel")
            input("\nTekan Enter untuk kembali...")
        
        elif choice == '7':
            show_banner()
            print(Fore.CYAN + "\nKALKULATOR BINER")
            result = binary_calculator()
            if result:
                add_to_history("Operasi Biner", result, "Kalkulator")
            input("\nTekan Enter untuk melanjutkan...")
        
        elif choice == '8':
            show_history()
        
        elif choice == '0':
            show_banner()
            animate_text(Fore.RED + "\nKeluar dari program...", 0.05)
            animate_text(Fore.YELLOW + "Terima kasih telah menggunakan konverter ini!", 0.05)
            time.sleep(1)
            break
        
        else:
            print(Fore.RED + "\nPilihan tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    main()