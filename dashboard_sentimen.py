import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

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

search_term = st.sidebar.text_input("Cari kata dalam komentar (opsional):", "")

# Filter data
filtered_df = df[df['sentimen_label'].isin(sentimen_filter)]

if search_term:
    filtered_df = filtered_df[filtered_df['komentar_asli'].str.contains(search_term, case=False, na=False)]

# Title
st.title("📊 Dashboard Analisis Sentimen Komentar YouTube")
st.markdown("Visualisasi interaktif hasil analisis sentimen dari komentar sosial media.")

# Tabel
st.subheader("Tabel Komentar")
st.dataframe(filtered_df[['komentar_asli', 'sentimen_label']])

# Plot distribusi sentimen
st.subheader("Distribusi Sentimen (Bar Chart)")
fig_bar, ax_bar = plt.subplots()
sns.countplot(data=filtered_df, x='sentimen_label', order=['Positif', 'Netral', 'Negatif'], ax=ax_bar)
ax_bar.set_ylabel("Jumlah Komentar")
st.pyplot(fig_bar)

# Pie chart
st.subheader("Distribusi Sentimen (Pie Chart)")
sentimen_counts = filtered_df['sentimen_label'].value_counts()
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(sentimen_counts, labels=sentimen_counts.index, autopct='%1.1f%%', startangle=90)
ax_pie.axis('equal')
st.pyplot(fig_pie)

# WordCloud
st.subheader("WordCloud per Sentimen")
for label in ['Positif', 'Netral', 'Negatif']:
    if label in filtered_df['sentimen_label'].values:
        text = " ".join(filtered_df[filtered_df['sentimen_label'] == label]['komentar_bersih'].dropna())
        if text.strip():
            wc = WordCloud(width=600, height=400, background_color='white').generate(text)
            st.markdown(f"**{label}**")
            fig_wc, ax_wc = plt.subplots()
            ax_wc.imshow(wc, interpolation='bilinear')
            ax_wc.axis("off")
            st.pyplot(fig_wc)
