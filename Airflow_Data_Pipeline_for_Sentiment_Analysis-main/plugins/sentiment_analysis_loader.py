# Import modul
from mongodb_loader import get_mongo_client
from sentiment_analysis import SentimentAnalysis
from dotenv import load_dotenv
import os
import sys
import pandas as pd
import postgres_loader

# Menambahkan direktori plugins ke dalam path Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'plugins')) 

# Memuat variabel lingkungan dari file .env ke dalam sistem
load_dotenv()

def run_analysis():
    mongo_uri = os.getenv("MONGO_URI")
    # Inisialisasi klien MongoDB dan mengakses koleksi
    db = get_mongo_client(mongo_uri)
    news_collection = db['news']['finnhub_news']

    # Mengambil data dari MongoDB
    news = [x for x in news_collection.find()]

    output = []
    # Melakukan analisis sentimen untuk setiap ringkasan berita
    for news_summary in news:
        result = SentimentAnalysis(text=news_summary["summary"]).execute()
        output.append(result)
        print(f"Summary '{news_summary['summary']}' successfully analyzed")

    # Mengonversi output menjadi DataFrame
    sentiment_output = pd.DataFrame(output)

    # Memuat DataFrame ke PostgreSQL menggunakan modul postgres_loader
    postgres_loader.load(sentiment_output, "sentiment_news_analysis")

    print("Successfully loaded to Postgres")

if __name__ == "__main__":
    run_analysis()
