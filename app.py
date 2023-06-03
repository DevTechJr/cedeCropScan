import streamlit as st
from model import predict
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

st.markdown('<style>body{text-align: center;}</style>', unsafe_allow_html=True)

# About section (sidebar)
st.sidebar.subheader('Cede CropScan OS')
st.sidebar.write('CropScan Functionality Prototype; an autonomous procedure performed by the Cede app.')

# Instructions section (sidebar)
st.sidebar.subheader('Instructions to use')
st.sidebar.write("Upload an image of a crop leaf and click on the __Predict__ button. \
The Cede app will immediately begin to scan the crop. Upon detection of an infection or damage, CropScan OS will send you an email immediately.")

st.sidebar.subheader('Future updates')
st.sidebar.write('We will be adding more disease classes to the database soon.')
st.sidebar.write('We have also planned to add possible remedies of these diseases to the app.')

# Main app interface
st.title('Cede\'s CropScan OS')
st.header('Version 1.3 (2023) - Prototype')
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
        if "healthy" not in prediction_class.lower():
            # Define email parameters
            sender_email = "cede.cropscan@gmail.com"
            receiver_email = "vangara.anirudhbharadwaj@gmail.com"
            password = "bmgbmawndqngvxin"
            
            # Get the current timestamp
            current_timestamp = datetime.now()

            # Format the timestamp in a user-friendly way
            formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")
            message = MIMEText(f'''Warning! Cede\'s CropScan feature has identified a crop have {prediction_class} at {formatted_timestamp} with a confidence of {prediction_probability}%. Cede suggests immediate aid and a check on the crop. Below is some more information regarding {prediction_class}:
            
                               
            ------- IDENTIFICATION -------
                               
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus non lacus lacus. Nulla finibus auctor mauris, quis ultrices dui elementum eu. Donec tristique tincidunt mollis. Nulla nec lorem eleifend, vestibulum eros quis, sagittis augue. Sed at ipsum faucibus, fringilla est et, posuere lacus. Curabitur nec vulputate justo. 
                               
            ------- LIFECYCLE -------
                               
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus non lacus lacus. Nulla finibus auctor mauris, quis ultrices dui elementum eu. Donec tristique tincidunt mollis. Nulla nec lorem eleifend, vestibulum eros quis, sagittis augue. Sed at ipsum faucibus, fringilla est et, posuere lacus. Curabitur nec vulputate justo. 

            ------- POTENTIAL DAMAGE -------
                               
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus non lacus lacus. Nulla finibus auctor mauris, quis ultrices dui elementum eu. Donec tristique tincidunt mollis. Nulla nec lorem eleifend, vestibulum eros quis, sagittis augue. Sed at ipsum faucibus, fringilla est et, posuere lacus. Curabitur nec vulputate justo. 
                               
            ------- TREATMENT -------

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus non lacus lacus. Nulla finibus auctor mauris, quis ultrices dui elementum eu. Donec tristique tincidunt mollis. Nulla nec lorem eleifend, vestibulum eros quis, sagittis augue. Sed at ipsum faucibus, fringilla est et, posuere lacus. Curabitur nec vulputate justo. 
                               ''')
            message["Subject"] = f"Cede CropScan - {prediction_class}"
            message["From"] = sender_email
            message["To"] = receiver_email

            # Send email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())

# Information section (sidebar)
st.subheader('Current Crop Database:')
bullet_points = [
    "Apple - scab, Black rot, Cedar apple rust",
    "Blueberry - Powdery mildew",
    "Cherry - Powdery mildew",
    "Corn - Cercospora leaf spot, Gray leaf spot, Common rust,Northern Leaf Blight",
    "Grape - Black rot, Esca (Black Measles), Leaf blight (Isariopsis Leaf Spot)",
    "Orange - Huanglongbing (Citrus greening)",
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