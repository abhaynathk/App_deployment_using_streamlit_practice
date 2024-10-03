import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode
import seaborn as sns
import datetime as dt
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns',None)
init_notebook_mode(connected=True)
import plotly.express as px
import altair as alt



def show_data_analysis():
    st.title("Top Hits Spotify from 2000-2019 Analysis\n\n")
    # Sample Data
    data=pd.read_csv(r"D:\VIT\Programming for DataScience\Datasets\songs_normalize.csv")

    # Sidebar Widgets
    st.sidebar.header("Options")
    category = st.sidebar.selectbox("Select a Artist:", data['year'])
    value_filter = st.sidebar.slider("Years", min_value=1980, max_value=2024, value=1980)
    multi_select = st.sidebar.multiselect("Select multiple categories", options=data['year'].unique())
    #dropping the duplicate values
    data.drop_duplicates(inplace=True)

    fig=px.imshow(data.corr(),text_auto=True,height=800,width=800,color_continuous_scale=px.colors.sequential.Greens,aspect='auto',title='<b>paiwise correlation of columns')
    fig.update_layout(title_x=0.5)
    st.plotly_chart(fig)
    # Create subplots
    fig = make_subplots(rows=3, cols=3, subplot_titles=(
     '<i>popularity', '<i>danceability', '<i>energy', 
     '<i>loudness', '<i>speechiness', '<i>acousticness', 
     '<i>liveness', '<i>valence', '<i>tempo'))

    # Add traces
    fig.add_trace(go.Histogram(x=data['popularity'] , name='popularity'), row=1, col=1)
    fig.add_trace(go.Histogram(x=data['danceability'], name='danceability'), row=1, col=2)
    fig.add_trace(go.Histogram(x=data['energy'], name='energy'), row=1, col=3)
    fig.add_trace(go.Histogram(x=data['loudness'], name='loudness'), row=2, col=1)
    fig.add_trace(go.Histogram(x=data['speechiness'], name='speechiness'), row=2, col=2)
    fig.add_trace(go.Histogram(x=data['acousticness'], name='acousticness'), row=2, col=3)
    fig.add_trace(go.Histogram(x=data['liveness'], name='liveness'), row=3, col=1)
    fig.add_trace(go.Histogram(x=data['valence'], name='valence'), row=3, col=2)
    fig.add_trace(go.Histogram(x=data['tempo'], name='tempo'), row=3, col=3)
    # Update layout
    fig.update_layout(height=900, width=900, title_text='<b>Feature Distribution', template='plotly_dark', title_x=0.5)

    # Display the figure in Streamlit
    st.title('Feature Distribution Histograms')
    st.plotly_chart(fig)

    # Create area chart
    fig = px.area(
     data.groupby('year', as_index=False).count().sort_values(by='song', ascending=False).sort_values(by='year'),
     x='year',
     y='song',
     markers=True,
     labels={'song': 'Total songs'},
     color_discrete_sequence=['green'],
     title='<b>Year by Year Songs Colle ction'
     )

    # Update layout
    fig.update_layout(hovermode='x', title_x=0.5)

    # Display the figure in Streamlit
    st.title('Year-by-Year Songs Collection')
    st.plotly_chart(fig)


    # Create histogram
    fig = px.histogram(
     data.groupby('genre', as_index=False).count().sort_values(by='song', ascending=False),
     x='genre',
     y='song',
     color_discrete_sequence=['green'],
     template='plotly_dark',
     marginal='box',
     title='<b>Total Songs Based on Genres</b>'
      )

      # Update layout
    fig.update_layout(title_x=0.5)

    # Display the figure in Streamlit
    st.title('Total Songs by Genre')
    st.plotly_chart(fig)

    
    
    if multi_select:
        multi_filtered_data = data[data['year'].isin(multi_select)]
        st.write(multi_filtered_data)
        fig_multi = px.bar(multi_filtered_data, x='year', y='artist', title="Selected Categories")
        st.plotly_chart(fig_multi)
    

















    



