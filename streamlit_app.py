import streamlit as st

st.title('Desechos tecnológicos')

date = st.date_input("Seleccionar la fecha de recogida de los aparatos electrónicos")

def anadir_tipo_desecho():
    option = st.selectbox('Celular',('Samsung','Iphone','Huawei','Xiaomi'))

st.button("Calendarizar recogida de desechos")

anadir_tipo_desecho()
