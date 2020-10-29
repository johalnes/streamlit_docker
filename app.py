import streamlit as st
import pandas as pd

st.write("## KPMG Forsikring - engangspremie beregninger")

st.write("__Velg fil som skal lastes opp og fra hvilken leverandør det kommer fra. Resultatet lagres på filformat klart for rapprt__")

file = st.file_uploader("Choose Excelfile", type="xlsx")

if file is not None:
    data=pd.read_excel(file)
    st.write(data.head())
    
vendor = st.selectbox("Velg leverandør",["Storebrand Liv","Gabler","Eika"])
