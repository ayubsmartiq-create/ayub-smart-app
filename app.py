import streamlit as st
import pandas as pd
import os
import datetime
import random

# إعداد الصفحة
st.set_page_config(page_title="مكتبة أيوب الذكية", layout="centered")

# تصميم الألوان (CSS)
st.markdown("""
    <style>
    /* 1. لون الخلفية الأساسية للموقع (كحلي ملكي) */
    .main { background-color: #0f172a; }
    .stApp { background-color: #0f172a; }

    /* 2. لون النص الرئيسي فوق المربعات (ذهبي) */
    .gold-title { 
        color: #c5a059 !important; 
        text-align: right; 
        font-family: 'Arial'; 
        font-weight: bold;
    }

    /* 3. تصميم المربعات (الحاويات) */
    .custom-box {
        background-color: #1e293b; /* لون المربع من الداخل */
        padding: 20px; 
        border-radius: 15px; 
        border-right: 5px solid #c5a059; /* خط ذهبي جانبي */
        margin-bottom: 20px;
        text-align: right;
    }

    /* 4. لون النص داخل المربعات (أبيض ناصع) */
    .box-text { 
        color: #ffffff !important; 
        font-size: 16px;
    }

    /* 5. تنسيق الحقول (Inputs) */
    input, textarea {
        background-color: #334155 !important;
        color: white !important; /* لون الكتابة داخل حقل الإدخال */
        border: 1px solid #c5a059 !important;
    }
    </style>
    """, unsafe_allow_html=True)
