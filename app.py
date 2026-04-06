import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon="🦅", layout="wide")

# 2. الثيم الملكي (تنظيف الواجهة وإرجاع الألوان)
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
    /* تعديل ألوان مربعات الكتابة */
    input, textarea, [data-baseweb="select"] {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    .header-box {
        background: linear-gradient(90deg, #1e3a8a, #312e81);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #facc15;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر (العنوان)
st.markdown("""
    <div class="header-box">
        <h1 style='color: white; margin:0;'>🦅 مكتبة أيوب الذكية 🦅</h1>
        <p style='color: #facc15; font-size:18px;'>خبير الذكاء الاصطناعي والخدمات الإلكترونية</p>
    </div>
""", unsafe_allow_html=True)

# 4. نظام الدردشة (Chat)
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "هلا بيك! أنا مساعد أيوب الذكي، شلون أكدر أخدمك؟"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("اكتب سؤالك هنا...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": "أبشر عيني، أيوب هسة يجاوبك."})
    st.rerun()

# 5. جدول الطلبات (الذي عاد من جديد)
st.divider()
st.subheader("📥 استمارة الطلب السريع")
with st.form("main_form"):
    name = st.text_input("الأسم الثلاثي")
    phone = st.text_input("رقم الواتساب")
    service = st.selectbox("نوع الخدمة", ["تقديم تعيينات", "فيزا سياحية", "قرطاسية وتصاميم", "بوتات ذكاء اصطناعي"])
    details = st.text_area("تفاصيل إضافية")
    
    if st.form_submit_button("إرسال الطلب 🚀"):
        if name and phone:
            # إرسال الطلب لإيميلك عبر Formspree
            requests.post("https://formspree.io/f/xvzvdjzq", data={"Name": name, "Phone": phone, "Service": service, "Details": details})
            st.success("عاشت إيدك! طلبك وصل لأيوب.")
        else:
            st.error("عيني املأ الأسم والرقم.")
