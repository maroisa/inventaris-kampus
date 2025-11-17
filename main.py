import menu
import crud


def menu_utama():
    pilihan = menu.get_pilihan(
        """==== MENU UTAMA ====
    1. Tampilkan inventaris
    2. Tambah inventaris
    3. Pinjam barang
    4. Kembalikan barang
    5. Daftarkan peminjam
    6. Keluar
    """,
        6,
    )

    match pilihan:
        case "1":
            res = crud.daftar_inventaris()
            print("\n" + "-" * 20)
            print("Daftar Barang")
            for i in res:
                print("-" * 20)
                print("Nama barang:", i[0] + " (" + i[1] + ")")
                print("Jumlah:", i[2])
                print("Kondisi:", i[3])
                print("-" * 20 + "\n")
            input("Input apapun untuk kembali...")
            menu_utama()
        case "2":
            res = crud.daftar_barang()
            pilihan = menu.get_pilihan("", len(res))
            item = res[int(pilihan) - 1]
            crud.tambah_inventaris(item[0])
            print("Barang " + item[1] + " telah ditambahkan ke inventaris!")
            input("Input apapun untuk kembali...")
            menu_utama()
        case _:
            return


menu_utama()
