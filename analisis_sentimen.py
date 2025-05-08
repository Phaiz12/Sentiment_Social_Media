import pandas as pd
from transformers import pipeline
from tqdm import tqdm

# Load komentar yang sudah dibersihkan
df = pd.read_csv('komentar_youtube_bersih.csv')

# Load pipeline IndoBERT Sentiment (butuh koneksi internet saat pertama kali)
sentiment_pipeline = pipeline("sentiment-analysis", model="indobenchmark/indobert-base-p1", tokenizer="indobenchmark/indobert-base-p1")

# Deteksi sentimen
hasil_sentimen = []
print("🔍 Menganalisis sentimen komentar...")
for komentar in tqdm(df['komentar_bersih']):
    try:
        hasil = sentiment_pipeline(komentar)[0]
        hasil_sentimen.append(hasil['label'].upper())  # UPPER biar jadi: POSITIVE / NEGATIVE / NEUTRAL
    except:
        hasil_sentimen.append("ERROR")

# Tambahkan ke DataFrame
df['sentimen'] = hasil_sentimen

# Simpan hasil akhir
df.to_csv('komentar_youtube_sentimen.csv', index=False)
print("✅ Hasil disimpan di 'komentar_youtube_sentimen.csv'")
