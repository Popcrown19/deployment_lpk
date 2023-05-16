import streamlit as st
from streamlit_option_menu import option_menu

navbar = option_menu(menu_title=None, options=['Kalibrasi Alat Gelas','Kalkulator Kalibrasi','About Us'],default_index=0, icons=['0', '0','0'], styles={'nav-link' : {'text-align': 'center'}})

# Kalibrasi Alat Gelas #
if navbar == 'Kalibrasi Alat Gelas' :
    tab1, tab2 = st.tabs(['Penjelasan', 'Rumus'])
    with tab1 :
        st.title('Penjelasan')
        st.write('jgjhgj')
       
    with tab2 :
        st.title('Rumus')
        st.write('Menghitung Volume Sebenarnya : ')
        st.write('V20 = m(1 - y(t - 20))/(ρair - ρudara)')
        st.write('Menghitung Densitas Air : ')
        st.write('0.999974 - (ta - 3.989)^2 (ta + 338.636)/563385.4(ta + 72.45147)')
        st.write('Menghitung Densitas Udara : ')
        st.write('0.464554P - H(0.00252tu - 0.020582)/(237.15 + tu)1000')
        
        st.write('Keterangan :')
        st.write('V20 = Volume sebenarnya (mL)')
        st.write('m = Massa air (gram)')
        st.write('ρair = Densitas air (gram/mL)')
        st.write('ρudara = Densitas udara (gram/mL)')
        st.write('ta = Suhu air (°C)')
        st.write('tu = Suhu udara (°C)')
        st.write('y = Koefisien muai volume (°C^-1)')
    
# Kalkulator Kalibrasi #
if navbar == 'Kalkulator Kalibrasi' :
    tab1, tab2 = st.tabs(['PERHITUNGAN DENSITAS', 'PERHITUNGAN VOLUME SEBENARNYA'])
    with tab1 :
        st.title('Menghitung Volume Sebenarnya pada Perhitungan Alat Gelas Kalibrasi')
        st.title('Perhitungan densitas air (gram/mL)')
        Suhu_air = st.number_input('Masukan nilai suhu air (°C)', format='%.1f')
        tombol = st.button('Hitung nilai densitas air')
        if tombol:
            Nilai_densitas_air = 0.999974 - (((Suhu_air - 3.989)**2) * (Suhu_air + 338.636)) / (563385.4 * (Suhu_air + 72.45147))
            st.success(f'Nilai densitas air adalah' +str(Nilai_densitas_air))

        st.title('Perhitungan densitas udara (gram/mL)')
        Kelembaban_udara = st.number_input('Masukan nilai kelembaban udara (%)', format='%.1f')
        Tekanan_udara = st.number_input('Masukan nilai tekanan udara (mmHg)', format='%.1f')
        Suhu_udara = st.number_input('Masukan nilai suhu udara (°C)', format='%.1f')
        tombol = st.button('Hitung nilai densitas udara')
        if tombol:
            Nilai_densitas_udara = ((0.464554 * Tekanan_udara) - (Kelembaban_udara * (0.00252 * Suhu_udara - 0.020582)))/((237.15 + Suhu_udara) * 1000)
            st.success(f'Nilai densitas udara adalah'+str(Nilai_densitas_udara))

    with tab2 :
        st.title('Perhitungan Volume Sebenarnya (mL)')
        Massa_air = st.number_input('Masukan nilai massa air (gram)', format='%.4f')
        Koefisien_muai_volume = st.number_input('Masukan nilai koefisien muai volume (°C^-1)', format='%.4f')
        Suhu_air = st.number_input('Masukan nilai suhu air (°C)',key=1, format='%.1f')
        Densitas_air = st.number_input('Masukan nilai densitas air (gram/mL)', format='%.4f')
        Densitas_udara = st.number_input('Masukan nilai densitas udara (gram/mL)', format='%.4f')

        tombol = st.button('Hitung nilai volume sebenarnya')
        
        if tombol:
            Nilai_volume_sebenarnya = (Massa_air * (1 - Koefisien_muai_volume * (Suhu_air - 20))) / (Densitas_air - Densitas_udara)
            st.success(f'Nilai volume sebenarnya adalah'+str(Nilai_volume_sebenarnya))
        if Densitas_air == 0 or Densitas_udara == 0:
                st.write('ADA DATA YANG BELUM TERISI!')
            
# Home #
if navbar == 'About Us':
   
    st.title('About Us')
    st.write('blabkaboalakskds (ISI TEKS NANTI KALIMATNYA)')
    st.write('Nama Anggota :')
    st.write('Adelia Almas Nurvani - 2220440')
    st.write('Carolyn El Yire Penna Hutajulu - 2220450')
    st.write('Muhammad Rafi Fadhlurrohman - 2220470')
    st.write('Oasima Oktaviani Matondang - 2220480')
    st.write('Violin Febriani - 2220496')
    
    