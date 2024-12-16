# import streamlit as st
# st.write("Hello, World!")

# st.title("Simple Web Form with Streamlit")
# st.header("User Information Users")
# st.subheader("Subheader")
# #input for name
# name = st.text_input("Enter your name: ")
# #dropdown menu
# options = ["Option 1", "Option 2","Option 3"]
# selected_option = st.selectbox("Choose an Option: ", options)

# #slider for slecting value


# #Submit button 
# if st.button("Submit"): 
#     st.write(f"Name: {name} ")
#     st.write(f"Selected Option: {selected_option}")



#     # stopped at 8:50
####################################################################################################################################################################

import streamlit as st
from datetime import datetime, date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, ))

# Set the title of the web page
st.title("Simple Web Form with Streamlit")

# Set a header
st.header("User Information Users")

# Text input for name
st.subheader("personal Details")
name = st.text_input("Enter your name: ")

# Dropdown menu for selecting an option
options = ["Option 1","Option 2","Options 3"]
selected_options = st.selectbox("Choose an Option: ", options)

# Slider for selecting a value
slider_value = st.slider("Select a value" , 1, 100, 50)

#Radio button for selecting gender
gender = st.radio("Select your genger: " , ("Male","Female"))

#Checkboxes for selecting hobbies
hobbies=[]
st.header("Slect your Hobbies")
if st.checkbox("Reading"):
    hobbies.append("Reading")
if st.checkbox("Travelling"):
    hobbies.append("Traveling")
if st.checkbox("Cooking"):
    hobbies.append("Cooking")

#Date picker for selecting birthdate
birthdate = st.date_input("Select your birthdate: ", datetime(2000,1,1))


# Submit button
if st.button("Submit"):
    st.write(f"Name: {name}")
    st.write(f"Selected Option: {selected_options}")
    st.write(f"Slider Value: {slider_value}")
    st.write(f"Gender: {gender}")
    st.write(f"Hobbies: {', ' .join(hobbies) if hobbies else 'None'}")
    st.write(f"Birthdate: {birthdate}")
# Additional information
st.subheader("Sumarry")
st.write("Fill out the form above and click the Submit button.")
# Footer

