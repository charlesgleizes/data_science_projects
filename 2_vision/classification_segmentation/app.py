import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from utils.add_logo import add_logo2

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


# local_css("style/style.css")
# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_4lyswkde.json")
img_silos_satelite = Image.open("images/silos_satelite.png").resize((250, 250))
img_silos_segmentation = Image.open("images/silos_segmentation.png").resize((250, 250))
img_food = Image.open("images/danger.png")
img_food = img_food.resize((200, 200))
img_mckinsey = Image.open('images/McKinsey_Script_Mark_2019.svg.png')

# ---- HEADER SECTION ----
with st.container():
    st.title("Foodix")

    image_column, text_column = st.columns([3, 1])
    with image_column:
        st.header("Our Mission : Diminish global famine crisis making cereals available for all families and communities across the globe")
        st.subheader(
            '''
            “The world is moving backwards in efforts to eliminate hunger and malnutrition.” (FAO)
    ''')
        st.write(
            '''
            • 828 million people were affected by hunger in 2021  
            • The number of hungry people increased by 150 million in 2019​  
            • 1 human being dying from famine every 4 seconds...
    ''')
        st.write("[Learn More >](https://www.fao.org/newsroom/detail/un-report-global-hunger-SOFI-2022-FAO/en)")
    with text_column:
        st_lottie(lottie_coding, height=500, key="coding") 
    
    st.markdown('''<h3 style='text-align: center; 
                color: midnightblue;
                '>We want to help solve this problem by providing sales and strategic managers with the information they need to place the silos in the place with the most impact.</h3>''', 
        unsafe_allow_html=True)

# ---- McKinsey description ----
with st.container():
    st.write("---")
    st.header("Who we are:")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("We are 6 McKinsey consultants with 20+ years of experiences")
    with right_column:
        st.write('')
    left_column_2, right_column_2 = st.columns(2)
    with left_column_2:
        st.write( """
            - Our experience includes, among other things, agriculture, infrastructures, sustainability and data science
            - +700 projects carried out throughout our career
            """
        )
        st.write("##")
        st.write(
            """
            About McKinsey:
            - Our expertise includes : Strategy, Transformation, Private Equity
            - +18000 consultants worldwide 
      
            If this sounds interesting to you, consider hiring us for your project.
            """
        )
        st.write("[Our Website >](https://www.mckinsey.com/)")
    with right_column_2:
        st.image(img_mckinsey)
    

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Little zoom on one of our project: classification and segmentation of silos on satellite images")
    st.write("For those who wish to have a quick overview of the technical part of the project.")
    st.write("##")

with st.container():
    text_column_1, image_column_1 = st.columns([3, 2])
    with text_column_1:
        st.subheader("Step 1 : Classification of Silos from Satellite images")
        st.write(
            """
                We use a deep learning algorithm to classify the image. More precisely, it is a CNN (Convolutionnal Neural Network) with a RMSProp optimizer and a Binary Cross-Entropy loss.
                Each image goes through 2 steps : preprocessing & prediction.
                Finaly, the classification is based on whether or not the model can find silos in the image, representing a certain zone of 128x128m.
            """
        )
    with image_column_1:
        st.image(img_silos_satelite)
    
    text_column_2, image_column_2 = st.columns([3, 2])
    with text_column_2:
        st.subheader("Step 2 : Image Segmentation and exact localization of silos")
        st.write(
            """
                Then, we segmentate our images to pinpoint the exact localization of the silos.
                To achieve this goal, we use a UNet algorithm with an Adam optimizer and a root mean square error loss.
            """
        )
    with image_column_2:
        st.image(img_silos_segmentation)
