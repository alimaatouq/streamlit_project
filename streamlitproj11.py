import pandas as pd
import numpy as np 
import streamlit as st 
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import subprocess
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)


Facebook_platform = pd.read_csv("facebook_platform.csv")
Facebook_age =  pd.read_csv("facebook_age.csv")
Facebook_region =  pd.read_csv("facebook_region.csv")


st.image(Image.open('semiannual.png'),width= 1800)

col1, col2, col3, col4 = st.beta_columns(4)
image = Image.open('purchase.png')
image2 = Image.open('add to cart.png')
image3 = Image.open('r.png')
image4 = Image.open('Dollar.png')
image5= Image.open('Purchases vs Revenue Breakdown.png')
with col1:
	st.image(image, width= 140)
	st.markdown("## Revenue")
	number = Facebook_platform["Purchases Conversion Value"].sum()
	number_f = "{:,.2f}".format(round(number))
	st.markdown(f"<h1 style=' color: green;'>${number_f}</h1>", unsafe_allow_html=True)
with col2:
	st.image(image2, width= 140)
	st.markdown("## Purchases")
	number = Facebook_platform["Purchases"].sum()
	number_f = "{:,.2f}".format(round(number))
	st.markdown(f"<h1 style='color: green;'>{number_f}</h1>", unsafe_allow_html=True)
with col3:
	st.image(image3, width= 140)
	st.markdown("## ROAS")
	number = Facebook_platform["Purchases Conversion Value"].sum()/Facebook_platform["Amount Spent (USD)"].sum() *100
	st.markdown(f"<h1 style='color: green;'>{round(number)}%</h1>", unsafe_allow_html=True)
with col4:
	st.image(image4, width= 140)
	st.markdown("## Budget Spent (USD)")
	number = Facebook_platform["Amount Spent (USD)"].sum()
	number_f = "{:,.2f}".format(round(number))
	st.markdown(f"<h1 style='color: green;'>${round(number)}</h1>", unsafe_allow_html=True)

st.sidebar.title('Dashboard Navigation')

st.sidebar.markdown('Filter Different KPIs with Dimension Grouping:')
chart_visual = st.sidebar.selectbox('Select Grouping by Dimension ', ('Category', 'Platform', 'Device','Region','Sub Category','Age Group'))

selected_kpi = st.sidebar.selectbox('Select KPI',options = ['Purchases','Revenue'])
K = Facebook_platform.groupby(["Category"]).sum()["Purchases"]
z = Facebook_platform.groupby(["Category"]).sum()["Purchases Conversion Value"]
g = Facebook_platform.groupby(["Platform"]).sum()["Purchases"]
f = Facebook_platform.groupby(["Platform"]).sum()["Purchases Conversion Value"]
L = Facebook_platform.groupby(["Impression Device"]).sum()["Purchases"]
M = Facebook_platform.groupby(["Impression Device"]).sum()["Purchases Conversion Value"]
R = Facebook_region.groupby(["Region"]).sum()["Purchases"]
RR = Facebook_region.groupby(["Region"]).sum()["Purchases Conversion Value"]
sub = Facebook_platform.groupby(["Sub Category"]).sum()["Purchases"]
subr = Facebook_platform.groupby(["Sub Category"]).sum()["Purchases Conversion Value"]
agep = Facebook_age.groupby(["Age"]).sum()["Purchases"]
ager = Facebook_age.groupby(["Age"]).sum()["Purchases Conversion Value"]
fig = go.Figure()

with open("style.css") as f:
	st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
	st.image(Image.open('Purchases vs Revenue Breakdown1.png'), width= 1800)
  
if chart_visual == 'Category':
    if selected_kpi == 'Purchases':
        fig = go.Figure(data=[go.Pie(labels=K.index, values=K.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))

    if selected_kpi == 'Revenue':
        fig = go.Figure(data=[go.Pie(labels=z.index, values=z.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))

elif chart_visual == 'Platform':
    if selected_kpi == 'Purchases':
        fig = go.Figure(data=[go.Pie(labels=g.index, values=g.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))
    if selected_kpi == 'Revenue':
        fig = go.Figure(data=[go.Pie(labels=f.index, values=f.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))

elif chart_visual == 'Device':
    if selected_kpi == 'Purchases':
        fig = go.Figure(data=[go.Pie(labels=L.index, values=L.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))
          
    if selected_kpi == 'Revenue':
        fig = go.Figure(data=[go.Pie(labels=M.index, values=M.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))

elif chart_visual == 'Region':
    if selected_kpi == 'Purchases':
        fig = go.Figure(data=[go.Pie(labels=R.index, values=R.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))
    if selected_kpi == 'Revenue':
        fig = go.Figure(data=[go.Pie(labels=RR.index, values=RR.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))
elif chart_visual == 'Sub Category':
    if selected_kpi == 'Purchases':
        fig = go.Figure(data=[go.Pie(labels=sub.index, values=sub.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))
    if selected_kpi == 'Revenue':
        fig = go.Figure(data=[go.Pie(labels=subr.index, values=subr.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))
elif chart_visual == 'Age Group':
    if selected_kpi == 'Purchases':
        fig = go.Figure(data=[go.Pie(labels=agep.index, values=agep.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))
        
        
        
    if selected_kpi == 'Revenue':
        fig = go.Figure(data=[go.Pie(labels=ager.index, values=ager.values)])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=15,
                  marker=dict(line=dict(width=2)))
        fig.update_layout(margin= dict(l=1,r=1,b=1,t=1))

st.plotly_chart(fig, use_container_width=True)

st.image(Image.open('Purchases vs Revenue Breakdown.png'),width= 1800)



duration = st.slider('Duration', 1, 180, value=1)
duration_num = (float(duration) - 81.114686) / 85.769567

purchase = st.text_input('Amount of Purchases you want to achieve', value=0)
purchase_num = (float(purchase) - 10.306912) / 34.629599


platform = st.radio('Choose platform', ['Audience network','Facebook', 'insta', 'messenger','others'])
Audience_network = 0
facebook = 0
insta = 0
messenger = 0
others = 0
if platform == 'Audience network':
	Audience_network = 1
elif platform == 'Facebook':
	facebook = 1
elif platform == 'instagram':
	insta = 1
elif platform == 'messenger':
	messenger = 1
elif platform == 'others':
	others = 1

objective = st.radio('Choose objective', ['Conversions', 'Catalog Sales', 'Engagement','Reach','Traffic','Video Views'])

Conversions = 0
Catalog_Sales = 0
Engagement = 0
Reach = 0
Traffic = 0
Video_Views = 0
if objective == 'Conversions':
	Conversions = 1
elif objective == 'Catalog Sales':
	Catalog_Sales = 1
elif objective == 'Engagement':
	Engagement = 1
elif objective == 'Reach':
	Reach = 1
elif objective == 'Traffic':
	Traffic = 1
elif objective == 'Video Views':
	Video_Views = 1

import pickle
from sklearn.linear_model import LinearRegression
model = pickle.load(open('model.sav', 'rb'))

predicted_val = model.predict([[duration_num, purchase_num, Audience_network, facebook, insta, messenger, others,Conversions,Catalog_Sales,Engagement,Reach,Traffic,Video_Views]])
st.write(f'Revenue = {predicted_val[0]}')
