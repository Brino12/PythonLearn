import bs4

def ekstraksi_data():

    bs4.beautifulsoup("<p>some<b>bad<i>HTML")

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

print('Ini adalah package gempa terkini')