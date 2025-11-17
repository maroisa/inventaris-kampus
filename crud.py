from db import init_db

conn = init_db()
cursor = conn.cursor()


def daftar_inventaris():
    cursor.execute(
        "select nama_barang, tipe_barang, count(*) as jumlah_barang, kondisi from inventaris i join barang b using (id_barang) group by id_barang, kondisi, nama_barang, tipe_barang order by id_barang;"
    )
    result = cursor.fetchall()

    return result


def daftar_inventaris_tersedia():
    cursor.execute(
        "select nama_barang, tipe_barang, count(*) as jumlah_barang from inventaris i join barang b using (id_barang) where kondisi='baik' group by id_barang, kondisi, nama_barang, tipe_barang order by id_barang;"
    )
    result = cursor.fetchall()

    print("\n" + "-" * 20)
    print("Daftar Barang")
    for i in result:
        print("-" * 20)
        print(i[0] + " (" + i[1] + ")")
        print("Jumlah:", i[2])
        print("-" * 20 + "\n")


def daftar_barang():
    cursor.execute("select * from barang")
    res = cursor.fetchall()
    print("-" * 20)
    print("Daftar barang")
    print("-" * 20)
    for i in range(len(res)):
        print(f"{i + 1}.", res[i][1])
    return res


def tambah_barang(nama, tipe):
    cursor.execute(
        "insert into barang(nama_barang, tipe_barang) values (%s, %s)", (nama, tipe)
    )
    conn.commit()


def tambah_inventaris(id_barang):
    cursor.execute(
        "insert into inventaris(id_barang, kondisi) values (%s, %s)",
        (id_barang, "baik"),
    )
    conn.commit()


def register_peminjam(nim, nama, prodi):
    cursor.execute(
        "insert into peminjam(nim_peminjam, nama_peminjam, prodi), values(%s,%s,%s)",
        (nim, nama, prodi),
    )

    conn.commit()


def pinjam_barang(tanggal_pinjam, tanggal_kembali):
    pass


def kembalikan_barang():
    pass
