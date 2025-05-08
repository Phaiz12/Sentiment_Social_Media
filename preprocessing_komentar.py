import pandas as pd
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Baca file
df = pd.read_csv('komentar_youtube.csv')

# Preprocessing fungsi
def bersihkan_teks(teks):
    teks = teks.lower()
    teks = re.sub(r'[^\w\s]', '', teks)
    teks = re.sub(r'\d+', '', teks)
    teks = re.sub(r'\s+', ' ', teks).strip()
    return teks

def preprocessing_indonesia(teks_list):
    factory_stopword = StopWordRemoverFactory()
    stopword = factory_stopword.create_stop_word_remover()
    
    factory_stemmer = StemmerFactory()
    stemmer = factory_stemmer.create_stemmer()
    
    hasil = []
    for teks in teks_list:
        teks = bersihkan_teks(teks)
        teks = stopword.remove(teks)
        teks = stemmer.stem(teks)
        hasil.append(teks)
    return hasil

# Proses komentar
df['komentar_bersih'] = preprocessing_indonesia(df['komentar_asli'])

# Simpan file hasil preprocessing
df.to_csv('komentar_youtube_bersih.csv', index=False)
print("Preprocessing selesai! File disimpan sebagai komentar_youtube_bersih.csv")
