import streamlit as st


# Title and Subtitle
st.title("🚀 Final Project - Beach Litter Segmentation")
st.subheader("📌 by Erlangga Dwi Atha")
st.divider()

# Introduction
st.markdown("""
    In this final project, I chose to create an image segmentation project 
    using <a href='https://www.sciencedirect.com/science/article/pii/S2352340922002839' target='_blank'>Beach Litter Segmentation Dataset</a>. 
    I used the <b>YOLOv8m</b> model for segmentation.
    
    The goal of this project is to develop a model capable of automatically identifying and categorizing 
    beach litter using deep learning techniques. With this approach, it is expected 
    to contribute to environmental conservation efforts in a more efficient and accurate manner.
    
    This website will showcase the results of the model predictions.
    
    This project still has some limitations, and constructive feedback and suggestions are highly appreciated for its further development.
""", unsafe_allow_html=True)
