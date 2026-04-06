import streamlit as st
import requests

# --- 1. إعدادات الهوية واللوغو الجديد ---
LOGO_URL = "https://i.postimg.cc/85M6mGvP/Ayub-Logo.png"

st.set_page_config(
    page_title="مكتبة أيوب الذكية", 
    page_icon=LOGO_URL, 
    layout="wide"
)

# كود إجبار الموبايل على إظهار الأيقونة الاحترافية
st.markdown(f"""
    <head>
        <link rel="apple-touch-icon" href="{LOGO_URL}">
        <link rel="icon" type="image/png" href="{LOGO_URL}">
        <link rel="shortcut icon" href="{LOGO_URL}">
        <meta name="apple-mobile-web-app-capable" content="yes">
    </head>
""", unsafe_allow_html=True)

# --- 2. ستايل CSS الملكي (حل مشكلة الألوان واختفاء النصوص) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [class*="css"], .stApp { 
        font-family: 'Cairo', sans-serif !important; 
        direction: rtl !important; text-align: right !important;
        background-color: #0f172a !important; 
    }

    /* إصلاح المربعات: خلفية بيضاء وكتابة سوداء */
    input, textarea, [data-baseweb="select"] {
        color: #000000 !important; 
        background-color: #ffffff !important; 
    }
    
    label { color: #facc15 !important; font-weight: bold !important; }

    .chat-bubble-user { 
        background: #075e54; color: white; padding: 12px; border-radius: 15px 15px 0 15px; 
        margin: 10px; float: right; clear: both; max-width: 85%;
    }
    .chat-bubble-bot { 
        background: #1e293b; color: white; padding: 12px; border-radius: 15px 15px 15px 0; 
        margin: 10px; float: left; clear: both; max-width: 85%; border: 1px solid #334155;
    }

    .header-box { background: linear-gradient(90deg, #1e3a8a, #312e81); padding: 25px; border-radius: 15px; border: 2px solid #facc15; text-align: center; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- 3. الهيدر واللوغو في واجهة الموقع ---
st.markdown(f"""<div class="header-box">
    <img src="{LOGO_URL}" width="100" style="margin-bottom:10px;">
    <h1 style='color: white; margin:0;'>🦅 مكتبة أيوب الذكية 🦅</h1>
    <p style='color: #facc15; font-size:18px;'>خبير الذكاء الاصطناعي والخدمات الإلكترونية في العراق</p>
</div>""", unsafe_allow_html=True)

# --- 4. نظام الدردشة المطور ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "هلا بيك عيني! أنا المساعد الذكي لمكتبة أيوب.. شمحتاج اليوم؟ 😊"}]

for msg in st.session_state.messages:
    div_class = "chat-bubble-bot" if msg["role"] == "bot" else "chat-bubble-user"
    st.markdown(f"<div class='{div_class}'>{msg['content']}</div>", unsafe_allow_html=True)

user_input = st.chat_input("اكتب سؤالك هنا...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    p = user_input.lower()
    
    if any(x in p for x in ["هلا", "هلو", "سلام"]):
        ans = "يا مية هلا بجيتك! نورت مكتبة أيوب.. تفضل شمحتاج؟"
    elif any(x in p for x in ["شلونك", "اخبارك"]):
        ans = "بخير ونعمة من الله، المهم أنت شلونك؟"
    elif any(x in p for x in ["ذكاء", "ai", "بوت"]):
        ans = "بالذكاء الاصطناعي نصمم بوتات، نحلل بيانات، ونطور شغلك.. اطلب وتدلل!"
    elif any(x in p for x in ["قرطاسية", "اقلام"]):
        ans = "عدنا أفخر أنواع القرطاسية وتجهيز الهدايا والطباعة الحرارية."
    else:
        ans = "أبشر عيني! بس وضحلي أكثر شمحتاج بخصوص التعيينات أو القرطاسية؟"

    st.session_state.messages.append({"role": "bot", "content": ans})
    st.rerun()

# --- 5. استمارة الطلب ---
st.divider()
with st.form("main_form"):
    st.markdown("### 📥 اطلب خدمتك الآن")
    name = st.text_input("الأسم الثلاثي")
    phone = st.text_input("رقم الواتساب")
    details = st.text_area("تفاصيل طلبك...")
    if st.form_submit_button("إرسال الطلب 🚀"):
        if name and phone:
            requests.post("https://formspree.io/f/xvzvdjzq", data={"Name": name, "Phone": phone, "Details": details})
            st.success("عاشت إيدك! طلبك وصل لأيوب.")
