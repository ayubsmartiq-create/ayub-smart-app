import streamlit as st
import requests
from datetime import datetime

# --- إعدادات الهوية الوطنية والتقنية ---
st.set_page_config(page_title="مكتبة أيوب الذكية | Ayub Smart Library", page_icon="🦅", layout="wide")

# رابط الربط الخاص بك (Formspree)
FORMSPREE_URL = "https://formspree.io/f/xvzvdjzq"

# --- ستايل CSS المحترف (تصميم ملكي معدل للموبايل) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [class*="css"], .stApp { 
        font-family: 'Cairo', sans-serif !important; 
        text-align: right !important; 
        direction: rtl !important; 
        background-color: #0f172a !important; 
        color: white !important;
    }
    
    .header-main { 
        background: linear-gradient(135deg, #1e3a8a 0%, #312e81 100%); 
        padding: 20px; border-radius: 15px; border: 2px solid #facc15; text-align: center;
    }

    /* ستايل فقاعات الدردشة (مثل واتساب) */
    .chat-bubble-user { 
        background: #075e54; color: white; padding: 10px 15px; 
        border-radius: 15px 15px 0 15px; margin: 10px 5px; float: right; clear: both; max-width: 85%;
    }
    .chat-bubble-bot { 
        background: #1e293b; color: white; padding: 10px 15px; 
        border-radius: 15px 15px 15px 0; margin: 10px 5px; float: left; clear: both; max-width: 85%; 
        border: 1px solid #334155;
    }
    
    .stButton>button, .stFormSubmitButton>button {
        background-color: #facc15 !important; color: #0f172a !important;
        font-weight: 900 !important; border-radius: 10px !important; width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- الهيدر واللوغو ---
with st.container():
    col_img, col_txt = st.columns([1, 4])
    with col_img:
        st.image("https://i.ibb.co/v4m0YmC/image.png", width=120)
    with col_txt:
        st.markdown("""
        <div class="header-main">
            <h1 style='color: white; margin:0;'>مكتبة أيوب الذكية 🦅</h1>
            <p style='color: #facc15; font-size:18px;'>المركز التقني الأول لخدمات التعيينات والذكاء الاصطناعي في العراق 🇮🇶</p>
        </div>
        """, unsafe_allow_html=True)

# --- أقسام المكتبة ---
st.divider()
tab1, tab2, tab3 = st.tabs(["🎁 قرطاسية وهدايا", "🤖 تقنية وذكاء", "📝 تعيينات وتقديم"])

with tab1:
    st.markdown("### 📚 تجهيزات كاملة\n* قرطاسية ماركات، دفاتر جامعية، أدوات رسم.\n* هدايا حسب الطلب، تغليف ملكي، طباعة حرارية.")
with tab2:
    st.markdown("### 🚀 خدمات المستقبل\n* تصميم هويات بصرية ولوغوات.\n* بناء أنظمة ذكاء اصطناعي وأتمتة أعمال.")
with tab3:
    st.success("✅ نتابع كافة الاستمارات والتعيينات الحكومية فور صدورها.")

# --- محرك الدردشة الذكي (عقل البوت المطور) ---
st.divider()
st.markdown("### 💬 دردش مع مساعد أيوب الذكي")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "يا هلا بيك عيني! أنا المساعد الذكي لمكتبة أيوب.. شمحتاج اليوم وتدلل؟ 😊"}]

for msg in st.session_state.messages:
    div_class = "chat-bubble-bot" if msg["role"] == "bot" else "chat-bubble-user"
    st.markdown(f"<div class='{div_class}'>{msg['content']}</div>", unsafe_allow_html=True)

user_input = st.chat_input("اكتب سؤالك هنا (مثلاً: شلونكم؟)")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    p = user_input.lower().strip()
    
    # محرك الردود المرن
    if any(word in p for word in ["سلام", "هلو", "مرحبا", "هلا", "صباح", "مساء"]):
        ans = "يا مية هلا بجيتك عيني! نورت مكتبة أخوك أيوب.. تفضل شمحتاج اليوم؟ ✨"
    elif any(word in p for word in ["شلونك", "اخبارك", "اشلونك", "شلونكم"]):
        ans = "بخير ونعمة من الله إذا أنت بخير! تسلم يا طيب، شأقدر أقدملك اليوم من خدماتنا؟"
    elif any(word in p for word in ["تعيين", "تقديم", "وظيفة", "استمارة"]):
        ans = "أبشر! إحنا مختصين بكل أنواع التقديمات. بس املأ اسمك وتفاصيلك بالاستمارة تحت وإحنا نتواصل وياك."
    elif any(word in p for word in ["موقع", "مكان", "وين"]):
        ans = "مقرنا باليوسفية - حي الصقور، بس نوصل لكل محافظات العراق من الشمال للجنوب! ✈️"
    elif any(word in p for word in ["شكرا", "رحم الله", "عاشت"]):
        ans = "تدلل عيني، هذا واجبي! مكتبة أيوب دائماً بخدمتك."
    else:
        ans = "عذراً عيني، ما فهمت قصدك بالضبط.. تقدر تسألني عن التعيينات، القرطاسية، أو التوصيل وتدلل!"

    st.session_state.messages.append({"role": "bot", "content": ans})
    st.rerun()

# --- استمارة الطلب الوطني ---
st.divider()
st.markdown("### 📥 استمارة الطلب (تصل لأيوب فوراً)")
with st.form("national_order", clear_on_submit=True):
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("الأسم الكامل")
        phone = st.text_input("رقم الواتساب")
    with c2:
        city = st.selectbox("المحافظة", ["بغداد", "البصرة", "نينوى", "بقية المحافظات"])
        serv = st.selectbox("نوع الخدمة", ["تعيينات", "قرطاسية", "تصميم", "أخرى"])
    
    msg = st.text_area("تفاصيل طلبك...")
    if st.form_submit_button("إرسال الطلب 🚀"):
        if name and phone:
            requests.post(FORMSPREE_URL, data={"Name": name, "Phone": phone, "City": city, "Service": serv, "Details": msg})
            st.balloons()
            st.success("وصل الطلب! راح نتواصل وياك بأقرب وقت.")
