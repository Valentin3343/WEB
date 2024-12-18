import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import streamlit as st

def lab7():

    zavd = st.selectbox("Виберіть номер завдання", [1, 2, 3], index=None, placeholder="Виберіть номер завдання...")

    if zavd == 1:

        x = np.linspace(1, 10, 500)
        y = 5 * np.sin(x) * np.cos(x**2 + 1/x)**2

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=r'$F(x) = 5 \sin(x) \cos^2(x^2 + \frac{1}{x})$', color='blue')
        plt.title("Графік функції F(x) = 5 * sin(x) * cos(x^2+1/x)^2")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()

        st.pyplot(plt)


    elif zavd == 2:
        
        text = st.text_input("Введіть текст для аналізу", "")


        if text:
            text = text.lower().replace(" ", "")
            count = Counter(text)

            unik = list(count.keys())
            chast = list(count.values())

            st.header("Гістограма частоти літер у тексті")
            plt.figure(figsize=(10, 6))
            plt.bar(unik, chast, color='blue')
            plt.title("Частота появи літер у тексті")
            plt.xlabel("Літери")
            plt.ylabel("Частота")
            st.pyplot(plt)


    elif zavd == 3:

        text = st.text_input("Введіть текст для аналізу", "")
        

        if text:

            krapka = 0
            okluk = text.count('!')
            putan = text.count('?')
            trukrap = text.count('...')

            text = text.replace('...', '<ELLIPSIS>')
            sentences = text.split('.')

            for sentence in sentences:
                sentence = sentence.strip()
                if sentence and '<ELLIPSIS>' not in sentence and '!' not in sentence and '?' not in sentence:
                    krapka += 1

            types = ['Звичайні', 'Питальні', 'Окличні', 'Трикрапка']
            chastota = [krapka, okluk, putan, trukrap]

            st.header("Гістограма частоти різних типів речень")
            plt.figure(figsize=(10, 6))
            plt.bar(types, chastota, color='green')
            plt.title("Частота різних типів речень у тексті")
            plt.xlabel("Типи речень")
            plt.ylabel("Частота")
            st.pyplot(plt)

