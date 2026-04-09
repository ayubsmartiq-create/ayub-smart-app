import streamlit as st
import pandas as pd
import os
import datetime
import random

# --- 1. التصميم الملكي الاحترافي (Global Gold Edition) ---
st.set_page_config(page_title="مكتبة أيوب الذكية", layout="wide")

st.markdown("""
    <style>
    /* الخلفية والنصوص العامة */
    .stApp { background-color: #000000; direction: rtl; }
    
    /* توحيد لون كل النصوص إلى الأصفر الذهبي الطوخ */
    h1, h2, h3, h4, p, label, span, div, .stMarkdown {
        color: #FFD700 !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif;
    }

    /* القوائم المنسدلة والحقول - النص والحدود ذهبية */
    .stTextInput input, .stSelectbox div, .stTextArea textarea, .stMultiSelect div {
        background-color: #111111 !important;
        color: #FFD700 !important;
        border: 2px solid #FFD700 !important;
        border-radius: 12px !important;
    }
    
    /* القائمة المنسدلة عند الفتح */
    div[data-baseweb="select"] ul {
        background-color: #111111 !important;
        color: #FFD700 !important;
    }

    /* صناديق الخدمات العالمية */
    .service-card {
        background: linear-gradient(145deg, #0a0a0a, #1a1a1a);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #FFD700;
        text-align: right;
        transition: 0.4s;
        height: 250px;
        box-shadow: 0px 10px 30px rgba(255, 215, 0, 0.05);
    }
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: 0px 15px 40px rgba(255, 215, 0, 0.2);
        border-width: 2px;
    }

    /* زر الإرسال */
    .stButton>button {
        background: linear-gradient(90deg, #FFD700, #b8860b) !important;
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 20px !important;
        padding: 15px !important;
        border-radius: 15px !important;
        border: none !important;
        box-shadow: 0px 5px 15px rgba(255, 215, 0, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. قسم الهوية ---
st.markdown('<h1 style="text-align:center; font-size: 55px; letter-spacing: 2px;">مكتبة أيوب الذكية</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size: 22px; opacity: 0.8;">المنصة الأولى للخدمات الرقمية والحلول الذكية</p>', unsafe_allow_html=True)

# --- 3. صناديق الخدمات الاحترافية ---
st.write("")
cols = st.columns(4)
services = [
    {"title": "الخدمات المكتبية", "desc": "طباعة صور، استنساخ، عمل CV احترافي، وتنسيق البحوث."},
    {"title": "التحويل المالي", "desc": "شحن وتفريغ زين كاش، ماستر كارد، وتعبئة كافة الأرصدة."},
    {"title": "الذكاء الاصطناعي", "desc": "إنشاء مواقع، تصميم شعارات، واستشارات في تطوير الأعمال الذكية."},
    {"title": "المونتاج والإبداع", "desc": "صناعة محتوى تيك توك، يوتيوب، وإدارة الحسابات الاجتماعية."}
]

for i, s in enumerate(services):
    with cols[i]:
        st.markdown(f"""
            <div class="service-card">
                <h3>{s['title']}</h3>
                <p>{s['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- 4. الاستمارة الذكية ---
st.write("---")
st.markdown('<h2 style="text-align:center;">إبدأ طلبك الآن</h2>', unsafe_allow_html=True)

with st.container():
    with st.form("smart_order_form"):
        u_name = st.text_input("الأسم الكريم الكامل")
        u_phone = st.text_input("رقم الواتساب الخاص بك")
        u_service = st.selectbox("اختر نوع الخدمة", [
            "عمل CV احترافي", "تحويل مالي (زين كاش)", "تصميم شعار (Logo)", 
            "إنشاء موقع إلكتروني", "استشارة ذكاء اصطناعي", "طباعة واستنساخ", 
            "مونتاج فيديو", "شراء رصيد", "أخرى"
        ])
        
        u_notes = ""
        if u_service == "أخرى":
            u_notes = st.text_area("يرجى ذكر تفاصيل الخدمة التي تحتاجها")
        else:
            u_notes = st.text_area("تفاصيل إضافية أو ملاحظات خاصة")
            
        submit = st.form_submit_button("إرسال الطلب إلى المكتبة")

if submit:
    if u_name and u_phone:
        order_id = f"AY-{random.randint(1000, 9999)}"
        order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # حفظ البيانات (تلقائياً)
        df = pd.DataFrame({"التاريخ": [order_date], "الرقم": [order_id], "الاسم": [u_name], "الهاتف": [u_phone], "الخدمة": [u_service], "الحالة": ["قيد المراجعة"]})
        file_db = "orders_database.csv"
        if not os.path.exists(file_db):
            df.to_csv(file_db, index=False, encoding='utf-8-sig')
        else:
            df.to_csv(file_db, mode='a', header=False, index=False, encoding='utf-8-sig')

        st.success(f"تم تسجيل طلبك برقم: {order_id}")
        
        # تحويل البيانات للواتساب
        MY_NUMBER = "9647739778877"
        wa_msg = f"طلب جديد من مكتبة أيوب الذكية%0A---%0Aالرقم: {order_id}%0Aالاسم: {u_name}%0Aالخدمة: {u_service}%0Aالتاريخ: {order_date}"
        wa_url = f"https://wa.me/{MY_NUMBER}?text={wa_msg}"
        
        st.markdown(f'<a href="{wa_url}" target="_blank"><div style="background-color:#25d366;color:white;padding:20px;border-radius:15px;text-align:center;font-weight:bold;font-size:18px;">اضغط هنا لتأكيد الطلب عبر الواتساب (مهم جداً) 🟢</div></a>', unsafe_allow_html=True)
        
        # ملاحظة الإيميل: Streamlit لا يرسل إيميلات مباشرة بدون سيرفر خارجي،
        # لكن الكود الآن مسجل للطلب في قاعدة البيانات.
    else:
        st.error("يرجى ملء الاسم ورقم الهاتف")

# --- 5. قسم حالة الطلب للزبون (تتبع احترافي) ---
st.write("---")
st.markdown('<h2 style="text-align:center;">تتبع حالة طلبك</h2>', unsafe_allow_html=True)
with st.container():
    search_id = st.text_input("أدخل رقم طلبك (AY-XXXX) لمعرفة الحالة")
    if search_id:
        if os.path.exists("orders_database.csv"):
            data = pd.read_csv("orders_database.csv")
            res = data[data['الرقم'].astype(str) == search_id]
            if not res.empty:
                status = res.iloc[-1]['الحالة']
                st.markdown(f"""
                    <div style="background-color:#111; padding:30px; border-radius:20px; border:1px solid #FFD700; text-align:center;">
                        <h3 style="margin:0;">حالة الطلب الحالية:</h3>
                        <h1 style="color:#FFD700; font-size:50px;">{status}</h1>
                        <p>سيتم التواصل معك فور تحديث الحالة</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("الرقم غير موجود، تأكد من كتابته بشكل صحيح.")
