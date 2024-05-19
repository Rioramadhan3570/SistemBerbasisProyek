# SISTEM PAKAR DIAGNOSA JENIS KULIT WAJAH
rule_penyakit = {
    'P01': ['G01', 'G02', 'G03', 'G04', 'G05', 'G06', 'G11'],
    'P02': ['G07', 'G08', 'G09', 'G16'],
    'P03': ['G01', 'G05', 'G10', 'G11', 'G12'],
    'P04': ['G07', 'G14', 'G15', 'G16', 'G17'],
    'P05': ['G12', 'G18', 'G19', 'G20']
}

data_nilai_pakar = {
    ('P01', 'G01'): 0.8,
    ('P01', 'G02'): 0.5,
    ('P01', 'G03'): 0.8,
    ('P01', 'G04'): 0.8,
    ('P01', 'G05'): 0.8,
    ('P01', 'G06'): 0.7,
    ('P02', 'G07'): 0.9,
    ('P02', 'G08'): 0.9,
    ('P02', 'G02'): 0.5,
    ('P02', 'G09'): 0.9,
    ('P02', 'G10'): 0.9,
    ('P03', 'G11'): 1.0,
    ('P03', 'G09'): 0.3,
    ('P03', 'G10'): 0.4,
    ('P03', 'G12'): 0.2,
    ('P03', 'G13'): 1.0,
    ('P04', 'G08'): 1.0,
    ('P04', 'G14'): 1.0,
    ('P04', 'G15'): 0.2,
    ('P05', 'G16'): 0.3,
    ('P05', 'G17'): 0.9,
    ('P05', 'G02'): 0.5,
    ('P05', 'G15'): 1.0,
    ('P06', 'G07'): 1.0,
    ('P06', 'G15'): 0.4,
    ('P06', 'G18'): 0.2,
    ('P07', 'G19'): 1.0,
    ('P07', 'G15'): 0.5,
    ('P07', 'G20'): 0.9,
    ('P07', 'G18'): 0.3,
    ('P08', 'G02'): 0.8,
    ('P08', 'G17'): 0.8,
    ('P08', 'G15'): 0.5,
    ('P09', 'G21'): 1.0,
    ('P09', 'G22'): 1.0,
    ('P09', 'G02'): 0.8,
    ('P10', 'G23'): 1.0,
    ('P10', 'G24'): 1.0,
    ('P10', 'G02'): 0.8,
}

data_gejala = {
    'G01': 'Diare berskala',
    'G02': 'Demam',
    'G03': 'Ada lendir',
    'G04': 'Bulu kusam',
    'G05': 'Perut besar, badan kecil',
    'G06': 'Makan banyak, kurus',
    'G07': 'Diare',
    'G08': 'Muntah',
    'G09': 'Anoreksia',
    'G10': 'Hipotermia',
    'G11': 'Gatal',
    'G12': 'Pruritus',
    'G13': 'Ruam kulit',
    'G14': 'Kembung',
    'G15': 'Nafsu makan berkurang',
    'G16': 'Flu',
    'G17': 'Sariawan',
    'G18': 'Lemes',
    'G19': 'Gakbisa pipis',
    'G20': 'Vu besar',
    'G21': 'Garuk telinga',
    'G22': 'Telinga bau, bernanah',
    'G23': 'Mata merah',
    'G24': 'Mata berair',
}

data_penyakit = {
    'P01': 'Helmintiasis',
    'P02': 'Panleukopenia',
    'P03': 'Scabies',
    'P04': 'Gastritis',
    'P05': 'Calicivirus',
    'P06': 'Enteritis',
    'P07': 'FUS',
    'P08': 'Gigiostomatitis',
    'P09': 'Otitis',
    'P10': 'Clamydia',
}

# Fungsi untuk menghitung CF kombinasi
def hitung_cf_kombinasi(nilai_user, nilai_pakar):
    return nilai_user * nilai_pakar

# Fungsi untuk menghitung CF gabungan
def hitung_cf_gabungan(cf1, cf2):
    return cf1 + cf2 - (cf1 * cf2)

# Menampilkan keterangan gejala
print("Keterangan Gejala:")
for kode_gejala, nama_gejala in data_gejala.items():
    print(f"{kode_gejala}: {nama_gejala}")
print()

# Menampilkan keterangan penyakit
print("Keterangan Penyakit:")
for kode_penyakit, nama_penyakit in data_penyakit.items():
    print(f"{kode_penyakit}: {nama_penyakit}")
print()


# Input gejala dari pengguna
gejala_input = []
while True:
    kode_gejala = input("Masukkan Kode Gejala yang Anda Alami / Tekan Enter untuk Selesai : ")
    if kode_gejala == "":
        break
    nilai_gejala = float(input(f"Masukkan Nilai untuk Gejala {data_gejala.get(kode_gejala, 'tidak valid')} (0-1): "))
    gejala_input.append((kode_gejala, nilai_gejala))
    print()

# Output
for penyakit, gejala_list in rule_penyakit.items():
    for gejala, nilai_user in gejala_input:
        if gejala in gejala_list:
            nilai_pakar = data_nilai_pakar.get((penyakit, gejala), 0)
            cf_kombinasi = hitung_cf_kombinasi(nilai_user, nilai_pakar)
            print(f"Kode Penyakit: {penyakit}, Kode Gejala: {gejala}, CF Kombinasi: {cf_kombinasi}")
    if all(data_nilai_pakar.get((penyakit, gejala), 0) == 0 for gejala, _ in gejala_input):
        print(f"Kode Penyakit: {penyakit}, CF Kombinasi: 0")


# Menampilkan hasil kesimpulan
print()
print("Beberapa Kemungkinan Penyakit yang Anda Alami:")
for penyakit in rule_penyakit:
    cf_gabungan = 0
    count = 0
    for gejala, nilai_user in gejala_input:
        if gejala in rule_penyakit[penyakit]:
            nilai_pakar = data_nilai_pakar.get((penyakit, gejala), 0)
            cf_kombinasi = hitung_cf_kombinasi(nilai_user, nilai_pakar)
            if cf_gabungan == 0:
                cf_gabungan = cf_kombinasi
            else:
                cf_gabungan = hitung_cf_gabungan(cf_gabungan, cf_kombinasi)
            count += 1
    if count > 0:
        print(f"- {data_penyakit[penyakit]} ({penyakit}): {cf_gabungan * 100}%")