import random

print("=== GAME TEBAK ANGKA ===")
print("Aku sudah memilih angka antara 1 sampai 50.")
print("Coba tebak angkanya!")

# komputer pilih angka
angka_rahasia = random.randint(1, 50)
percobaan = 0

while True:
    tebak = int(input("Masukkan tebakanmu: "))
    percobaan += 1

    if tebak < angka_rahasia:
        print("Terlalu kecil!")
    elif tebak > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"🎉 Benar! Angkanya {angka_rahasia}.")
        print(f"Kamu menebak dengan {percobaan} percobaan.")
        break