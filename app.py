import streamlit as st
import pandas as pd

st.title("Nassau Candy - Shipping Optimization Dashboard")

# Load your optimized file
df = pd.read_csv(r'D:\Nassau Codiinator\Final_Optimized_Data.csv')

# Dropdown for Product
selected_product = st.selectbox("Select Product:", df['Product Name'].unique())

# Filter data
product_data = df[df['Product Name'] == selected_product]

# Show findings
st.write(f"Optimization Analysis for {selected_product}")
st.dataframe(product_data[['City', 'State/Province', 'Nearest_Factory']].head(10))

# Visual Summary
st.bar_chart(product_data['Nearest_Factory'].value_counts())