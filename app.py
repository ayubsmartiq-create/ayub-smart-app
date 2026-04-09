import streamlit as st
import pandas as pd
import os
import datetime
import random

# --- 1. التصميم الملكي (Global Gold Design) ---
st.set_page_config(page_title="مكتبة أيوب الذكية", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    .stApp { background-color: #000000; direction: rtl; }
    
    h1, h2, h3, h4, p, label, span, div {
        color: #FFD700 !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif;
    }

    /* صناديق الخدمات المتميزة */
    .service-card {
        background: linear-gradient(145deg, #0a0a0a, #1a1a1a);
        padding: 25px; border-radius: 20px; border: 1px solid #FFD700;
        text-align: right; transition: 0.3s; height: 260px;
        box-shadow: 0px 8px 25px rgba(255, 215, 0, 0.05);
    }
    .service-card:hover { transform: translateY(-10px); box-shadow: 0px 15px 40px rgba(255, 215, 0, 0.2); }

    /* مساعد أيوب الذكي (تصميم الصندوق الجديد) */
    .ai-assistant-box {
        background: rgba(255, 215, 0, 0.05);
        padding: 30px; border-radius: 25px;
        border: 2px dashed #FFD700;
        margin-bottom: 20px;
    }

    /* أوسمة الثقة والأمان */
    .trust-badge {
        background-color: #0a2a0a; color: #00ff00 !important;
        padding: 12px; border-radius: 12px; border: 1px solid #00ff00;
        text-align: center !important; font-size: 15px; margin-bottom: 12px;
        font-weight: bold;
    }

    /* زر الإرسال */
    .stButton>button {
        background: linear-gradient(90deg, #FFD700, #b8860b) !important;
        color: #000000 !important; font-weight: bold !important;
        font-size: 18px !important; width: 100% !important; border-radius: 15px !important;
        height: 55px; border: none !important;
    }

    /* إخفاء القائمة الجانبية تماماً لتجنب أي خربطة */
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. واجهة المحتوى الرئيسي ---
st.markdown('<h1 style="text-align:center; font-size: 60px; margin-bottom:0;">مكتبة أيوب الذكية</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size: 22px; opacity: 0.8;">إبداع عراقي.. حلول ذكية عالمية</p>', unsafe_allow_html=True)

# عرض الخدمات
st.write("")
c1, c2, c3, c4 = st.columns(4)
services = [
    ("الخدمات المكتبية", "طباعة فاخرة وتنسيق CV احترافي عالمي."),
    ("التحويل المالي", "إدارة زين كاش، ماستر كارد، وتعبئة رصيد."),
    ("الذكاء الاصطناعي", "بناء مواقع ذكية وتصاميم برمجية متطورة."),
    ("المونتاج الرقمي", "صناعة محتوى TikTok و Reels بجودة سينمائية.")
]
for i, (title, desc) in enumerate(services):
    with [c1, c2, c3, c4][i]:
        st.markdown(f'<div class="service-card"><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

st.write("---")

# --- 3. قسم الذكاء الاصطناعي والاستمارة (في قلب الصفحة) ---
col_ai, col_form = st.columns([1, 1.2], gap="large")

with col_ai:
    st.markdown('<div class="ai-assistant-box">', unsafe_allow_html=True)
    st.markdown('<h3>🤖 مساعد أيوب الذكي</h3>', unsafe_allow_html=True)
    st.write("أهلاً بك عيوني.. أنا هنا لمساعدتك. اسألني أي شيء عن الخدمات أو الأسعار!")
    
    ai_input = st.text_input("بماذا يمكنني مساعدتك؟", placeholder="اكتب هنا (مثلاً: شلون الأسعار؟)")
    if ai_input:
        if any(word in ai_input for word in ["شلون", "هلا", "مرحبا"]):
            st.info("هلا بيك! نورتنا. نحن نقدم أفضل الخدمات الرقمية في العراق.")
        elif any(word in ai_input for word in ["سعر", "بكم", "كلفة"]):
            st.info("أسعارنا تنافسية جداً وتناسب الجميع. سجل طلبك وسنتواصل معك فوراً.")
        elif any(word in ai_input for word in ["وقت", "متى"]):
            st.info("السرعة هي شعارنا؛ أغلب طلباتنا تنجز خلال ساعات قليلة.")
        else:
            st.info("تدلل، سؤالك مهم.. يمكنك أيضاً الضغط على زر الواتساب بعد الطلب للتحدث مع أيوب مباشرة.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # عناصر الأمان
    st.markdown('<div class="trust-badge">🔒 تشفير كامل لبياناتك</div>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">✅ ضمان الجودة واسترداد الأموال</div>', unsafe_allow_html=True)

with col_form:
    st.markdown('<h3>📝 سجل طلبك الآن</h3>', unsafe_allow_html=True)
    with st.form("main_order_form"):
        u_name = st.text_input("الأسم الكامل")
        u_phone = st.text_input("رقم الواتساب")
        u_srv = st.selectbox("نوع الخدمة", ["تصميم CV", "تحويل مالي", "برمجة موقع", "مونتاج فيديو", "أخرى"])
        u_det = st.text_area("تفاصيل الطلب")
        submit_btn = st.form_submit_button("إرسال الطلب 🚀")

if submit_btn:
    if u_name and u_phone:
        order_no = f"AY-{random.randint(1000, 9999)}"
        # حفظ في CSV
        df = pd.DataFrame({"التاريخ": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")], "الرقم": [order_no], "الاسم": [u_name], "الهاتف": [u_phone], "الخدمة": [u_srv], "الحالة": ["قيد المراجعة"]})
        df.to_csv("orders_database.csv", mode='a', header=not os.path.exists("orders_database.csv"), index=False, encoding='utf-8-sig')
        
        st.success(f"تم التسجيل! رقم الطلب: {order_no}")
        wa_url = f"https://wa.me/9647739778877?text=أهلاً أيوب، سجلت طلب رقم: {order_no}"
        st.markdown(f'<a href="{wa_url}" target="_blank"><div style="background-color:#25d366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">تأكيد عبر واتساب أيوب 🟢</div></a>', unsafe_allow_html=True)
        st.balloons()
    else: st.error("يرجى ملء كافة البيانات.")

# --- 4. تتبع الطلب والحقوق ---
st.write("---")
