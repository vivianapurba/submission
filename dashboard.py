import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import scipy.stats as stats

# Configure page
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
st.title("Bike Sharing Dashboard")
st.subheader("Made by : Viviana Purba")
# Load data
bikesharing_clean = pd.read_csv("dashboard/bikesharing_clean.csv")

# First row: Rental Trends and Weekday Changes
col1, col2 = st.columns(2)
with col1:
    st.header("Tren Rental Sepeda")
    total_count_by_year = bikesharing_clean.groupby(['month', 'year'])['total_count'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='month', y='total_count', hue='year', data=total_count_by_year, 
                 palette=['blue', 'orange'], markers=['o', 's'], ax=ax)
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Sepeda yang Dirental')
    ax.set_title('Tren Rental Sepeda pada Tahun 2011-2012')
    ax.legend(loc='upper right')
    ax.set_xticks(range(1, 13))
    st.pyplot(fig)

with col2:
    st.header("Hari Rental Sepeda Terbanyak")
    category = ['Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu']
    avg_weekday = bikesharing_clean.groupby('weekday')['total_count'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=category, y=avg_weekday, 
                palette=['gray' if x != max(avg_weekday) else 'orange' for x in avg_weekday], ax=ax)
    ax.set_xlabel('Hari')
    ax.set_ylabel('Total Rata-Rata Sepeda yang dirental')
    ax.set_title('Total Sepeda yang Dirental dalam Seminggu')
    st.pyplot(fig)

# Add a horizontal divider
st.markdown("---")

# Second row: Holiday vs Non-Holiday and Season Trends
col3, col4 = st.columns(2)

with col3:
    st.header("Penggunaan Rental Sepeda Hari Libur vs Hari Biasa")
    avg_holiday = bikesharing_clean[bikesharing_clean['holiday'] == 1]['total_count'].mean()
    avg_non_holiday = bikesharing_clean[bikesharing_clean['holiday'] == 0]['total_count'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(['Hari Libur', 'Hari Biasa'], [avg_holiday, avg_non_holiday], color=['gray', 'orange'])
    ax.set_xlabel('Jenis Hari')
    ax.set_ylabel('Rata-Rata Total Sepeda yang Dirental')
    ax.set_title('Perbedaan Penggunaan Rental Sepeda antara Hari Libur dan Hari Biasa')
    st.pyplot(fig)

with col4:
    st.header("Perubahan Total Rental Sepeda dalam 1 Hari Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.pointplot(data=bikesharing_clean[['hour','total_count','season']], x='hour', y='total_count', 
                  hue='season', ax=ax, palette='Set1')
    ax.set(title="Total rental sepeda dalam 1 hari berdasarkan musim")
    ax.set_xlabel('Jam')
    ax.set_ylabel('Total rental sepeda')
    ax.legend(loc='upper right')
    ax.set_xticks(range(0, 24))
    st.pyplot(fig)

# Add another horizontal divider
st.markdown("---")

# Third row: Temperature Analysis
st.header("Total Rental Sepeda Tebanyak berdasarkan Suhu")
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]  
labels = ['(0°C-8°C)', '(8°C-16°C )', '(16°C-24°C)', '(24°C-32°C)', '(32°C-41°C)']
bikesharing_clean['temp_group'] = pd.cut(bikesharing_clean['temp'], bins=bins, labels=labels)
temp_mean = bikesharing_clean.groupby('temp_group')['total_count'].mean()
fig, ax = plt.subplots(figsize=(10, 6))
temp_mean.plot(kind='barh', color=["#FFE5B4", "#FFCC80", "#FFB74D", "#FF9800", "#E65100"], ax=ax)
ax.set_ylabel('Kategori Suhu')
ax.set_xlabel('Rata-Rata Total Sepeda yang Dirental')
ax.set_title('Rata-Rata Total Sepeda berdasarkan Suhu', fontsize=14)
st.pyplot(fig)
