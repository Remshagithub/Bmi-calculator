import streamlit as st

# Page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="⚖", layout="centered")

# Title & Description
st.title("Body Mass Index (BMI) Calculator")
st.markdown("""
### Enter your *weight* and *height* to calculate your BMI.
BMI is an important health indicator that determines your body condition based on weight and height.
""")

# Input Fields
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")

with col2:
    height = st.number_input("Enter your height (m)", min_value=0.1, format="%.2f")

# BMI Calculation
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    
    st.subheader("Your BMI:")
    st.markdown(f"<h2 style='color: #007BFF;'>{bmi:.2f}</h2>", unsafe_allow_html=True)
    
    # BMI Categories
    if bmi < 18.5:
        st.warning("You are underweight")
    elif 18.5 <= bmi <= 24.9:
        st.success("You have a healthy weight")
    elif 25 <= bmi <= 29.9:
        st.warning("You are overweight")
    elif 30 <= bmi <= 34.9:
        st.error("You are obese")
    else:
        st.success("You are perfect! 💪")

# Footer
st.markdown("""
---
✅ This calculator is for guidance only. Please consult a healthcare professional for expert advice.
""")