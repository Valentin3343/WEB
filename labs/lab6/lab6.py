import requests
from bs4 import BeautifulSoup
from collections import Counter
import streamlit as st

def lab6():

    url = st.text_input("Введіть URL сторінки:")

    if url:
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'html.parser')

            top_words = Counter(soup.get_text().lower().split()).most_common(10)
            st.subheader("Топ-10 слів")
            for word, count in top_words:
                st.write(f"{word}: {count}")

            tags = Counter(tag.name for tag in soup.find_all())
            st.subheader("Частота HTML-тегів")
            for tag, count in tags.items():
                st.write(f"<{tag}>: {count}")

            st.subheader("Додаткова інформація")
            st.write(f"Кількість посилань: {len(soup.find_all('a'))}")
            st.write(f"Кількість зображень: {len(soup.find_all('img'))}")

        except requests.exceptions.RequestException as e:
            st.error(f"Помилка: {e}")
