*import streamlit as st

st.title('Desechos tecnológicos')

date = st.date_input("Seleccionar la fecha de recogida de los aparatos electrónicos")

def anadir_tipo_desecho():
    option = st.selectbox('Celular',('Samsung','Iphone','Huawei','Xiaomi'))
    option_cantidad = st.selectbox('Cantidad', ('0-5','5-10','10-20'))

def calendarizar():
    st.button(label="Calendarizar recogida de desechos", help=None, on_click=st.balloons, args=None, kwargs=None, key=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")

st.map()

anadir_tipo_desecho()
calendarizar()






