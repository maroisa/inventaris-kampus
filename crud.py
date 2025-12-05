from db import init_db

conn = init_db()
cursor = conn.cursor()

def daftar_inventaris():
    cursor.execute(
        """
        SELECT nama_barang, tipe_barang, COUNT(*) AS jumlah_barang, kondisi
        FROM inventaris i
        JOIN barang b USING(id_barang)
        GROUP BY id_barang, kondisi, nama_barang, tipe_barang
        ORDER BY id_barang
        """
    )
    return cursor.fetchall()


def daftar_inventaris_tersedia():
    cursor.execute(
        """
        SELECT id_barang, nama_barang, tipe_barang, COUNT(*) AS jumlah_barang
        FROM inventaris i
        JOIN barang b USING(id_barang)
        WHERE kondisi='baik'
        GROUP BY id_barang, nama_barang, tipe_barang
        ORDER BY id_barang
        """
    )
    return cursor.fetchall()


def daftar_barang():
    cursor.execute("SELECT * FROM barang")
    return cursor.fetchall()


def tambah_barang(nama, tipe):
    cursor.execute(
        "INSERT INTO barang(nama_barang, tipe_barang) VALUES (?, ?)",
        (nama, tipe),
    )
    conn.commit()


def cek_inventaris(id_barang):
    cursor.execute(
        """
        SELECT * FROM inventaris
        JOIN barang USING(id_barang)
        WHERE id_barang=? AND kondisi='baik'
        LIMIT 1
        """,
        (id_barang,),
    )
    return cursor.fetchone()


def tambah_inventaris(id_barang):
    cursor.execute(
        "INSERT INTO inventaris(id_barang, kondisi) VALUES (?, ?)",
        (id_barang, "baik"),
    )
    conn.commit()


def pinjam_barang(nama_peminjam, id_inventaris, tanggal_pinjam, tanggal_kembali):
    cursor.execute(
        """
        INSERT INTO peminjaman(nama_peminjam, tanggal_pinjam, tanggal_kembali)
        VALUES (?, ?, ?)
        """,
        (nama_peminjam, tanggal_pinjam, tanggal_kembali),
    )
    id_peminjaman = cursor.lastrowid

    cursor.execute(
        """
        INSERT INTO detail_peminjaman(id_peminjaman, id_inventaris, jumlah_barang)
        VALUES (?, ?, 1)
        """,
        (id_peminjaman, id_inventaris),
    )

    cursor.execute(
        "UPDATE inventaris SET kondisi='dipinjam' WHERE id_inventaris=?",
        (id_inventaris,),
    )

    conn.commit()
    return id_peminjaman

def daftar_peminjaman_aktif():
    cursor.execute(
        """
        SELECT p.id_peminjaman, nama_peminjam, b.nama_barang, i.id_inventaris
        FROM peminjaman p
        JOIN detail_peminjaman dp ON dp.id_peminjaman = p.id_peminjaman
        JOIN inventaris i ON i.id_inventaris = dp.id_inventaris
        JOIN barang b ON b.id_barang = i.id_barang
        WHERE p.tanggal_dikembalikan IS NULL
        """
    )
    return cursor.fetchall()


def kembalikan_barang(id_peminjaman, kondisi_kembali):
    cursor.execute(
        "SELECT id_inventaris FROM detail_peminjaman WHERE id_peminjaman=?",
        (id_peminjaman,),
    )
    row = cursor.fetchone()
    id_inventaris = row["id_inventaris"]

    cursor.execute(
        "UPDATE inventaris SET kondisi=? WHERE id_inventaris=?",
        (kondisi_kembali, id_inventaris),
    )

    cursor.execute(
        "UPDATE peminjaman SET tanggal_dikembalikan = DATE('now') WHERE id_peminjaman=?",
        (id_peminjaman,),
    )

    cursor.execute(
        "UPDATE detail_peminjaman SET kondisi_kembali=? WHERE id_peminjaman=?",
        (kondisi_kembali, id_peminjaman),
    )

    conn.commit()


def riwayat_peminjaman():
    cursor.execute(
        """
        SELECT
            p.id_peminjaman,
            nama_peminjam,
            b.nama_barang,
            i.id_inventaris,
            p.tanggal_pinjam,
            p.tanggal_kembali,
            p.tanggal_dikembalikan,
            dp.kondisi_kembali
        FROM peminjaman p
        JOIN detail_peminjaman dp ON dp.id_peminjaman = p.id_peminjaman
        JOIN inventaris i ON i.id_inventaris = dp.id_inventaris
        JOIN barang b ON b.id_barang = i.id_barang
        ORDER BY p.id_peminjaman DESC
        """
    )
    return cursor.fetchall()
