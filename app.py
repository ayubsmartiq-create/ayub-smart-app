import streamlit as st
import pandas as pd
import os
import datetime
import random

# --- 1. إعدادات الصفحة والتصميم الملكي (مصحح للأخطاء) ---
st.set_page_config(page_title="مكتبة أيوب الذكية", layout="wide")

st.markdown("""
    <style>
    /* تصحيح اتجاه الصفحة بالكامل */
    .main, .stApp { direction: rtl; background-color: #000000; }
    
    /* منع تقطيع الكلام في القائمة الجانبية */
    section[data-testid="stSidebar"] { width: 300px !important; direction: rtl; }
    
    /* توحيد اللون الذهبي لكل النصوص */
    h1, h2, h3, h4, p, label, span, div { 
        color: #FFD700 !important; 
        text-align: right !important; 
        font-family: 'Cairo', sans-serif;
        white-space: normal !important; /* يمنع ظهور الكلام بشكل عمودي */
    }

    /* صناديق الخدمات العالمية */
    .service-card {
        background: linear-gradient(145deg, #0a0a0a, #1a1a1a); padding: 25px;
        border-radius: 20px; border: 1px solid #FFD700; text-align: right;
        margin-bottom: 20px; box-shadow: 0px 5px 15px rgba(255, 215, 0, 0.1);
    }

    /* أزرار الأمان */
    .trust-badge {
        background-color: #0a2a0a; color: #00ff00 !important;
        padding: 10px; border-radius: 10px; border: 1px solid #00ff00;
        text-align: center !important; font-size: 14px; margin-bottom: 10px;
    }

    /* زر الإرسال الملكي */
    .stButton>button {
        background: linear-gradient(90deg, #FFD700, #b8860b) !important;
        color: #000000 !important; font-weight: bold !important; 
        width: 100% !important; border-radius: 15px !important; height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. المساعد الذكي (في الجانب بطريقة مرتبة) ---
with st.sidebar:
    st.markdown('<h2 style="text-align:center;">🤖 مساعد أيوب</h2>', unsafe_allow_html=True)
    st.write("أهلاً بيك عيوني.. اسألني أي شي ببالك عن خدماتنا وباللهجة اللي تعجبك!")
    chat_input = st.text_input("اكتب سؤالك هنا...")
    if chat_input:
        if "شلون" in chat_input or "هلا" in chat_input:
            st.info("هلا بيك! نورت مكتبة أيوب الذكية.")
        elif "سعر" in chat_input or "بكم" in chat_input:
            st.info("أسعارنا مناسبة جداً، قدم طلب وراح نتواصل وياك وما نختلف.")
        else:
            st.info("تدلل، راسل أيوب واتساب وراح يجاوبك فوراً.")

# --- 3. محتوى الموقع الرئيسي ---
st.markdown('<h1 style="text-align:center; font-size: 50px;">مكتبة أيوب الذكية</h1>', unsafe_allow_html=True)
st.write("")

# صناديق الخدمات
c1, c2, c3, c4 = st.columns(4)
servs = [
    ("الخدمات المكتبية", "طباعة و CV احترافي"),
    ("التحويل المالي", "زين كاش وماستر كارد"),
    ("الذكاء الاصطناعي", "مواقع وشعارات ذكية"),
    ("المونتاج والإبداع", "فيديوهات تيك توك")
]
for i, (t, d) in enumerate(servs):
    with [c1, c2, c3, c4][i]:
        st.markdown(f'<div class="service-card"><h3>{t}</h3><p>{d}</p></div>', unsafe_allow_html=True)

# --- 4. الاستمارة والأمان ---
st.write("---")
col_f, col_t = st.columns([2, 1])

with col_f:
    st.markdown('<h3>📝 اطلب خدمتك</h3>', unsafe_allow_html=True)
    with st.form("main_form"):
        name = st.text_input("الأسم الكريم")
        phone = st.text_input("رقم الواتساب")
        srv = st.selectbox("نوع الخدمة", ["عمل CV", "تحويل مالي", "تصميم شعار", "موقع إلكتروني", "أخرى"])
        note = st.text_area("تفاصيل الطلب")
        btn = st.form_submit_button("إرسال الطلب الآن 🚀")

with col_t:
    st.markdown('<br><br>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">🔒 اتصال مشفر وآمن 100%</div>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">✅ ضمان جودة واسترداد مبلغ</div>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">📞 دعم فني متواصل 24/7</div>', unsafe_allow_html=True)

if btn:
    if name and phone:
        oid = f"AY-{random.randint(1000, 9999)}"
        # حفظ البيانات مع معالجة الأخطاء (on_bad_lines)
        df = pd.DataFrame({"التاريخ": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")], "الرقم": [oid], "الاسم": [name], "الهاتف": [phone], "الخدمة": [srv], "الحالة": ["قيد المراجعة"]})
        df.to_csv("orders_database.csv", mode='a', header=not os.path.exists("orders_database.csv"), index=False, encoding='utf-8-sig')
        
        st.success(f"تم التسجيل! رقم طلبك: {oid}")
        st.markdown(f'''<a href="https://wa.me/9647739778877?text=طلب جديد: {oid}" target="_blank"><div style="background-color:#25d366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">تأكيد عبر واتساب أيوب 🟢</div></a>''', unsafe_allow_html=True)
    else:
        st.error("املأ البيانات يرحم والديك")

# --- 5. التتبع والحقوق ---
st.write("---")
with st.expander("🔍 تتبع حالة طلبك"):
    sid = st.text_input("رقم الطلب (AY-XXXX)")
    if sid and os.path.exists("orders_database.csv"):
        try:
            data = pd.read_csv("orders_database.csv", on_bad_lines='skip')
            res = data[data['الرقم'].astype(str).str.contains(sid)]
            if not res.empty:
                st.info(f"حالة طلبك: {res.iloc[-1]['الحالة']}")
        except: st.warning("اكتب رقم الطلب بشكل صحيح")

st.markdown(f'<div style="text-align:center; color:#555; font-size:12px; margin-top:50px;">جميع الحقوق محفوظة © {datetime.datetime.now().year} - مكتبة أيوب الذكية</div>', unsafe_allow_html=True)
