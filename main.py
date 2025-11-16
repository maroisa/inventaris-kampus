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
    """,
        5,
    )

    match pilihan:
        case "1":
            crud.tampilkan_inventaris()
            menu_utama()


menu_utama()
