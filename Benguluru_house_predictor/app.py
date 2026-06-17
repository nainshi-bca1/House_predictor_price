

import streamlit as st
import joblib
import pandas as pd

# Load the trained model
# Assuming 'RidgeModel_new.joblib' was successfully saved from the pipeline object
# You might need to re-run the cell where the 'pipe' was defined and saved if it wasn't successful.
try:
    model = joblib.load('RidgeModel_new.joblib')
except FileNotFoundError:
    st.error("Model file 'RidgeModel_new.joblib' not found. Please ensure it has been saved correctly.")
    st.stop()

st.title('Bengaluru House Price Prediction')

# Input fields for features
st.header('Enter House Details')

location = st.selectbox('Location', ['other', 'Whitefield', 'Sarjapur  Road', 'Electronic City', 'Kanakpura Road', 'Thanisandra', 'Yelahanka', 'Uttarahalli', 'Hebbal', 'Raja Rajeshwari Nagar', 'Marathahalli', 'Hennur Road', 'Banashankari', 'Haralur Road', 'Electronic City Phase II', 'Hosur Road', 'Old Airport Road', 'Kothanur', 'Rustam Bagh', 'Kadugodi', '7th Phase JP Nagar', 'Kaggadasapura', 'Chandapura', 'Kengeri', 'Domlur', 'Yeshwanthpur', 'Sarjapur', 'Kasavanhalli', 'Begur Road', 'Ramamurthy Nagar', 'Malleshwaram', 'Varthur', 'Bommasandra', 'BTM 2nd Stage', 'Tin Factory', 'Bellandur', 'Panathur', 'JP Nagar', 'Cunningham Road', 'HSR Layout', 'Devanahalli', 'Gottigere', 'Mysore Road', 'KR Puram', 'Frazer Town', 'Anekal', 'Jigani', 'Attibele', 'Lakshminarayana Pura', 'Hoodi', 'Koramangala', 'Hosa Road', 'Kudlu Gate', 'Akshaya Nagar', 'Binny Pete', 'Thigalarapalya', 'Talaghattapura', 'Vidyaranyapura', 'Subramanyapura', 'Old Madras Road', 'Bommanahalli', 'Balagere', 'Kenchenahalli', 'Green Glen Layout', 'EPIP Zone', 'Rajaji Nagar', 'Kodichikkanahalli', 'Kaval Byrasandra', 'Konanakunte', 'Kothannur', 'TC Palaya', 'Kasturi Nagar', 'Ambalipura', 'Manyata Tech Park', 'Bhoganhalli', 'Yelahanka New Town', 'Jalahalli', 'Magadi Road', 'Singasandra', 'Budigere', 'Kengeri Satellite Town', 'Brookefield', 'Bannerghatta Road', 'Kaikondrahalli', 'Harlur', 'Hulimavu', 'Hoskote', 'HBR Layout', 'Doddathoguru', 'Somasundara Palya', 'Kumbalgodu', 'Horamavu Agara', 'Nagavara', 'Horamavu', 'Whitefield,', 'Ambedkar Nagar', 'Battarahalli', 'Kannamangala', 'Tumkur Road', 'Kengeri Hobli', 'Dodda Nekkundi', 'Ardendale', 'Channasandra', 'Vasanthapura', 'Benson Town', 'Hegde Nagar', 'Thurahalli', 'Varthur Road', 'Kathriguppe', 'Halanayakanahalli', 'Hegganahalli', 'Gunjur', 'Singena Agrahara', 'Electronic City Phase I', 'Yelahanka, Jakkur', 'Byatarayanapura', 'Margondanahalli', 'Arekere', 'Seegehalli', 'Kanakapura', 'Dasanapura', 'Kengeri Main Road', 'Ramakrishnappa Layout', 'Bisuvanahalli', 'Jakkur', 'Kundalahalli', 'Bikasipura', 'Sahakara Nagar', 'Rayasandra', 'Kodigehalli', 'Begur', 'Banashankari Stage III', 'Choodasandra', 'Hadosiddapura', 'JP Nagar, Phase 1', 'Subramanya Pura', 'Jalahalli West', 'Doddenakundi Industrial Estate', 'Jayamahal', 'Gollahalli', 'Carmelaram', 'Kudlu', 'K Narayanapura', 'Borewell Road', 'Kanakapura Road,', 'Chikkalasandra', 'Talakaveri Layout', 'Jakkur Plantation', 'Chikkabanavar', 'Hoodi Residential Locality', 'Kothanur,', 'Kodihalli', 'Vittasandra', 'HSR Layout Sector 2', 'Nagasandra', 'Varthur, Whitefield', 'Kalyan Nagar', 'Balagere Road', 'Chikkaballapur', 'Hongasandra', 'Kogilu', 'Old Town', 'Gubbalala', 'Pattandur Agrahara', 'BTM Layout', 'Koramangala,', 'Nallurhalli', 'Konappana Agrahara', 'Panathur Road', 'Banashankari Stage II', 'Dodsworth Layout', 'ITPL', 'Anjanapura', 'Varanasi', 'Kannahalli', 'Hennur Bande', 'Abbigere', 'Sarjapur Road,', 'Sompura', 'Kengeri Satellite Town,', 'Rachenahalli', 'Banashankari Stage VI', 'Harlur Road', 'Ananth Nagar', 'R.T. Nagar', 'Hulimavu,', 'CV Raman Nagar', 'Tindlu', 'Marsur', '2nd Phase Judicial Layout', 'Thyagaraja Nagar', 'HAL 2nd Stage'])
total_sqft = st.number_input('Total Square Feet', min_value=300.0, max_value=50000.0, value=1200.0)
bath = st.slider('Number of Bathrooms', min_value=1, max_value=16, value=2)
bhk = st.slider('Number of BHK', min_value=1, max_value=16, value=2)

if st.button('Predict Price'):
    # Create a DataFrame for prediction
    input_data = pd.DataFrame([{
        'location': location,
        'total_sqft': total_sqft,
        'bath': float(bath),
        'bhk': float(bhk)
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted House Price: ₹ {prediction:.2f} Lakhs')

# To run this Streamlit app:
# 1. Save the code above to a file named `app.py`.
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved `app.py`.
# 4. Run the command: `streamlit run app.py`
# 5. Your web browser will open with the Streamlit application.