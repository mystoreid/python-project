import os
import json
import time
import random
import sys
from datetime import datetime, timedelta

# Configuration
CORRECT_KEY = "1234"
BTC_ADDRESS = "1F1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
AMOUNT = "0.5 BTC"
LOCK_FILE = "kunci.json"
HACKER_NAME = "FIZ"
ATTEMPT_LIMIT = 3

def typewriter(text, speed=0.03):
    """Typewriter animation effect (Fitur 12)"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def create_lock_file():
    """Create the fake encryption lock file (Fitur 1)"""
    deadline = datetime.now() + timedelta(hours=72)
    data = {
        "encryption_key": "AES-256-GCM",
        "status": "ACTIVE",
        "victim_id": f"TERMUX-{random.randint(1000,9999)}",
        "ransom_amount": AMOUNT,
        "bitcoin_address": BTC_ADDRESS,
        "deadline": deadline.isoformat(),
        "warning": "DO NOT MODIFY OR DELETE THIS FILE! SYSTEM WILL REMAIN LOCKED!",
        "hacker": HACKER_NAME,
        "contact": "darkweb_recovery@protonmail.com",
        "multi_lang_warning": {
            "en": "Your system has been locked!",
            "id": "Sistem Anda telah dikunci!",
            "es": "¡Tu sistema ha sido bloqueado!"
        }
    }
    
    with open(LOCK_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_fake_encryption():
    """Show fake file encryption process (Fitur 1)"""
    fake_files = [
        "/sdcard/DCIM/Camera/photo01.jpg",
        "/sdcard/Download/document.pdf",
        "/sdcard/WhatsApp/Media/image.png",
        "/data/data/com.termux/files/home/important.txt",
        "/sdcard/Music/song.mp3",
        "/sdcard/Android/data/com.whatsapp/files/backup.db"
    ]
    
    print("\n[!] ENCRYPTING FILES [!]")
    for file in fake_files:
        print(f"[*] Encrypting {file}...", end='')
        sys.stdout.flush()
        time.sleep(random.uniform(0.1, 0.5))
        print("\033[1;32m DONE\033[1;31m")
    print("\033[1;31m[!] ALL PERSONAL FILES ENCRYPTED [!]\033[0m")
    time.sleep(1)

def fake_system_scan():
    """Show fake system scan (Fitur 2)"""
    print("\n[*] SCANNING SYSTEM INFORMATION [*]")
    time.sleep(1)
    
    info = {
        "Device ID": random.randint(1000000, 9999999),
        "IP Address": f"192.168.1.{random.randint(1, 255)}",
        "Termux Version": random.choice(['3.0.1', '2.9.9', '3.1.0']),
        "Storage Used": f"{random.randint(30, 90)}GB/{random.randint(100, 256)}GB",
        "Battery Level": f"{random.randint(10, 90)}%",
        "Network": random.choice(['WiFi', 'Mobile Data'])
    }
    
    for key, value in info.items():
        print(f"{key}: {value}")
        time.sleep(0.2)
    
    print("\033[1;31m[!] SYSTEM VULNERABILITIES FOUND [!]\033[0m")
    time.sleep(1)

def check_payment():
    """Fake Bitcoin payment tracker (Fitur 3)"""
    print("\n[*] CONNECTING TO BITCOIN NETWORK [*]")
    for i in range(3):
        print(f"Establishing connection... {i+1}/3", end='\r')
        time.sleep(0.5)
    
    print("\n\nBlockchain Info:")
    print(f"Address: {BTC_ADDRESS}")
    print("Confirmed transactions: 0")
    print("Last block: 783,421")
    print("\033[1;31m[!] PAYMENT NOT RECEIVED!\033[0m")
    time.sleep(3)

def show_timer(seconds=10):
    """Visual timer with progress bar (Fitur 4)"""
    print("\n")
    for i in range(seconds, 0, -1):
        bar = '#' * i + ' ' * (seconds - i)
        print(f"Self-destruct: [{bar}] {i}s remaining", end='\r')
        time.sleep(1)
    print("\n")

def fake_gps():
    """Show fake GPS location (Fitur 5)"""
    cities = {
        'Jakarta': (-6.2088, 106.8456),
        'Bandung': (-6.9175, 107.6191),
        'Surabaya': (-7.2575, 112.7521),
        'Medan': (3.5952, 98.6722)
    }
    city, coords = random.choice(list(cities.items()))
    print("\n[*] LOCATING DEVICE [*]")
    time.sleep(1.5)
    print(f"Coordinates: {coords[0]:.4f}, {coords[1]:.4f}")
    print(f"Approximate address: {city}, Indonesia")
    print("Accuracy: ±50 meters")
    print("\033[1;31m[!] LOCATION LOGGED [!]\033[0m")
    time.sleep(2)

def password_attempt_limiter():
    """Password attempt limiter (Fitur 6)"""
    attempts = ATTEMPT_LIMIT
    while attempts > 0:
        key = input("\nEnter decryption key: ")
        if key == CORRECT_KEY:
            return True
        attempts -= 1
        print(f"\033[1;31m[-] WRONG KEY! {attempts} attempts remaining\033[0m")
        if attempts == 1:
            print("\033[1;31m[!] WARNING: Last attempt before data wipe!\033[0m")
    return False

def fake_virus_scan():
    """Fake virus scan (Fitur 7)"""
    print("\n[*] RUNNING MALWARE SCAN [*]")
    time.sleep(1)
    
    threats = [
        "Trojan-Ransom.Linux.CrySiS",
        "Exploit.CVE-2023-1234",
        "Backdoor:Linux/Agent.A",
        "Riskware.Linux.BitcoinMiner"
    ]
    
    for threat in threats:
        print(f"Detected: {threat}", end='')
        sys.stdout.flush()
        time.sleep(0.3)
        print("\033[1;31m HIGH THREAT\033[0m")
        time.sleep(0.2)
    
    print("\n\033[1;31m[!] SYSTEM COMPROMISED [!]\033[0m")
    time.sleep(2)

def auto_delete_after_deadline():
    """Fake auto-delete sequence (Fitur 8)"""
    print("\n\033[1;31m[!] DEADLINE PASSED! INITIATING DATA WIPE [!]\033[0m")
    time.sleep(1)
    
    for i in range(5, 0, -1):
        print(f"Deleting all personal files in {i}...", end='\r')
        time.sleep(1)
    
    print("\n\033[1;31m[!] ALL DATA PERMANENTLY DESTROYED [!]\033[0m")
    time.sleep(2)

def fake_data_exfil():
    """Fake network traffic (Fitur 11)"""
    print("\n[*] EXFILTRATING SENSITIVE DATA [*]")
    data_types = [
        "Browser History",
        "Saved Passwords",
        "Contact List",
        "SMS Messages",
        "Gallery Photos"
    ]
    
    for i, data in enumerate(data_types, 1):
        print(f"Sending {data}...", end='')
        sys.stdout.flush()
        time.sleep(random.uniform(0.3, 0.7))
        print("\033[1;32m COMPLETE\033[1;31m")
    
    print("\n\033[1;31m[!] DATA TRANSFER TO C2 SERVER COMPLETE [!]\033[0m")
    time.sleep(2)

def show_multi_lang_warning():
    """Multi-language warning (Fitur 12)"""
    warnings = {
        "en": "WARNING! YOUR DEVICE HAS BEEN LOCKED!",
        "id": "PERINGATAN! PERANGKAT ANDA TELAH DIKUNCI!",
        "es": "¡ADVERTENCIA! ¡TU DISPOSITIVO HA SIDO BLOQUEADO!"
    }
    
    print("\n" + "═"*50)
    for lang, message in warnings.items():
        print(f"[{lang.upper()}] {message}")
        time.sleep(0.5)
    print("═"*50 + "\n")
    time.sleep(2)

def show_ransom_screen():
    """Main ransom screen"""
    deadline = datetime.now() + timedelta(hours=72)
    
    while True:
        clear_screen()
        print("\033[1;31m")  # Red color
        
        # Current time calculation
        current_time = datetime.now()
        remaining = deadline - current_time
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # ASCII Art Header
        print(r"  _____ _   _  _____ _______ ______ _____  _   _  ____  ")
        print(r" |_   _| \ | |/ ____|__   __|  ____|  __ \| \ | |/ __ \ ")
        print(r"   | | |  \| | (___    | |  | |__  | |__) |  \| | |  | |")
        print(r"   | | | . ` |\___ \   | |  |  __| |  _  /| . ` | |  | |")
        print(r"  _| |_| |\  |____) |  | |  | |____| | \ \| |\  | |__| |")
        print(r" |_____|_| \_|_____/   |_|  |______|_|  \_\_| \_|\____/ ")
        print("\n" + "��"*50)
        print(f"           H A C K E D   B Y   {HACKER_NAME}")
        print("═"*50 + "\n")
        
        # Status information
        print(f"[+] VICTIM ID: TERMUX-{random.randint(1000,9999)}")
        print(f"[+] ENCRYPTION: AES-256 (Military Grade)")
        print(f"[+] RANSOM AMOUNT: {AMOUNT}")
        print(f"[+] BITCOIN ADDRESS: {BTC_ADDRESS}")
        print(f"\n[!] TIME REMAINING: {remaining.days}d {hours}h {minutes}m {seconds}s")
        print("[!] AFTER DEADLINE ALL DATA WILL BE PERMANENTLY DESTROYED!")
        
        # Menu
        print("\n\033[1;37m[ MAIN MENU ]\033[1;31m")
        print("[1] Enter decryption key")
        print("[2] Show payment instructions")
        print("[3] Verify payment")
        print("[4] View encrypted files")
        print("[5] System information")
        print("[6] Device location")
        print("[7] Run malware scan")
        print("[8] View data exfiltration")
        print("[9] Multi-language warning")
        
        choice = input("\nSelect option: ")
        
        if choice == "1":
            if password_attempt_limiter():
                # Unlock sequence
                print("\n\033[1;32m[+] KEY ACCEPTED! Unlocking system...\033[0m")
                time.sleep(2)
                os.remove(LOCK_FILE)
                clear_screen()
                print("\033[1;32m")
                print(r"  _____ _   _  _____ _______ ______ _____  _   _  ____  ")
                print(r" |_   _| \ | |/ ____|__   __|  ____|  __ \| \ | |/ __ \ ")
                print(r"   | | |  \| | (___    | |  | |__  | |__) |  \| | |  | |")
                print(r"   | | | . ` |\___ \   | |  |  __| |  _  /| . ` | |  | |")
                print(r"  _| |_| |\  |____) |  | |  | |____| | \ \| |\  | |__| |")
                print(r" |_____|_| \_|_____/   |_|  |______|_|  \_\_| \_|\____/ ")
                print("\n[+] SYSTEM UNLOCKED! You may now use Termux normally.")
                print("[+] All files have been restored successfully.")
                print("\033[0m")
                break
            else:
                auto_delete_after_deadline()
        elif choice == "2":
            print("\n\033[1;37m[ PAYMENT INSTRUCTIONS ]\033[1;31m")
            print("1. Send exactly 0.5 BTC to address:", BTC_ADDRESS)
            print("2. Include your Victim ID in the transaction notes")
            print("3. Wait for 3 blockchain confirmations (~30 minutes)")
            print("4. The decryption key will appear automatically")
            print("\nNOTE: Partial payments will not be accepted!")
            input("\nPress Enter to continue...")
        elif choice == "3":
            check_payment()
        elif choice == "4":
            show_fake_encryption()
        elif choice == "5":
            fake_system_scan()
        elif choice == "6":
            fake_gps()
        elif choice == "7":
            fake_virus_scan()
        elif choice == "8":
            fake_data_exfil()
        elif choice == "9":
            show_multi_lang_warning()

def main():
    """Main function"""
    clear_screen()
    print("\033[1;31mInitializing attack sequence...\033[0m")
    time.sleep(1)
    
    # Run all features
    create_lock_file()
    fake_system_scan()
    show_fake_encryption()
    fake_data_exfil()
    fake_virus_scan()
    fake_gps()
    show_multi_lang_warning()
    
    # Show main ransom screen
    show_ransom_screen()

if __name__ == "__main__":
    main()