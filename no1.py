import pandas as pd
import streamlit as st

# Membaca file Excel
file_path = "PROJEK SIM PETERNAKAN NIO-1.xlsx"
df = pd.read_excel(file_path)

# Streamlit
st.title("Data dari Excel")
st.write("Berikut adalah data yang dibaca dari file Excel:")
st.dataframe(df)


