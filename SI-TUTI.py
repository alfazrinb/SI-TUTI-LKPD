# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: siddhardhan
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
# mutasi_model = pickle.load(open("D:\\BPK Perwakilan Provinsi Maluku\\DAC\\DAC\\SI-REMPA\\model_mutasi_pegawai_fix_banget.sav", "rb"))
ketua_tim_model = pickle.load(open("model_pembentukan_ketua_tim.sav", "rb"))
anggota_tim_model = pickle.load(open("model_pembentukan_anggota_tim.sav", "rb"))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('SI TUTI LKPD (Sistem Penentuan Tim LKPD)',
                          
                          ['Rekomendasi Ketua Tim',
                          'Rekomendasi Anggota Tim'],
                          icons=['person','activity'],
                          default_index=0
                          )

def get_str(n):
    if (n == 0):
        prediksi_kt = f'Anthony Valentino Poluan'
    elif (n == 1):
        prediksi_kt = f'Anugerah Risky Agung Garuda Dipratama'
    elif (n == 2):
        prediksi_kt = f'Ervin Rifian'
    elif (n == 3):
        prediksi_kt = f'Fuad Fauzi'
    elif (n == 4):
        prediksi_kt = f'Gusti Agung Diah Krisnawati'
    elif (n == 5):
        prediksi_kt = f'Indra Trijadi'
    elif (n == 6):
        prediksi_kt = f'Irwan Wicaksono'
    elif (n == 7):
        prediksi_kt = f'Leonardo Amarduan'
    elif (n == 8):
        prediksi_kt = f'Mario Bayu Prasetya Putra'
    elif (n == 9):
        prediksi_kt = f'Melisa Elfrida Situngkir'
    elif (n == 10):
        prediksi_kt = f'Mhd Nugraha Harahap'
    elif (n == 11):
        prediksi_kt = f'Yogi Yogaswara'
    else:
        prediksi_kt = f'Yusman Sumantri'
    return prediksi_kt

