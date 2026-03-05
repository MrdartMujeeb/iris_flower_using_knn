import streamlit as st
import pandas as pd
import pickle

# Page Title
st.title("Iris Flower Prediction App")

# User Name Input
name = st.text_input("Enter your Name")

# Load Dataset
data = pd.read_csv("iris.csv")

# Load Model
model = pickle.load(open("model.pkl", "rb"))

# Show Dataset Option
if st.checkbox("Show Training Dataset"):
    st.write(data)

st.subheader("Select the Flower Features")

# Feature Inputs
sepal_length = st.slider(
    "Sepal Length (cm)",
    float(data["SepalLengthCm"].min()),
    float(data["SepalLengthCm"].max()),
)

sepal_width = st.slider(
    "Sepal Width (cm)",
    float(data["SepalWidthCm"].min()),
    float(data["SepalWidthCm"].max()),
)

petal_length = st.slider(
    "Petal Length (cm)",
    float(data["PetalLengthCm"].min()),
    float(data["PetalLengthCm"].max()),
)

petal_width = st.slider(
    "Petal Width (cm)",
    float(data["PetalWidthCm"].min()),
    float(data["PetalWidthCm"].max()),
)

# Prediction Button
if st.button("Make Prediction"):

    input_data = pd.DataFrame(
        {
            "SepalLengthCm": [sepal_length],
            "SepalWidthCm": [sepal_width],
            "PetalLengthCm": [petal_length],
            "PetalWidthCm": [petal_width],
        }
    )

    prediction = model.predict(input_data)

    st.success(f"Predicted Flower Species: {prediction[0]}")

    if name:
        st.write(f"Thank you {name} for using the application!")

