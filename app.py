import streamlit as st

# --- 1. الإعدادات الأساسية للمتصفح ---
st.set_page_config(page_title="مكتبة أيوب هاني الذكية", page_icon="🦅", layout="wide")

# --- 2. تصميم الألوان والهوية (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل الخط عربي والاتجاه من اليمين */
    html, body, [class*="css"], .stApp {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0f172a !important; /* كحلي ملكي عميق */
    }

    /* الكتابة العامة بيضاء صافية */
    p, h1, h2, h3, h4, span, label, li {
        color: #ffffff !important;
    }

    /* ميزة ذكية: الكتابة داخل المربعات (Input) لونها ذهبي لتتميز عن النص الأبيض */
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
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 40px;
    }

    /* تصميم كروت الخدمات */
    .service-card {
        background: #1e293b;
        padding: 25px;
        border-radius: 20px;
        border-bottom: 4px solid #c5a059;
        transition: 0.4s;
        text-align: center;
        height: 100%;
    }
    .service-card:hover {
        transform: translateY(-10px);
        border-bottom: 4px solid #facc15;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. عرض مقدمة الموقع ---
st.markdown("""
    <div class="header-box">
        <h1 style="color: #c5a059 !important; font-weight: 900; font-size: 42px;">🦅 مكتبة أيوب هاني الذكية</h1>
        <p style="font-size: 20px; color: #cbd5e1 !important;">بوابتك الرقمية للمونتاج والخدمات المكتبية في القصر الأوسط</p>
    </div>
""", unsafe_allow_html=True)

# --- 4. قسم عرض الخدمات ---
st.write("### 🛠️ خدماتنا المتميزة")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059;">📂 خدمات مكتبية</h3>
            <p>• استنساخ وطباعة ملونة<br>• تصميم CV احترافي<br>• تقديم على التعيينات<br>• تحويل ملفات PDF</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059;">🎬 مونتاج وإبداع</h3>
            <p>• مونتاج CapCut Pro<br>• تصميم لوغوهات وهويات<br>• تصميم منيو وكارتات<br>• تعديل صور بالذكاء الاصطناعي</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059;">💰 معاملات مالية</h3>
            <p>• سحب وإيداع زين كاش<br>• تحويل أموال للمحافظات<br>• شحن بطاقات ألعاب<br>• دفع فواتير وخدمات</p>
        </div>
    """, unsafe_allow_html=True)
