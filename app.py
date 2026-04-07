import streamlit as st

# 1. إعدادات الصفحة الأساسية واللوغو الخاص بك
LOGO_URL = "https://raw.githubusercontent.com/ayubsmartiq-create/ayub-smart-app/main/Ayub-Logo.png"
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon=LOGO_URL, layout="wide")

# 2. هندسة الألوان (CSS) - لجعل الموقع فخم والكتابة واضحة
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل كل النصوص العامة بيضاء تماماً */
    html, body, [class*="css"], .stApp, p, h1, h2, h3, h4, span, label, .stMarkdown {{
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; 
        text-align: right !important;
        color: #ffffff !important; /* لون النص أبيض */
    }}
    
    /* خلفية الموقع زرقاء غامقة ملكية */
    .stApp {{
        background-color: #0f172a !important;
    }}
    
    /* تصميم المربعات (Input Boxes): خلفية غامقة وكتابة بيضاء واضحة */
    input, textarea, select, div[data-baseweb="select"] > div {{
        background-color: #1e293b !important; /* لون المربع غامق */
        color: #ffffff !important; /* الكتابة داخل المربع بيضاء */
        border: 2px solid #facc15 !important; /* إطار ذهبي مميز */
        border-radius: 10px !important;
    }}

    /* حل مشكلة اختفاء النص عند الكتابة داخل المربعات */
    input {{ color: white !important; -webkit-text-fill-color: white !important; }}
    textarea {{ color: white !important; -webkit-text-fill-color: white !important; }}

    /* تصميم رأس الصفحة (الهيدر) */
    .header-box {{
        background: linear-gradient(135deg, #1e40af, #1e3a8a);
        padding: 30px; border-radius: 20px; border-bottom: 5px solid #facc15;
        text-align: center; margin-bottom: 25px;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة الرئيسي (الهيدر)
st.markdown('<div class="header-box"><h1>🦅 مكتبة أيوب الذكية </h1><p>دقة، سرعة، واحترافية رقمية من قلب اليوسفية</p></div>', unsafe_allow_html=True)

st.write("---")
st.info("أهلاً بك يا أيوب! تم تأسيس الهيكل بنجاح. جرب الآن إذا كانت الألوان مريحة للعين.")
