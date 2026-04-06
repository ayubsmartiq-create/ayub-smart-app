import streamlit as st
import requests

# رابط جديد ومستقر للوجو (جربه الآن)
LOGO_URL = "https://raw.githubusercontent.com/ayubsmartiq-create/ayub-smart-app/main/Ayub-Logo.png"

st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon=LOGO_URL, layout="wide")

# كود إخفاء النصوص العلوية وإظهار الأيقونة
st.markdown(f"""
    <head>
        <link rel="apple-touch-icon" href="{LOGO_URL}">
        <link rel="icon" href="{LOGO_URL}">
        <style>
            /* إخفاء أي نصوص برمجية قد تظهر بالخطأ */
            header {{ visibility: hidden; }}
            .reportview-container .main {{ background-color: #0f172a; }}
        </style>
    </head>
""", unsafe_allow_html=True)

st.image(LOGO_URL, width=150)
st.title("🦅 مكتبة أيوب الذكية 🦅")
st.write("هلا بيك! أنا المساعد الذكي لمكتبة أيوب.. شمحتاج اليوم؟ 😊")

# نظام الدردشة البسيط
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("اكتب سؤالك هنا...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": "أبشر يا غالي، أيوب هسة يجاوبك!"})
    st.rerun()
