import streamlit as st
import pandas as pd
import joblib

# Title and description
st.title('Car Damage Prediction System')
st.write('Predict internal damage based on external damage assessment')

# Create input form
st.subheader('Enter External Damage Details')

part_name = st.selectbox('External Part Name', ['bullbar', 'bumper', 'hood', 'door', 'fender'])
recommended_fix = st.selectbox('Recommended Fix', ['repair', 'replace'])
damage_type = st.selectbox('Damage Type', ['buckled', 'scratched', 'broken', 'dented', 'torn'])
part_category = st.selectbox('Part Category', ['external'])

if st.button('Predict Internal Damage'):
    # Create input DataFrame
    input_data = pd.DataFrame({
        'part_name_ext': [part_name],
        'recommended_fix_ext': [recommended_fix],
        'Damage Type_ext': [damage_type],
        'part_category_ext': [part_category]
    })
    
    try:
        # Load the model
        model = joblib.load('damage_prediction_model.joblib')
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display results
        st.subheader('Prediction Results')
        st.write(f'Predicted Internal Damage: {prediction[0]}')
        
        # Add confidence information
        st.info('Note: This prediction is based on historical damage assessment data.')
        
    except Exception as e:
        st.error(f'Error in prediction: {str(e)}')

# Add explanatory information
st.sidebar.header('About')
st.sidebar.write('This system predicts potential internal car damage based on external damage assessment.')
st.sidebar.write('Input the external damage details to get a prediction of possible internal damage.')
