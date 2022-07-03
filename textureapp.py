import streamlit as st
import pickle
import pandas as pd
import numpy as np


pipe = pickle.load(open('texture.pkl','rb'))
st.title('Coarsity Predictor')


Sand = st.number_input('Sand')
Silt = st.number_input('Silt')
cacl2ph = st.number_input('cacl2ph')
h2oph = st.number_input('h2oph')
EC = st.number_input('EC')
OC = st.number_input('OC')
CaCO3 = st.number_input('CaCO3')
P = st.number_input('P')
N = st.number_input('N')
K = st.number_input('K')
Clay = st.number_input('Clay')


# 'pH(CaCl2)':[pH(CaCl2)],'pH(H2O)':[pH(H2O)],
if st.button('Predict Coarse'):
      input=pd.DataFrame({'Sand':[Sand],'Silt':[Silt],'cacl2ph':[cacl2ph],'h2oph':[h2oph],'EC':[EC],'OC':[OC],'CaCO3':[CaCO3],'P':[P],'N':[N],'K':[K],'Clay':[Clay]})
      result = pipe.predict(input)
      st.success('THE Coarsity FOR GIVEN DATA WILL BE {}'.format(result))
# st.header(result)