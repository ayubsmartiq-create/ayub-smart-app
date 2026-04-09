import streamlit as st
import pandas as pd
import os
import datetime
import random

# --- 1. التصميم الملكي العالمي (Global Gold Edition) ---
st.set_page_config(page_title="مكتبة أيوب الذكية", layout="wide")

st.markdown("""
    <style>
    /* الإعدادات العامة والخطوط */
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    .stApp { background-color: #000000; direction: rtl; }
    
    h1, h2, h3, h4, p, label, span, div, .stMarkdown {
        color: #FFD700 !important;
        text-align: right !important;
        font-family: 'Cairo', sans-serif;
    }

    /* منع تقطيع النصوص في القائمة الجانبية */
    section[data-testid="stSidebar"] { width: 350px !important; direction: rtl; background-color: #050505 !important; }
    
    /* الحقول والقوائم المنسدلة */
    .stTextInput input, .stSelectbox div, .stTextArea textarea {
        background-color: #111111 !important;
        color: #FFD700 !important;
        border: 2px solid #FFD700 !important;
        border-radius: 12px !important;
        text-align: right !important;
    }

    /* صناديق الخدمات */
    .service-card {
        background: linear-gradient(145deg, #0a0a0a, #1a1a1a);
        padding: 25px; border-radius: 20px; border: 1px solid #FFD700;
        text-align: right; transition: 0.4s; height: 260px;
        box-shadow: 0px 10px 30px rgba(255, 215, 0, 0.05);
    }
    .service-card:hover { transform: translateY(-10px); box-shadow: 0px 15px 40px rgba(255, 215, 0, 0.2); }

    /* الأمان والحقوق */
    .trust-badge {
        background-color: #0a2a0a; color: #00ff00 !important;
        padding: 10px; border-radius: 10px; border: 1px solid #00ff00;
        text-align: center !important; font-size: 14px; margin-bottom: 10px;
    }
    
    .footer {
        text-align: center !important; color: #555 !important;
        padding: 20px; margin-top: 50px; border-top: 1px solid #222;
    }

    /* زر الإرسال */
    .stButton>button {
        background: linear-gradient(90deg, #FFD700, #b8860b) !important;
        color: #000000 !important; font-weight: bold !important;
        font-size: 20px !important; width: 100% !important; border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. مساعد أيوب الذكي (Sidebar) ---
with st.sidebar:
    st.markdown('<h2 style="text-align:center;">🤖 مساعد أيوب الذكي</h2>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; color:#FFD700;">أهلاً بيك عيوني.. أنا هنا حتى أساعدك بطلباتك. اسألني أي شي!</div>', unsafe_allow_html=True)
    
    ai_msg = st.text_input("بماذا أفكر؟ (اسأل المساعد هنا)")
    if ai_msg:
        responses = {
            "شلون": "أهلاً بيك! نورتنا. إحنا نوفر خدمات مونتاج، تحويل مالي، وبحوث بأعلى جودة.",
            "سعر": "تدلل، أسعارنا مناسبة جداً وما نختلف وياك. اطلب الخدمة وراح نتواصل وياك بالتفاصيل.",
            "وقت": "إحنا معروفين بالسرعة، أغلب الخدمات تخلص بنفس اليوم أو خلال 24 ساعة حسب نوع الطلب.",
            "امان": "بياناتك ويانا بأمان كامل، ونضمن لك جودة الشغل واسترداد فلوسك إذا ما عجبك العمل.",
            "شكرا": "ولو، تدلل يا غالي.. إحنا بخدمتك دائماً!"
        }
        found = False
        for key in responses:
            if key in ai_msg:
                st.info(responses[key])
                found = True
                break
        if not found:
            st.info("كلامك ذهب، بس ياريت توضح سؤالك أكثر أو راسل أيوب مباشرة واتساب.")

# --- 3. قسم الهوية وصناديق الخدمات ---
st.markdown('<h1 style="text-align:center; font-size: 55px;">مكتبة أيوب الذكية</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size: 22px; opacity: 0.8;">المنصة الأولى للخدمات الرقمية المتكاملة</p>', unsafe_allow_html=True)

cols = st.columns(4)
services = [
    {"t": "الخدمات المكتبية", "d": "طباعة، استنساخ، وعمل CV احترافي عالمي."},
    {"t": "التحويل المالي", "d": "زين كاش، ماستر كارد، وتعبئة كافة الأرصدة."},
    {"t": "الذكاء الاصطناعي", "d": "إنشاء مواقع، تصميم شعارات، وحلول برمجية ذكية."},
    {"t": "المونتاج والإبداع", "d": "صناعة محتوى تيك توك، يوتيوب، وإدارة حسابات."}
]
for i, s in enumerate(services):
    with cols[i]:
        st.markdown(f'<div class="service-card"><h3>{s["t"]}</h3><p>{s["d"]}</p></div>', unsafe_allow_html=True)

# --- 4. الاستمارة الذكية والأمان ---
st.write("---")
col_form, col_trust = st.columns([2, 1])

with col_form:
    st.markdown('<h3>📝 سجل طلبك الجديد</h3>', unsafe_allow_html=True)
    with st.form("smart_form"):
        u_name = st.text_input("الأسم الكريم الكامل")
        u_phone = st.text_input("رقم الواتساب")
        u_service = st.selectbox("نوع الخدمة", ["عمل CV", "زين كاش", "تصميم شعار", "موقع إلكتروني", "مونتاج", "أخرى"])
        u_notes = st.text_area("تفاصيل الطلب")
        submit = st.form_submit_button("إرسال الطلب 🚀")

with col_trust:
    st.markdown('<br><br>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">🔒 اتصال مشفر وآمن 100%</div>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">✅ ضمان جودة العمل واسترداد المبلغ</div>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">📞 دعم فني متواصل 24/7</div>', unsafe_allow_html=True)

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
        
        # إشعار الواتساب
        MY_NUMBER = "9647739778877"
        wa_url = f"https://wa.me/{MY_NUMBER}?text=طلب جديد من {u_name}%0Aالرقم: {order_id}%0Aالخدمة: {u_service}"
        st.markdown(f'<a href="{wa_url}" target="_blank"><div style="background-color:#25d366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">تأكيد عبر واتساب أيوب 🟢</div></a>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("يرجى ملء الاسم ورقم الهاتف")

# --- 5. نظام تتبع الطلب المطور ---
st.write("---")
st.markdown('<h2 style="text-align:center;">🔍 تتبع حالة طلبك</h2>', unsafe_allow_html=True)
search_id = st.text_input("أدخل رقم طلبك (مثال: AY-1234)")

if search_id:
    if os.path.exists("orders_database.csv"):
        try:
            data = pd.read_csv("orders_database.csv", on_bad_lines='skip')
            res = data[data['الرقم'].astype(str) == search_id]
            if not res.empty:
                status = res.iloc[-1]['الحالة']
                st.markdown(f"""
                    <div style="background-color:#111; padding:30px; border-radius:20px; border:2px solid #FFD700; text-align:center;">
                        <h3 style="margin:0;">أهلاً {res.iloc[-1]['الاسم']}، حالة طلبك هي:</h3>
                        <h1 style="color:#FFD700; font-size:45px; margin:20px 0;">{status}</h1>
                        <p style="color:#aaa !important;">سيصلك إشعار فور اكتمال العمل.</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("هذا الرقم غير موجود، يرجى التأكد من الرقم.")
        except: st.error("عذراً، حدث خطأ في قراءة السجلات.")

# --- 6. حقوق الملكية (Footer) ---
st.markdown(f"""
    <div class="footer">
        جميع الحقوق محفوظة لمكتبة أيوب الذكية © {datetime.datetime.now().year}<br>
        بإدارة المبدع أيوب هاني | ayub.smart.iq@gmail.com
    </div>
""", unsafe_allow_html=True)
