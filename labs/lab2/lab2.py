import streamlit as st
import heapq
import random

def max_elem(listing):
    return heapq.nlargest(5, listing)

def lab2():

    listing = [random.randint(-100, 100) for i in range(8)]
    top5 = max_elem(listing)
    st.write(f"Список: {listing}")
    st.write(f"Від'ємні елементи: {top5}")
    st.button("Оновити")

