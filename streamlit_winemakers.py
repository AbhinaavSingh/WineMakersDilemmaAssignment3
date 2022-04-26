from numpy import dsplit
import streamlit as st


# Whenever sensi or speci go below 0.5, the model reaches breakeven

st.title('Winemakers Dilemma:Assignment 3')

st.text('Machine Learning in Practice, Spring 2022')
st.text('Name: Abhinaav Singh')
st.text('Andrew ID: abhinaas')

# mold_val = 10
# no_sugar_val = 60
# typical_sugar_val = 30 
# high_sugar_val = 10

mold_val = st.slider('Chance of botrytis', step=1, value=10)
no_sugar_val = st.slider('Chance of No Sugar', step=1, value=60)
typical_sugar_val = st.slider('Chance of Typical Sugar', step=1, value=30)
high_sugar_val = st.slider('Chance of High Sugar', step=1, value=10)

ds_value = 0.76* ((mold_val/100)*3300000 + 0.9*420000) + 0.25* ((no_sugar_val/100)*960000 + (typical_sugar_val/100)*1410000 + (high_sugar_val/100)*1500000) 
dns_value = 0.77* ((no_sugar_val/100)*960000 + (typical_sugar_val/100)*1410000 + (high_sugar_val/100)*1500000) + 0.23*((mold_val/100)*3300000 + 0.9*420000)
clairvoyance_value = 0.82* (ds_value) + 0.18* (dns_value)


if (no_sugar_val + typical_sugar_val + high_sugar_val) > 100:
    st.error("Error: Total Sugar Level can't be over 100\%")



# st.write(f'{n} + 1 = {clairvoyance_value}')

st.success(f'Value of  EV = {clairvoyance_value}')

if(clairvoyance_value > 960000): 
    st.success('Recommended Alternative: Clairvoyance')
else:
    st.success('Recommended Alternative: No Clairvoyance')

