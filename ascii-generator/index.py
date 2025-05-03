import time
import os
import json
from pyfiglet import Figlet
from random import choice
from getpass import getpass

# ======================
# DISPLAY CONFIGURATION
# ======================
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m'
}

BORDER = "═" * 60
HEADER = f"""
{COLORS['cyan']}╔══════════════════════════════════════════════════════════╗
║{COLORS['yellow']}          ____   _   _   _   _   _____   _____          {COLORS['cyan']}║
║{COLORS['yellow']}         / ___| | | | | | \ | | |_   _| |_   _|         {COLORS['cyan']}║
║{COLORS['yellow']}        | |     | | | | |  \| |   | |     | |           {COLORS['cyan']}║
║{COLORS['yellow']}        | |___  | |_| | | |\  |   | |     | |           {COLORS['cyan']}║
║{COLORS['yellow']}         \____|  \___/  |_| \_|   |_|     |_|           {COLORS['cyan']}║
╚══════════════════════════════════════════════════════════╝{COLORS['reset']}
"""

POPULAR_FONTS = [
    "slant", "block", "bubble", "digital", 
    "script", "starwars", "roman", "graffiti"
]

# ======================
# FILE MANAGEMENT
# ======================
USERS_FILE = "users.json"
HISTORY_FILE = "history.json"

def show_file_warning():
    """Display warning about files that will be created"""
    warning = f"""
{COLORS['yellow']}╔══════════════════════════════════════════════════════════╗
║                      WARNING!                       ║
╠══════════════════════════════════════════════════════════╣
║ This program will create 2 files in the same folder:     ║
║                                                          ║
║ 1. {USERS_FILE:<56}║
║ 2. {HISTORY_FILE:<56}║
║                                                          ║
║ These files will store:                                  ║
║ - User login data                                        ║
║ - ASCII art creation history                             ║
╚══════════════════════════════════════════════════════════╝{COLORS['reset']}
"""
    print(warning)
    input(f"{COLORS['cyan']}Press Enter to continue or Ctrl+C to exit...{COLORS['reset']}")

def initialize_files():
    """Create files if they don't exist"""
    for filename in [USERS_FILE, HISTORY_FILE]:
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump({}, f)
            print(f"{COLORS['yellow']}Created {filename}{COLORS['reset']}")

# ======================
# CORE FUNCTIONS
# ======================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(title=""):
    clear_screen()
    print(HEADER)
    if title:
        print(f"{COLORS['cyan']}{BORDER}")
        print(f"{title.center(60)}")
        print(f"{BORDER}{COLORS['reset']}\n")

def register_user():
    show_header("REGISTRATION")
    print(f"{COLORS['blue']}Create a new account{COLORS['reset']}\n")
    
    username = input("Username: ")
    if len(username) < 3:
        print(f"{COLORS['red']}Username must be at least 3 characters{COLORS['reset']}")
        time.sleep(1.5)
        return False
    
    pin = getpass("PIN (4 digits): ")
    if not pin.isdigit() or len(pin) != 4:
        print(f"{COLORS['red']}PIN must be 4 digits{COLORS['reset']}")
        time.sleep(1.5)
        return False
    
    with open(USERS_FILE, 'r+') as file:
        users = json.load(file)
        if username in users:
            print(f"{COLORS['red']}Username already exists!{COLORS['reset']}")
            time.sleep(1.5)
            return False
        
        users[username] = pin
        file.seek(0)
        json.dump(users, file)
    
    print(f"\n{COLORS['green']}Registration successful!{COLORS['reset']}")
    time.sleep(1.5)
    return True

def login():
    show_header("LOGIN")
    print(f"{COLORS['blue']}Please enter your credentials{COLORS['reset']}\n")
    
    username = input("Username: ")
    pin = getpass("PIN: ")
    
    with open(USERS_FILE, 'r') as file:
        users = json.load(file)
        if users.get(username) == pin:
            print(f"\n{COLORS['green']}Login successful!{COLORS['reset']}")
            time.sleep(1)
            return username
        else:
            print(f"\n{COLORS['red']}Invalid username or PIN!{COLORS['reset']}")
            time.sleep(1.5)
            return None

