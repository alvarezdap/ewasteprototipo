import streamlit as st
import pandas as pd

st.title('Ecuawaste')
st.header('Desechos tecnológicos')

date = st.date_input("Seleccionar la fecha de recogida de los desechos tecnológicos")

def anadir_tipo_desecho():
    option_celular = st.selectbox('Celular',('Samsung','Iphone','Huawei','Xiaomi'),key=1)
    st.text_input("Cantidad", key=2)
    option_celular = st.selectbox('Computadoras',('Laptops','PCs'),key=3)
    st.text_input("Cantidad", key=4)
    option_celular = st.selectbox('Televisiones',('Samsung','LG','TCL'),key=5)
    st.text_input("Cantidad", key=6)

def calendarizar():
    st.button(label="Calendarizar recogida de desechos", help=None, on_click=st.balloons, args=None, kwargs=None, key=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")

st.map()

anadir_tipo_desecho()
calendarizar()






