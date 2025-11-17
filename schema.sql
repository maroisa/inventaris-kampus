DROP TABLE IF EXISTS detail_peminjaman;
DROP TABLE IF EXISTS peminjaman;
DROP TABLE IF EXISTS inventaris;
DROP TABLE IF EXISTS peminjam;
DROP TABLE IF EXISTS barang;

CREATE TABLE barang (
    id_barang INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_barang TEXT NOT NULL UNIQUE,
    tipe_barang TEXT NOT NULL
);

CREATE TABLE peminjam (
    id_peminjam INTEGER PRIMARY KEY AUTOINCREMENT,
    nim_peminjam TEXT NOT NULL UNIQUE,
    nama_peminjam TEXT NOT NULL,
    prodi TEXT NOT NULL
);

CREATE TABLE inventaris (
    id_inventaris INTEGER PRIMARY KEY AUTOINCREMENT,
    id_barang INTEGER,
    kondisi TEXT CHECK(kondisi IN ('baik', 'rusak', 'dipinjam')) NOT NULL,
    FOREIGN KEY(id_barang) REFERENCES barang(id_barang)
);

CREATE TABLE peminjaman (
    id_peminjaman INTEGER PRIMARY KEY AUTOINCREMENT,
    id_peminjam INTEGER,
    tanggal_pinjam TEXT DEFAULT CURRENT_DATE,
    tanggal_kembali TEXT NOT NULL,
    tanggal_dikembalikan TEXT,
    FOREIGN KEY(id_peminjam) REFERENCES peminjam(id_peminjam)
);

CREATE TABLE detail_peminjaman (
    id_detail_peminjaman INTEGER PRIMARY KEY AUTOINCREMENT,
    id_peminjaman INTEGER,
    id_inventaris INTEGER,
    jumlah_barang INTEGER NOT NULL,
    kondisi_kembali TEXT CHECK(kondisi_kembali IN ('baik', 'rusak')),
    FOREIGN KEY(id_peminjaman) REFERENCES peminjaman(id_peminjaman),
    FOREIGN KEY(id_inventaris) REFERENCES inventaris(id_inventaris)
);

INSERT INTO barang(nama_barang, tipe_barang) VALUES
('Lenovo LOQ', 'Laptop'),
('Lenovo Thinkpad X1', 'Laptop'),
('Mikrotik hEX S', 'Router'),
('Cisco Catalyst 8300', 'Router'),
('VGA to HDMI', 'Adapter');

INSERT INTO peminjam(nim_peminjam, nama_peminjam, prodi) VALUES
('K123121', 'John Doe', 'PTIK'),
('K123125', 'Foo', 'PTM'),
('K124012', 'Bar', 'PTB'),
('K124132', 'John Kenshi', 'Informatika');

INSERT INTO inventaris(id_barang, kondisi) VALUES
(1,'baik'),
(2,'baik'),
(3,'baik'),
(3,'baik'),
(3,'baik'),
(3,'dipinjam'),
(3,'dipinjam'),
(3,'rusak'),
(4,'baik'),
(4,'baik'),
(5,'baik');