def log_history(username, text, font):
    """Save creation history"""
    with open(HISTORY_FILE, 'r+') as file:
        history = json.load(file)
        if username not in history:
            history[username] = []
        
        history[username].append({
            'text': text,
            'font': font,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
        })
        
        file.seek(0)
        json.dump(history, file)

def show_history(username):
    show_header("YOUR HISTORY")
    
    try:
        with open(HISTORY_FILE, 'r') as file:
            history = json.load(file)
            user_history = history.get(username, [])
            
            if not user_history:
                print(f"{COLORS['yellow']}No history yet.{COLORS['reset']}")
            else:
                print(f"{COLORS['cyan']}Last 5 creations:{COLORS['reset']}\n")
                for i, entry in enumerate(user_history[-5:], 1):
                    print(f"{COLORS['yellow']}{i}. {entry['timestamp']}{COLORS['reset']}")
                    print(f"Text: {entry['text']}")
                    print(f"Font: {entry['font']}\n")
    except:
        print(f"{COLORS['red']}Error loading history.{COLORS['reset']}")
    
    input(f"\n{COLORS['cyan']}Press Enter to continue...{COLORS['reset']}")

def show_colors():
    show_header("AVAILABLE COLORS")
    print(f"{COLORS['blue']}Color options:{COLORS['reset']}\n")
    for name, code in COLORS.items():
        if name != 'reset':
            print(f"{code}This is {name} color{COLORS['reset']}")
    input(f"\n{COLORS['cyan']}Press Enter to continue...{COLORS['reset']}")

def show_fonts():
    show_header("AVAILABLE FONTS")
    print(f"{COLORS['blue']}Font preview (showing 'Hello'):{COLORS['reset']}\n")
    sample_text = "Hello"
    for font in POPULAR_FONTS:
        f = Figlet(font=font)
        print(f"{COLORS['yellow']}{font.upper()}:{COLORS['reset']}")
        print(f.renderText(sample_text))
    input(f"\n{COLORS['cyan']}Press Enter to continue...{COLORS['reset']}")

def about():
    show_header("ABOUT")
    about_text = f"""
{COLORS['blue']}ASCII ART GENERATOR{COLORS['reset']}
Version 2.0

{COLORS['yellow']}Features:{COLORS['reset']}
- Text to ASCII art conversion
- Multiple font options
- Color customization
- User accounts system
- Creation history tracking
"""
    print(about_text)
    input(f"{COLORS['cyan']}Press Enter to continue...{COLORS['reset']}")

def author():
    show_header("AUTHOR")
    author_text = f"""
{COLORS['blue']}Created by:{COLORS['reset']}
Your Name

{COLORS['yellow']}Contact:{COLORS['reset']}
GitHub: https://github.com/yourprofile
Email: your@email.com
"""
    print(author_text)
    input(f"{COLORS['cyan']}Press Enter to continue...{COLORS['reset']}")

def animate_text(text, fonts, delay, colored):
    """Animate text with different fonts"""
    for i, font in enumerate(fonts):
        show_header("ASCII ART PREVIEW")
        
        f = Figlet(font=font)
        if colored:
            color = choice(list(COLORS.keys())[:-1])
            colored_text = f"{COLORS[color]}{f.renderText(text)}{COLORS['reset']}"
            print(colored_text)
        else:
            print(f.renderText(text))
            
        print(f"\n{COLORS['cyan']}Frame {i+1}/{len(fonts)} | Delay: {delay}s{COLORS['reset']}")
        time.sleep(delay)

def save_to_file(text, font, filename="ascii_art.txt"):
    """Save ASCII art to text file"""
    try:
        f = Figlet(font=font)
        with open(filename, "w") as file:
            file.write(f.renderText(text))
        print(f"\n{COLORS['green']}Saved as '{filename}'{COLORS['reset']}")
        time.sleep(1)
    except:
        print(f"\n{COLORS['red']}Error saving file!{COLORS['reset']}")
        time.sleep(1)

