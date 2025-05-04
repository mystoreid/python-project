import time
import random
import string
import os
import sys
from threading import Thread
from colorama import init, Fore, Style
import itertools

# Inisialisasi Colorama
init()

# Fungsi untuk efek suara ketikan (opsional, hanya Windows)
def play_typing_sound():
    try:
        import winsound
        while True:
            winsound.Beep(random.randint(600, 1000), 50)
            time.sleep(0.05)
    except:
        pass

# Animasi Matrix kompleks (karakter hijau yang jatuh)
def matrix_animation():
    columns = os.get_terminal_size().columns
    rows = os.get_terminal_size().lines - 5
    streams = [{'pos': 0, 'speed': random.uniform(0.5, 2), 'length': random.randint(5, 15)} for _ in range(columns)]
    chars = string.ascii_letters + string.digits + string.punctuation

    # Mulai efek suara
    sound_thread = Thread(target=play_typing_sound)
    sound_thread.daemon = True
    sound_thread.start()

    while True:  # Loop tak terbatas untuk animasi Matrix
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Update posisi stream
        for stream in streams:
            stream['pos'] += stream['speed']
            if stream['pos'] > rows + stream['length']:
                stream['pos'] = 0
                stream['length'] = random.randint(5, 15)
                stream['speed'] = random.uniform(0.5, 2)

        # Gambar animasi
        for row in range(rows):
            line = ""
            for col, stream in enumerate(streams):
                dist = stream['pos'] - row
                if 0 <= dist < stream['length']:
                    # Efek memudar
                    if dist < stream['length'] * 0.3:
                        color = Fore.GREEN + Style.BRIGHT
                    elif dist < stream['length'] * 0.6:
                        color = Fore.GREEN
                    else:
                        color = Fore.LIGHTGREEN_EX
                    # Efek glitch acak
                    if random.random() < 0.01:
                        line += f"{Fore.RED}{random.choice(chars)}"
                    else:
                        line += f"{color}{random.choice(chars)}"
                else:
                    line += " "
            print(line)
        
        # Pesan di bagian bawah
        print(f"\n{Fore.RED}{Style.BRIGHT}[!] Termux Anda Telah Kami Hack{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Untuk menghentikan program, tekan CTRL+C{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.05)

# Animasi progress bar saat Ctrl+C
def exit_progress_bar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.YELLOW}{Style.BRIGHT}[*] Tunggu sebentar sedang loading nih{Style.RESET_ALL}")
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    print(f"{Fore.YELLOW}{Style.BRIGHT}[*] Progress: [", end="")
    for i in range(20):
        print("█", end="", flush=True)
        sys.stdout.write(f"\b{next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"] 100%{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}[*] Jika loading sudah selesai maka program akan dihentikan{Style.RESET_ALL}")
    time.sleep(1)
    
    # Pesan penutup
    os.system('cls' if os.name == 'nt' else 'clear')
    closing_message = (
        f"{Fore.CYAN}{Style.BRIGHT}Terimakasih Telah Mengunjungi Script Prank Ini Walau Gajelas Si\n"
        f"Github : https://github.com/webstoreid\n"
        f"Tele   : https://t.me/-\n"
        f"Author : Hafiz Tools\n"
        f"Tema   : Hack\n"
        f"Status : Active\n"
        f"Tujuan : Prank Have Fun{Style.RESET_ALL}"
    )
    print(closing_message)
    time.sleep(2)

# Fungsi untuk peringatan awal
def warning_prompt():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}{Style.BRIGHT}[!] Anda benar-benar yakin ingin menjalankan code ini?{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1. Ya{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}2. Tidak{Style.RESET_ALL}")
    while True:
        choice = input(f"{Fore.CYAN}Pilih opsi (1/2): {Style.RESET_ALL}")
        if choice == '1':
            return True
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.CYAN}{Style.BRIGHT}Program dihentikan.{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}Pilih opsi yang valid (1 atau 2)!{Style.RESET_ALL}")

# Fungsi utama
def hack_prank():
    # Tampilkan peringatan awal
    if warning_prompt():
        try:
            matrix_animation()  # Jalankan animasi Matrix berulang-ulang
        except KeyboardInterrupt:
            exit_progress_bar()  # Tampilkan progress bar dan pesan penutup
            sys.exit(0)

# Jalankan prank
if __name__ == "__main__":
    hack_prank()