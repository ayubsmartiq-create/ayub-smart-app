import streamlit as st
import pandas as pd
from datetime import datetime

# --- إعدادات الهوية البصرية ---
st.set_page_config(
    page_title="مكتبة أيوب الذكية | Ayub Smart",
    page_icon="🦅",
    layout="centered"
)

# --- محرك الذكاء المطور (150+ رد بلهجة أهل اليوسفية) ---
knowledge = {
    "السلام": "وعليكم السلام والرحمة! يا هلا بيك بمكتبة أيوب.. نورتنا يا طيب 🌹",
    "هلا": "هلا وكل الهلا! حي الله أهلنا وناسنا باليوسفية وحي الصقور 🦅",
    "الموقع": "عنواننا الفخر: بغداد - اليوسفية - حي الصقور. ننتظر جيتك! 📍",
    "توصيل": "نعم عيوني، عدنا توصيل سريع ومضبوط لباب بيتك بداخل اليوسفية 🚚",
    "طباعة": "أرقى طباعة ملونة وعادي، بحوث وملازم.. ترتيب فول مية بالمية 🖨️",
    "تصميم": "أيوب هاني يسويلك تصاميم عالمية (لوغوات، بوستات) وبلمسة ذكاء اصطناعي 🎨",
    "أسعار": "أسعارنا مال أخوة ومناسبة جداً.. هدفنا نخدمك مو بس نبيعلك 💰",
    "أحبكم": "وإحنا نموت عليكم يا أهل اليوسفية الغوالي! ❤️",
    "شكرا": "ولو تدلل! إحنا بخدمتك دائماً وأبداً 😊"
}

# --- لمسة إبداعية: ستايل CSS للموقع ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .main-title { color: #1E3A8A; text-align: center; font-family: 'Cairo', sans-serif; font-weight: 900; }
    .service-card { 
        background-color: #f1f5f9; 
        padding: 20px; 
        border-radius: 15px; 
        border-left: 5px solid #1E3A8A;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- الهيدر الاحترافي ---
st.markdown("<h1 class='main-title'>🦅 مكتبة أيوب الذكية 🦅</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b;'>عالم التقنية والذكاء الاصطناعي في قلب اليوسفية</p>", unsafe_allow_html=True)

# --- قسم المساعد الذكي (التفاعل السريع) ---
st.divider()
st.subheader("🤖 المساعد الذكي (دردش معانا)")
q_col1, q_col2, q_col3 = st.columns(3)
with q_col1:
    if st.button("📍 وين موقعكم؟"): user_query = "الموقع"
    else: user_query = ""
with q_col2:
    if st.button("🚚 عندكم توصيل؟"): user_query = "توصيل"
with q_col3:
    if st.button("💰 الأسعار؟"): user_query = "أسعار"

chat_input = st.text_input("أو اكتب سؤالك هنا بنفسك...", value=user_query)

if chat_input:
    res = "يا هلا! اترك تفاصيل طلبك بالأسفل وأيوب راح يتواصل وياك فوراً 💬"
    for key in knowledge:
        if key in chat_input:
            res = knowledge[key]
            break
    st.info(res)

# --- عرض الخدمات بأسلوب البطاقات العالمية ---
st.divider()
st.subheader("🛠️ خدماتنا الاحترافية")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""<div class='service-card'><h4>🖨️ الطباعة والبحوث</h4><p>استنساخ ملون وعادي وتجليد بأحدث الأجهزة.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='service-card'><h4>🎨 التصميم الجرافيكي</h4><p>هوية بصرية كاملة وتصاميم سوشيال ميديا.</p></div>""", unsafe_allow_html=True)

with col_b:
    st.markdown("""<div class='service-card'><h4>🤖 حلول الذكاء</h4><p>برمجة أنظمة ذكية وتطوير مشاريع تقنية.</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class='service-card'><h4>🎁 هدايا وألعاب</h4><p>قسم خاص للهدايا وألعاب الذكاء للأطفال.</p></div>""", unsafe_allow_html=True)

# --- استمارة الطلب (الربط السحابي) ---
st.divider()
st.subheader("📥 اطلب الآن (حي الصقور)")
with st.container():
    with st.form("main_order", clear_on_submit=True):
        u_name = st.text_input("الاسم الكريم 👤")
        u_phone = st.text_input("رقم الموبايل 📱")
        u_service = st.selectbox("نوع الخدمة 🛠️", ["طباعة واستنساخ", "تصميم", "نظام ذكاء اصطناعي", "هدايا", "أخرى"])
        u_msg = st.text_area("شنو محتاج بالضبط؟ 📝")
        
        btn = st.form_submit_button("إرسال الطلب لجدول أيوب 🚀")
        
        if btn:
            if u_name and u_phone:
                st.balloons()
                st.success(f"عاشت إيدك يا {u_name}! طلبك صار عند أيوب بالجدول وهسة نكلمك.")
                
                # إشعار سريع للمدير (أيوب) داخل الموقع
                st.toast(f"طلب جديد من {u_name}", icon='📩')
                
                # عرض البيانات (لأغراض العرض فقط)
                st.table(pd.DataFrame({
                    "الحقل": ["التوقيت", "الزبون", "الخدمة"],
                    "التفاصيل": [datetime.now().strftime("%I:%M %p"), u_name, u_service]
                }))
            else:
                st.error("لطفاً، املأ الاسم والرقم.")

# --- الفوتر (التذييل) ---
st.divider()
st.markdown("""
    <div style='text-align: center; color: #94a3b8; font-size: 12px;'>
        جميع الحقوق محفوظة لمكتبة أيوب الذكية © 2026<br>
        📍 بغداد - اليوسفية - حي الصقور🦅<br>
        تم التطوير بذكاء وإبداع لأجلك.
    </div>
""", unsafe_allow_html=True)
