from utils.add_logo import add_logo2
import streamlit as st
import matplotlib.pyplot as plt
import os
import tensorflow as tf
from utils.classif import classif_silo
from utils.segment import segment_silo
import os
import io
from PIL import Image
import numpy as np
import pandas as pd

# Sidebar __________________________________________________________________________
st.set_page_config(page_title="Foodix-Individual-Prediction", page_icon=":corn:", layout="wide")
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

def saveImage(byteImage):
    bytesImg = io.BytesIO(byteImage)
    imgFile = Image.open(bytesImg)   
   
    return imgFile

# Models _____________________________________________________________________________
classif_model = tf.keras.models.load_model(os.path.join(os.getcwd(), 'models/classification_model'))
segment_model = tf.keras.models.load_model(os.path.join(os.getcwd(), 'models/segmentation_model'))

# Main Body __________________________________________________________________________
with st.container():
    st.title("Individual Predictions 🔎")
    st.subheader("Upload your own pictures and apply the model to them")
    st.write(
        '''
           To upload an individual picture simply drag and drop it in the box.
        '''
    )

list_file_png = st.file_uploader("Upload a PNG image", type=([".png"]), accept_multiple_files=True)

if list_file_png:
    # Collect bytes
    files_bytes = [file.read() for file in list_file_png]
    # Apply model
    probas = classif_silo(files_bytes, classif_model)

    # Plotting the proportion of images having silos
    n_pic_silos = np.sum(probas>.5)
    n_pic_no_silos = np.sum(probas<=.5)
    data_bar_chart = pd.DataFrame({
        "Type": ["Silo found", "No silo found"], 
        "Number" : [n_pic_silos, n_pic_no_silos]
    })
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("<span style='text-align: center; color: black;'>**Repartition of the images**</span>", unsafe_allow_html=True)
        st.bar_chart(data_bar_chart, x="Type", y="Number", width=200, use_container_width=False)

    st.write(f"✅ Silo detected in {np.sum(probas>.5)} images.")

    idx_silos = 0
    list_no_silos = []
    col1, col2, col3, col4, col5 = st.columns(5)
    col_silos_class = [col1, col4]
    col_silos_segm = [col2, col5]
    for idx, file_pgn in enumerate(list_file_png):
        proba = probas[idx]

        if idx_silos%2==0:
            col1, col2, col3, col4, col5 = st.columns(5)
            col_silos_class = [col1, col4]
            col_silos_segm = [col2, col5]

        if proba>.5: # Silo detected
            if (idx_silos%2==0):
                title1 = file_pgn.name
            else:
                title2 = file_pgn.name

            with col_silos_class[idx_silos%2]:
                st.image(file_pgn)
                
            with col_silos_segm[idx_silos%2]:
                file_bytes = file_pgn.read()
                segmented_image = segment_silo(file_bytes, segment_model)
                st.image(segmented_image, clamp=True)

            idx_silos += 1

            # Display the title
            if idx_silos%2==0:
                col1_temp, col2_temp = st.columns(2)
                with col1_temp:
                    st.write(f"File : {title1}")
                with col2_temp:
                    st.write(f"&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;File : {title2}")

        else: # No silo detected
            list_no_silos += [file_pgn]
    if idx_silos%2!=0:
        col1_temp, col2_temp = st.columns(2)
        with col1_temp:
            st.write(f"File : {title1}")
            
    # Display the images where no silo was detected
    st.write("")
    st.write(f"❌ No silo detected in {len(list(probas))-np.sum(probas>.5)} images.")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col_no_silos = [col1, col2, col3, col4, col5, col6]
    for idx, file_pgn in enumerate(list_no_silos):
        with col_no_silos[idx%6]:
            st.image(file_pgn)
            st.write(f"File : {file_pgn.name}")