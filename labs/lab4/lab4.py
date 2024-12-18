import streamlit as st
import random

def lab4():
    task = st.selectbox("Оберіть завдання", ["Завдання 1", "Завдання 2"], index=None, placeholder="Оберіть завдання...")


    if task == "Завдання 1":

        slova1 = ["Кіт", "Робот", "Викладач", "Мандрівник", "Астроном"]
        slova2 = ["мріє", "читає", "будує", "досліджує", "знаходить"]
        slova3 = ["книгу", "планету", "будинок", "машину часу", "комету"]

        if st.button("Згенерувати речення"):
            st.text(f"{random.choice(slova1)} {random.choice(slova2)} {random.choice(slova3)}")



    elif task == "Завдання 2":

        uploaded_file = st.file_uploader("Завантажте файл з текстом (book.txt):", type="txt")

        if uploaded_file is not None:
            text = uploaded_file.read().decode("utf-8")

            st.write("**Аналіз тексту:**")
            st.write(f"Символів з пробілами: {len(text)}")
            st.write(f"Символів без пробілів: {len(text.replace(' ', ''))}")

            words = text.split()
            st.write(f"Усього слів: {len(words)}")
            st.write(f"Різних слів: {len(set(words))}")

            unique_once = sum(words.count(word) == 1 for word in set(words))
            st.write(f"Унікальних слів, які зустрічаються 1 раз: {unique_once}")

