def hitung_total_nilai(data_nilai_akhir):
  total_nilai = sum(data_nilai_akhir.values())
  jumlah_mahasiswa = len(data_nilai_akhir)
  return total_nilai, total_nilai / jumlah_mahasiswa


def hitung_nilai_akhir(nilai_uts, nilai_uas):
  return ((nilai_uts + nilai_uas) / 2)


def tampilkan_nilai_akhir(data_nilai_akhir):
   print("\nHasil Nilai Akhir Mahasiswa:")
   for i, (nama, nilai_akhir) in enumerate(data_nilai_akhir.items()):
     print("Nama: {}, Nilai akhir = {:.2f}".format(nama, nilai_akhir))
   total_nilai, rata_rata = hitung_total_nilai(data_nilai_akhir)
   print("\nTotal Nilai Seluruh Mahasiswa:", total_nilai)
   print("Rata-rata Nilai Mahasiswa: {:.2f}". format(rata_rata))


def main():
  data_mahasiswa = {
    "Larynt": (75.6, 85),
    "Sawfa": (87, 95),
    "Kenanga": (100, 98.5),
  }

  # Menghitung nilai akhir
  for nama, (nilai_uts, nilai_uas) in data_mahasiswa.items():
    data_mahasiswa[nama] = hitung_nilai_akhir(nilai_uts, nilai_uas)

  tampilkan_nilai_akhir(data_mahasiswa)

if __name__ == "__main__":
  main()