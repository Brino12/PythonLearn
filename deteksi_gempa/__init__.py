import bs4
import requests


def ekstraksi_data():
    try:
        content = requests.get('https:bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        print(content.text)

        # soup = bs4.beautifulsoup(content)
        # print(soup.prettify())

        hasil = dict()
        hasil['tanggal'] = '06 Maret 2022'
        hasil['waktu'] = '05:40:28 WIB'
        hasil['magnitudo'] = '5.0'
        hasil['kedalaman'] = '43 km'
        hasil['lokasi'] = {'LU': 3.55, 'BT': 126.10}
        hasil['potensi gempa'] = 'Tidak Berpotensi Tsunami'
        return hasil
    else:
        return None

def tampilkan_data(result):

    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return

    print('Gempa Terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi: LS={result['lokasi']['LS']}, BT={result['lokasi']['BT']}")
    print(f"potensi gempa {result['potensi gempa']}")

print('Ini adalah package gempa terkini')