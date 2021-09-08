import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
import datetime
import matplotlib.pyplot as plt



# st.image("https://www.argentina.gob.ar/sites/default/files/mt_fase_cenadif_logo.jpg", width = 500)
st.image("https://www.argentina.gob.ar/sites/default/files/mt_fase_cenadif_logo.jpg")
st.title('Graficador de Pruebas de freno')
# widget de latex
# st.latex('\includegraphics{cenadif_logo.jpg}')
# st.latex('f(x) = a\sin( \omega  x)')
# uploaded_file = None

# uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)

uploaded_file = st.file_uploader("Elija un archivo .csv de prueba de freno")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file,sep=';',encoding='latin1',skiprows=(1,1))
    st.write(df)
    df['Tiempo'] = df['Tiempo'].replace(',','.', regex=True).astype(np.float)
    df['Aceleración'] = df['Aceleración'].replace(',','.', regex=True).astype(np.float)
    
#     fig, ax = plt.subplots()
#     df.plot(kind='line',x='Tiempo',y='Aceleración', ax=ax)
    fig = px.line(data_frame=df,x='Tiempo',y='Aceleración',title='Aceleración Prueba de freno')
#     plt.ylabel("Aceleración")
#     st.write(fig)
    st.plotly_chart(fig)
    
    

# Add a selectbox to the sidebar:
add_selectbox1 = st.sidebar.multiselect(
    'Material Rodante',
    ('Todos','Qingdao','Zhuzhou','Puzhen','CCK','SDD7')
)


add_selectbox2 = st.sidebar.multiselect(
    'Línea',
    ('Todas','Roca','Sarmiento','Mitre','Belgrano Sur','Belgrano Norte','Belgrano','San Martín','Urquiza')
)

add_selectbox3 = st.sidebar.multiselect(
    'Velocidades',
    ('Todas','20','30','40','60','80','90','100','110')
)


# t = st.time_input('Set an alarm for', datetime.time(8, 45))
# st.write('Alarm is set for', t)








# widget input numerica
a = st.number_input('Insert a',1)

# texto
st.write('a = ', a)

#widget de sliders
b = st.slider('w', 0, 10, 1)


n = st.slider('n', 0, 500, 25) 

# python 

x=np.linspace(0,10,int(n))
y=a*np.sin(b*x)
fig = px.line(x=x,y=y)

# Plot!
st.plotly_chart(fig)


