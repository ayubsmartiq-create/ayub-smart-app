import streamlit as st
import requests
from datetime import datetime

# --- إعدادات الهوية الوطنية والتقنية ---
st.set_page_config(page_title="مكتبة أيوب الذكية | Ayub Smart Library", page_icon="🦅", layout="wide")

# رابط الربط الخاص بك
FORMSPREE_URL = "https://formspree.io/f/xvzvdjzq"

# --- ستايل CSS المحترف والمعدل للموبايل (جبار) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* فرض التنسيق على كل شي */
    html, body, [class*="css"], .stApp { 
        font-family: 'Cairo', sans-serif !important; 
        text-align: right !important; 
        direction: rtl !important; 
        background-color: #0f172a !important; /* خلفية داكنة */
        color: white !important;
    }
    
    /* ستايل الهيدر الملكي */
    .header-main { 
        background: linear-gradient(135deg, #1e3a8a 0%, #312e81 100%); 
        padding: 20px; 
        border-radius: 15px; 
        border: 2px solid #facc15; 
        text-align: center !important;
    }
    
    /* أقسام المكتبة */
    .stTabs [data-baseweb="tab-list"] { background-color: rgba(255,255,255,0.05); border-radius: 10px; }
    .stTabs [data-baseweb="tab"] { color: #facc15 !important; font-weight: bold; }
    .stTabs [aria-selected="true"] { color: white !important; border-bottom-color: #facc15 !important; }

    /* ستايل فقاعات الدردشة */
    .chat-bubble-user { 
        background: #075e54; 
        color: white; 
        padding: 10px 15px; 
        border-radius: 15px 15px 0 15px; 
        margin: 5px; 
        float: right; 
        clear: both; 
        max-width: 80%;
    }
    .chat-bubble-bot { 
        background: #1e293b; 
        color: white; 
        padding: 10px 15px; 
        border-radius: 15px 15px 15px 0; 
        margin: 5px; 
        float: left; 
        clear: both; 
        max-width: 80%; 
        border: 1px solid #334155;
    }
    
    /* ستايل الأزرار واستمارات الإرسال */
    .stButton>button, .stFormSubmitButton>button {
        background-color: #facc15 !important;
        color: #0f172a !important;
        font-weight: 900 !important;
        border-radius: 10px !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- الهيدر الملكي باللوغو ---
with st.container():
    col_img, col_txt = st.columns([1, 4])
    with col_img:
        st.image("https://i.ibb.co/v4m0YmC/image.png", width=120)
    with col_txt:
        st.markdown("""
        <div class="header-main">
            <h1 style='color: white; margin:0;'>مكتبة أيوب الذكية 🦅</h1>
            <p style='color: #facc15; font-size:18px;'>الوجهة التقنية والخدمية الأولى لكل العراقيين 🇮🇶</p>
        </div>
        """, unsafe_allow_html=True)

# --- استكشف أقسامنا (المعدلة للموبايل) ---
st.divider()
st.markdown("### 📂 استكشف أقسامنا الوطنية")
tab_gif, tab_ai, tab_jobs = st.tabs(["🎁 هدايا وقرطاسية", "🤖 ذكاء وتقنية", "📝 تعيينات وتقديم"])

with tab_gif:
    st.markdown("""
    **📍 القرطاسية:** ماركات عالمية، دفاتر فاخرة، أدوات هندسية ورسم.
    <br>**🎁 الهدايا:** تجهيز وتغليف ملكي، ألعاب ذكاء، طباعة دروع وأكواب.
    """, unsafe_allow_html=True)

with tab_ai:
    st.markdown("""
    **🚀 الخدمات التقنية:**
    * **ذكاء اصطناعي:** بناء بوتات وأنظمة أتمتة.
    * **التصميم:** لوغوات باحترافية عراقيّة.
    * **الطباعة:** ليزرية فائقة الدقة.
    """)

with tab_jobs:
    st.success("✅ نتابع التقديم على جميع التعيينات والاستمارات الحكومية.")
    st.markdown("""
    * **تعيينات** (عقود، ملاك، أمنية).
    * **دراسات** (جامعات، أهلي، صباحي).
    * **تحديث بيانات** تموينية وانتخابية.
    """)

# --- دردشة أيوب الذكية (تشبه الواتساب) ---
st.divider()
st.markdown("### 💬 دردشة سريعة مع أيوب")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "bot", "content": "هلا بيك عيني! اسأل أي شي ببالك عن المكتبة أو التعيينات وتدلل! 😊"}]

for msg in st.session_state.chat_history:
    cls = "chat-bubble-bot" if msg["role"] == "bot" else "chat-bubble-user"
    st.markdown(f"<div class='{cls}'>{msg['content']}</div>", unsafe_allow_html=True)

user_input = st.chat_input("اكتب سؤالك هنا...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.markdown(f"<div class='chat-bubble-user'>{user_input}</div>", unsafe_allow_html=True)
    
    # ردود سريعة
    ans = "حلو! بس وضحلي قصدك أكثر حتى أخدمك.."
    txt = user_input.lower()
    if "سلام" in txt or "هلا" in txt: ans = "وعليكم السلام والرحمة! نورت مكتبتك يا طيب، شلون أساعدك اليوم؟ ✨"
    elif "تعيين" in txt or "شلون اقدم" in txt: ans = "أبشر! عدنا فريق مختص يقدم لك ع التعيين باحترافية. شمحتاج هسة؟"
    elif "موقع" in txt: ans = "عنواننا باليوسفية حي الصقور، بس التوصيل لكل العراق طيارة! ✈️"
    
    st.session_state.chat_history.append({"role": "bot", "content": ans})
    st.markdown(f"<div class='chat-bubble-bot'>{ans}</div>", unsafe_allow_html=True)

# --- استمارة الطلب الوطني (الاحترافية) ---
st.divider()
st.markdown("### 📥 استمارة الطلب الوطني")
with st.form("national_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        f_name = st.text_input("الأسم الثلاثي")
        f_phone = st.text_input("رقم الواتساب")
    with col2:
        f_city = st.selectbox("المحافظة", ["بغداد", "البصرة", "نينوى", "أربيل", "بقية المحافظات"])
        f_service = st.selectbox("الخدمة", ["تعيينات", "قرطاسية", "تصميم", "أخرى"])
    
    f_details = st.text_area("تفاصيل الطلب...")
    
    btn_submit = st.form_submit_button("إرسال الطلب الوطني")
    if btn_submit:
        if f_name and f_phone:
            requests.post(FORMSPREE_URL, data={"name":f_name, "phone":f_phone, "city":f_city, "service":f_service, "details":f_details})
            st.balloons()
            st.success("عاشت إيدك! طلبك طار ووصل لأيوب، راح نتواصل وياك.")
