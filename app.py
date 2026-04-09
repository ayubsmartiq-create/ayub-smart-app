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
# نص فوق المربع (ذهبي)
st.markdown('<h1 class="gold-title">🦅 مكتبة أيوب هاني الذكية</h1>', unsafe_allow_html=True)

# المربع وبداخله نص (أبيض)
st.markdown("""
    <div class="custom-box">
        <p class="box-text">أهلاً بك يا بطل! هذا المربع مصمم لعرض المعلومات بوضوح وبألوان متناسقة مع هويتك البصرية.</p>
    </div>
    """, unsafe_allow_html=True)
# --- عنوان قسم الخدمات ---
st.markdown('<h2 class="gold-title">🛠️ خدماتنا الاحترافية</h2>', unsafe_allow_html=True)

# القسم الأول: المونتاج
st.markdown("""
    <div class="custom-box">
        <h3 style="color: #c5a059;">🎬 صناعة المحتوى والمونتاج</h3>
        <p class="box-text">
            • مونتاج فيديوهات تيك توك وريلز باحترافية عالي.<br>
            • إضافة انتقالات وترجمة تلقائية (Subtitles).<br>
            • تعديل الألوان وهندسة الصوت باستخدام CapCut Pro.
        </p>
    </div>
    """, unsafe_allow_html=True)

# القسم الثاني: الخدمات المكتبية والبحوث
st.markdown("""
    <div class="custom-box">
        <h3 style="color: #c5a059;">📄 الخدمات المكتبية والبحوث</h3>
        <p class="box-text">
            • طباعة وبحوث التخرج والتقارير المدرسية.<br>
            • تصميم السيرة الذاتية (CV) بنماذج عصرية.<br>
            • سحب وتصوير المستندات بدقة عالية.
        </p>
    </div>
    """, unsafe_allow_html=True)

# القسم الثالث: الهوية البصرية
st.markdown("""
    <div class="custom-box">
        <h3 style="color: #c5a059;">🎨 التصميم الجرافيكي</h3>
        <p class="box-text">
            • تصميم لوغو (Logo) خاص لمشروعك.<br>
            • تصميم كروت عمل (Business Cards).<br>
            • بوستات إعلانية احترافية للفيسبوك والانستغرام.
        </p>
    </div>
    """, unsafe_allow_html=True)
# عنوان الاستمارة بلون ذهبي
st.markdown('<h2 class="gold-title">📝 اطلب خدمتك الآن</h2>', unsafe_allow_html=True)

# المربع الكبير الذي يضم الاستمارة
with st.container():
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    
    # بداية النموذج
    with st.form("order_form"):
        u_name = st.text_input("الاسم الثلاثي")
        u_phone = st.text_input("رقم الهاتف (واتساب)")
        u_service = st.selectbox("اختار الخدمة", ["مونتاج فيديو", "تصميم شعار", "طباعة وبحوث", "خدمة أخرى"])
        u_details = st.text_area("تفاصيل إضافية (اختياري)")
        
        # زر الإرسال
        submit_btn = st.form_submit_button("إرسال الطلب وحفظه")
    
    st.markdown('</div>', unsafe_allow_html=True)
