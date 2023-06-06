# Name,Artist,Album,Popularity,Lyrics
# pip install streamlit pandas matplotlib seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='SAD - Atividade 03', page_icon=':bar_chart:', layout='centered', initial_sidebar_state='auto')
    
st.title('SAD - Atividade 03')

st.sidebar.title("Configurações de Exibição")

dt = pd.read_csv('songs.csv')

if st.sidebar.checkbox('Mostrar filtros dos dados'):
    artista = st.sidebar.selectbox('Artista', ['Todos'] + list(dt['Artist'].unique()))
    album = st.sidebar.selectbox('Album', ['Todos'] + list(dt['Album'].unique()))
    popularidade = st.sidebar.selectbox('Popularidade', ['Todos'] + list(dt['Popularity'].unique()))
    musica = st.sidebar.selectbox('Música', ['Todas'] + list(dt['Name'].unique()))

    if artista != 'Todos':
        dt = dt[dt['Artist'] == artista]
    if album != 'Todos':
        dt = dt[dt['Album'] == album]
    if popularidade != 'Todos':
        dt = dt[dt['Popularity'] == popularidade]
    if musica != 'Todas':
        dt = dt[dt['Name'] == musica]

st.write(dt)

# media de popularidade por artista
st.subheader('Média de popularidade por artista')
dt_media_pop = dt.groupby('Artist')['Popularity'].mean()
st.write(dt_media_pop)

# media de popularidade por musica
st.subheader('Média de popularidade por música')
dt_media_pop = dt.groupby('Name')['Popularity'].mean()
st.write(dt_media_pop)

# grafico com as musicas mais populares
st.subheader('Gráfico com as médias de músicas mais populares')
music_mean = dt.groupby('Name')['Popularity'].mean()
music_mean = music_mean.sort_values(ascending=False)
music_mean = music_mean.head(10)
fig, ax = plt.subplots()
sns.set_style('darkgrid')
sns.barplot(x=music_mean.values, y=music_mean.index, ax=ax)
ax.set_title('As 10 Músicas mais populares')
ax.set_xlabel('Popularidade')
ax.set_ylabel('Música')
st.pyplot(fig)



