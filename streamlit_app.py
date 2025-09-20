import streamlit as st

st.title('Desechos tecnológicos')

date = st.date_input("Seleccionar la fecha de recogida de los aparatos electrónicos")

def anadir_tipo_desecho():
    option = st.selectbox('Celular',('Samsung','Iphone','Huawei','Xiaomi'))

anadir_tipo_desecho()


st.button("Calendarizar recogida de desechos")
st.success('Calendarizado!', icon="✅")

