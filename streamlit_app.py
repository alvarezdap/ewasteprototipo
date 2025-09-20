import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.title('Desechos tecnológicos')

date = st.date_input("Seleccionar la fecha de recogida de los aparatos electrónicos")

def anadir_tipo_desecho():
    option_celular = st.selectbox('Celular',('Samsung','Iphone','Huawei','Xiaomi'))
    option_cantidad = st.selectbox('Cantidad', ('0-100','100-500','500-1000','1000-5000','5000-10000'))

def calendarizar():
    st.button(label="Calendarizar recogida de desechos", help=None, on_click=st.balloons, args=None, kwargs=None, key=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")

st.map(latitude="-1.831239", longitude="-78.183406")

anadir_tipo_desecho()
calendarizar()






