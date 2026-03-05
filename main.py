import streamlit as st
import pandas as pd
import pickle
st.header("Iris flower Prediction App")                                                                                                                     #aftab
st.text_input("Enter your Name: ", key="name")                                                                                                              #aftab
data = pd.read_csv('Iris.csv')                                                                                                                              #aftab
model = pickle.load(open('model.json', 'rb'))                                                                                                               #aftab
if st.checkbox('Show Training Dataframe'):                                                                                                                  #aftab
    data
st.subheader("Please select relevant features of your flower!")
input_Length1 = st.slider('Sepal length(cm)', 0.0, max(data["SepalLengthCm"]),1.0)
input_Length2 = st.slider('Sepal Width(cm)', 0.0, max(data["SepalWidthCm"]),1.0)
input_Length3 = st.slider('Petal length(cm)', 0.0, max(data["PetalLengthCm"]),1.0)
input_Height = st.slider('Petal Width(cm)', 0.0, max(data["PetalWidthCm"]),1.0)
if st.button('Make Prediction'):
    data={'SepalLengthCm':[input_Length1], 'SepalWidthCm':[input_Length2], 'PetalLengthCm':[input_Length3], 'PetalWidthCm':[input_Height]}
    inputs = pd.DataFrame(data)
    prediction = model.predict(inputs)
    print("final pred", prediction)
    st.write(f"Your flower species is: {prediction}")
    st.write(f"Thank you {st.session_state.name}! I hope you liked it.")
    