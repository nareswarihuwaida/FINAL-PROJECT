# Import modul
import finnhub_loader
import mongodb_loader

def extract_load():
    # Mengambil data
    news = finnhub_loader.scrape_news()

    # Load data ke koleksi 'finnhub_news' di MongoDB
    collection = mongodb_loader.load('news', 'finnhub_news')
    collection.insert_many(news)

    print("Successfully load news to MongoDB")

if __name__ == "__main__":
    extract_load()