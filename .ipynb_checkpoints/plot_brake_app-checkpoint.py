import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import datetime
import matplotlib.pyplot as plt


def read_my_csv(file_name):
    df = pd.read_csv('./example_files/' + file_name, sep=';',encoding='latin1',skiprows=(1,1))
    df['Tiempo'] = df['Tiempo'].replace(',','.', regex=True).astype(np.float)
    df['Aceleración'] = df['Aceleración'].replace(',','.', regex=True).astype(np.float)
    return df

st.set_page_config(page_title="Historial Ensayos de performance de freno", page_icon=":station:", layout="wide")




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
    
st.write('Ejemplo de registros')

fig = make_subplots(rows=1, cols=1,
                    shared_xaxes=True)

df = read_my_csv('0013.csv')
# fig = px.line(data_frame=df,x='Tiempo',y='Aceleración',title='Aceleración Prueba de freno') 
fig.add_trace(go.Scatter(x=df['Tiempo'], y=df['Aceleración'],name="0013.csv"), row=1, col=1)
df = read_my_csv('0014.csv')
# fig.add_trace(px.line(data_frame=df,x='Tiempo',y='Aceleración'))
fig.add_trace(go.Scatter(x=df['Tiempo'], y=df['Aceleración'], name="0014.csv"), row=1, col=1)
df = read_my_csv('0015.csv')
fig.add_trace(go.Scatter(x=df['Tiempo'], y=df['Aceleración'], name="0015.csv"), row=1, col=1)
df = read_my_csv('0016.csv')
fig.add_trace(go.Scatter(x=df['Tiempo'], y=df['Aceleración'], name="0016.csv"), row=1, col=1)
df = read_my_csv('0017.csv')
fig.add_trace(go.Scatter(x=df['Tiempo'], y=df['Aceleración'], name="0017.csv"), row=1, col=1)

fig.update_layout(yaxis_title="Aceleración [m/s²]", xaxis_title="Tiempo [s]", title="Ensayos de performance de freno")

st.plotly_chart(fig, use_container_width=True)

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


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:'CENADIF - Subgerencia de Ingenieria y Projectos especiales'; 
                visibility: visible;
                display: block;
                position: relative;
                #background-color: red;
                padding: 5px;
                top: 2px;
                font-size: 15px;
                color: blue;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


