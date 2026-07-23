import streamlit as st
import pandas as pd

st.title("Nassau Candy - Shipping Optimization Dashboard")

# Load your optimized file
df = pd.read_csv('Final_Optimized_Data.csv')

# Dropdown for Product
selected_product = st.selectbox("Select Product:", df['Product Name'].unique())

# Filter data
product_data = df[df['Product Name'] == selected_product]

# Show findings
st.write(f"Optimization Analysis for {selected_product}")
st.dataframe(product_data[['City', 'State/Province', 'Nearest_Factory']].head(10))

# Visual Summary
st.bar_chart(product_data['Nearest_Factory'].value_counts())

# Isse app.py ke end mein ya jahan tum table show kar rahe ho, wahan paste karo
with st.expander("📊 Predictive Model Performance Metrics"):
    st.write("To enhance decision making, we implemented a Random Forest Regressor.")
    col1, col2, col3 = st.columns(3)
    col1.metric("RMSE", "269.87")
    col2.metric("MAE", "216.17")
    col3.metric("R2 Score", "-0.03")
    st.info("Note: The model is currently at the baseline stage. Accuracy will improve with more granular feature data.")
