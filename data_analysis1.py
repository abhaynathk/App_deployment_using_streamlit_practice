import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

def show_data_analysis():
    st.title("Top Hits Spotify from 2000-2019 \n\n")
    st.title(" \t\tAnalysis \n\n")
    # Load data
    data = pd.read_csv(r"D:\VIT\Programming for DataScience\Datasets\songs_normalize.csv")
    data.drop_duplicates(inplace=True)
    
    # Sidebar Widgets for filtering
    st.sidebar.header("Filter Options")
    selected_year = st.sidebar.selectbox("Select Year", options=data['year'].unique(), index=0)
    genre_filter = st.sidebar.multiselect("Select Genre(s)", options=data['genre'].unique())
    min_popularity = st.sidebar.slider("Min Popularity", int(data['popularity'].min()), int(data['popularity'].max()), int(data['popularity'].min()))

    # Filter data based on user input
    filtered_data = data[(data['year'] == selected_year) & (data['popularity'] >= min_popularity)]
    
    if genre_filter:
        filtered_data = filtered_data[filtered_data['genre'].isin(genre_filter)]
    
    # Pairwise Correlation Heatmap
    fig = px.imshow(
        filtered_data.corr(), text_auto=True, height=800, width=800,
        color_continuous_scale=px.colors.sequential.Greens, aspect='auto', title='<b>Pairwise Correlation of Columns'
    )
    fig.update_layout(title_x=0.5)
    st.plotly_chart(fig)

    # Feature Distribution Histograms
    fig = make_subplots(rows=3, cols=3, subplot_titles=(
        '<i>popularity', '<i>danceability', '<i>energy', 
        '<i>loudness', '<i>speechiness', '<i>acousticness', 
        '<i>liveness', '<i>valence', '<i>tempo'))

    fig.add_trace(go.Histogram(x=filtered_data['popularity'], name='popularity'), row=1, col=1)
    fig.add_trace(go.Histogram(x=filtered_data['danceability'], name='danceability'), row=1, col=2)
    fig.add_trace(go.Histogram(x=filtered_data['energy'], name='energy'), row=1, col=3)
    fig.add_trace(go.Histogram(x=filtered_data['loudness'], name='loudness'), row=2, col=1)
    fig.add_trace(go.Histogram(x=filtered_data['speechiness'], name='speechiness'), row=2, col=2)
    fig.add_trace(go.Histogram(x=filtered_data['acousticness'], name='acousticness'), row=2, col=3)
    fig.add_trace(go.Histogram(x=filtered_data['liveness'], name='liveness'), row=3, col=1)
    fig.add_trace(go.Histogram(x=filtered_data['valence'], name='valence'), row=3, col=2)
    fig.add_trace(go.Histogram(x=filtered_data['tempo'], name='tempo'), row=3, col=3)

    fig.update_layout(height=900, width=900, title_text='<b>Feature Distribution', template='plotly_dark', title_x=0.5)
    st.plotly_chart(fig)

    # Year-by-Year Songs Collection (filtered by selected year and genres)
    fig = px.area(
        filtered_data.groupby('year', as_index=False).count().sort_values(by='song', ascending=False).sort_values(by='year'),
        x='year', y='song', markers=True, labels={'song': 'Total songs'},
        color_discrete_sequence=['green'], title='<b>Year by Year Songs Collection'
    )
    fig.update_layout(hovermode='x', title_x=0.5)
    st.plotly_chart(fig)

    # Total Songs Based on Genres (filtered by selected genres)
    fig = px.histogram(
        filtered_data.groupby('genre', as_index=False).count().sort_values(by='song', ascending=False),
        x='genre', y='song', color_discrete_sequence=['green'], template='plotly_dark',
        marginal='box', title='<b>Total Songs Based on Genres</b>'
    )
    fig.update_layout(title_x=0.5)
    st.plotly_chart(fig)

    # Multi-select Filtered Data Display
    st.write("Filtered Data by Year and Genre:")
    st.write(filtered_data)

