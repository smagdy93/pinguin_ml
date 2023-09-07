import streamlit as st
import pandas as pd
import pickle
st.title('Penguin Classifier: A Machine Learning App')
st.write("This app uses 6 inputs to predict the species of penguin using " "a model built on the Palmer's Penguin's dataset. Use the form below" " to get started!")
penguin_df = pd.read_csv('penguins.csv')
rf_pickle = open('pinguin_ml\random_forest_penguin.pickle', 'rb')
map_pickle = open('pinguin_ml\output_penguin.pickle', 'rb')
rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
rf_pickle.close()
map_pickle.close()
