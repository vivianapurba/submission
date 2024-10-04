import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import scipy.stats as stats

st.set_page_config(page_title="Bike Sharing", layout="wide")
st.title("Bike Sharing Dashboard by Viviana Purba")
st.markdown("---")

# Load cleaned data
bikesharing_clean = all_df = pd.read_csv("bikesharing_clean.csv")

# Create a sidebar for selecting visualization options
st.sidebar.header("Select Visualization Options")
select_option = st.sidebar.selectbox("Select a visualization", ["Tren Rental Sepeda", "Perubahan Total Sepeda dalam Seminggu", "Perbedaan Penggunaan Rental Sepeda", "Total Rental Sepeda dalam 1 Hari", "Rata-Rata Total Sepeda berdasarkan Suhu"])

# Create a container for the visualization
viz_container = st.container()

# Load the cleaned data
bikesharing_clean = pd.read_csv("bikesharing_clean.csv")

# Define the visualization functions
def tren_rental_sepeda():
    total_count_by_year = bikesharing_clean.groupby(['month', 'year'])['total_count'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='month', y='total_count', hue='year', data=total_count_by_year, palette=['blue', 'orange'], markers=['o', 's'])
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Sepeda yang Dirental')
    plt.title('Tren Rental Sepeda pada Tahun 2011-2012')
    plt.legend(loc='upper right')
    plt.xticks(range(1, 13))
    st.pyplot()

def perubahan_total_sepeda():
    category = ['Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu']
    avg_weekday = bikesharing_clean.groupby('weekday')['total_count'].mean()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=category, y=avg_weekday, palette=['gray' if x != max(avg_weekday) else 'orange' for x in avg_weekday])
    plt.xlabel('Hari')
    plt.ylabel('Total Rata-Rata Sepeda yang dirental')
    plt.title('Perubahan Total Sepeda yang Dirental dalam Seminggu')
    st.pyplot()

def perbedaan_penggunaan_rental_sepeda():
    avg_holiday = bikesharing_clean[bikesharing_clean['holiday'] == 1]['total_count'].mean()
    avg_non_holiday = bikesharing_clean[bikesharing_clean['holiday'] == 0]['total_count'].mean()
    plt.figure(figsize=(10, 6))
    plt.bar(['Hari Libur', 'Hari Biasa'], [avg_holiday, avg_non_holiday])
    plt.xlabel('Jenis Hari')
    plt.ylabel('Rata-Rata Total Sepeda yang Dirental')
    plt.title('Perbedaan Penggunaan Rental Sepeda antara Hari Libur dan Hari Biasa')
    st.pyplot()

def total_rental_sepeda_dalam_1_hari():
    fig,ax = plt.subplots(figsize=(12, 6))
    sns.pointplot(data=bikesharing_clean[['hour','total_count','season']],x='hour',y='total_count',hue='season',ax=ax, palette='Set1')
    ax.set(title="Total rental sepeda dalam 1 hari berdasarkan musim")
    ax.set_xlabel('Jam')
    ax.set_ylabel('Total rental sepeda')
    ax.legend(loc='upper right')
    plt.xticks(range(0, 24))
    st.pyplot()

def rata_rata_total_sepeda_berdasarkan_suhu():
    bins = [0, 0.2, 0.4, 0.6, 0.8, 1]  
    labels = ['(0°C-8°C)', '(8°C-16°C)', '(16°C-24°C)', '(24°C-32°C)', '(32°C-41°C)']
    bikesharing_clean['temp_group'] = pd.cut(bikesharing_clean['temp'], bins=bins, labels=labels)
    temp_mean = bikesharing_clean.groupby('temp_group')['total_count'].mean()
    plt.figure(figsize=(10, 6))
    temp_mean.plot(kind='barh', color=["#FFE5B4", "#FFCC80", "#FFB74D", "#FF9800", "#E65100"])
    plt.ylabel('Kategori Suhu')
    plt.xlabel('Rata-Rata Total Sepeda yang Dirental')
    plt.title('Rata-Rata Total Sepeda berdasarkan Suhu', fontsize=14)
    plt.tight_layout()
    st.pyplot()

# Display the selected visualization
if select_option == "Tren Rental Sepeda":
    tren_rental_sepeda()
elif select_option == "Perubahan Total Sepeda dalam Seminggu":
    perubahan_total_sepeda()
elif select_option == "Perbedaan Penggunaan Rental Sepeda":
    perbed