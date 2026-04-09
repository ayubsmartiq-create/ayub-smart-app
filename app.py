import streamlit as st
import pandas as pd
import os
import datetime
import random
# إعدادات الصفحة
st.set_page_config(page_title="مكتبة أيوب الذكية", layout="centered")

# التصميم البرمجي (CSS)
st.markdown("""
    <style>
    /* لون الخلفية الأساسية */
    .stApp { background-color: #0f172a; }

    /* تنسيق العنوان الذهبي فوق المربعات */
    .gold-title { 
        color: #c5a059 !important; 
        text-align: right; 
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* تنسيق المربعات (الحاويات) */
    .custom-box {
        background-color: #1e293b; 
        padding: 20px; 
        border-radius: 15px; 
        border-right: 5px solid #c5a059;
        margin-bottom: 25px;
        text-align: right;
    }

    /* لون النص داخل المربعات */
    .box-text { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)
st.markdown('<h1 class="gold-title">🦅 مكتبة أيوب هاني الذكية</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="custom-box">
        <p class="box-text">أهلاً بك في منصتنا الإلكترونية. نحن هنا لنقدم لك أفضل خدمات المونتاج، التصميم، والخدمات المكتبية بأعلى جودة.</p>
    </div>
    """, unsafe_allow_html=True)
