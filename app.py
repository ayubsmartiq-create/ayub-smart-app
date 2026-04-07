import streamlit as st

# 1. إعدادات الصفحة الأساسية واللوغو
LOGO_URL = "https://raw.githubusercontent.com/ayubsmartiq-create/ayub-smart-app/main/Ayub-Logo.png"
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon=LOGO_URL, layout="wide")

# 2. هندسة الألوان والخطوط (CSS) - التركيز على اللون الأبيض
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل كل نصوص الموقع باللون الأبيض */
    html, body, [class*="css"], .stApp, p, h1, h2, h3, h4, span, label, div {{
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; 
        text-align: right !important;
        color: #ffffff !important;
    }}
    
    /* خلفية الموقع زرقاء غامقة جداً لتبرز الخط الأبيض */
    .stApp {{
        background-color: #0f172a !important;
    }}
    
    /* تصميم رأس الصفحة (الهيدر) */
    .header-box {{
        background: linear-gradient(135deg, #1e40af, #1e3a8a);
        padding: 30px; border-radius: 20px; border-bottom: 5px solid #facc15;
        text-align: center; margin-bottom: 25px;
    }}

    /* تعديل لون حقول الكتابة ليكون النص داخلها أسود (حتى يرى الزبون ما يكتب) */
    input, textarea, select {{
        color: #000000 !important;
        background-color: #ffffff !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة الرئيسي (الهيدر)
st.markdown('<div class="header-box"><h1>🦅 مكتبة أيوب الذكية </h1><p>خيارك الذكي للخدمات الإلكترونية والمونتاج</p></div>', unsafe_allow_html=True)

st.write("أهلاً بك يا بطل! هذا هو الهيكل الأساسي لموقعك باللون الأبيض.")
