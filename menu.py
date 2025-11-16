def get_pilihan(message: str, num: int):
    rangePilihan = tuple(str(i) for i in range(1, num + 1))

    print(message)
    pilihan = input("Masukkan pilihan: ")

    while not pilihan in rangePilihan:
        print("\nInput tidak valid")
        pilihan = input("Masukkan pilihan: ")

    return pilihan
