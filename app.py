import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon="🦅", layout="wide")

# --- ستايل CSS الاحترافي (حل مشكلة اختفاء النصوص) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* ضبط الخط والألوان العامة */
    html, body, [class*="css"], .stApp { 
        font-family: 'Cairo', sans-serif !important; 
        direction: rtl !important; text-align: right !important;
        background-color: #0f172a !important; 
    }

    /* إصلاح لون النصوص في المربعات والإدخال */
    input, textarea, select, .stSelectbox, div[data-baseweb="select"] {
        color: #000000 !important; /* الكتابة داخل المربعات بالأسود الواضح */
        background-color: #ffffff !important; /* المربعات باللون الأبيض */
    }
    
    label { color: #facc15 !important; font-weight: bold !important; font-size: 18px !important; } /* عناوين المربعات بالذهبي */

    /* ستايل فقاعات الدردشة */
    .chat-bubble-user { 
        background: #075e54; color: white; padding: 12px; border-radius: 15px 15px 0 15px; 
        margin: 10px; float: right; clear: both; max-width: 85%;
    }
    .chat-bubble-bot { 
        background: #1e293b; color: white; padding: 12px; border-radius: 15px 15px 15px 0; 
        margin: 10px; float: left; clear: both; max-width: 85%; border: 1px solid #334155;
    }

    /* تنسيق الأقسام (Tabs) */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #1e3a8a; color: white !important; border-radius: 10px; padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] { background-color: #facc15 !important; color: #0f172a !important; }

    .header-box { background: linear-gradient(90deg, #1e3a8a, #312e81); padding: 25px; border-radius: 15px; border: 2px solid #facc15; text-align: center; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- الهيدر ---
st.markdown("""<div class="header-box">
    <h1 style='color: white; margin:0;'>🦅 مكتبة أيوب الذكية 🦅</h1>
    <p style='color: #facc15; font-size:20px; font-weight:bold;'>منصتكم الأولى للذكاء الاصطناعي والخدمات في كل العراق 🇮🇶</p>
</div>""", unsafe_allow_html=True)

# --- أقسام المكتبة والخدمات بالتفصيل ---
st.markdown("<h2 style='color:#facc15;'>📂 خدماتنا المتكاملة</h2>", unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["📚 القرطاسية", "🤖 الذكاء الاصطناعي", "🤝 مساعدة الناس", "💳 الدفع والتوصيل"])

with tab1:
    st.markdown("""
    * **الماركات:** نوفر أرقى الأقلام والسجلات (Rotring, Faber-Castell).
    * **تجهيز كامل:** حقائب، دفاتر جامعية، وأدوات هندسية.
    * **الرسم الفني:** ألوان، لوحات، وفرش للمحترفين.
    * **الهدايا:** طباعة حرارية (أكواب، دروع) وتغليف فاخر.
    """)

with tab2:
    st.markdown("""
    * **برمجة البوتات:** نصمم لك مساعد ذكي لعملك مثل هذا البوت.
    * **تحليل البيانات:** نحول بياناتك لتقارير ذكية تساعدك بالقرار.
    * **تصميم AI:** توليد صور وشعارات خرافية بالذكاء الاصطناعي.
    * **الأتمتة:** نبرمج لك مهامك المتكررة لتخلص بضغطة زر.
    """)

with tab3:
    st.markdown("""
    * **تعيينات العراق:** نقدملك على (العقود، الملاك، الوظائف الأمنية) بدقة 100%.
    * **الطلاب:** تقديم مركزي، مسائي، وأهلي، وتدقيق استمارات.
    * **المعاملات:** تحديث البطاقة التموينية، الانتخابية، والتقديم ع القروض.
    * **الاستشارات:** أي استشارة تقنية أو إلكترونية إحنا بخدمتكم.
    """)

with tab4:
    st.info("🚚 نوصل لكل محافظات العراق (من الشمال للجنوب) بأسعار تنافسية.")
    st.markdown("""
    * **كاش عند الاستلام:** ادفع بعد ما تفحص غراضك.
    * **زين كاش / ماستر كارد:** متوفر الدفع الإلكتروني بكل سهولة.
    """)

# --- محرك الدردشة (عقل أيوب الذكي) ---
st.divider()
st.markdown("<h2 style='color:#facc15;'>💬 مساعد أيوب الذكي (واتساب)</h2>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "يا هلا بيك عيني! أنا المساعد الذكي لمكتبة أيوب.. اسألني عن أي خدمة وأبشر! 😊"}]

for msg in st.session_state.messages:
    div_class = "chat-bubble-bot" if msg["role"] == "bot" else "chat-bubble-user"
    st.markdown(f"<div class='{div_class}'>{msg['content']}</div>", unsafe_allow_html=True)

user_input = st.chat_input("اكتب سؤالك هنا...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    p = user_input.lower()
    
    # محرك الردود
    if any(x in p for x in ["هلا", "هلو", "سلام", "مرحبا"]):
        ans = "يا مية هلا بجيتك! نورت مكتبة أيوب.. شمحتاج عيني؟"
    elif any(x in p for x in ["شلونك", "اخبارك"]):
        ans = "بخير ونعمة من الله، المهم أنت شلونك؟ شمحتاج نقدملك؟"
    elif any(x in p for x in ["قرطاسية", "اقلام", "تجهيز"]):
        ans = "عدنا قرطاسية ماركات وتجهيز هدايا وطباعة. تقدر تشوف قسم القرطاسية فوق للتفاصيل."
    elif any(x in p for x in ["ذكاء", "ai", "بوت"]):
        ans = "بالذكاء الاصطناعي نصمم بوتات، نحلل بيانات، ونسوي أتمتة لأعمالك.. أنت بس اطلب!"
    elif any(x in p for x in ["تعيين", "تقديم", "وظيفة"]):
        ans = "أي تعيين ينزل بالعراق نقدملك عليه باحترافية. املأ الاستمارة تحت وإحنا نخابرك."
    else:
        ans = "تدلل عيني! بس وضحلي أكثر شمحتاج بخصوص (القرطاسية، الذكاء، أو التعيينات)؟"

    st.session_state.messages.append({"role": "bot", "content": ans})
    st.rerun()

# --- استمارة الطلب (تم إصلاح الألوان) ---
st.divider()
st.markdown("<h2 style='color:#facc15;'>📥 استمارة الطلب الوطني</h2>", unsafe_allow_html=True)
with st.form("national_order"):
    f_name = st.text_input("الأسم الكامل (يظهر بالأسود داخل المربع)")
    f_phone = st.text_input("رقم الموبايل")
    f_service = st.selectbox("نوع الخدمة", ["تعيينات", "قرطاسية", "ذكاء اصطناعي", "أخرى"])
    f_details = st.text_area("تفاصيل طلبك...")
    
    if st.form_submit_button("إرسال الطلب الآن 🚀"):
        if f_name and f_phone:
            requests.post("https://formspree.io/f/xvzvdjzq", data={"Name": f_name, "Phone": f_phone, "Service": f_service, "Details": f_details})
            st.balloons()
            st.success("عاشت إيدك! طلبك صار عند أيوب وهسة راح يتواصل وياك.")
