import streamlit as st
import random
import math

def lab1():

    task = st.selectbox("**Оберіть завдання (1-3):**", [1, 2, 3], key="lab1_task", index=None, placeholder="Оберіть завдання...")

    if task == 1:
        a = st.number_input("**Введіть a:**")
        b = ((math.sqrt(2) / 2) * math.sin(a / 2))
        st.latex(r"""\frac{\sqrt{2}}{2}\sin\frac{a}{2} = """ + f"{b}")
    
    elif task == 2:
        n = st.number_input("**Введіть кількість годин:**", min_value=0, value=0)
        ameba = 2 ** (n // 3)
        st.write(f"Кількість амеб через {n} годин: {ameba}")
    
    elif task == 3:
        n = st.number_input("**Кількість елементів списку:**", min_value=0, value=0)
        lst = [random.randint(-100, 100) for і in range(n)]
        minus = [x for x in lst if x < 0]
        even_index_elements = [lst[i] for i in range(0, len(lst), 2)]
        average = sum(even_index_elements) / len(even_index_elements) if even_index_elements else 0
        st.write(f"Список: {lst}")
        st.write(f"Від'ємні елементи: {minus}")
        st.write(f"Максимальний від'ємний елемент: {max(minus, default='Немає')}")
        st.write(f"Середнє арифметичне елементів з парними індексами: {average}")
