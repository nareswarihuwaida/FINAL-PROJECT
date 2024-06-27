# Import modul
from textblob import TextBlob
import re

class SentimentAnalysis:

    def __init__(self, text):
        self.text = text

    # Hanya untuk bahasa Inggris
    def execute(self):
        # Membuat objek TextBlob dari teks yang diberikan
        analysis = TextBlob(self.text)

        # Menentukan sentimen
        if analysis.sentiment.polarity > 0:
            data = {'text': self.text, 'sentiment': 'positive'}
        elif analysis.sentiment.polarity == 0:
            data = {'text': self.text, 'sentiment': 'neutral'}
        else:
            data = {'text': self.text, 'sentiment': 'negative'}

        return data

if __name__ == "__main__":
    # Memanggil fungsi execute untuk contoh teks
    SentimentAnalysis('hard to learn NLTK').execute()