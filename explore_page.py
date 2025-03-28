# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:48:43 2024

@author: HALDEN
"""
import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)



def clean_education(x):
    if x=='Bachelor’s degree (B.A., B.S., B.Eng., etc.)':
        return 'Bachelor’s degree'
    if x=='Master’s degree (M.A., M.S., M.Eng., MBA, etc.)':
        return 'Master’s degree'
    if x=='Professional degree (JD, MD, Ph.D, Ed.D, etc.)' :
        return 'Post grad'
    return 'Less than a Bachelors'
 
    
 
@st.cache_data
def load_data_1():
    
     df = pd.read_csv("D:/vscode/python_files/deploying_using_stremlt/salaryprediction/survey_results_public.csv")
     df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
     df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
     df=df[df["Salary"].notnull()]
     df=df.dropna()
     df=df[df["Employment"]=="Employed full-time"]
     df=df.drop("Employment",axis=1)
     
     country_map=shorten_categories(df.Country.value_counts(), 400)
     df["Country"]=df["Country"].map(country_map)
     df=df[df["Salary"]<=250000]
     df=df[df["Salary"]>=10000]
     df=df[df["Country"]!="Other"]
     
     df["YearsCodePro"]=df["YearsCodePro"].apply(clean_experience)
     df["EdLevel"]=df["EdLevel"].apply(clean_education)
     return df
 
df=load_data_1()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")
    st.write(
        """### Stack Overflow Developer Survey 2023"""
        
        )
    
    
    data=df["Country"].value_counts()
    
    fig1, ax1=plt.subplots()
    ax1.pie(data,labels=data.index, autopct="%1.1f%", shadow=True, startangle=90)
    ax1.axis("equal")
    
    st.write("""### Number of data from Different countries""")
    st.pyplot(fig1)
    
    st.write(
        """#### Mean Salary Based On Country"""
        
        )
    data=df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    
    st.bar_chart(data)