import streamlit as st
import pandas as pd
import numpy as np

st.title('Menghitung Volume Sebenarnya pada Perhitungan Alat Gelas Kalibrasi')

st.title('Perhitungan densitas air')
Suhu_air = st.number_input('Masukan nilai suhu air')

tombol = st.button('Hitung nilai densitas air')

if tombol:
    Nilai_densitas_air = 0,999974-((Suhu_air-3,989)**2*(Suhu_air+338,636))/(563385,4*(Suhu_air+72,45147))
    st.success(f'Nilai densitas air adalah (Nilai_densitas_air)')

