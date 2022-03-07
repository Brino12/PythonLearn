"""
Deteksi gempa
"""

def  ekstraksi_data():
    """
    Tanggal: 07 Maret 2022,
    Waktu: 10:47:23 WIB
    Magnitudo: 4.3
    Kedalaman: 10 km
    Lokasi: LS = 7.98  BT = 122.47
    Pusat Gempa: Pusat gempa berada di laut 66 km BaratLaut Larantukan
    Keterangan: Dirasakan (Skala MMI): I-II Larantuka, I-II Lembata
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '07 Maret 2022'
    hasil['waktu'] = '10:47:23 WIB'
    hasil['magnitudo'] = '4.3'
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls': 7.98, 'bt': 122.47}
    hasil['pusat'] = 'Pusat gempa berada di laut 66 km BaratLaut Larantukan'
    hasil['keterangan'] = 'Dirasakan (Skala MMI): I-II Larantuka, I-II Lembata'
    return hasil



def tampilkan_data(result):
    print('Gempa Terakhir Berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS = {result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Keterangan {result['keterangan']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)
