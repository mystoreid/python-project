def main():
    print("Pilih mode:")
    print("1. Teks -> Biner")
    print("2. Biner -> Teks")
    choice = input("Masukkan pilihan (1/2): ")
    
    if choice == '1':
        text = input("Masukkan teks: ")
        print(f"Hasil: {text_to_binary(text)}")
    elif choice == '2':
        binary = input("Masukkan biner: ")
        print(f"Hasil: {binary_to_text(binary)}")
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()