# 🚗 Car Price Prediction App

This project is a *machine learning-based web application* developed using *Streamlit* to predict the price of used cars. The app allows users to input key features of a car, such as mileage, engine capacity, age, and transmission type, and generates an estimated price using a pre-trained *Random Forest Regressor* model.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training and Tuning](#model-training-and-tuning)
- [Contributing](#contributing)

## Overview

The *Car Price Prediction App* enables users to predict the resale value of a car based on its features. The prediction is generated using a machine learning model trained on historical car sales data. The app is designed with an intuitive interface to make it easy for users to input car features and get immediate price predictions.

### New in app_final.py:
- Two separate sections (expanders) for *Car Specifications* and *Other Details* to streamline the input process.
- Car specifications like manufacturer, car model, variant, fuel type, and engine are grouped separately from other fields such as city, insurance, kilometers driven, etc.
- Improved layout with dynamic filtering of models, variants, and fuel types based on the selected manufacturer and model.
  
## Features

- *Input fields for car features*: 
  - Manufacturer, Car Model, Variant, Fuel Type, Body Type
  - Mileage (kmpl)
  - Engine capacity (cc)
  - Age of the car (years)
  - Transmission type (manual or automatic)
  - City, Insurance, Kilometers Driven
  - Number of Owners
- *Real-time price prediction*: Users can get an instant prediction of the car's price based on the input features.
- *Dynamic dropdowns*: Model and variant options change based on the selected manufacturer, providing a more user-friendly experience.
- *Streamlit UI*: A user-friendly interface for car price prediction.
  
## Installation

### Prerequisites
- Python 3.x
- Streamlit
- scikit-learn
- Matplotlib
- Pandas
- Numpy
- Pillow (for image processing)

### Steps
1. Clone the repository:
   bash
   git clone https://github.com/harishey2003/Car-Dheko---Used-Car-Price-Prediction.git
   cd Car-Dheko-Used-Car-Price-Prediction
   

2. Install the required dependencies:
   bash
   pip install -r requirements.txt
   

3. Download the pre-trained model:
   - Ensure that the random_forest_model_with_preprocessor.pkl file (pre-trained Random Forest model with preprocessor) is placed in the project directory.

4. Run the Streamlit app for basic functionality:
   bash
   streamlit run app.py
   

5. Run the enhanced Streamlit app with advanced features:
   bash
   streamlit run app_final.py
   

## Usage

1. After starting the app (app_final.py for full features), open the browser to access the app interface.
2. Use the *Car Specifications* section to input details such as:
   - *Manufacturer*: Select the car's manufacturer.
   - *Car Model*: Choose the car model (filtered based on the selected manufacturer).
   - *Variant*: Choose the variant of the selected car model.
   - *Fuel Type*: Choose between petrol, diesel, or other fuel types.
   - *Body Type*: Select the body type (SUV, Sedan, etc.).
   - *Mileage*: Enter the car’s fuel efficiency in kilometers per liter.
   - *Engine*: Enter the engine capacity in cubic centimeters (cc).
   - *Seats* and *Number of Cylinders* can also be input.
3. Use the *Other Details* section to input additional information:
   - *City*: Enter the city where the car is located.
   - *Insurance*: Select the insurance status.
   - *Kilometers Driven*: Enter the number of kilometers the car has been driven.
   - *Model Year*: Specify the year the car was manufactured.
   - *Number of Owners*: Select how many owners the car has had.
4. Click the Predict Price button to view the predicted price.
5. The predicted price will be displayed below, along with an optional explanation of how different features contributed to the final price.

## Model Training and Tuning

The model used in this project is a *Random Forest Regressor*, trained on historical car sales data. 

### Hyperparameter Tuning
Hyperparameters were optimized using *RandomizedSearchCV* for better model accuracy. The following hyperparameters were tuned:
- n_estimators: Number of trees in the forest.
- max_depth: Maximum depth of the tree.
- min_samples_split: Minimum number of samples required to split a node.
- min_samples_leaf: Minimum number of samples required to be at a leaf node.

### Feature Engineering
Key features used in the model include:
- Manufacturer, CarModel, Variant, FuelType, BodyType
- Mileage (kmpl)
- Engine Capacity (cc)
- Age of Car (years)
- Transmission Type (Manual/Automatic)
- Insurance, Kilometers Driven, City

The preprocessing pipeline ensures categorical and numerical features are handled appropriately.
## 🎨 Examples

Here are some screenshots of the Streamlit application:

### Feature App
![Base App](screenshots/screenshot1.png)

### Basic App
![Feature App](screenshots/screenshot2.png)

## Contributing

We welcome contributions to the project! To contribute:

1. Fork the repository.
2. Create a new branch for your feature (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add a feature').
4. Push to the branch (git push origin feature-branch).
5. Create a pull request.
