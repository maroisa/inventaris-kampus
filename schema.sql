drop table if exists detail_peminjaman;
drop table if exists inventaris;
drop table if exists peminjaman;

drop table if exists barang;
drop table if exists peminjam;

create type kondisi_inventaris_enum as enum('baik', 'rusak', 'dipinjam');
create type kondisi_enum as enum('baik', 'rusak');

create table barang (
    id_barang serial primary key,
    nama_barang varchar(100) not null unique,
    tipe_barang varchar(100) not null
);

create table peminjam (
    id_peminjam serial primary key,
    nim_peminjam varchar(20) not null unique,
    nama_peminjam varchar(100) not null,
    prodi varchar(100) not null
);

create table inventaris (
    id_inventaris serial primary key,
    id_barang int references barang,
    kondisi kondisi_inventaris_enum not null
);

create table peminjaman (
    id_peminjaman serial primary key,
    id_peminjam int references peminjam,
    tanggal_pinjam date default current_date,
    tanggal_kembali date not null,
    tanggal_dikembalikan date
);

create table detail_peminjaman (
    id_detail_peminjaman serial primary key,
    id_peminjaman int references peminjaman,
    id_inventaris int references inventaris,
    jumlah_barang int not null,
    kondisi_kembali kondisi_enum
);

insert into barang(nama_barang, tipe_barang) values
('Lenovo LOQ', 'Laptop'),
('Lenovo Thinkpad X1', 'Laptop'),
('Mikrotik hEX S', 'Router'),
('Cisco Catalyst 8300', 'Router'),
('VGA to HDMI', 'Adapter');

insert into peminjam(nim_peminjam, nama_peminjam, prodi) values
('K123121', 'John Doe', 'PTIK'),
('K123125', 'Foo', 'PTM'),
('K124012', 'Bar', 'PTB'),
('K124132', 'John Kenshi', 'Informatika');


insert into inventaris(id_barang, kondisi) values
(1, 'baik'),
(2, 'baik'),
(3, 'baik'),
(3, 'baik'),
(3, 'baik'),
(3, 'dipinjam'),
(3, 'dipinjam'),
(3, 'rusak'),
(4, 'baik'),
(4, 'baik'),
(5, 'baik');
