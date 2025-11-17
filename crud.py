from db import init_db

conn = init_db()
cursor = conn.cursor()


def daftar_inventaris():
    cursor.execute(
        "select nama_barang, tipe_barang, count(*) as jumlah_barang, kondisi "
        "from inventaris i join barang b using (id_barang) "
        "group by id_barang, kondisi, nama_barang, tipe_barang "
        "order by id_barang;"
    )
    return cursor.fetchall()


def daftar_inventaris_tersedia():
    cursor.execute(
        "select id_barang, nama_barang, tipe_barang, count(*) as jumlah_barang "
        "from inventaris i join barang b using (id_barang) "
        "where kondisi='baik' "
        "group by id_barang, kondisi, nama_barang, tipe_barang "
        "order by id_barang;"
    )
    return cursor.fetchall()


def daftar_barang():
    cursor.execute("select * from barang")
    return cursor.fetchall()


def tambah_barang(nama, tipe):
    cursor.execute(
        "insert into barang(nama_barang, tipe_barang) values (%s, %s)", (nama, tipe)
    )
    conn.commit()


def cek_inventaris(id_barang):
    cursor.execute(
        "select * from inventaris join barang using(id_barang) "
        "where id_barang=%s and kondisi='baik' limit 1",
        (id_barang,),
    )
    return cursor.fetchone()


def tambah_inventaris(id_barang):
    cursor.execute(
        "insert into inventaris(id_barang, kondisi) values (%s, %s)",
        (id_barang, "baik"),
    )
    conn.commit()


def register_peminjam(nim, nama, prodi):
    cursor.execute(
        "insert into peminjam(nim_peminjam, nama_peminjam, prodi) values (%s,%s,%s)",
        (nim, nama, prodi),
    )
    conn.commit()


def pinjam_barang(id_peminjam, id_inventaris, tanggal_pinjam, tanggal_kembali):
    cursor.execute(
        "insert into peminjaman(id_peminjam, tanggal_pinjam, tanggal_kembali) "
        "values (%s, %s, %s) returning id_peminjaman",
        (id_peminjam, tanggal_pinjam, tanggal_kembali),
    )
    id_peminjaman = cursor.fetchone()[0]

    cursor.execute(
        "insert into detail_peminjaman(id_peminjaman, id_inventaris, jumlah_barang) "
        "values (%s, %s, %s)",
        (id_peminjaman, id_inventaris, 1),
    )

    cursor.execute(
        "update inventaris set kondisi='dipinjam' where id_inventaris=%s",
        (id_inventaris,),
    )

    conn.commit()
    return id_peminjaman


def daftar_peminjam():
    cursor.execute("select * from peminjam")
    return cursor.fetchall()


def daftar_peminjaman_aktif():
    cursor.execute(
        "select p.id_peminjaman, pm.nama_peminjam, b.nama_barang, i.id_inventaris "
        "from peminjaman p "
        "join peminjam pm on pm.id_peminjam = p.id_peminjam "
        "join detail_peminjaman dp on dp.id_peminjaman = p.id_peminjaman "
        "join inventaris i on i.id_inventaris = dp.id_inventaris "
        "join barang b on b.id_barang = i.id_barang "
        "where tanggal_dikembalikan is null"
    )
    return cursor.fetchall()


def kembalikan_barang(id_peminjaman, kondisi_kembali):
    cursor.execute(
        "select id_inventaris from detail_peminjaman where id_peminjaman=%s",
        (id_peminjaman,),
    )
    id_inventaris = cursor.fetchone()[0]

    cursor.execute(
        "update inventaris set kondisi=%s where id_inventaris=%s",
        (kondisi_kembali, id_inventaris),
    )

    cursor.execute(
        "update peminjaman set tanggal_dikembalikan=current_date "
        "where id_peminjaman=%s",
        (id_peminjaman,),
    )

    cursor.execute(
        "update detail_peminjaman set kondisi_kembali=%s where id_peminjaman=%s",
        (kondisi_kembali, id_peminjaman),
    )

    conn.commit()
