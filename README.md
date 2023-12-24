# Cosmetic Products Stock Management System

![plot](https://github.com/senakurtak/dbms-project/assets/101430394/d7320453-48d9-4db2-b0d0-ad0563a0c92c)


## Functionalities

* Create Tables

```sql
CREATE TABLE kategoriler (
	kategori_id serial4 NOT NULL,
	kategori_adi varchar(255) NOT NULL,
	CONSTRAINT kategoriler_pkey PRIMARY KEY (kategori_id)
);

CREATE TABLE stok_hareketleri (
	hareket_id serial4 NOT NULL,
	urun_id int4 NULL,
	miktar int4 NULL,
	hareket_tarihi date NULL,
	hareket_tipi varchar(50) NULL,
	CONSTRAINT stok_hareketleri_pkey PRIMARY KEY (hareket_id)
);

CREATE TABLE ureticiler (
	uretici_id serial4 NOT NULL,
	firma_adi varchar(255) NOT NULL,
	iletisim_bilgileri text NULL,
	CONSTRAINT ureticiler_pkey PRIMARY KEY (uretici_id)
);


CREATE TABLE urunler (
	urun_id serial4 NOT NULL,
	urun_adi varchar(255) NOT NULL,
	kategori_id int4 NULL,
	uretici_id int4 NULL,
	birim_fiyati numeric(10, 2) NULL,
	renk bpchar(7) NULL,
	hacim int4 NULL,
	CONSTRAINT urunler_pkey PRIMARY KEY (urun_id)
);

ALTER TABLE urunler ADD CONSTRAINT urunler_kategori_id_fkey FOREIGN KEY (kategori_id) REFERENCES kategoriler(kategori_id);
ALTER TABLE urunler ADD CONSTRAINT urunler_uretici_id_fkey FOREIGN KEY (uretici_id) REFERENCES ureticiler(uretici_id);
```

* Add subjects to a stok_hareketleri
```sql
INSERT INTO stok_hareketleri (hareket_id, urun_id, miktar, hareket_tarihi, hareket_tipi) VALUES 
(1, 20, '2023-01-01', 'Giriş'),
(2, 15, '2023-01-02', 'Giriş'),
```
