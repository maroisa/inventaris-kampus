import crud


def get_pilihan(message: str, num: int):
    rangePilihan = tuple(str(i) for i in range(1, num + 1))

    print(message)
    pilihan = input("Masukkan pilihan: ")

    while pilihan not in rangePilihan:
        print("\nInput tidak valid")
        pilihan = input("Masukkan pilihan: ")

    return pilihan


def menu_utama():
    while True:
        pilihan = get_pilihan(
            """==== MENU UTAMA ====
1. Tampilkan inventaris
2. Tambah inventaris
3. Pinjam barang
4. Kembalikan barang
5. Riwayat Peminjaman
6. Daftarkan peminjam
7. Tampilan peminjam
8. Keluar
""",
            8,
        )

        if pilihan == "1":
            res = crud.daftar_inventaris()
            print("\n===== DAFTAR INVENTARIS =====")
            for row in res:
                print(f"{row[0]} ({row[1]}) | Jumlah: {row[2]} | Kondisi: {row[3]}")
            input("Kembali...")
            continue

        if pilihan == "2":
            barang = crud.daftar_barang()
            print("\n==== PILIH BARANG ====")
            for i, b in enumerate(barang):
                print(f"{i + 1}. {b[1]}")
            print(f"{len(barang) + 1}. Kembali")

            p = get_pilihan("", len(barang) + 1)

            if int(p) == len(barang) + 1:
                continue

            item = barang[int(p) - 1]
            crud.tambah_inventaris(item[0])
            print(f"{item[1]} telah ditambahkan.")
            input("Kembali...")
            continue

        if pilihan == "3":
            res = crud.daftar_inventaris_tersedia()
            print("\n===== BARANG TERSEDIA =====")
            for row in res:
                print(f"ID {row[0]} | {row[1]} ({row[2]}) | Jumlah: {row[3]}")

            id_barang = input("Masukkan ID barang: ")
            inventaris = crud.cek_inventaris(id_barang)

            if not inventaris:
                print("Barang tidak tersedia.")
                input("Kembali...")
                continue

            peminjam = crud.daftar_peminjam()
            print("\n==== PILIH PEMINJAM ====")
            for i, p in enumerate(peminjam):
                print(f"{i + 1}. {p[2]} ({p[1]})")

            idx = int(input("Pilih peminjam: ")) - 1
            p_id = peminjam[idx][0]

            tgl_pinjam = input("Tanggal pinjam (YYYY-MM-DD): ")
            tgl_kembali = input("Tanggal kembali (YYYY-MM-DD): ")

            crud.pinjam_barang(p_id, inventaris[0], tgl_pinjam, tgl_kembali)
            print("Peminjaman berhasil.")
            input("Kembali...")
            continue

        if pilihan == "4":
            aktif = crud.daftar_peminjaman_aktif()
            if not aktif:
                print("Tidak ada peminjaman aktif.")
                input("Kembali...")
                continue

            print("\n==== PEMINJAMAN AKTIF ====")
            for a in aktif:
                print(f"ID Peminjaman: {a[0]} | {a[1]} | {a[2]} (Inventaris: {a[3]})")

            pilih = input("Masukkan ID peminjaman yang dikembalikan: ")
            kondisi = input("Kondisi kembali (baik/rusak): ")

            crud.kembalikan_barang(pilih, kondisi)
            print("Barang berhasil dikembalikan.")
            input("Kembali...")
            continue

        if pilihan == "5":
            data = crud.riwayat_peminjaman()
            print("\n==== RIWAYAT PEMINJAMAN ====")
            for r in data:
                print("-" * 30)
                print(f"ID Peminjaman: {r['id_peminjaman']}")
                print(f"Peminjam: {r['nama_peminjam']}")
                print(f"Barang: {r['nama_barang']} (Inv: {r['id_inventaris']})")
                print(f"Tanggal Pinjam: {r['tanggal_pinjam']}")
                print(f"Tanggal Kembali (rencana): {r['tanggal_kembali']}")
                print(f"Tanggal Dikembalikan: {r['tanggal_dikembalikan']}")
                print(f"Kondisi Kembali: {r['kondisi_kembali']}")
                print("-" * 30)
            input("Kembali...")
            continue

        if pilihan == "6":
            nim = input("NIM: ")
            nama = input("Nama: ")
            prodi = input("Prodi: ")

            crud.register_peminjam(nim, nama, prodi)
            print("Peminjam berhasil ditambahkan.")
            input("Kembali...")
            continue
        if pilihan == "7":
            peminjam = crud.daftar_peminjam()
            print("\n==== PILIH PEMINJAM ====")
            for i, p in enumerate(peminjam):
                print(f"{i + 1}. {p[2]} ({p[1]})")

            input("Kembali...")
            continue

        break


menu_utama()
