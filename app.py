import streamlit as st
from model import predict
import time

st.markdown('<style>body{text-align: center;}</style>', unsafe_allow_html=True)

# About section (sidebar)
st.sidebar.subheader('Hortus OS 1.3')
st.sidebar.write('CropScan Functionality Prototype; an autonomous procedure performed by Hortus Rover.')

# Instructions section (sidebar)
st.sidebar.subheader('Instructions to use')
st.sidebar.write("Upload an image of a crop leaf and click on the __Predict__ button. \
This would all be performed autonomously by the Hortus Rover. Upon detection of an infected or damaged plant, Hortus OS will send you an email immediately.")

st.sidebar.subheader('Future updates')
st.sidebar.write('We will be adding more disease classes to the database soon.')
st.sidebar.write('We have also planned to add possible remedies of these diseases to the app.')

# Main app interface
st.title('Hortus OS')
st.header('Version 1.3 (2023) - Alpha Division #2134')
st.text('')
img = st.file_uploader(label='Upload crop leaf image (PNG, JPG or JPEG)', type=['png', 'jpg', 'jpeg'])
if img is not None:
    predict_button = st.button(label='Predict')
    if predict_button:
        st.text('')
        st.text('')
        st.image(image=img.read(), caption='Uploaded image')
        prediction_class, prediction_probability = predict(img)
        st.subheader('Prediction')
        my_bar = st.progress(0)
        progress_text = st.write("Loading Data...")
        for percent_complete in range(25):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        progress_text = st.write("Analysing Crop Input...")
        for percent_complete in range(25,51):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        progress_text = st.write("Looking For Patterns...")
        for percent_complete in range(50,76):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        progress_text = st.write("Determining A Prediction...")
        for percent_complete in range(75,100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)
        with st.spinner('Loading Prediction Output...'):
                time.sleep(3)
        st.info(f'Classification: {prediction_class}, Probability: {prediction_probability}%')

# Information section (sidebar)
st.subheader('Current Crop Database:')
bullet_points = [
    "Apple - scab, Black rot, Cedar apple rust",
    "Blueberry - Powdery mildew",
    "Cherry - Powdery mildew",
    "Corn - Cercospora leaf spot, Gray leaf spot, Common rust,Northern Leaf Blight",
    "Grape - Black rot, Esca (Black Measles), Leaf blight (Isariopsis Leaf Spot)",
    "Orange - Haunglongbing (Citrus greening)",
    "Peach - Bacterial spot",
    "Bell Pepper - Bacterial spot",
    "Potato - Early blight, Late blight",
    "Raspberry - Gray leaf spot",
    "Soybean - Leaf scorch",
    "Squash - Powdery mildew",
    "Strawberry - Leaf scorch",
    "Tomato - Bacterial spot, Early blight, Late blight, Leaf Mold, Septoria leaf spot, \
 Spider mites Two-spotted spider mite, Target Spot, Tomato Yellow Leaf Curl Virus, Tomato mosaic virus,"
]
for item in bullet_points:
    st.write(f"- {item}")