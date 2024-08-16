# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 16:53:48 2024

@author: HALDEN
"""

import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


page=st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))

if page=="Predict":
    
     show_predict_page()
 
    
else:
    show_explore_page()
     
