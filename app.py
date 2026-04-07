import streamlit as st
import requests

# 1. إعدادات الهوية
LOGO_URL = "https://raw.githubusercontent.com/ayubsmartiq-create/ayub-smart-app/main/Ayub-Logo.png"
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon=LOGO_URL, layout="wide")

# 2. تصميم CSS (إضافة ستايل التتبع)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"], .stApp {{
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; text-align: right !important;
        background-color: #0f172a !important; color: white !important;
    }}
    .status-box {{
        background-color: #1e293b; padding: 20px; border-radius: 15px;
        border: 1px solid #facc15; text-align: center; margin-top: 10px;
    }}
    .header-box {{
        background: linear-gradient(135deg, #1e40af, #1e3a8a);
        padding: 30px; border-radius: 20px; border-bottom: 5px solid #facc15;
        text-align: center; margin-bottom: 25px;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر
st.markdown(f'<div class="header-box"><h1>🦅 مكتبة أيوب الذكية 🦅</h1><p>نظام الخدمات الإلكترونية المطور</p></div>', unsafe_allow_html=True)

# 4. التبويبات (Tabs) - لتنظيم الموقع
tab1, tab2 = st.tabs(["📑 طلب خدمة جديدة", "🔍 تتبع حالة طلبك"])

with tab1:
    st.subheader("📝 استمارة التقديم")
    with st.form("main_form"):
        name = st.text_input("الأسم الثلاثي")
        phone = st.text_input("رقم الهاتف")
        service = st.selectbox("نوع الخدمة", ["تقديم تعيينات", "ذكاء اصطناعي", "مونتاج", "قرطاسية"])
        details = st.text_area("التفاصيل")
        submit = st.form_submit_button("إرسال الطلب 🚀")
        if submit:
            if name and phone:
                requests.post("https://formspree.io/f/xvzvdjzq", data={"الاسم": name, "الهاتف": phone, "الخدمة": service, "التفاصيل": details})
                st.success("تم الإرسال! سيتم تزويدك برقم الطلب عبر الواتساب.")
            else:
                st.warning("يرجى ملء البيانات.")

with tab2:
    st.subheader("🔎 استعلم عن معاملتك")
    track_phone = st.text_input("أدخل رقم الموبايل المسجل به:")
    if st.button("فحص الحالة"):
        if track_phone:
            # هنا مستقبلاً نربطها بجدول بيانات، حالياً سنضع رسالة ترحيبية ذكية
            st.markdown(f"""
                <div class="status-box">
                    <h4 style="color: #facc15;">حالة الطلب للرقم: {track_phone}</h4>
                    <p>🟡 قيد المراجعة والتدقيق</p>
                    <small>سيتم تحديث الحالة فور إنجاز المعاملة من قبل أيوب</small>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("يرجى إدخال الرقم.")

# 5. المساعد الذكي (أسفل الصفحة)
st.divider()
with st.expander("🤖 اسأل مساعد أيوب (AI)"):
    if "msgs" not in st.session_state: st.session_state.msgs = []
    for m in st.session_state.msgs: st.chat_message(m["role"]).write(m["content"])
    prompt = st.chat_input("كيف أخدمك؟")
    if prompt:
        st.session_state.msgs.append({"role": "user", "content": prompt})
        st.session_state.msgs.append({"role": "assistant", "content": "أهلاً بك، أيوب سيقوم بالرد عليك بخصوص هذا الاستفسار قريباً."})
        st.rerun()
# أضف هذا الكود في نهاية ملف app.py المرة الجاية

st.markdown(f"""
    <a href="https://wa.me/9647739778877" class="whatsapp-btn" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="50">
    </a>
    <style>
    .whatsapp-btn {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        filter: drop-shadow(2px 4px 6px black);
    }}
    </style>
""", unsafe_allow_html=True)
# أضف هذا داخل استمارة التقديم (Form)
uploaded_file = st.file_uploader("📎 ارفع المستمسكات أو الصور المطلوبة هنا (اختياري)", type=['png', 'jpg', 'pdf'])

# أضف هذا القسم في أسفل الصفحة للتواصل السريع
st.markdown("""
    <div style="text-align: center; padding: 20px; background: #1e293b; border-radius: 15px; margin-top: 30px;">
        <h3 style="color: #facc15;">📞 تواصل معنا مباشرة</h3>
        <p>للاستفسارات العاجلة، يمكنك مراسلتنا عبر:</p>
        <a href="https://wa.me/9647700000000" style="text-decoration: none; color: #25d366; font-weight: bold; font-size: 20px;">واتساب المكتبة ✅</a>
        <br><br>
        <p style="font-size: 12px; color: gray;">الموقع: بغداد - اليوسفية - مكتبة أيوب الذكية</p>
    </div>
""", unsafe_allow_html=True)
