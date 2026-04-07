import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon="🦅", layout="wide")

# 2. تصميم الواجهة (CSS) - ألوان مستوحاة من اللوغو الخاص بك
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل كل النصوص العامة بيضاء */
    html, body, [class*="css"], .stApp, p, h1, h2, h3, h4, span, label {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; 
        text-align: right !important;
        color: #ffffff !important;
    }
    
    /* خلفية الموقع زرقاء غامقة ملكية */
    .stApp {
        background-color: #0f172a !important;
    }
    
    /* تصميم المربعات (Input Boxes): خلفية غامقة وكتابة بيضاء */
    input, textarea, select, div[data-baseweb="select"] > div {
        background-color: #1e293b !important; /* أزرق غامق مريح */
        color: #ffffff !important; /* الكتابة بيضاء */
        border: 2px solid #c5a059 !important; /* إطار ذهبي نفس اللوغو */
        border-radius: 10px !important;
    }

    /* ضمان ظهور النص المكتوب داخل المربعات باللون الأبيض */
    input { color: white !important; -webkit-text-fill-color: white !important; }
    textarea { color: white !important; -webkit-text-fill-color: white !important; }

    /* تصميم رأس الصفحة (الهيدر) */
    .header-box {
        background: linear-gradient(135deg, #0b3d61, #1e293b);
        padding: 20px; border-radius: 20px; border-bottom: 5px solid #c5a059;
        text-align: center; margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. عرض اللوغو والهيدر
# ملاحظة: سنستخدم رابط اللوغو الذي رفعته أنت سابقاً أو يمكنك رفعه على GitHub باسم Ayub-Logo.png
st.markdown("""
    <div class="header-box">
        <h1 style="color: #c5a059 !important;">🦅 مكتبة أيوب الذكية</h1>
        <p>دقة، سرعة، واحترافية رقمية من قلب القصر الأوسط</p>
    </div>
""", unsafe_allow_html=True)

st.write("---")
st.success("تم تشغيل الخطوة الأولى بنجاح! الألوان والخطوط جاهزة الآن.")
