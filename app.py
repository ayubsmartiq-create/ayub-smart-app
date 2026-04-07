import streamlit as st
import requests

# 1. إعدادات الهوية البصرية (اللوغو والأيقونة)
LOGO_URL = "https://raw.githubusercontent.com/ayubsmartiq-create/ayub-smart-app/main/Ayub-Logo.png"

st.set_page_config(
    page_title="مكتبة أيوب الذكية",
    page_icon=LOGO_URL,
    layout="wide"
)

# 2. تصميم CSS الاحترافي (الثيم الملكي)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [class*="css"], .stApp {{
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0f172a !important;
        color: white !important;
    }}

    /* شريط الأخبار المتحرك */
    .ticker-wrap {{
        width: 100%; overflow: hidden; background: #1e3a8a; 
        padding: 10px 0; border-bottom: 2px solid #facc15;
    }}
    .ticker {{
        display: inline-block; white-space: nowrap;
        animation: ticker 30s linear infinite;
    }}
    @keyframes ticker {{
        0% {{ transform: translateX(100%); }}
        100% {{ transform: translateX(-100%); }}
    }}
    .ticker-item {{ display: inline-block; padding: 0 50px; color: #facc15; font-weight: bold; }}

    .header-box {{
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
        padding: 40px; border-radius: 25px; border: 2px solid #facc15;
        text-align: center; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}

    .service-card {{
        background: #1e293b; padding: 20px; border-radius: 15px;
        border-right: 5px solid #facc15; margin-bottom: 20px;
    }}

    .payment-icon {{
        background: white; color: #1e3a8a; padding: 5px 15px;
        border-radius: 8px; font-weight: bold; margin: 5px; display: inline-block;
    }}

    /* تحسين شكل الاستمارة */
    .stTextInput input, .stTextArea textarea, .stSelectbox div {{
        background-color: white !important; color: black !important; border-radius: 10px !important;
    }}
    
    .stButton button {{
        background: linear-gradient(90deg, #facc15, #eab308) !important;
        color: #1e3a8a !important; font-weight: 900 !important;
        border-radius: 12px !important; width: 100%; height: 3.5em;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. شريط النبض الإخباري (آخر التحديثات)
st.markdown("""
    <div class="ticker-wrap">
        <div class="ticker">
            <span class="ticker-item">🔥 إطلاق استمارة تعيينات العقود الجديدة - بادر بالتقديم الآن</span>
            <span class="ticker-item">💡 تم تفعيل قسم استشارات الذكاء الاصطناعي</span>
            <span class="ticker-item">📢 مكتبة أيوب تضمن لكم سرعة الإنجاز ودقة البيانات</span>
            <span class="ticker-item">🛡️ بياناتكم في أمان تام بفضل بروتوكول الحماية الجديد</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. الهيدر الرئيسي
st.markdown(f"""
    <div class="header-box">
        <img src="{LOGO_URL}" width="140" style="filter: drop-shadow(0 0 10px #facc15);">
        <h1 style='color: white; margin-top: 15px;'>🦅 مكتبة أيوب الذكية 🦅</h1>
        <p style='color: #facc15; font-size: 20px;'>نصمم مستقبلك الرقمي بأحدث حلول الذكاء الاصطناعي</p>
    </div>
""", unsafe_allow_html=True)

# 5. عرض الأقسام والدردشة
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("""
    <div class="service-card">
        <h3 style='color: #facc15;'>⚙️ أقسامنا الاحترافية</h3>
        <p><b>1️⃣ بوابة التقديم الإلكتروني:</b> استمارات، عقود، وقروض بدقة 100%.</p>
        <p><b>2️⃣ مختبر الذكاء الاصطناعي:</b> بناء بوتات وحلول برمجية ذكية.</p>
        <p><b>3️⃣ المونتاج والتصميم:</b> خدمات CapCut وتصاميم الجرافيك الاحترافية.</p>
        <p><b>4️⃣ المتجر الرقمي:</b> قرطاسية ومستلزمات تقنية مع التوصيل.</p>
    </div>
    <div class="service-card">
        <h3 style='color: #facc15;'>💳 طرق الدفع المتاحة</h3>
        <span class="payment-icon">زين كاش</span>
        <span class="payment-icon">آسيا حوالة</span>
        <span class="payment-icon">ماستر كارد</span>
        <span class="payment-icon">رصيد</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🤖 مساعد أيوب الذكي")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "هلا بيك بمكتبة أيوب! أنا هنا حتى أوجهك للقسم الصحيح. شنو معاملتك اليوم؟"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("اكتب استفسارك هنا...")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": "أبشر عيني، استلمت استفسارك وأيوب راح يتابع وياك."})
        st.rerun()

# 6. استمارة الطلب المتكاملة (ترسل للإيميل)
st.divider()
st.markdown("<h2 style='text-align: center; color: #facc15;'>📝 استمارة الطلب السريع</h2>", unsafe_allow_html=True)

with st.form("main_order_form"):
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("الأسم الثلاثي")
        phone = st.text_input("رقم الهاتف (واتساب)")
    with c2:
        service_type = st.selectbox("اختر القسم", ["التقديم الإلكتروني", "حلول ذكاء اصطناعي", "تصميم ومونتاج", "طلب قرطاسية"])
        priority = st.select_slider("درجة الأولوية", options=["طبيعي", "مستعجل", "مستعجل جداً (VIP)"])
    
    details = st.text_area("تفاصيل الطلب (اكتب ملاحظاتك هنا)")
    
    submit_btn = st.form_submit_button("إرسال الطلب إلى مكتبة أيوب 🚀")

    if submit_btn:
        if name and phone:
            # إرسال البيانات إلى Formspree (الإيميل اللي سجلناه سابقاً)
            try:
                post_data = {
                    "الاسم": name,
                    "الهاتف": phone,
                    "القسم": service_type,
                    "الأولوية": priority,
                    "التفاصيل": details
                }
                requests.post("https://formspree.io/f/xvzvdjzq", data=post_data)
                st.success(f"عاشت إيدك يا {name}! طلبك وصل بنجاح وسيتم التواصل معك.")
            except:
                st.error("عذراً، حدث خطأ في الإرسال. جرب مرة ثانية.")
        else:
            st.warning("يرجى ملء الاسم ورقم الهاتف لضمان تواصلنا معك.")

# 7. التذييل (Footer)
st.markdown("""
    <hr style='border-color: #334155;'>
    <p style='text-align: center; color: #64748b; font-size: 14px;'>
        🛡️ جميع البيانات مشفرة وتُحذف تلقائياً فور إنجاز المعاملة لضمان خصوصيتكم.<br>
        © 2026 مكتبة أيوب الذكية - اليوسفية، بغداد.
    </p>
""", unsafe_allow_html=True)
