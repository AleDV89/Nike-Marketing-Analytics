#--------------------Library-------------------#
import numpy as np  
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
import streamlit as st
from streamlit.components.v1 import html
import streamlit.components.v1 as components
import folium
from folium import plugins
from folium.plugins import FastMarkerCluster
import plotly.express as px
import os
import requests
from PIL import Image
import matplotlib.pyplot as plt
import pickle
import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context
import pyodbc
import pymssql
from neuralprophet import NeuralProphet


#-------Set up the Streamlit page----------#
st.set_page_config(
    page_title="Nike",
    page_icon="✔️",
    layout="wide", 
    initial_sidebar_state="expanded",
)

#----------Images--------#
front_page = "app_imagenes/Just Do It.png"
# Mostrar la imagen en la aplicación
st.image(front_page)

#---------HEADER---------#
st.title(" Nike Market Analysis and Predictive Sales")

st.markdown("""
    <font size="2">Most people think of Nike as a retail company—but ask anyone who works there, and they’ll tell you it is so much more. When it comes to harnessing the power of data, Nike is proven by their Consumer Insights and Commercial Analytics teams, which work hand in hand to transform the way people shop for Nike through the website, app, and beyond.</font>
""", unsafe_allow_html=True)

#---------LINKS--------#
st.markdown("<h1 style='text-align: center; font-size: 24px; font-weight: 400;'>More information about Nike Data Analytic</h1>", unsafe_allow_html=True)
#--------Columns--------#
col1, col2, col3 = st.columns(3)

#------link1-----#
image_path1 = r"C:\Users\alede\Desktop\TERCER_PROYECTO\app_imagenes\forbes.png"
# URL
url1 = "https://www.forbes.com/sites/forbestechcouncil/2019/10/07/how-nike-is-using-analytics-to-personalize-their-customer-experience/?sh=5fee61a71611"

with col1:
    st.image(image_path1, width=300)
    st.write('<font size="2">How Nike Is Using Analytics To Personalize Their CX</font>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url1}" target="_blank">See Link</a>', unsafe_allow_html=True)


#-----link 2--------# 
image_path2 = r"C:\Users\alede\Desktop\TERCER_PROYECTO\app_imagenes\office1.png"
# URL 
url2 = "https://www.youtube.com/watch?v=Mtinwvz0psI"
with col2:
    st.image(image_path2, width=300)
    st.write('<font size="2">Nike Insights and Analytics</font>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url2}" target="_blank">See Link</a>', unsafe_allow_html=True)


#-------link3------#
image_path3 = r"C:\Users\alede\Desktop\TERCER_PROYECTO\app_imagenes\office 2.png"
# URL 
url3 = "https://jobs.nike.com/es/blog/why-should-nike-care-about-data"


with col3:
    st.image(image_path3, width=300)
    st.write('<font size="2">Data and Designs</font>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url3}" target="_blank">See Link</a>', unsafe_allow_html=True)



# ---------------------Tabs----------------------#
tab0, tab1, tab2, tab3 =st.tabs(["About Our Data", "Sales Prediction", "New SQL Database", "Conclusion"])

#------------------Body Content-------#
with tab0:  # 1° tab
    st.header("*About Our Data*")
    st.markdown("""
    <font size="2">This project focuses on analyzing market trends, consumer behavior insights, and predictive sales for Nike products. It also includes a comparison with Adidas to provide comprehensive insights into the sportswear industry. Using Python, the project involves developing a machine learning model and an interactive application to visualize the analysis results.</font>
    """, unsafe_allow_html=True)

#-------------------Video---------------#
    video_link= r"C:\Users\alede\Desktop\TERCER_PROYECTO\app_video\video.mp4"
    st.video(video_link)

import streamlit as st
import pandas as pd
import pickle

#-------------------PAGE 2----------
with tab1:  # 2° tab

    model = r'C:\Users\alede\Desktop\TERCER_PROYECTO\notebooks\modelo_neuralprophet.pkl'

    with open(model, 'rb') as file:
        modelo_neuralprophet = pickle.load(file)

    # Def a function
    def mostrar_precios(df):
        st.subheader('Sales over time')
        st.write(df)

    # We adjust the app
    st.title('Nike Sales Prediction with NeuralProphet')

    # Load the data
    df = pd.read_csv(r'C:\Users\alede\Desktop\TERCER_PROYECTO\notebooks\forecast_neuralprophet.csv')  
    mostrar_precios(df)

    st.markdown("""
    <font size="2">By leveraging the capabilities of neural networks, NeuralProphet can provide more accurate forecasts compared to traditional time series forecasting methods.</font>
    """, unsafe_allow_html=True)
    
        # Gráfico de series temporales
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(6, 4))

    df['residual1'] = df['y'] - df['yhat1']

    ax1.set_title('Model residuals')
    ax1.plot(df['residual1'])

    ax2.set_title('Series vs prediction')
    ax2.plot(df['y'])
    ax2.plot(df['yhat1'])
    ax2.legend(['Original series', 'Estimation'])

    ax3.set_title('Series trend')
    ax3.plot(df['trend'])

    ax4.set_title('Weekly timing of the series')
    ax4.plot(df['season_weekly'])

    st.pyplot(fig)
    
    
    


#-----------------NEW SQL DATA BASE---------------#
#with tab2:
# Configurations
    #server="servervike.database.windows.net"
    #user = "alejandradentice"
    #password = "AlexyALE 2016@!!"
    #database = "nike_proyect"

# Make inquiries
    # def type_product(product):
        #conn = pymssql.connect(server=server, user=user, password=password, database=database)
        #cursor = conn.cursor()

        #cursor.execute("SELECT COUNT(*) FROM NikeProd WHERE ProductType = %s", (product,))
        #cantidad = cursor.fetchone()[0]
        #conn.close()
        #return cantidad

    # def main():
        #st.write("#Number of Products by Type")

        #t_product = ["STREET", "ATHLETIC"]
        #selecc = st.radio("Select the type of product:", t_product)

        #quantity = type_product(selecc)

        #st.write(f"Quantity of type products {selecc}: {quantity}")

    #if __name__ == "__main__":
        #main()


#------------------POWER BI---------#







#--------------------CONCLUSION---------------------#
with tab3: 
    st.header("*Proyect Conclusion*")
    st.markdown("In this Dataset there are 48 states of the USA. The states of Hawaii and Alaska are not included in it.")
    # embed streamlit docs in a streamlit app
    HtmlFile = open("notebooks/mi_mapa.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, width=400, height=500, scrolling=True)
    #-----------USA MARKET INSIGHTS--------#
    st.markdown("*The Nike USA market has 6 retailers")
    st.markdown("*The state that sells the most Nike products is New York and the state that sells the least is the state of Nebraska.")
    st.markdown("*In the month of June and July of 2021, they launched their most expensive products.")
    st.markdown("*The most recurring payment method than in the store despite the fact that in the year 2020-2021 was the Covid pandemic.")
    st.markdown("*In 2020, sales were low and starting in January 2021, sales began to rebound.")
    st.markdown("*The types of products that sell the most are Footwear.")
    st.markdown("*Finally, the customer's perception of the Nike brand with Adidas is that Adidas products have more reviews and lower prices than Nike's, but Nike products are the most searched for on the web and have the best ratings.")