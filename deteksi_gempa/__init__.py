
import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('Li')
        i = 0
        magnitudo = None
        ls = None
        bt = None

        for res in result:
            print(i, res)
            if i = 1:
                magnitudo = res.text
            elif i == 2:
                lokasi =




        hasil = dict()
        hasil['tanggal'] = tanggal.text #'06 Maret 2022'
        hasil['waktu'] = waktu #'05:40:28 WIB'
        hasil['magnitudo'] = magnitudo #'5.0'
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