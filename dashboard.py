import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import scipy.stats as stats

st.set_page_config(page_title="Bike Sharing", layout="centered")
st.title("Bike Sharing Dashboard /n by Viviana Purba")
st.markdown("---")

# Load data
bikesharing_clean = pd.read_csv("dashboard/bikesharing_clean.csv")

# Create a container for the plots
container = st.container()

with container:
with col1:
    st.header("Tren Rental Sepeda")
    st.write("Grafik ini menunjukkan tren rental sepeda pada tahun 2011-2012.")
    total_count_by_year = bikesharing_clean.groupby(['month', 'year'])['total_count'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='month', y='total_count', hue='year', data=total_count_by_year, palette=['blue', 'orange'], markers=['o', 's'], ax=ax)
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Sepeda yang Dirental')
    ax.set_title('Tren Rental Sepeda pada Tahun 2011-2012')
    ax.legend(loc='upper right')
    ax.set_xticks(range(1, 13))
    st.pyplot(fig)

with col2:
    st.header("Perubahan Total Sepeda dalam Seminggu")
    st.write("Grafik ini menunjukkan perubahan total sepeda yang dirental dalam seminggu.")
    category = ['Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu']
    avg_weekday = bikesharing_clean.groupby('weekday')['total_count'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=category, y=avg_weekday, palette=['gray' if x != max(avg_weekday) else 'orange' for x in avg_weekday], ax=ax)
    ax.set_xlabel('Hari')
    ax.set_ylabel('Total Rata-Rata Sepeda yang dirental')
    ax.set_title('Perubahan Total Sepeda yang Dirental dalam Seminggu')
    st.pyplot(fig)

with col3:
    st.header("Perbedaan Penggunaan Rental Sepeda")
    st.write("Grafik ini menunjukkan perbedaan penggunaan rental sepeda antara hari libur dan hari biasa.")
    avg_holiday = bikesharing_clean[bikesharing_clean['holiday'] == 1]['total_count'].mean()
    avg_non_holiday = bikesharing_clean[bikesharing_clean['holiday'] == 0]['total_count'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(['Hari Libur', 'Hari Biasa'], [avg_holiday, avg_non_holiday])
    ax.set_xlabel('Jenis Hari')
    ax.set_ylabel('Rata-Rata Total Sepeda yang Dirental')
    ax.set_title('Perbedaan Penggunaan Rental Sepeda antara Hari Libur dan Hari Biasa')
    st.pyplot(fig)

with col4:
    st.header("Total Rental Sepeda dalam 1 Hari")
    st.write("Grafik ini menunjukkan total rental sepeda dalam 1 hari berdasarkan musim.")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.pointplot(data=bikesharing_clean[['hour','total_count','season']],x='hour',y='total_count',hue='season',ax=ax, palette='Set1')
    ax.set(title="Total rental sepeda dalam 1 hari berdasarkan musim")
    ax.set_xlabel('Jam')
    ax.set_ylabel('Total rental sepeda')
    ax.legend(loc='upper right')
    ax.set_xticks(range(0, 24))
    st.pyplot(fig)

with col5:
    st.header("Rata-Rata Total Sepeda berdasarkan Suhu")
    st.write("Grafik ini menunjukkan rata-rata total sepeda yang dirental berdasarkan suhu.")
    bins = [0, 0.2, 0.4, 0.6, 0.8, 1]  
    labels = ['(0°C-8°C)', '(8°C-16°C )', '(16°C-24°C)', '(24°C-32°C)', '(32°C-41°C)']
    bikesharing_clean['temp_group'] = pd.cut(bikesharing_clean['temp'], bins=bins, labels=labels)
    temp_mean = bikesharing_clean.groupby('temp_group')['total_count'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    temp_mean.plot(kind='barh', color=["#FFE5B4", "#FFCC80", "#FFB74D", "#FF9800", "#E65100"], ax=ax)
    ax.set_ylabel('Kategori Suhu')
    ax.set_xlabel('Rata-Rata Total Sepeda yang Dirental')
    ax.set_title('Rata-Rata Total Sepeda berdasarkan Suhu', fontsize=14)
    ax.set_xticks(range(0, 6))
    st.pyplot(fig)
