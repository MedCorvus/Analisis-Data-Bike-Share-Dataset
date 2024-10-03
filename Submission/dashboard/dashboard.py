import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='whitegrid')
plt.style.use('dark_background')

def day_of_week_df(df):
    df['day_of_week'] = df['dteday'].dt.day_name()
    day_of_week_data = df.groupby(by=["day_of_week", "yr"]).agg({
        "cnt": "sum"
    }).reset_index() 
    return day_of_week_data

def hourly_df(df):
    hourly_df = df.groupby(by=["hr","yr"]).agg({
        "cnt": "sum"
    }).reset_index() 
    return hourly_df

def monthly_df(df):
    monthly_df = df.groupby(by=["mnth","yr"]).agg({
        "cnt": "sum"
    }).reset_index() 
    return monthly_df

def holiday_df(df):
    holiday_df = df.groupby(by=["holiday","yr"]).agg({
        "cnt": "sum"
    }).reset_index() 
    return holiday_df

def weather_df(df):
    weather_df = df.groupby(by=["weathersit","yr"]).agg({
        "cnt": "sum"
    }).reset_index() 
    return weather_df

def workingday_df(df):
    workingday_df = df.groupby(by=["workingday","yr"]).agg({
        "cnt": "sum"
    }).reset_index() 
    return workingday_df

def season_df(df):
    season_df = df.groupby(by=["season","yr"]).agg({
        "cnt": "sum"
    }).reset_index() 
    return season_df

def casualRegister_df(df):
    casual_year_df = df.groupby("yr")["casual"].sum().reset_index()
    casual_year_df.columns = ["yr", "total_casual"]
    reg_year_df = df.groupby("yr")["registered"].sum().reset_index()
    reg_year_df.columns = ["yr", "total_registered"]  
    casual_register_df = casual_year_df.merge(reg_year_df, on="yr")
    return casual_register_df

day_df = pd.read_csv("all_data.csv")
hour_df = pd.read_csv("hour.csv")

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar:
    st.image("Date.png")
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

first_df = day_df[(day_df["dteday"] >= str(start_date)) & 
                       (day_df["dteday"] <= str(end_date))]

second_df = hour_df[(hour_df["dteday"] >= str(start_date)) & 
                       (hour_df["dteday"] <= str(end_date))]

hourly_df = hourly_df(second_df)
hourly_df = hourly_df.replace({
    "yr": {0: 2011, 1: 2012}
})
monthly_df = monthly_df(first_df)
holiday_df = holiday_df(first_df)
workingday_df = workingday_df(first_df)
season_df = season_df(first_df)
weather_df = weather_df(first_df)
casual_register_df = casualRegister_df(first_df)
day_of_week_data = day_of_week_df(first_df)

st.header('=== BIKE SHARING DATA ===')

filtered_df = second_df[(second_df['dteday'] >= str(start_date)) & (second_df['dteday'] <= str(end_date))]
total_per_hour = filtered_df.groupby(['hr', 'workingday'])['cnt'].sum().reset_index()
total_per_hour['workingday'] = total_per_hour['workingday'].replace({0: 'Holiday', 1: 'Working Day'})
holiday_data = total_per_hour[total_per_hour['workingday'] == 'Holiday']
working_day_data = total_per_hour[total_per_hour['workingday'] == 'Working Day']
st.subheader("- Diagram Total Perbandingan Penyewaan per Jam pada Hari Kerja dan Hari Libur")
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(holiday_data['hr'], holiday_data['cnt'], width=0.4, label='Holiday', color='orange', align='center')
ax.bar(working_day_data['hr'] + 0.4, working_day_data['cnt'], width=0.4, label='Working Day', color='blue', align='center')
ax.set_title('Jumlah Penyewaan Sepeda per Jam: Weekday vs Holiday (Rentang Waktu yang Dipilih)')
ax.set_xlabel('Hour')
ax.set_ylabel('Count of Total Bike Rentals')
ax.set_xticks(holiday_data['hr'])
ax.set_xticklabels(holiday_data['hr'], rotation=0)
ax.legend()
plt.tight_layout()
st.pyplot(fig)

total_registered = first_df['registered'].sum()
total_casual = first_df['casual'].sum()
total_users = total_registered + total_casual
percent_registered = (total_registered / total_users) * 100
percent_casual = (total_casual / total_users) * 100
labels = ['Registered', 'Casual']
sizes = [percent_registered, percent_casual]
colors = ['blue', 'orange']
st.subheader('- Diagram Total Penyewa sepeda yang Terdaftar vs Penyewa Kasual')
fig, ax = plt.subplots(figsize=(3, 5))
ax.bar(labels, sizes, color=colors)
ax.set_xticks(labels)
ax.set_xticklabels(labels, rotation=45)
ax.set_title('Persentase Registered vs Casual')
ax.set_ylabel('Persentase (%)')
for index, value in enumerate(sizes):
    ax.text(index, value, f'{value:.1f}%', ha='center', va='bottom')
plt.tight_layout()
st.pyplot(fig)

st.subheader("- Diagram Total Penyewaan Sepeda Berdasarkan Hari dalam Minggu")
fig, ax = plt.subplots()
day_counts = day_of_week_data.groupby('day_of_week')['cnt'].sum()
colors = sns.dark_palette("blue", n_colors=len(day_counts), reverse=True)
ax.pie(day_counts, labels=day_counts.index, autopct='%1.1f%%', colors=colors)
plt.title("Proporsi Penyewaan Sepeda per Hari")
plt.tight_layout()
st.pyplot(fig)