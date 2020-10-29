import streamlit as st
import pandas as pd

st.write("## IBNR analyse")

st.write("__Velg fil som skal lastes opp og fra hvilken leverandør det kommer fra. Resultatet lagres på filformat klart for rapprt__")

file = st.file_uploader("Choose Excelfile", type="xlsx")

if file is not None:
    data=pd.read_excel(file)
    st.write(data.head())
    
vendor = st.selectbox("Velg produkt",["Motorvogn Ansvar", "Motorvogn kasko","Hus - privatbolig"])
