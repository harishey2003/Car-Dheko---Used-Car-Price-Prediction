import streamlit as st
import pandas as pd
import pickle
import locale

# Load the pre-trained model
model_filename = r"C:\Users\Lenovo\Downloads\car_dheko_jupyternotebook\random_forest_model.pkl"
with open(model_filename, "rb") as file:
    loaded_rf_model = pickle.load(file)

# Add some basic styling using markdown
st.markdown(
    """
    <style>
    .main {
        background-color: #F5F5F5;
        padding: 10px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border: None;
        padding: 10px 24px;
        font-size: 16px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main title and description
st.title("🚗 Car Price Prediction App")
st.write(
    """
    Welcome to the *Car Price Prediction* app!  
    Use the inputs below to adjust features for the car you want to price.
    """
)

# Input features section
st.header("🔧 Input Car Features")

# Main layout with columns
col1, col2 = st.columns(2)

with col1:
    Mileage = st.number_input(
        "Mileage (kmpl)", min_value=5.0, max_value=30.0, value=20.0, step=0.1
    )
    AgeOfCar = st.slider("Age of Car (Years)", min_value=1, max_value=50, value=5)

with col2:
    Engine = st.number_input(
        "Engine Capacity (cc)", min_value=500, max_value=5000, value=998, step=100
    )
    TransmissionType = st.selectbox("Transmission Type", ("Manual", "Automatic"))

# Mapping transmission type to numerical values
TransmissionType_Automatic = 1 if TransmissionType == "Automatic" else 0
TransmissionType_Manual = 1 if TransmissionType == "Manual" else 0

# Create input DataFrame
input_data = {
    "Mileage": Mileage,
    "Engine": Engine,
    "AgeOfCar": AgeOfCar,
    "TransmissionType_Automatic": TransmissionType_Automatic,
    "TransmissionType_Manual": TransmissionType_Manual,
}

input_df = pd.DataFrame([input_data])

# Show the input values for confirmation
st.subheader("Your Input Features")
st.table(input_df)

# Set locale to Indian
locale.setlocale(locale.LC_ALL, "en_IN.UTF-8")

def format_price(price):
    return f"₹{locale.format_string('%.2f', price, grouping=True)}"

# Prediction button
if st.button("🔍 Predict Car Price"):
    predicted_price = loaded_rf_model.predict(input_df)

    # Display the predicted price with styling
    st.success(f"💰 The Predicted Price of the Car is: {format_price(predicted_price[0])}")
    st.balloons()  # Adding an animation when the prediction is made
