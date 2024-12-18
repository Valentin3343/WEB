import streamlit as st

def lab5():

    action = st.selectbox("Оберіть дію:",[
        "Додати переклад", 
        "Знайти переклади", 
        "Показати весь словник",
        "Очистити словник"
        ],index=None, placeholder="Оберіть дію..."
        )

    dictionary = st.session_state.get("dictionary", {})


    if action == "Додати переклад":
        eng = st.text_input("Введіть англійське слово:")
        ua = st.text_input("Введіть переклад:")
        if st.button("Додати"):
            if not eng.strip():
                    st.warning("Введіть англійське слово.")
            elif not ua.strip():
                    st.warning("Введіть переклад.")
            else:
                if eng in dictionary:
                    dictionary[eng].append(ua)
                else:
                    dictionary[eng] = [ua]
                st.session_state["dictionary"] = dictionary
                st.success(f"Переклад '{ua}' для слова '{eng}' додано!")



    elif action == "Знайти переклади":
        eng = st.text_input("Введіть англійське слово для пошуку:")
        if st.button("Знайти"):
            if not eng.strip():
                st.warning("Введіть слово для пошуку.")
            else:
                translations = dictionary.get(eng)
                if translations is None:
                    st.error("Слово не знайдено.")
                else:
                    st.write(f"Переклади: {translations}")


    elif action == "Показати весь словник":
        if dictionary:
            st.write("Вміст словника:")
            for eng, ua_list in dictionary.items():
                st.write(f"{eng}: {', '.join(ua_list)}")
        else:
            st.error("Словник порожній.")


    elif action == "Очистити словник":
        if st.button("Очистити словник"):
            st.session_state["dictionary"] = {}
            st.success("Словник очищено.")