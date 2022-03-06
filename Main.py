""""
06 Maret 2022, 05:40:28 WIB
5.0
43 km
3.55 LU - 126.10 BT
67 km Tenggara TAHUNA-KEP.SANGIHE-SULUT
tidak berpotensi TSUNAMI
"""
import deteksi_gempa

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = deteksi_gempa.ekstraksi_data()
    deteksi_gempa.tampilkan_data(result)