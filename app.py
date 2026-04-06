import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="مكتبة أيوب الذكية",
    page_icon="🦅",
    layout="wide"
)

# 2. الثيم الملكي (الخلفية، الألوان، والجداول)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0f172a !important;
        color: white !important;
    }

    /* إصلاح المربعات والجداول */
    input, textarea, [data-baseweb="select"] {
        color: #000000 !important;
        background-color: #ffffff !important;
    }

    .header-box {
        background: linear-gradient(90deg, #1e3a8a, #312e81);
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #facc15;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* ستايل فقاعات الدردشة */
    .chat-bubble {
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        max-width: 80%;
    }
    .user-msg { background-color: #075e54; float: right; }
    .bot-msg { background-color: #1e293b; border: 1px solid #334155; float: left; }
    </style>
""", unsafe_allow_html=True)

# 3. واجهة الموقع
st.markdown("""
    <div class="header-box">
        <h1 style='color: white;'>🦅 مكتبة أيوب الذكية 🦅</h1>
        <p style='color: #facc15; font-size: 20px;'>خبير الذكاء الاصطناعي والخدمات الإلكترونية في العراق</p>
    </div>
""", unsafe_allow_html=True)

# 4. نظام الدردشة
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "هلا بيك عيني! أنا المساعد الذكي لمكتبة أيوب.. شمحتاج اليوم؟ 😊"}]

for msg in st.session_state.messages:
    style = "user-msg" if msg["role"] == "user" else "bot-msg"
    st.markdown(f"<div class='chat-bubble {style}'>{msg['content']}</div><div style='clear:both;'></div>", unsafe_allow_html=True)

user_input = st.chat_input("اكتب سؤالك هنا...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    # رد تلقائي بسيط
    st.session_state.messages.append({"role": "bot", "content": "تدلل عيني، أيوب هسة يشوف رسالتك ويجاوبك."})
    st.rerun()

# 5. جدول طلب الخدمة (اللي اختفى ورجعناه)
st.divider()
st.subheader("📥 استمارة طلب خدمة")
with st.form("order_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("الأسم الثلاثي")
    with col2:
        phone = st.text_input("رقم الموبايل")
    
    service = st.selectbox("نوع الخدمة", ["تقديم تعيينات", "فيزا سياحية", "قرطاسية وتصاميم", "استشارة ذكاء اصطناعي"])
    details
