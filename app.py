import streamlit as st
import random
import datetime

# --- 1. معلومات المكتبة الأساسية ---
# استبدل الأصفار برقمك الفعلي (بدون + وبدون أصفار بالبداية)
MY_WHATSAPP = "9647700000000" 

# --- 2. إعدادات الصفحة ---
st.set_page_config(page_title="مكتبة أيوب هاني الذكية", page_icon="🦅", layout="wide")

# --- 3. تصميم الألوان والهوية (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل الخط عربي والاتجاه من اليمين */
    html, body, [class*="css"], .stApp {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0f172a !important; /* كحلي ملكي */
    }

    /* الكتابة العامة بيضاء صافية */
    p, h1, h2, h3, h4, span, label, li {
        color: #ffffff !important;
    }

    /* ميزة ذكية: الكتابة داخل المربعات لونها ذهبي لتتميز */
    input, textarea, select, div[data-baseweb="select"] > div {
        background-color: #1e293b !important;
        color: #facc15 !important; /* ذهبي للمدخلات */
        border: 2px solid #c5a059 !important;
        border-radius: 12px !important;
    }

    /* تصميم مقدمة الموقع (الرأس) */
    .header-box {
        background: linear-gradient(135deg, #0b3d61 0%, #1e293b 100%);
        padding: 40px;
        border-radius: 25px;
        border-right: 10px solid #c5a059;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. واجهة الموقع (المقدمة) ---
st.markdown("""
    <div class="header-box">
        <h1 style="color: #c5a059 !important; font-weight: 900; font-size: 40px;">🦅 مكتبة أيوب هاني الذكية</h1>
        <p style="font-size: 18px; color: #cbd5e1 !important;">خيارك الأول للمونتاج الاحترافي والخدمات المكتبية | القصر الأوسط</p>
    </div>
""", unsafe_allow_html=True)

st.info("نظام التشغيل الآن جاهز.. بانتظار إضافة الأقسام.")
