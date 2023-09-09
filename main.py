import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
import random
import plotly.express as px
import plotly.graph_objects as go
from plotly.tools import make_subplots
from utils import add_logo
from PIL import Image

st.set_page_config(layout="wide")

# Logo
image = Image.open('ffnpt_logo.png')
col1, col2 = st.columns([8, 1])
#col2.image('https://images.squarespace-cdn.com/content/v1/5dd3cc5b7fd99372fbb04561/11220443-3caa-4681-9e3c-b518097ea2d0/Official+logo_fullname_fullcolour_for+dark+bg+-+no+outline%40FFNPT.png?format=100w',use_column_width='auto', width=200,)

col2.image(image)


#####

# Open the Excel file for reading
df = pd.read_excel('test_data.xlsx', sheet_name="project")

st.title("Show case dashboard for the FFNPT KPIs")

######### INTRO SECTION ###########

intro_col_1, intro_col_2, dummy, intro_col_3 = st.columns([2,1,.3,2])
with intro_col_1:
    st.markdown(" The FFNPT has already gained support from the World Health Organization, the European Parliament, and many other groups and individuals. Cities and subnational governments have also endorsed the treaty, as well as civil society organizations that have formed a global network. The text encourages readers to take action by endorsing the FFNPT themselves and calling on their own governments to support it. \n This page depicts the level of endorsement over time for four specific KPIs")
    
with intro_col_2:
    column = st.multiselect('Select one or several KPIs', df.columns.drop(['status', 'year']), default=['nation_endorse'])
    
with intro_col_3:
    st.markdown("Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff...  Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff...")
    


######### DISPLAY SECTION ###########

disp_col_1, dummy, disp_col_2 = st.columns([3,.3,3])

with disp_col_1:
    fig = px.line(df, x='year', y=column, markers=True, color_discrete_sequence=["#FF5203", "#FFB347","#0A1172", "#ADD8E6",],)
    fig.update_layout(yaxis_title='endorsements',) 
    st.plotly_chart(fig)

with disp_col_2:
	data = {
		'Category': ['A', 'B', 'C', 'D'],
		'Value': [10, 20, 30, 40]
	}
	fig = px.pie(data, values='Value', names='Category', hole=0.8, color_discrete_sequence=["#FF5203", "#FFB347","#0A1172", "#ADD8E6",])
	fig.update_traces(marker=dict(line=dict(color='black', width=1)))
	st.plotly_chart(fig)



# Display a map using the longitude and latitude data
st.markdown("## Confirmed outcome spots")

# df_geo = pd.read_excel('test_data.xlsx', sheet_name="geo")
# long = df_geo['long']
# lat = df_geo['lat']
# st.map(pd.DataFrame({'lat': lat, 'lon': long}), zoom=1,)

map_col_1, dummy, map_col_2 = st.columns([1.5,.1,5])

with map_col_1:
     st.markdown("Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff...  Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff... Some other stuff...")    

with map_col_2:

	chart_data = pd.DataFrame(
		np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
		columns=['lat', 'lon'])

	st.pydeck_chart(pdk.Deck(
		map_style='light',
		initial_view_state=pdk.ViewState(
			latitude=37.76,
			longitude=-122.4,
			zoom=10,
			pitch=50,
		),
		layers=[
			pdk.Layer(
				'HexagonLayer',
				data=chart_data,
				get_position='[lon, lat]',
				radius=200,
				elevation_scale=4,
				elevation_range=[0, 1000],
				pickable=True,
				extruded=True,
			),
			pdk.Layer(
				'ScatterplotLayer',
				data=chart_data,
				get_position='[lon, lat]',
				get_color='[200, 30, 0, 160]',
				get_radius=200,
			),
		],
	))

