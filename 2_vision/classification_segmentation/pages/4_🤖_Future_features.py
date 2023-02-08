import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from utils.add_logo import add_logo2
import webbrowser

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Foodix-Silo-Detection", page_icon=":corn:", layout="wide")  
add_logo2("images/geosilo_logo.png")
markdown = """
GitHub Repository: <https://github.com/MRL1998/MCK_Silos.git>
"""

st.sidebar.success("👆👆👆 Select a page above:")
st.sidebar.title("💻 Our work: ")
st.sidebar.info(markdown)

st.sidebar.title("📬 Contact:")
markdown = """
zidi.yang@hec.edu 
milos.basic@hec.edu
antoine.mellerio@hec.edu
camille.epitalon@hec.edu
augustin.de-la-brosse@hec.edu
michael.liersch@hec.edu
"""
st.sidebar.info(markdown)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.title("Future features")
st.subheader("Streamline and optimize customer acquisition process")

st.write("""
         To reduce food waste through storage losses as quick as possible Foudix has to sell as
         many as possible silos with their revolutionary tecchnology. 
         The future sales process:
            - Identify on multilayered heatmaps (farm-density + agricultural data) the areas with the highest demand
            - Put your marker down in a 10km radius and let optimized algorithms search silos 
            - Receive a map with all silos and a csv files with the neirest address to each corresponding silo
         """
        )
st.write("---")

st.subheader("Sales process")

col1, arrow ,col2 = st.columns([4,2, 4])

france_heatmap = Image.open("images/agriculture_france.png")
marked_map = Image.open("images/map_marked.png")
# arrow_pic = Image.open("images/arrow.png")
with col1:
     st.markdown("<h5 style='text-align: center; color: midnightblue;'>Multilayered agricultural data heatmaps </h5>", unsafe_allow_html=True)
     st.image(france_heatmap)
with arrow:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # st.image(arrow_pic)
with col2:
    st.markdown("<h5 style='text-align: center; color: midnightblue;'>Marked Silos next to roads in 10km radius</h5>", unsafe_allow_html=True)
    st.image(marked_map)

st.write("---")
