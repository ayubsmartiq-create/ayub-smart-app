import streamlit as st
import datetime

# --- 1. إعدادات المتصفح الأساسية ---
st.set_page_config(page_title="مكتبة أيوب هاني الذكية", page_icon="🦅", layout="wide")

# --- 2. هندسة التصميم (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* الخلفية العامة والنصوص */
    html, body, [class*="css"], .stApp {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0f172a !important; /* كحلي ملكي عميق */
    }

    /* الكتابة العامة باللون الأبيض الصافي */
    p, h1, h2, h3, h4, span, label, li {
        color: #ffffff !important;
    }

    /* تصميم مربعات الإدخال - الكتابة داخلها بلون ذهبي هادئ لتمييزها */
    input, textarea, select, div[data-baseweb="select"] > div {
        background-color: #1e293b !important; /* لون أفتح قليلاً للمربعات */
        color: #facc15 !important; /* اللون الذهبي للكتابة داخل المربعات */
        border: 2px solid #c5a059 !important;
        border-radius: 12px !important;
    }

    /* تصميم رأس الصفحة (المقدمة المحترفة) */
    .header-container {
        background: linear-gradient(135deg, #0b3d61 0%, #1e293b 100%);
        padding: 40px;
        border-radius: 25px;
        border-right: 8px solid #c5a059;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        text-align: center;
        margin-bottom: 40px;
    }

    /* كروت الخدمات */
    .service-card {
        background: #1e293b;
        padding: 25px;
        border-radius: 20px;
        border-bottom: 4px solid #c5a059;
        transition: 0.3s;
        height: 100%;
    }
    .service-card:hover {
        transform: translateY(-10px);
        border-bottom: 4px solid #facc15;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. عرض المقدمة المحترفة ---
st.markdown("""
    <div class="header-container">
        <h1 style="color: #c5a059 !important; font-weight: 900; font-size: 45px;">🦅 مكتبة أيوب هاني الذكية</h1>
        <p style="font-size: 20px; color: #cbd5e1 !important;">بوابتك الرقمية للخدمات المكتبية والمونتاج الاحترافي في القصر الأوسط</p>
    </div>
""", unsafe_allow_html=True)

# --- 4. قسم الخدمات والأنواع ---
st.write("### 🛠️ خدماتنا المتميزة")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059; text-align: center;">📂 الخدمات المكتبية</h3>
            <ul style="list-style-type: none; padding: 0;">
                <li>✅ استنساخ وطباعة ملازم</li>
                <li>✅ عمل سيرة ذاتية (CV) ملكية</li>
                <li>✅ التقديم على الاستمارات والتعيينات</li>
                <li>✅ تحويل ودمج ملفات PDF</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059; text-align: center;">🎬 المونتاج والإبداع</h3>
            <ul style="list-style-type: none; padding: 0;">
                <li>✅ مونتاج فيديوهات CapCut احترافي</li>
                <li>✅ تصميم لوغو وهويات بصرية</li>
                <li>✅ تصميم منيو مطاعم وكارتات عمل</li>
                <li>✅ معالجة الصور بالذكاء الاصطناعي</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059; text-align: center;">💰 معاملات زين كاش</h3>
            <ul style="list-style-type: none; padding: 0;">
                <li>✅ سحب وإيداع (Zain Cash)</li>
                <li>✅ تحويل أموال لكافة المحافظات</li>
                <li>✅ دفع فواتير الماء والكهرباء</li>
                <li>✅ شحن بطاقات ألعاب (PUBG / ITUNES)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
