# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:48:15 2024

@author: HALDEN
"""

import streamlit as st
import pickle
import numpy as np


def load_model():
    data=pickle.load(open('D:/vscode/python_files/deploying_using_stremlt/salaryprediction/saved_steps.pkl','rb'))
     
    
    return data

data=load_model() 

regressor=data['model']
le_country=data["le_country"]
le_education=data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    
    st.write("""### We need some information to predict the salary""")
    Countries=(
     'Afghanistan',
     'Albania',
     'Algeria',
     'Andorra',
     'Angola',
     'Antigua and Barbuda',
     'Argentina',
     'Armenia',
     'Australia',
     'Austria',
     'Azerbaijan',
     'Bahrain',
     'Bangladesh',
     'Barbados',
     'Belarus',
     'Belgium',
     'Belize',
     'Benin',
     'Bolivia',
     'Bosnia and Herzegovina',
     'Botswana',
     'Brazil',
     'Brunei Darussalam',
     'Bulgaria',
     'Burkina Faso',
     'Burundi',
     'Cambodia',
     'Cameroon',
     'Canada',
     'Cape Verde',
     'Chile',
     'China',
     'Colombia',
     'Costa Rica',
     'Croatia',
     'Cuba',
     'Cyprus',
     'Czech Republic',
     "Côte d'Ivoire",
     'Denmark',
     'Djibouti',
     'Dominica',
     'Dominican Republic',
     'Ecuador',
     'Egypt',
     'El Salvador',
     'Estonia',
     'Ethiopia',
     'Fiji',
     'Finland',
     'France',
     'Gabon',
     'Georgia',
     'Germany',
     'Ghana',
     'Greece',
     'Guatemala',
     'Guinea',
     'Guinea-Bissau',
     'Guyana',
     'Honduras',
     'Hong Kong (S.A.R.)',
     'Hungary',
     'Iceland',
     'India',
     'Indonesia',
     'Iran, Islamic Republic of...',
     'Iraq',
     'Ireland',
     'Isle of Man',
     'Israel',
     'Italy',
     'Jamaica',
     'Japan',
     'Jordan',
     'Kazakhstan',
     'Kenya',
     'Kosovo',
     'Kuwait',
     'Kyrgyzstan',
     "Lao People's Democratic Republic",
     'Latvia',
     'Lebanon',
     'Lesotho',
     'Libyan Arab Jamahiriya',
     'Liechtenstein',
     'Lithuania',
     'Luxembourg',
     'Madagascar',
     'Malawi',
     'Malaysia',
     'Maldives',
     'Mali',
     'Malta',
     'Mauritania',
     'Mauritius',
     'Mexico',
     'Monaco',
     'Mongolia',
     'Montenegro',
     'Morocco',
     'Mozambique',
     'Myanmar',
     'Namibia',
     'Nepal',
     'Netherlands',
     'New Zealand',
     'Nicaragua',
     'Niger',
     'Nigeria',
     'Nomadic',
     'Norway',
     'Oman',
     'Pakistan',
     'Palau',
     'Palestine',
     'Panama',
     'Paraguay',
     'Peru',
     'Philippines',
     'Poland',
     'Portugal',
     'Qatar',
     'Republic of Korea',
     'Republic of Moldova',
     'Romania',
     'Russian Federation',
     'Rwanda',
     'Saint Kitts and Nevis',
     'Saint Lucia',
     'Saint Vincent and the Grenadines',
     'Saudi Arabia',
     'Senegal',
     'Serbia',
     'Sierra Leone',
     'Singapore',
     'Slovakia',
     'Slovenia',
     'Somalia',
     'South Africa',
     'South Korea',
     'Spain',
     'Sri Lanka',
     'Sudan',
     'Suriname',
     'Swaziland',
     'Sweden',
     'Switzerland',
     'Syrian Arab Republic',
     'Taiwan',
     'Tajikistan',
     'Thailand',
     'The former Yugoslav Republic of Macedonia',
     'Togo',
     'Trinidad and Tobago',
     'Tunisia',
     'Turkey',
     'Turkmenistan',
     'Uganda',
     'Ukraine',
     'United Arab Emirates',
     'United Kingdom of Great Britain and Northern Ireland',
     'United Republic of Tanzania',
     'United States of America',
     'Uruguay',
     'Uzbekistan',
     'Venezuela, Bolivarian Republic of...',
     'Viet Nam',
     'Yemen',
     'Zambia',
     'Zimbabwe'
        
        
        
        )
    education=(
     'Associate degree (A.A., A.S., etc.)',
     'Bachelor’s degree (B.A., B.S., B.Eng., etc.)',
     'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)',
     'Primary/elementary school',
     'Professional degree (JD, MD, Ph.D, Ed.D, etc.)',
     'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)',
     'Some college/university study without earning a degree',
     'Something else'  
        )
    
    country = st.selectbox("country",Countries)
    education = st.selectbox("EdLevel",education)
    
    experience=st.slider("Years of Experience ",0,50,3)
    
    ok=st.button("Calculate Salary")
    if ok:
        X=np.array([["United States of America", 'Master’s degree', 15 ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)
        
        salary=regressor.predict(X)
        salary=salary[0]
        st.subheader(f"the estimated salary is  ${salary}")
