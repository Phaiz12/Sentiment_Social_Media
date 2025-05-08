import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('komentar_youtube_sentimen.csv')

# Mapping label
label_mapping = {
    'LABEL_2': 'Positive',
    'LABEL_3': 'Neutral',
    'LABEL_4': 'Negative'
}
df['sentimen_label'] = df['sentimen'].map(label_mapping)

# Hitung jumlah masing-masing sentimen
sentimen_count = df['sentimen_label'].value_counts()

# Visualisasi 1: Pie Chart
plt.figure(figsize=(6,6))
colors = ['#66bb6a', '#ffee58', '#ef5350']  # green, yellow, red
sentimen_count.plot.pie(autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Distribusi Sentimen Komentar')
plt.ylabel('')
plt.tight_layout()
plt.savefig('pie_sentimen.png')
plt.show()

# Visualisasi 2: Bar Chart
plt.figure(figsize=(6,4))
sentimen_count.plot(kind='bar', color=colors)
plt.title('Jumlah Komentar per Sentimen')
plt.xlabel('Sentimen')
plt.ylabel('Jumlah')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('bar_sentimen.png')
plt.show()