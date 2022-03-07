import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        tarik = soup.find('span', {'class': 'waktu'})
        tarik = tarik.text.split(', ')
        tanggal = tarik[0]
        waktu = tarik[1]

        tekan = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        tekan = tekan.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        kedalaman = None
        lokasi = None
        dirasakan = None

        for res in tekan:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: LS = {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")

