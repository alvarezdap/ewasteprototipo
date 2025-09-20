import streamlit as st
import plotly.express as px

api_token=st.secrets['mapbox']

st.title('Desechos tecnológicos')

date = st.date_input("Seleccionar la fecha de recogida de los aparatos electrónicos")

def plotea_mapa():
    global api_token
    mapa=load_the_spreadsheet("Hoja 1")
    fig=px.scatter_mapbox(mapa,
                              lat='Lat',
                              lon='Lon',
                              hover_name='Nombre',
                              hover_data=['Especie','Provincia','Ciudad'],
                              color=mapa['Especie'],
                              size_max=1000000,
                              zoom=8,
                              mapbox_style='stamen-toner'
                              )
    
    fig.update_layout(autosize=True,hovermode='closest',mapbox=dict(accesstoken=api_token['api_token'],bearing=0,center=dict(lat=-1.4386338911881158,lon=-78.34621847043944),pitch=0,zoom=5))
    fig.update_traces(marker=dict(size=10))                                                                                  
    fig.update_layout(scattermode='group',margin={'r':0,'t':0,'l':0,'b':0})

    return st.plotly_chart(fig)



def anadir_tipo_desecho():
    option = st.selectbox('Celular',('Samsung','Iphone','Huawei','Xiaomi'))

anadir_tipo_desecho()
plotea_mapa()

st.button("Calendarizar recogida de desechos")

