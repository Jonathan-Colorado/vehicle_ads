import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
df.rename({'model': 'vehicle'}, axis=1, inplace=True)

df.insert(loc=3, column='make', value=df['vehicle'].apply(lambda x: x.split(' ', 1)[0]))
df.insert(loc=4, column='model', value=df['vehicle'].apply(lambda x: x.split(' ', 1)[1]))

df[['model_year', 'cylinders', 'odometer']] = df[['model_year', 'cylinders', 'odometer']].astype('Int64')
df['date_posted'] = pd.to_datetime(df.date_posted)

df['is_4wd'] = df.is_4wd.fillna(0)
df['is_4wd'] = df.is_4wd.astype('int')
df['is_4wd'] = df.is_4wd.astype('bool')

st.header('Data Viewer')
st.dataframe(df)
