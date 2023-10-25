
# run in terminal by typing: streamlit run app.py

import streamlit as st
import pandas as pd
# import pickle


# model = pickle.load(open('logreg_model.pkl','rb'))
st.title('Iris Variety Prediction')

# Create Form
with st.form(key='form_parameters'):
    sepal_length = st.slider('Sepal Length', 4.0, 8.0, 4.0)
    sepal_width = st.slider('Sepal Width', 2.0, 4.5, 2.0)
    petal_length = st.slider('Petal Length', 1.0, 7.0, 1.0)
    petal_width = st.slider('Petal Width', 0.1, 2.5, 0.1)
    st.markdown('---')

    submitted = st.form_submit_button('Predict')

# Data Inference
data_inf = {
    'sepal.length': sepal_length,
    'sepal.width': sepal_width,
    'petal.length': petal_length,
    'petal.width': petal_width
}
data_inf = pd.DataFrame([data_inf])

if submitted:
    # Predict using Logistic Regression
    y_pred_inf = 'blah'  # model.predict(data_inf)
    st.write('## Iris Variety = ' + str(y_pred_inf))
