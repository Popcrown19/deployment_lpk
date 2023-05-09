import streamlit as st

st.title('Menghitung Volume Sebenarnya pada Perhitungan Alat Gelas Kalibrasi')

st.title('Perhitungan densitas air')
Suhu_air = st.number_input('Masukan nilai suhu air')

tombol = st.button('Hitung nilai densitas air')

if tombol:
    Nilai_densitas_air = 0.999974 - (((Suhu_air - 3.989)**2) * (Suhu_air + 338.636)) / (563385.4 * (Suhu_air + 72.45147))
    st.success(f'Nilai densitas air adalah' +str(Nilai_densitas_air))

st.title('Perhitungan densitas udara')
Kelembaban_udara = st.number_input('Masukan nilai kelembaban udara')
Tekanan_udara = st.number_input('Masukan nilai tekanan udara')
Suhu_udara = st.number_input('Masukan nilai suhu udara')

tombol = st.button('Hitung nilai densitas udara')

if tombol:
    Nilai_densitas_udara = ((0.464554 * Tekanan_udara) - (Kelembaban_udara * (0.00252 * Suhu_udara - 0.020582)))/((237.15 + Suhu_udara) * 1000)
    st.success(f'Nilai densitas udara adalah'+str(Nilai_densitas_udara))

st.title('Perhitungan Volume Sebenarnya')
Massa_air = st.number_input('Masukan nilai massa air')
Koefisien_muai_volume = st.number_input('Masukan nilai koefisien muai volume')
Suhu_air = st.number_input('Masukan nilai suhu air',key=1)
Densitas_air = st.number_input('Masukan nilai densitas air')
Densitas_udara = st.number_input('Masukan nilai densitas udara')

tombol = st.button('Hitung nilai volume sebenarnya')

if tombol:
    Nilai_volume_sebenarnya = (Massa_air * (1 - Koefisien_muai_volume * (Suhu_air - 20))) / (Densitas_air - Densitas_udara)
    st.success(f'Nilai volume sebenarnya adalah'+str(Nilai_volume_sebenarnya))


