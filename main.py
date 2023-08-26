import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px

# Set the title of the app
st.title('World Population')

# Display the introduction text
st.write('The world population is the total number of humans currently living, and was estimated to have reached 7.9 billion people as of March 2020. It took over 200,000 years of human history for the world\'s population to reach 1 billion, and only 200 years more to reach 7 billion.')

# Create dummy data for the trend graph
trend_data = pd.DataFrame({
    'year': [1950, 1960, 1970, 1980, 1990, 2000, 2010],
    'population': [2.5, 3.0, 3.7, 4.4, 5.3, 6.1, 6.9]
})

# Create a visual delimiter
st.markdown('---')

# Display explanatory text for the trend graph
st.write('The graph below shows the increase of global population over time. The x-axis represents the year and the y-axis represents the world population in billions.')

# Create a slider to change the population for the initial year
initial_population = st.slider('Initial Population (1950)', min_value=1.0, max_value=5.0, value=2.5)

# Update the trend data with the selected initial population
trend_data.loc[0, 'population'] = initial_population

# Create the trend graph
st.line_chart(trend_data)

# Create dummy data for the map
map_data = pd.DataFrame({
    'lat': [51.5074, 40.7128],
    'lon': [-0.1278, -74.0060],
    'population': [8.9, 8.4]
})

# Define a function to calculate the fill color based on the population
def calculate_fill_color(population):
    if population < 5:
        return [255, 99, 71] # Red
    elif population < 10:
        return [255, 165, 0] # Orange
    else:
        return [50, 205, 50] # Green

# Add a fill_color column to the map data
map_data['fill_color'] = map_data['population'].apply(calculate_fill_color)

# Create a visual delimiter
st.markdown('---')

# Display explanatory text for the map
st.write('The map below shows the population per country using different colors depending on their population. Countries with a population less than 5 million are shown in red, countries with a population between 5 and 10 million are shown in orange, and countries with a population greater than 10 million are shown in green.')

# Create the map
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=0,
        longitude=0,
        zoom=1,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ColumnLayer',
            data=map_data,
            get_position='[lon, lat]',
            get_elevation='population',
            elevation_scale=1000,
            radius=50000,
            get_fill_color='fill_color',
            pickable=True,
            auto_highlight=True,
        )
    ],
))

# Create dummy data for the bubble chart
bubble_data = pd.DataFrame({
    'continent': ['Europe', 'North America'],
    'population': [747.7, 579]
})

# Create a visual delimiter
st.markdown('---')

# Display explanatory text for the bubble chart
st.write('The bubble chart below shows the population of each continent on the y-axis and the continent on the x-axis. The size of each bubble is proportional to the continent\'s population.')

# Create the bubble chart
fig = px.scatter(bubble_data, x='continent', y='population', size='population', text='continent')
fig.update_traces(textposition='top center')
st.plotly_chart(fig)
