""""
06 Maret 2022, 05:40:28 WIB
5.0
43 km
3.55 LU - 126.10 BT
67 km Tenggara TAHUNA-KEP.SANGIHE-SULUT
tidak berpotensi TSUNAMI
"""

def ekstraksi_data():

    hasil = dict()
    hasil['tanggal'] = '06 Maret 2022'
    hasil['waktu'] = '05:40:28 WIB'
    hasil['magnitudo'] = '5.0'
    hasil['kedalaman'] = '43 km'
    hasil['lokasi'] = {'LU': 3.55, 'BT': 126.10}
    hasil['potensi gempa'] = 'Tidak Berpotensi Tsunami'

    return hasil

def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi: LS={result['lokasi']['LS']}, BT={result['lokasi']['BT']}")
    print(f"potensi gempa {result['potensi gempa']}")

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)