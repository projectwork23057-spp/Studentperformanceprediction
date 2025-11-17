import streamlit as st
import pickle
import pandas as pd
model=0
# Load the saved model
with open('model.pkl', 'rb') as f:
    try:
        model = pickle.load(f)
    except Exception as e:
        print(e,type(e))

st.title("Student Performance Prediction System")

# User input
#feature1 = st.slider("Feature 1", 0.0, 10.0, 5.0)
Thirdsem=st.slider("scaled",300,900,1)
Studyhour=st.slider("Studyhour",1,4,1)
Attendance=st.slider("Attendance",60,100,1)
Health=st.slider("health",0,1,1)
InternetAccess=st.slider("InternetAccess",0,1,1)
Region=st.slider("Region",0,1,1)
DaysScholarORhosteler=st.slider("D/H",0,1,1)
Time=st.slider("Time",5,40,1)
ParentsEducated=st.slider("Parent's educated",0,1,1)
ClassResponse=st.slider("class response",0,2,1)
st.write(type((Thirdsem)))
# Preprocess input (if necessary)
# ...

# Make prediction
if st.button("Predict"):
    # Assuming your model expects a DataFrame or specific input format
    input_data = pd.DataFrame([['Thirdsem','Studyhour','Attendance','Health','InternetAccess','Region','DaysScholarORhosteler','Time','ParentsEducated','ClassResponse']], columns=['scaled','Study hours','Attendance','health','Internet Access','Region','D/H','Time',"Parent's educated",'class response'])
    prediction = model.predict(input_data)
    st.write(f"The prediction is: {prediction[0]}")









