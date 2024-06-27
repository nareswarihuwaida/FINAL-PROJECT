# Import modul
from dotenv import load_dotenv
import os
import finnhub

# Memuat variabel lingkungan dari file .env ke dalam sistem
load_dotenv()

def scrape_news():
    # Mendefinisikan API untuk mendapatkan berita umum dari Finnhub
    api_key = os.getenv("FINNHUB_API_KEY")
    finnhub_client = finnhub.Client(api_key=api_key)

    news = finnhub_client.general_news('general', min_id=0)

    return news