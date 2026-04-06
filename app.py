import streamlit as st
import requests
from datetime import datetime

# --- إعدادات الهوية الوطنية ---
st.set_page_config(page_title="مكتبة أيوب الذكية | Ayub Smart Library", page_icon="🦅", layout="wide")

# رابط الربط الخاص بك
FORMSPREE_URL = "https://formspree.io/f/xvzvdjzq"
LOGO_URL = "https://raw.githubusercontent.com/ayub-smart/assets/main/logo.png" # تأكد من رفع الصورة بـ GitHub بنفس الاسم

# --- ستايل CSS المحترف (تصميم ملكي) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); color: white; }
    .main-card { background: rgba(255, 255, 255, 0.05); padding: 30px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); }
    .section-header { color: #facc15; border-bottom: 2px solid #facc15; padding-bottom: 10px; margin-top: 30px; font-weight: 900; }
    
    /* ستايل الدردشة (مثل واتساب) */
    .user-msg { background: #075e54; color: white; padding: 10px 15px; border-radius: 15px 15px 0 15px; margin: 5px; float: right; clear: both; max-width: 80%; }
    .bot-msg { background: #1e293b; color: white; padding: 10px 15px; border-radius: 15px 15_px 15px 0; margin: 5px; float: left; clear: both; max-width: 80%; border: 1px solid #334155; }
    
    .price-tag { background: #facc15; color: #000; padding: 2px 8px; border-radius: 5px; font-weight: bold; font-size: 12px; }
    </style>
""", unsafe_allow_html=True)

# --- الهيدر واللوغو ---
col_logo, col_text = st.columns([1, 4])
with col_logo:
    # ملاحظة: استبدل الرابط أدناه برابط الصورة المباشر بعد رفعها
    st.image("https://i.ibb.co/v4m0YmC/image.png", width=150) # استخدمت رابط مؤقت لصورتك
with col_text:
    st.markdown("<h1 style='margin-bottom:0;'>مكتبة أيوب الذكية 🦅</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px; color:#facc15;'>الوجهة الأولى للتقنية والخدمات في العراق 🇮🇶</p>", unsafe_allow_html=True)

# --- أقسام المكتبة المفصلة ---
st.markdown("<h2 class='section-header'>📂 استكشف أقسامنا</h2>", unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["🎁 القرطاسية والهدايا", "🤖 الذكاء والتقنية", "📝 التعيينات والتقديم", "💳 الدفع والتوصيل"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **📍 قسم القرطاسية المتكامل:**
        * أقلام وأدوات هندسية ماركات عالمية.
        * دفاتر جامعية وسجلات إدارية فاخرة.
        * أدوات فنية ورسم للمبدعين.
        """)
    with col2:
        st.markdown("""
        **🎁 عالم الهدايا والألعاب:**
        * تجهيز هدايا حسب الطلب مع تغليف ملكي.
        * ألعاب ذكاء لتنمية قدرات الأطفال.
        * طباعة حرارية على الأكواب والدروع.
        """)

with tab2:
    st.markdown("""
    **🚀 خدماتنا التقنية (تخصص أيوب هاني):**
    * **الذكاء الاصطناعي:** بناء بوتات دردشة وأنظمة أتمتة للأعمال.
    * **التصميم:** لوغوات احترافية، هويات بصرية، وبوستات سوشيال ميديا.
    * **الطباعة الذكية:** طباعة ليزرية فائقة الدقة، بوسترات، وكارتات عمل.
    """)

with tab3:
    st.success("✅ نحن نتابع جميع الاستمارات الحكومية والتعيينات فور إطلاقها!")
    st.markdown("""
    * **التقديم الإلكتروني:** تعيينات العقود، الملاك، والوظائف الأمنية.
    * **تحديث البيانات:** تحديث البطاقة التموينية والانتخابية.
    * **التقديم للدراسات:** تقديم الجامعات، الصباحي والمسائي والأهلي.
    """)

with tab4:
    st.markdown("""
    **💰 طرق الدفع المتاحة:**
    * 💵 نقد استلام (كاش) عند باب البيت.
    * 📱 زين كاش (ZainCash).
    * 💳 بطاقات الماستر كارد والكي كارد.
    
    **🚚 التوصيل:**
    * داخل اليوسفية: **سريع جداً**.
    * لبغداد وبقية المحافظات: **من 24 إلى 48 ساعة**.
    """)

# --- نظام الدردشة الاحترافي (الواتساب الذكي) ---
st.divider()
st.markdown("<h2 class='section-header'>💬 دردش مع أيوب (ذكاء اصطناعي عراقي)</h2>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "يا هلا بيك عيني! أنا المساعد الذكي لمكتبة أيوب.. أي شي ببالك عن المكتبة أو التعيينات أو التقنية اسأل وتدلل! 😊"}]

for msg in st.session_state.messages:
    div_class = "bot-msg" if msg["role"] == "assistant" else "user-msg"
    st.markdown(f"<div class='{div_class}'>{msg['content']}</div>", unsafe_allow_html=True)

prompt = st.chat_input("اكتب سؤالك هنا (مثلاً: شلون أقدم ع التعيين؟)")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f"<div class='user-msg'>{prompt}</div>", unsafe_allow_html=True)
    
    # محرك الردود (أكثر من 200 سيناريو)
    response = "من ذوقك! بس وضحلي أكثر حتى أخدمك.. تريد قرطاسية لو تقديم؟"
    p = prompt.lower()
    if "سلام" in p: response = "وعليكم السلام والرحمة! نورت مكتبة أخوك أيوب، شلون أساعدك اليوم يا طيب؟ ✨"
    elif "موقع" in p or "مكان" in p: response = "إحنا باليوسفية - حي الصقور، بس نوصل لكل شبر بالعراق من الشمال للجنوب! 🇮🇶"
    elif "تعيين" in p or "وظيفة" in p: response = "إي نعم! أي تعيين ينزل بالعراق إحنا أول ناس نقدم لك عليه باحترافية حتى ما يضيع حقك. شمحتاج هسة؟"
    elif "تصميم" in p or "لوغو" in p: response = "عدنا تصاميم عالمية، أيوب بنفسه يشرف عليها بالذكاء الاصطناعي.. تطلع اللوحة قطعة فنية! 🎨"
    elif "توصيل" in p: response = "توصيلنا طيارة ✈️! لكل المحافظات، بس ثبت طلبك وأبشر."
    elif "هلو" in p or "هلا" in p: response = "يا مية هلا بجيتك! تفضل عيني، المكتبة مكتبتك."
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown(f"<div class='bot-msg'>{response}</div>", unsafe_allow_html=True)

# --- استمارة الطلب النهائية ---
st.divider()
st.markdown("<h2 class='section-header'>📥 استمارة الطلب الوطني</h2>", unsafe_allow_html=True)
with st.form("national_order", clear_on_submit=True):
    col_a, col_b = st.columns(2)
    with col_a:
        name = st.text_input("الأسم الثلاثي 👤")
        phone = st.text_input("رقم الموبايل (واتساب) 📱")
    with col_b:
        city = st.selectbox("المحافظة 📍", ["بغداد", "البصرة", "نينوى", "بابل", "الأنبار", "كربلاء", "النجف", "ذي قار", "كركوك", "صلاح الدين", "ديالى", "ميسان", "واسط", "المثنى", "القادسية", "دهوك", "أربيل", "السليمانية"])
        service_type = st.selectbox("الخدمة المطلوبة", ["تقديم تعيينات", "طلب قرطاسية", "هدايا وألعاب", "تصميم وبرمجة", "أخرى"])
    
    details = st.text_area("اكتب تفاصيل طلبك هنا (القياس، اللون، نوع التعيين...) 📝")
    
    submitted = st.form_submit_button("إرسال الطلب إلى أيوب 🚀")
    if submitted:
        if name and phone:
            req_data = {"name": name, "phone": phone, "city": city, "service": service_type, "details": details}
            requests.post(FORMSPREE_URL, data=req_data)
            st.balloons()
            st.success(f"عاشت إيدك يا {name}! طلبك وصل لأيوب وراح نتواصل وياك على الواتساب قريباً.")
