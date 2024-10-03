import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt



def show_data_analysis():
    # Sample Data
    data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': np.random.randint(10, 100, 5)
    })

    # Sidebar Widgets
    st.sidebar.header("Options")
    category = st.sidebar.selectbox("Select a Category:", data['Category'])
    value_filter = st.sidebar.slider("Minimum Value", min_value=0, max_value=100, value=10)
    multi_select = st.sidebar.multiselect("Select multiple categories", options=data['Category'].unique())

    # Filter data based on slider
    filtered_data = data[data['Values'] >= value_filter]
    st.write(f"Filtered Data (Values >= {value_filter}):")
    st.write(filtered_data)

    # Matplotlib Plot
    fig, ax = plt.subplots()
    ax.bar(filtered_data['Category'], filtered_data['Values'], color='skyblue')
    ax.set_xlabel("Category")
    ax.set_ylabel("Values")
    ax.set_title("Category vs Values")
    st.pyplot(fig)

    #  Plotly Plot
    fig_plotly = px.bar(filtered_data, x='Category', y='Values', title="Category vs Values (Interactive)")
    st.plotly_chart(fig_plotly)

    # Altair Plot
    chart_altair = alt.Chart(filtered_data).mark_bar().encode(
      x='Category',
      y='Values'
    ).properties(
    title="Category vs Values (Altair)"
    )
    st.altair_chart(chart_altair)

    # Multi-select for categories
    if multi_select:
        multi_filtered_data = data[data['Category'].isin(multi_select)]
        st.write(multi_filtered_data)
        fig_multi = px.bar(multi_filtered_data, x='Category', y='Values', title="Selected Categories")
        st.plotly_chart(fig_multi)
    

















    



