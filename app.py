import streamlit as st
import pandas as pd
import os
import datetime
import random

# --- 1. الإعدادات الملكية (Global Styles) ---
st.set_page_config(page_title="مكتبة أيوب الذكية", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    .stApp { background-color: #000000; direction: rtl; }
    
    /* منع تقطيع الكلام في القائمة الجانبية وتوسيعها */
    [data-testid="stSidebar"] {
        width: 380px !important;
        background-color: #050505 !important;
        direction: rtl;
    }
    
    h1, h2, h3, h4, p, label, span, div {
        color: #FFD700 !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif;
        white-space: normal !important; /* لضمان عدم ظهور النص بشكل عمودي */
    }

    /* صناديق الخدمات المتميزة */
    .service-card {
        background: linear-gradient(145deg, #0a0a0a, #1a1a1a);
        padding: 20px; border-radius: 20px; border: 1px solid #FFD700;
        text-align: right; transition: 0.3s; height: 250px;
        box-shadow: 0px 8px 25px rgba(255, 215, 0, 0.05);
    }
    .service-card:hover { transform: translateY(-5px); box-shadow: 0px 12px 35px rgba(255, 215, 0, 0.15); }

    /* أوسمة الثقة والأمان للزبون */
    .trust-badge {
        background-color: #0a2a0a; color: #00ff00 !important;
        padding: 12px; border-radius: 12px; border: 1px solid #00ff00;
        text-align: center !important; font-size: 15px; margin-bottom: 12px;
        font-weight: bold;
    }

    /* أزرار العمليات */
    .stButton>button {
        background: linear-gradient(90deg, #FFD700, #b8860b) !important;
        color: #000000 !important; font-weight: bold !important;
        font-size: 18px !important; width: 100% !important; border-radius: 15px !important;
        height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. مساعد أيوب الذكي ( sidebar منسق بدون خربطة) ---
with st.sidebar:
    st.markdown('<h2 style="text-align:center;">🤖 مساعد أيوب الذكي</h2>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">متصل الآن وجاهز لخدمتكم ✅</div>', unsafe_allow_html=True)
    
    st.write("أهلاً بك عيوني.. أنا هنا لمساعدتك في الحصول على أفضل خدمة رقمية في العراق. اسألني عن أي شيء!")
    
    chat_input = st.text_input("اكتب استفسارك هنا...")
    if chat_input:
        if any(word in chat_input for word in ["شلون", "هلا", "مرحبا"]):
            st.info("هلا بيك عيوني! نورت مكتبة أيوب الذكية، المنصة الأولى للحلول الرقمية.")
        elif any(word in chat_input for word in ["سعر", "بكم", "كلفة"]):
            st.info("أسعارنا هي الأفضل! اطلب الخدمة الآن وسنتصل بك لتأكيد التفاصيل.")
        elif any(word in chat_input for word in ["وقت", "متى"]):
            st.info("نحن نقدر وقتك؛ أغلب خدماتنا تنفذ خلال ساعات قليلة جداً.")
        else:
            st.info("تدلل، سؤالك محل اهتمامنا. يمكنك أيضاً التواصل مع أيوب مباشرة عبر الواتساب.")

# --- 3. واجهة المحتوى الرئيسي ---
st.markdown('<h1 style="text-align:center; font-size: 50px;">مكتبة أيوب الذكية</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size: 20px; opacity: 0.9;">إبداع بلا حدود.. ذكاء بلا قيود</p>', unsafe_allow_html=True)

# عرض الخدمات في أعمدة
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

# --- 4. استمارة الطلب وعناصر الأمان ---
st.write("---")
f_col, t_col = st.columns([2, 1])

with f_col:
    st.markdown('<h3>📝 سجل طلبك باحترافية</h3>', unsafe_allow_html=True)
    with st.form("main_order_form"):
        u_name = st.text_input("الأسم الكامل")
        u_phone = st.text_input("رقم الهاتف (واتساب)")
        u_srv = st.selectbox("نوع الخدمة المطلوبة", ["تصميم CV", "تحويل مالي", "برمجة موقع", "مونتاج فيديو", "أخرى"])
        u_det = st.text_area("تفاصيل إضافية")
        submit_btn = st.form_submit_button("إرسال الطلب الآن 🚀")

with t_col:
    st.markdown('<br><br>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">🔒 تشفير بيانات كامل وآمن</div>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">✅ ضمان جودة واسترداد أموال</div>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">📞 دعم فني واتساب 24/7</div>', unsafe_allow_html=True)

if submit_btn:
    if u_name and u_phone:
        order_no = f"AY-{random.randint(1000, 9999)}"
        # حفظ البيانات في ملف CSV
        order_data = pd.DataFrame({
            "التاريخ": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")],
            "الرقم": [order_no], "العميل": [u_name], "الهاتف": [u_phone],
            "الخدمة": [u_srv], "الحالة": ["قيد المعالجة"]
        })
        db_path = "orders_database.csv"
        order_data.to_csv(db_path, mode='a', index=False, header=not os.path.exists(db_path), encoding='utf-8-sig')
        
        st.success(f"تم التسجيل بنجاح! رقم طلبك هو: {order_no}")
        wa_link = f"https://wa.me/9647739778877?text=أهلاً أيوب، قمت بطلب خدمة: {u_srv} برقم: {order_no}"
        st.markdown(f'<a href="{wa_link}" target="_blank"><div style="background-color:#25d366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">تأكيد عبر واتساب أيوب 🟢</div></a>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("لطفاً، املأ الاسم والرقم للتواصل معك.")

# --- 5. قسم تتبع الطلبات ---
st.write("---")
st.markdown('<h2 style="text-align:center;">🔍 تتبع حالة طلبك</h2>', unsafe_allow_html=True)
search_id = st.text_input("أدخل رقم طلبك (AY-XXXX)")
if search_id:
    if os.path.exists("orders_database.csv"):
        try:
            full_data = pd.read_csv("orders_database.csv", on_bad_lines='skip')
            user_order = full_data[full_data['الرقم'].astype(str) == search_id]
            if not user_order.empty:
                st.markdown(f'''
                    <div style="border: 2px solid #FFD700; padding: 20px; border-radius: 15px; text-align: center; background-color: #111;">
                        <h3>أهلاً {user_order.iloc[-1]["العميل"]}</h3>
                        <p>حالة طلبك الحالية هي:</p>
                        <h1 style="color: #FFD700 !important; font-size: 40px;">{user_order.iloc[-1]["الحالة"]}</h1>
                    </div>
                ''', unsafe_allow_html=True)
            else:
                st.warning("الرقم غير موجود، تأكد من كتابته بشكل صحيح.")
        except: st.error("نواجه مشكلة بسيطة في قراءة البيانات، جرب لاحقاً.")

# --- 6. الحقوق واللمسة النهائية ---
st.markdown(f"""
    <div style="text-align:center; color:#666; font-size:14px; margin-top:60px; border-top: 1px solid #333; padding-top: 20px;">
        جميع الحقوق محفوظة © {datetime.datetime.now().year} - مكتبة أيوب الذكية<br>
        تطوير نظام أيوب للذكاء الاصطناعي | بغداد، العراق 🇮🇶
    </div>
""", unsafe_allow_html=True)
