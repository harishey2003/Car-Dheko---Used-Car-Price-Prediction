import pickle
import pandas as pd
import streamlit as st
import locale

# Load the saved model and preprocessor
model_filename = r"C:\Users\Lenovo\Downloads\car_dheko_jupyternotebook\random_forest_model_with_preprocessor.pkl"
with open(model_filename, "rb") as file:
    loaded_model, preprocessor = pickle.load(file)

# Set locale to Indian format
locale.setlocale(locale.LC_ALL, "en_IN.UTF-8")

# Streamlit Page Title
st.title("🚗 Car Price Prediction")

st.write(
    """
    Welcome to the *Car Price Prediction App*! Enter the details of your car below and we'll predict the estimated resale value based on our machine learning model.
    """
)

# Load the dataset
data_path = r"C:\Users\Lenovo\Downloads\car_dheko_jupyternotebook\data\df_filtered.csv"
data = pd.read_csv(data_path)

# Format price in Indian format
def format_price(price):
    return f"₹{locale.format_string('%.2f', price, grouping=True)}"

# Ensure the dataset is loaded
if data is not None:
    # Extract unique values for dropdowns from the dataset
    cities = data["City"].unique()
    insurances = data["Insurance"].unique()
    manufacturers = data["Manufacturer"].unique()

    # Create two columns for the layout
    col1, col2 = st.columns(2)

    # Left column for Car Specifications
    with col1:
        st.subheader("🔧 Car Specifications")
        st.write("Please provide the specifications of your car:")

        # Select Manufacturer
        Manufacturer = st.selectbox(
            "Manufacturer",
            manufacturers,
            help="Select the car manufacturer (e.g., Maruti, Hyundai, etc.)",
        )

        # Filter car models based on the selected manufacturer
        filtered_car_models = data[data["Manufacturer"] == Manufacturer]["CarModel"].unique()
        CarModel = st.selectbox(
            "Car Model",
            filtered_car_models,
            help="Choose the car model after selecting the manufacturer.",
        )

        # Filter variant names based on the selected car model
        filtered_variants = data[data["CarModel"] == CarModel]["VariantName"].unique()
        VariantName = st.selectbox("Variant Name", filtered_variants)

        # Filter Fuel Type based on the car model
        filtered_fueltypes = data[data["CarModel"] == CarModel]["FuelType"].unique()
        FuelType = st.selectbox("Fuel Type", filtered_fueltypes)

        # Filter Body Type based on the car model
        filtered_bodytypes = data[data["CarModel"] == CarModel]["BodyType"].unique()
        BodyType = st.selectbox("Body Type", filtered_bodytypes)

        # Filter Transmission Type based on the car model
        filtered_transmissiontypes = data[data["CarModel"] == CarModel]["TransmissionType"].unique()
        TransmissionType = st.selectbox("Transmission Type", filtered_transmissiontypes)

        # Number of Cylinders
        filtered_cylinders = data[data["CarModel"] == CarModel]["No of Cylinder"].unique()
        No_of_Cylinder = st.selectbox("Number of Cylinders", filtered_cylinders)

        # Seats
        filtered_seats = data[data["CarModel"] == CarModel]["Seats"].unique()
        Seats = st.selectbox("Number of Seats", filtered_seats)

        # Calculate mean values for Mileage and Engine based on selected CarModel, VariantName, and FuelType
        filtered_data_mileage_engine = data[
            (data["CarModel"] == CarModel)
            & (data["VariantName"] == VariantName)
            & (data["FuelType"] == FuelType)
        ]

        mean_mileage = filtered_data_mileage_engine["Mileage"].mean() if not filtered_data_mileage_engine.empty else 15.0
        mean_engine = filtered_data_mileage_engine["Engine"].mean() if not filtered_data_mileage_engine.empty else 1200.0
        mean_model_year = filtered_data_mileage_engine["ModelYear"].mean() if not filtered_data_mileage_engine.empty else 2000

        Mileage = st.number_input(
            "Mileage (km/l)",
            min_value=5.0,
            max_value=150.0,
            step=0.1,
            value=float(mean_mileage),
            help="Fuel efficiency of the car in kilometers per liter.",
        )
        Engine = st.number_input(
            "Engine Capacity (cc)",
            min_value=600,
            max_value=15000,
            step=50,
            value=int(mean_engine),
            help="Engine capacity of the car in cubic centimeters (cc).",
        )
        ModelYear = st.number_input(
            "Model Year",
            min_value=1950,
            max_value=2024,
            step=1,
            value=int(mean_model_year),
            help="Manufacturing year of the car.",
        )
        AgeOfCar = 2024 - ModelYear

    # Right column for Other Details
    with col2:
        st.subheader("📋 Other Details")
        st.write("Please provide additional details about the car:")

        # City
        City = st.selectbox("City", cities, help="Select the city where the car is located.")

        # Insurance
        Insurance = st.selectbox("Insurance", insurances, help="Select the insurance status of the car.")

        # Kilometers Driven
        KmsDriven = st.number_input(
            "Kilometers Driven",
            min_value=0,
            max_value=1000000,
            step=5000,
            value=100000,
            help="Total kilometers driven by the car.",
        )

        # Number of Owners
        NumberOwner = st.selectbox(
            "Number of Owners",
            [1, 2, 3, 4, 5],
            help="Select the number of owners the car has had.",
        )

        # When the user clicks 'Predict Price'
        if st.button("💡 Predict Price", type="primary"):
            # Define new car data for prediction
            new_data = {
                "City": City,
                "FuelType": FuelType,
                "BodyType": BodyType,
                "TransmissionType": TransmissionType,
                "Insurance": Insurance,
                "Manufacturer": Manufacturer,
                "CarModel": CarModel,
                "VariantName": VariantName,
                "KmsDriven": KmsDriven,
                "NumberOwner": NumberOwner,
                "ModelYear": ModelYear,
                "Mileage": Mileage,
                "Engine": Engine,
                "No of Cylinder": No_of_Cylinder,
                "Seats": Seats,
                "AgeOfCar": AgeOfCar,
            }

            # Convert new data to a DataFrame
            new_data_df = pd.DataFrame([new_data])

            # Apply the same preprocessing used during training
            new_data_preprocessed = preprocessor.transform(new_data_df)

            # Predict the price
            predicted_price = loaded_model.predict(new_data_preprocessed)

            # Display the prediction
            st.success(f"### Price: {format_price(predicted_price[0])}")
            st.write("Based on the details provided, this is the estimated resale price.")
