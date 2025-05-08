# install dulu dependensinya jika belum
# pip install youtube-comment-downloader pandas sastrawi

from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# === Step 1: Scraping komentar dari YouTube ===
def ambil_komentar_youtube(url):
    downloader = YoutubeCommentDownloader()
    komentar_list = []
    
    for comment in downloader.get_comments_from_url(url):
        komentar_list.append(comment['text'])
    
    return komentar_list

# === Step 2: Preprocessing dasar Bahasa Indonesia ===
def bersihkan_teks(teks):
    # lowercase
    teks = teks.lower()
    # hapus emoji & simbol
    teks = re.sub(r'[^\w\s]', '', teks)
    # hapus angka
    teks = re.sub(r'\d+', '', teks)
    # hapus spasi berlebih
    teks = re.sub(r'\s+', ' ', teks).strip()
    return teks

def preprocessing_indonesia(list_komentar):
    # Inisialisasi tools
    factory_stopword = StopWordRemoverFactory()
    stopword = factory_stopword.create_stop_word_remover()
    
    factory_stemmer = StemmerFactory()
    stemmer = factory_stemmer.create_stemmer()
    
    hasil_bersih = []
    
    for komentar in list_komentar:
        teks = bersihkan_teks(komentar)
        teks = stopword.remove(teks)
        teks = stemmer.stem(teks)
        hasil_bersih.append(teks)
    
    return hasil_bersih

# === Step 3: Simpan ke CSV ===
def simpan_ke_csv(komentar_asli, komentar_bersih, nama_file):
    df = pd.DataFrame({
        "komentar_asli": komentar_asli,
        "komentar_bersih": komentar_bersih
    })
    df.to_csv(nama_file, index=False)
    print(f"Berhasil disimpan ke {nama_file}")

# === Eksekusi ===
if __name__ == "__main__":
    url_video = input("Masukkan URL YouTube: ")
    
    print("Mengambil komentar...")
    komentar_asli = ambil_komentar_youtube(url_video)
    
    print("Memproses komentar...")
    komentar_bersih = preprocessing_indonesia(komentar_asli)
    
    simpan_ke_csv(komentar_asli, komentar_bersih, "komentar_youtube_bersih.csv")