# Mutasi Prediction Page
if (selected == 'Rekomendasi Ketua Tim'):
    
    # page title
    # st.title('Prediksi Mutasi Pegawai Dengan Machine Learning')
    st.markdown("<h1 style='text-align: center; color: Black;'>Sistem Penentuan Ketua Tim LKPD</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1 :
        Gender = st.selectbox('Gender', ["Pria","Wanita"])
        
        if Gender == "Pria" :
            Gender = 0
        else :
            Gender = 1
    with col2 :

        Jurusan = st.selectbox('Latar Belakang Pendidikan',
                           ['Akuntansi', 'Ekonomi Pembangunan', 'Ilmu Ekonomi Studi Pembangunan', 
                            'Ilmu Hukum', 'Ilmu Komunikasi', 'Ilmu Statistik', 'Manajemen', 
                            'Sastra Inggris', 'Teknik Informatika', 'Teknik Lingkungan', 'Teknik Sipil'])

        if Jurusan == "Akuntansi":
            Jurusan = 0
        elif Jurusan == "Ekonomi Pembangunan":
            KodePangkat = 1
        elif Jurusan == "Ilmu Ekonomi Studi Pembangunan":
            Jurusan = 2
        elif Jurusan == "Ilmu Hukum":
            Jurusan = 3
        elif Jurusan == "Ilmu Komunikasi":
            Jurusan = 4
        elif Jurusan == 'Ilmu Statistik':
            Jurusan = 5
        elif Jurusan== "Manajemen":
            Jurusan = 6
        elif Jurusan == "Sastra Inggris":
            Jurusan = 7
        elif Jurusan == "Teknik Informatika":
            Jurusan = 8
        elif Jurusan == "Teknik Lingkungan":
            Jurusan = 9
        else :
            Jurusan = 10

    with col1:

        Strata_Pendidikan = st.selectbox('Strata Pendidikan', ['S1','S2'])

        if Strata_Pendidikan == 'S1':
            Strata_Pendidikan = 0
        else :
            Strata_Pendidikan = 1
    with col2:

        Riwayat_Entitas = st.selectbox('Entitas',
                                   ['Kabupaten Buru', 'Kabupaten Buru Selatan', 'Kabupaten Maluku Barat Daya', 
                                    'Kabupaten Maluku Tengah', 'Kabupaten Maluku Tenggara', 'Kabupaten Tanimbar',
                                    'Kepulauan Aru', 'Kota Tual', 'Pemerintah Kota Ambon', 'Provinsi Maluku', 
                                    'Seram Bagian Barat', 'Seram Bagian Timur'])

        if Riwayat_Entitas == 'Kabupaten Buru':
            Riwayat_Entitas = 0
        elif Riwayat_Entitas == 'Kabupaten Buru Selatan':
            Riwayat_Entitas = 1
        elif Riwayat_Entitas == 'Kabupaten Maluku Barat Daya':
            Riwayat_Entitas = 2
        elif Riwayat_Entitas == 'Kabupaten Maluku Tengah':
            Riwayat_Entitas = 3
        elif Riwayat_Entitas == 'Kabupaten Maluku Tenggara':
            Riwayat_Entitas = 4
        elif Riwayat_Entitas == 'Kabupaten Tanimbar':
            Riwayat_Entitas = 5
        elif Riwayat_Entitas == 'Kepulauan Aru':
            Riwayat_Entitas = 6
        elif Riwayat_Entitas == 'Kota Tual':
            Riwayat_Entitas = 7
        elif Riwayat_Entitas == 'Pemerintah Kota Ambon':
            Riwayat_Entitas = 8
        elif Riwayat_Entitas == 'Provinsi Maluku':
            Riwayat_Entitas = 9
        elif Riwayat_Entitas == 'Seram Bagian Barat':
            Riwayat_Entitas = 10
        else :
            Riwayat_Entitas = 11
    
    with col1:
        Opini = st.selectbox('Opini Sebelumnya',['TMP', 'WDP', 'WTP'])

        if Opini == 'TMP':
            Opini = 0
        elif Opini == 'WDP':
            Opini = 1
        else :
            Opini = 3
    with col2:
        Anggaran_Pendapatan = st.text_input('Anggaran Pendapatan')
    
    with col1:
        Realisasi_Pendaptan = st.text_input('Realisasi Pendaptan')
    
    with col2:
        Anggaran_Belanja = st.text_input('Anggaran Belanja')
    
    with col1:
        Realisasi_Belanja = st.text_input('Realisasi Belanja')
    
    with col2:
        Total_Aset = st.text_input('Total Aset')
    
    # code for Prediction
    prediksi_kt = ''
    
    # creating a button for Prediction
    s1=None
    s2=None
    
    if st.button('Rekomendasi'):
        ketua_tim = ketua_tim_model.predict_proba([[Gender, Jurusan, Strata_Pendidikan, Riwayat_Entitas, Opini,
                                                        Anggaran_Pendapatan, Realisasi_Pendaptan, Anggaran_Belanja,
                                                        Realisasi_Belanja, Total_Aset]])                          
        a, b = np.argsort(ketua_tim,axis=1)[0][-2:]
        s1=get_str(a)
        s2=get_str(b)
    
    f'Berikut Pegawai yang Direkomendasikan untuk Pemeriksaan Pada Entitas {Riwayat_Entitas}'    
    st.success(s1)
    st.success(s2)

###################### Rekomendasi Anggota Tim ##############################
def get_str(n):
    if (n == 0):
        prediksi_satker = f'A. ZHUNNUR AENI BAHARUDDIN'
    elif (n == 1):
        prediksi_satker = f'ADIL GANGSAR AGINDA'
    elif (n == 2):
        prediksi_satker = f'ADITYA BARMITZVAH INA'
    elif (n == 3):
        prediksi_satker = f'AINUL MUHAIDIR'
    elif (n == 4):
        prediksi_satker = f'ALFAZRIN BANAPON'
    elif (n == 5):
        prediksi_satker = f'ANDREAN ARIF SUHANDA'
    elif (n == 6):
        prediksi_satker = f'AZIF FAISAL ALBARI'
    elif (n == 7):
        prediksi_satker = f'Aditya Wahyu Dewanggajati'
    elif (n == 8):
        prediksi_satker = f'BURHAMSYAH AMIN'
    elif (n == 9):
        prediksi_satker = f'DANIEL PATA`SAUNG'
    elif (n == 10):
        prediksi_satker = f'DHYARTOMA PANDHU ISKANDAR'
    elif (n == 11):
        prediksi_satker = f'DIO PRAM PERMADI'
    elif (n == 12):
        prediksi_satker = f'Dyah Pythaloka'
    elif (n == 13):
        prediksi_satker = f'ERIK SUSANTO BARA'
    elif (n == 14):
        prediksi_satker = f'FAIZAL TAUFIK IBRAHIM'
    elif (n == 15):
        prediksi_satker = f'FAJAR ADE PUTRA'
    elif (n == 16):
        prediksi_satker = f'FAJAR ALY'
    elif (n == 17):
        prediksi_satker = f'FARIDA HEMAS MARDIKAYANTI'
    elif (n == 18):
        prediksi_satker = f'FIHARA FITRIANY'
    elif (n == 19):
        prediksi_satker = f'GANIS ARIFIA NINGRUM'
    elif (n == 20):
        prediksi_satker = f'GUPITA PERMATANINGAYU'
    elif (n == 21):
        prediksi_satker = f'HAFIZ MAHMUD AHMAD'
    elif (n == 22):
        prediksi_satker = f'Indri Alvera S.Turnip'
    elif (n == 23):
        prediksi_satker = f'KADEK ANGGIANA DWI CAHYANI'
    elif (n == 24):
        prediksi_satker = f'KARTINI'
    elif (n == 25):
        prediksi_satker = f'KHOIMATUN NAQIYAH'
    elif (n == 26):
        prediksi_satker = f'LISA RULYANTINI MUNASSAR'
    elif (n == 27):
        prediksi_satker = f'MARDIANA LATIFAH'
    elif (n == 28):
        prediksi_satker = f'MUHAMMAD ILHAM AKBAR'
    elif (n == 29):
        prediksi_satker = f'Muhamad Indro Swasono'
    elif (n == 30):
        prediksi_satker = f'Muhammad Taufiqurahman'
    elif (n == 31):
        prediksi_satker = f'NIKO PUSPAWARDANA'
    elif (n == 32):
        prediksi_satker = f'OKKY CAROLINA'
    elif (n == 33):
        prediksi_satker = f'PRIMA ARISTAMA'
    elif (n == 34):
        prediksi_satker = f'Putu Tirtana Setiawan'
    elif (n == 35):
        prediksi_satker = f'RINALDY'
    elif (n == 36):
        prediksi_satker = f'RISNA RIDHAYANA'
    elif (n == 37):
        prediksi_satker = f'Ronal Polatua Panggabean'
    elif (n == 38):
        prediksi_satker = f'Ronald Dustin Kastanya'
    elif (n == 39):
        prediksi_satker = f'SAMUEL SITOMPUL'
    elif (n == 40):
        prediksi_satker = f'SITI SANGADAH'
    elif (n == 41):
        prediksi_satker = f'SYAKUR ADHI TYASMORO'
    elif (n == 42):
        prediksi_satker = f'VIDYA ANNISAH PUTRI'
    elif (n == 43):
        prediksi_satker = f'WAHYUDIN BUCA KALAUW'
    elif (n == 44):
        prediksi_satker = f'Wimbo Mahadi'
    elif (n == 45):
        prediksi_satker = f'YUNISA DHIFA LUQYANA'
    else:
        prediksi_satker = f'YUNITA DWICAHYANI'
    return prediksi_satker


# Heart Disease Prediction Page
if (selected == 'Rekomendasi Anggota Tim'):
    
    # page title
    # st.title('Heart Disease Prediction using ML')
    st.markdown("<h1 style='text-align: center; color: Black;'>Sistem Penentuan Anggota Tim LKPD</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1 :
        Gender = st.selectbox('Gender', ["Pria","Wanita"])
        
        if Gender == "Pria" :
            Gender = 0
        else :
            Gender = 1

    with col2 :

        Jurusan = st.selectbox('Latar Belakang Pendidikan',
                           ['Akuntansi', 'Ekonomi Pembangunan', 'Ilmu Ekonomi Studi Pembangunan', 
                            'Ilmu Hukum', 'Ilmu Komunikasi', 'Ilmu Statistik', 'Manajemen', 
                            'Sastra Inggris', 'Teknik Informatika', 'Teknik Lingkungan', 'Teknik Sipil'])

        if Jurusan == "Akuntansi":
            Jurusan = 0
        elif Jurusan == "Ekonomi Pembangunan":
            KodePangkat = 1
        elif Jurusan == "Ilmu Ekonomi Studi Pembangunan":
            Jurusan = 2
        elif Jurusan == "Ilmu Hukum":
            Jurusan = 3
        elif Jurusan == "Ilmu Komunikasi":
            Jurusan = 4
        elif Jurusan == 'Ilmu Statistik':
            Jurusan = 5
        elif Jurusan== "Manajemen":
            Jurusan = 6
        elif Jurusan == "Sastra Inggris":
            Jurusan = 7
        elif Jurusan == "Teknik Informatika":
            Jurusan = 8
        elif Jurusan == "Teknik Lingkungan":
            Jurusan = 9
        else :
            Jurusan = 10
    
    with col1:

        Strata_Pendidikan = st.selectbox('Strata Pendidikan', ['S1','S2'])

        if Strata_Pendidikan == 'S1':
            Strata_Pendidikan = 0
        else :
            Strata_Pendidikan = 1

    with col2:

        Riwayat_Entitas = st.selectbox('Entitas',
                                   ['Kabupaten Buru', 'Kabupaten Buru Selatan', 'Kabupaten Maluku Barat Daya', 
                                    'Kabupaten Maluku Tengah', 'Kabupaten Maluku Tenggara', 'Kabupaten Tanimbar',
                                    'Kepulauan Aru', 'Kota Tual', 'Pemerintah Kota Ambon', 'Provinsi Maluku', 
                                    'Seram Bagian Barat', 'Seram Bagian Timur'])

        if Riwayat_Entitas == 'Kabupaten Buru':
            Riwayat_Entitas = 0
        elif Riwayat_Entitas == 'Kabupaten Buru Selatan':
            Riwayat_Entitas = 1
        elif Riwayat_Entitas == 'Kabupaten Maluku Barat Daya':
            Riwayat_Entitas = 2
        elif Riwayat_Entitas == 'Kabupaten Maluku Tengah':
            Riwayat_Entitas = 3
        elif Riwayat_Entitas == 'Kabupaten Maluku Tenggara':
            Riwayat_Entitas = 4
        elif Riwayat_Entitas == 'Kabupaten Tanimbar':
            Riwayat_Entitas = 5
        elif Riwayat_Entitas == 'Kepulauan Aru':
            Riwayat_Entitas = 6
        elif Riwayat_Entitas == 'Kota Tual':
            Riwayat_Entitas = 7
        elif Riwayat_Entitas == 'Pemerintah Kota Ambon':
            Riwayat_Entitas = 8
        elif Riwayat_Entitas == 'Provinsi Maluku':
            Riwayat_Entitas = 9
        elif Riwayat_Entitas == 'Seram Bagian Barat':
            Riwayat_Entitas = 10
        else :
            Riwayat_Entitas = 11
    
    with col1:
        Opini = st.selectbox('Opini Sebelumnya',['TMP', 'WDP', 'WTP'])

        if Opini == 'TMP':
            Opini = 0
        elif Opini == 'WDP':
            Opini = 1
        else :
            Opini = 3
    with col2:
        Anggaran_Pendapatan = st.text_input('Anggaran Pendapatan')
    
    with col1:
        Realisasi_Pendaptan = st.text_input('Realisasi Pendaptan')
    
    with col2:
        Anggaran_Belanja = st.text_input('Anggaran Belanja')
    
    with col1:
        Realisasi_Belanja = st.text_input('Realisasi Belanja')
    
    with col2:
        Total_Aset = st.text_input('Total Aset')

     
    # code for Prediction
    prediksi_satker = ''
    
    # creating a button for Prediction
    s1=None
    s2=None
    s3=None
    # s4=None
    # s5=None
    
    if st.button('Rekomendasi'):
        anggota_tim = anggota_tim_model.predict_proba([[Gender, Jurusan, Strata_Pendidikan, Riwayat_Entitas, Opini,
                                                        Anggaran_Pendapatan, Realisasi_Pendaptan, Anggaran_Belanja,
                                                        Realisasi_Belanja, Total_Aset]])                          
        a,b,c = np.argsort(anggota_tim,axis=1)[0][-3:]
        s1=get_str(c)
        s2=get_str(b)
        s3=get_str(a)
        # s4=get_str(d)
        # s5=get_str(e)

    f'Berikut Pegawai yang Direkomendasikan untuk Pemeriksaan Pada Entitas {Riwayat_Entitas}'    
    st.success(s1)
    st.success(s2)
    st.success(s3)
    # st.success(s4)
    # st.success(s5)