def create_ascii(username):
    show_header("CREATE ASCII ART")
    
    text = input("Enter your text: ")
    if not text.strip():
        print(f"\n{COLORS['red']}Text cannot be empty!{COLORS['reset']}")
        time.sleep(1.5)
        return
    
    try:
        delay = float(input("Animation delay (seconds, default 0.5): ") or 0.5)
    except ValueError:
        delay = 0.5
    
    if input("Show animation? (y/n): ").lower() == 'y':
        colored = input("Use random colors? (y/n): ").lower() == 'y'
        animate_text(text, POPULAR_FONTS, delay, colored)
    
    print(f"\n{COLORS['yellow']}Available fonts:{COLORS['reset']}", ", ".join(POPULAR_FONTS))
    font = input("Choose font: ")
    if font not in POPULAR_FONTS:
        font = "slant"
        print(f"{COLORS['red']}Invalid font, using default{COLORS['reset']}")
    
    f = Figlet(font=font)
    final_art = f.renderText(text)
    
    color_choice = input("Choose color (red/green/yellow/blue/magenta/cyan/white): ").lower()
    if color_choice in COLORS:
        final_art = f"{COLORS[color_choice]}{final_art}{COLORS['reset']}"
    
    print(f"\n{COLORS['cyan']}Your ASCII Art:{COLORS['reset']}\n")
    print(final_art)
    
    log_history(username, text, font)
    
    if input("\nSave to text file? (y/n): ").lower() == 'y':
        filename = input("Filename (default: ascii_art.txt): ") or "ascii_art.txt"
        save_to_file(text, font, filename)

def main_menu(username):
    while True:
        show_header("MAIN MENU")
        print(f"{COLORS['green']}Welcome, {username}!{COLORS['reset']}\n")
        
        print(f"{COLORS['cyan']}Menu options:{COLORS['reset']}")
        print(f"1. {COLORS['blue']}Create ASCII Art{COLORS['reset']}")
        print(f"2. {COLORS['blue']}View Colors{COLORS['reset']}")
        print(f"3. {COLORS['blue']}View Fonts{COLORS['reset']}")
        print(f"4. {COLORS['blue']}View History{COLORS['reset']}")
        print(f"5. {COLORS['blue']}About{COLORS['reset']}")
        print(f"6. {COLORS['blue']}Author{COLORS['reset']}")
        print(f"0. {COLORS['red']}Exit{COLORS['reset']}")
        
        choice = input("\nChoose option (0-6): ")
        
        if choice == "1":
            create_ascii(username)
        elif choice == "2":
            show_colors()
        elif choice == "3":
            show_fonts()
        elif choice == "4":
            show_history(username)
        elif choice == "5":
            about()
        elif choice == "6":
            author()
        elif choice == "0":
            print(f"\n{COLORS['yellow']}Goodbye, {username}!{COLORS['reset']}")
            break
        else:
            print(f"\n{COLORS['red']}Invalid option!{COLORS['reset']}")
            time.sleep(1)

def auth_flow():
    show_file_warning()
    initialize_files()
    
    while True:
        show_header("WELCOME")
        print(f"{COLORS['cyan']}Please choose:{COLORS['reset']}")
        print(f"1. {COLORS['green']}Login{COLORS['reset']}")
        print(f"2. {COLORS['blue']}Register{COLORS['reset']}")
        print(f"0. {COLORS['red']}Exit{COLORS['reset']}")
        
        choice = input("\nChoose option (0-2): ")
        
        if choice == "1":
            username = login()
            if username:
                main_menu(username)
        elif choice == "2":
            if register_user():
                print(f"\n{COLORS['green']}Registration successful! Please login.{COLORS['reset']}")
                time.sleep(1.5)
        elif choice == "0":
            print(f"\n{COLORS['yellow']}Thank you for using this program!{COLORS['reset']}")
            break
        else:
            print(f"\n{COLORS['red']}Invalid option!{COLORS['reset']}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        auth_flow()
    except KeyboardInterrupt:
        print(f"\n{COLORS['red']}Program stopped by user.{COLORS['reset']}")
    except Exception as e:
        print(f"\n{COLORS['red']}Error: {str(e)}{COLORS['reset']}")