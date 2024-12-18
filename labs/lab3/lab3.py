import streamlit as st
import os

def read_file(file_name):
    try:
        with open(f"labs/lab3/{file_name}", 'r') as file_local:
            return file_local.readlines()
    except FileNotFoundError:
        return []

def write_file(file_name, data):
    with open(f"labs/lab3/{file_name}", 'w') as file_local:
        file_local.writelines(data)

def list_groups():
    path = "labs/lab3/"
    if not os.path.exists(path):
        os.makedirs(path)
    return [f[:-4] for f in os.listdir(path) if f.endswith(".txt")]

def lab3():

    task = st.selectbox("**Оберіть завдання:**",
    [
        "Створити групу",
        "Додати студента",
        "Переглянути студентів",
        "Видалити студента"
    ], index=None, placeholder="Оберіть завдання...")




    if task == "Створити групу":
        new_group = st.text_input("**Введіть назву нової групи (англійською, наприклад 11-KI):**")
        if st.button("Створити групу"):
            if not new_group:
                st.warning("Введіть назву групи.")
            else:
                new_group_file = f"labs/lab3/{new_group}.txt"
                try:
                    with open(new_group_file, "x") as file:
                        st.success(f"Групу '{new_group}' створено.")
                except FileExistsError:
                    st.error(f"Група '{new_group}' вже існує.")



    elif task == "Додати студента":
            
        groups = list_groups()
        group = st.selectbox("**Назва групи (наприклад, 11-KI):**", options=["Оберіть групу"] + groups)
        group_file = f"{group}.txt" if group != "Оберіть групу" else None

        if group == "Оберіть групу":
            st.warning("Оберіть групу зі списку.")
        
        else:
            surname = st.text_input("**Прізвище студента:**")
            avg_score = str(st.number_input("**Середній бал студента:**", step = 1))
            
            if st.button("Додати студента"):
                if not surname.strip():
                    st.warning("Прізвище не може бути порожнім.")
                elif not avg_score.strip():
                    st.warning("Середній бал не може бути порожнім.")
                else:
                    data = read_file(group_file)
                    data.append(f"{surname.strip()} {avg_score.strip()}\n")
                    write_file(group_file, data)
                    st.success("Студента додано.")



    elif task == "Переглянути студентів":

        groups = list_groups()
        group = st.selectbox("**Назва групи (наприклад, 11-KI):**", options=["Оберіть групу"] + groups)
        group_file = f"{group}.txt" if group != "Оберіть групу" else None

        if group == "Оберіть групу":
            st.warning("Оберіть групу зі списку.")
        else:
            data = read_file(group_file)
            if not data:
                st.info("Список студентів порожній.")
            else:
                for i, student in enumerate(data, 1):
                    st.text(f"{i}. {student.strip()}")



    elif task == "Видалити студента":

        groups = list_groups()
        group = st.selectbox("**Назва групи (наприклад, 11-KI):**", options=["Оберіть групу"] + groups)
        group_file = f"{group}.txt" if group != "Оберіть групу" else None

        if group == "Оберіть групу":
            st.warning("Оберіть групу зі списку.")
        else:
            data = read_file(group_file)
            if not data:
                st.info("Список студентів порожній.")
            else:
                student_to_delete = st.selectbox("**Виберіть студента для видалення:**", [line.strip() for line in data], index=None, placeholder="Виберіть студента для видалення...")
                if st.button("Видалити студента"):
                    data = [line for line in data if line.strip() != student_to_delete]
                    write_file(group_file, data)
                    st.success(f"Студента '{student_to_delete}' видалено.")
