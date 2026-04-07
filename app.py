import streamlit as st
import requests

# 1. الهوية البصرية للمكتبة
LOGO_URL = "https://raw.githubusercontent.com/ayubsmartiq-create/ayub-smart-app/main/Ayub-Logo.png"

st.set_page_config(
    page_title="مكتبة أيوب الذكية",
    page_icon="🦅",
    layout="wide"
)

# 2. تصميم CSS يركز على الفخامة والوضوح
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [class*="css"], .stApp {{
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0f172a !important;
    }}

    .header-box {{
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #facc15;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }}

    .service-card {{
        background: #1e293b;
        padding: 25px;
        border-radius: 20px;
        border-right: 6px solid #facc15;
        margin-bottom: 20px;
    }}

    /* تحسين شكل المدخلات */
    .stTextInput input, .stTextArea textarea {{
        background-color: white !important;
        color: black !important;
        border-radius: 12px !important;
        font-size: 16px !important;
    }}

    .stButton button {{
        background: #facc15 !important;
        color: #1e3a8a !important;
        font-weight: 900 !important;
        border-radius: 15px !important;
        transition: 0.3s;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر التعريفي للمكتبة
st.markdown(f"""
    <div class="header-box">
        <img src="{LOGO_URL}" width="140">
        <h1 style='color: white; margin-top: 15px;'>🦅 مكتبة أيوب الذكية 🦅</h1>
        <p style='color: #facc15; font-size: 20px;'>إنجاز المعاملات الإلكترونية والحلول الذكية بأعلى دقة</p>
    </div>
""", unsafe_allow_html=True)

# 4. محتوى المكتبة (نصوص احترافية)
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("""
    <div class="service-card">
        <h3 style='color: #facc15;'>📌 لماذا تختار مكتبتنا؟</h3>
        <p>✅ <b>السرعة:</b> ننجز معاملات التقديم والفيزا بوقت قياسي.</p>
        <p>✅ <b>الخصوصية:</b> بياناتك ومعلوماتك في أمان تام معنا.</p>
        <p>✅ <b>الذكاء:</b> نستخدم أحدث أدوات الـ AI لتوفير أفضل الاستشارات.</p>
        <hr style='border-color: #334155;'>
        <p style='font-size: 14px; color: #cbd5e1;'>📍 الموقع: بغداد - اليوسفية <br> 📞 متواجدون لخدمتكم على مدار الساعة</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🤖 اسأل مساعد أيوب")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "مرحباً بك في مكتبة أيوب الذكية! كيف يمكنني مساعدتك في معاملاتك اليوم؟"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("اكتب استفسارك هنا...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": "تم استلام رسالتك، سيقوم أيوب بالرد عليك فوراً."})
        st.rerun()

# 5. استمارة طلب الخدمة
st.markdown("<h2 style='text-align: center; color: #facc15;'>📝 استمارة الطلب الإلكتروني</h2>", unsafe_allow_html=True)

with st.form("ayub_library_form"):
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("الأسم الكامل للمتقدم")
        phone = st.text_input("رقم الهاتف (واتساب)")
    with c2:
        service = st.selectbox("نوع المعاملة", 
                               ["التقديم على التعيينات", "فيزا سياحية / دراسية", "ترجمة وتصاميم", "استشارة تقنية / AI"])
        urgent = st.radio("درجة المستعجل", ["طبيعي", "مستعجل جداً"], horizontal=True)
    
    details = st.text_area("تفاصيل الطلب أو الملاحظات")
    
    submitted = st.form_submit_button("إرسال الطلب للمراجعة 🚀")
    if submitted:
        if name and phone:
            requests.post("https://formspree.io/f/xvzvdjzq", 
                          data={"الاسم": name, "الهاتف": phone, "الخدمة": service, "الأهمية": urgent, "التفاصيل": details})
            st.success(f"شكراً لك يا {name}. تم إرسال طلبك لمكتبة أيوب بنجاح!")
        else:
            st.error("يرجى إدخال الاسم والرقم لضمان التواصل.")

st.markdown("<p style='text-align: center; color: #64748b;'>نحن لسنا مجرد مكتبة، نحن شريكك التقني الأول</p>", unsafe_allow_html=True)
