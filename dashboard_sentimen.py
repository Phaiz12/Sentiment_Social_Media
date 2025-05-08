import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('komentar_youtube_sentimen.csv')

# Mapping label ke sentimen
label_mapping = {
    'LABEL_2': 'Positif',
    'LABEL_3': 'Netral',
    'LABEL_4': 'Negatif'
}
df['sentimen_label'] = df['sentimen'].map(label_mapping)

# Sidebar
st.sidebar.title("Dashboard Analisis Sentimen")
sentimen_filter = st.sidebar.multiselect(
    "Filter berdasarkan sentimen:",
    options=df['sentimen_label'].unique(),
    default=df['sentimen_label'].unique()
)

# Filter data
filtered_df = df[df['sentimen_label'].isin(sentimen_filter)]

# Title
st.title("Analisis Sentimen Komentar YouTube")
st.write("Visualisasi dan eksplorasi hasil analisis sentimen dari komentar YouTube.")

# Show dataframe
st.subheader("Tabel Komentar")
st.dataframe(filtered_df[['komentar_asli', 'sentimen_label']])

# Plot pie chart
st.subheader("Distribusi Sentimen")
sentimen_counts = filtered_df['sentimen_label'].value_counts()
fig, ax = plt.subplots()
ax.pie(sentimen_counts, labels=sentimen_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)
