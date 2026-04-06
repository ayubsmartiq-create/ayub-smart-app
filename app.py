import streamlit as st
import requests

# --- 1. رابط اللوغو المباشر (تأكد من الرابط) ---
LOGO_URL = "https://i.postimg.cc/85M6mGvP/Ayub-Logo.png"

# --- 2. إعدادات الصفحة الرسمية ---
st.set_page_config(
    page_title="مكتبة أيوب الذكية", 
    page_icon=LOGO_URL, 
    layout="wide"
)

# --- 3. كود إجبار الآيفون والأندرويد على إظهار الأيقونة الاحترافية ---
st.markdown(f"""
    <head>
        <link rel="apple-touch-icon" sizes="180x180" href="{LOGO_URL}">
        <link rel="apple-touch-icon" href="{LOGO_URL}">
        
        <link rel="icon" type="image/png" href="{LOGO_URL}">
        <link rel="shortcut icon" href="{LOGO_URL}">
        
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="مكتبة أيوب">
    </head>
""", unsafe_allow_html=True)

# --- 4. ستايل CSS الملكي (ألوان وخطوط) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [class*="css"], .stApp { 
        font-family: 'Cairo', sans-serif !important; 
        direction: rtl !important; 
        text-align: right !important;
        background-color: #0f172a !important; 
    }

    /* إصلاح ألوان المربعات: كتابة سوداء على خلفية بيضاء */
    input, textarea, [data-baseweb="select"] {
        color: #000000 !important; 
        background-color: #ffffff !important; 
    }
    
    label { color: #facc15 !important; font-weight: bold !important; }

    /* ستايل فقاعات الدردشة */
    .chat-bubble-user { 
        background: #075e54; color: white; padding: 12px; border-radius: 15px 15px 0 15px; 
        margin: 10px; float: right; clear: both; max-width: 85%;
    }
    .chat-bubble-bot { 
        background: #1e293b; color: white; padding: 12px; border-radius: 15px 15px 15px 0; 
        margin: 10px; float: left; clear: both; max-width: 85%; border: 1px solid #334155;
    }

    /* صندوق الهيدر (العنوان واللوغو) */
    .header-box { 
        background: linear-gradient(90deg, #1e3a8a, #312e81); 
        padding: 25px; border-radius: 15px; border: 2px solid #facc15; 
        text-align: center; margin-bottom: 20px; 
    }
    </style>
""", unsafe_allow_html=True)

# --- 5. الهيدر واللوغو في الواجهة ---
st.markdown(f"""<div class="header-box">
    <img src="{LOGO_URL}" width="110" style="margin-bottom:10px; border-radius: 10px;">
    <h1 style='color: white; margin:0;'>🦅 مكتبة أيوب الذكية 🦅</h1>
    <p style='color: #facc15; font-size:18px;'>خبير الذكاء الاصطناعي والخدمات الإلكترونية</p>
</div>""", unsafe_allow_html=True)

# --- 6. نظام الدردشة المطور ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "هلا بيك بمكتبة أيوب الذكية! شمحتاج اليوم عيني؟ 😊"}]

for msg in st.session_state.messages:
    div_class = "chat-bubble-bot" if msg["role"] == "bot" else "chat-bubble-user"
    st.markdown(f"<div class='{div_class}'>{msg['content']}</div>", unsafe_allow_html=True)

user_input = st.chat_input("اكتب سؤالك هنا...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    p = user_input.lower()
    
    # ردود ذكية بسيطة
    if any(x in p for x in ["هلا", "هلو", "سلام"]):
        ans = "يا مية هلا بجيتك! نورت مكتبة أيوب.. تفضل شمحتاج؟"
    elif any(x in p for x in ["تعيين", "تقديم", "استمارة"]):
        ans = "أبشر! عدنا قسم خاص للتقديم على التعيينات والفيزا وكل المعاملات الإلكترونية."
    elif any(x in p for x in ["ذكاء", "ai", "بوت"]):
        ans = "بالذكاء الاصطناعي نصمم لك بوتات خاصة ونطور شغلك.. اطلب وتدلل!"
    else:
        ans = "أبشر عيني! بس وضحلي طلبك بخصوص التعيينات أو القرطاسية حتى أساعدك."

    st.session_state.messages.append({"role": "bot", "content": ans})
    st.rerun()

# --- 7. استمارة طلب الخدمة ---
st.divider()
with st.form("main_order_form"):
    st.markdown("### 📥 اطلب خدمتك الآن")
    name = st.text_input("الأسم الثلاثي")
    phone = st.text_input("رقم الواتساب")
    details = st.text_area("تفاصيل طلبك (تعيين، قرطاسية، استشارة ذكاء اصطناعي...)")
    
    submit = st.form_submit_button("إرسال الطلب 🚀")
    if submit:
        if name and phone:
            # إرسال البيانات لبريدك (تأكد من ID الفورم الخاص بك)
            requests.post("https://formspree.io/f/xvzvdjzq", data={"Name": name, "Phone": phone, "Details": details})
            st.success(f"عاشت إيدك يا {name}! طلبك وصل لأيوب وهسة يجاوبك.")
        else:
            st.error("عيني املأ الأسم والرقم حتى نكدر نتواصل وياك.")
