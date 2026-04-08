import streamlit as st
import random
import datetime

# --- 1. معلومات المكتبة الأساسية ---
# تأكد من وضع رقمك هنا بدلاً من الأصفار
MY_WHATSAPP = "9647700000000" 

# --- 2. إعدادات المتصفح ---
st.set_page_config(page_title="مكتبة أيوب هاني الذكية", page_icon="🦅", layout="wide")

# --- 3. تصميم الألوان والهوية (CSS المطور) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0f172a !important;
    }

    /* الكتابة العامة بيضاء */
    p, h1, h2, h3, h4, span, label, li {
        color: #ffffff !important;
    }

    /* تعديل المربعات والقوائم المنسدلة (لحل مشكلة اللون الأبيض) */
    div[data-baseweb="select"] > div, input, textarea {
        background-color: #1e293b !important;
        color: #facc15 !important; 
        border: 2px solid #c5a059 !important;
        border-radius: 12px !important;
    }

    /* تلوين النص داخل قائمة الخيارات نفسها */
    div[role="listbox"] ul, div[role="listbox"] li {
        background-color: #1e293b !important;
        color: #ffffff !important;
    }

    .header-box {
        background: linear-gradient(135deg, #0b3d61 0%, #1e293b 100%);
        padding: 40px;
        border-radius: 25px;
        border-right: 10px solid #c5a059;
        text-align: center;
        margin-bottom: 40px;
    }

    .service-card {
        background: #1e293b;
        padding: 25px;
        border-radius: 20px;
        border-bottom: 4px solid #c5a059;
        text-align: center;
        height: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. واجهة الموقع ---
st.markdown("""
    <div class="header-box">
        <h1 style="color: #c5a059 !important; font-weight: 900; font-size: 42px;">🦅 مكتبة أيوب هاني الذكية</h1>
        <p style="font-size: 20px;">بوابتك الرقمية للمونتاج والخدمات المكتبية في القصر الأوسط</p>
    </div>
""", unsafe_allow_html=True)

# --- 5. قسم الخدمات ---
st.write("### 🛠️ خدماتنا المتميزة")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="service-card"><h3 style="color: #c5a059;">📂 مكتبية</h3><p>• استنساخ وطباعة<br>• تصميم CV ملكي<br>• تقديم تعيينات</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="service-card"><h3 style="color: #c5a059;">🎬 مونتاج</h3><p>• فيديوهات CapCut<br>• تصميم لوغوهات<br>• هويات بصرية</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="service-card"><h3 style="color: #c5a059;">💰 مالي</h3><p>• زين كاش<br>• تحويل أموال<br>• شحن ألعاب</p></div>', unsafe_allow_html=True)

# --- 6. استمارة الطلب ---
st.write("---")
with st.form("order_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        u_name = st.text_input("👤 الاسم الثلاثي")
    with col_b:
        u_phone = st.text_input("📞 رقم الواتساب")
    
    u_service = st.selectbox("🎯 نوع الخدمة", ["استنساخ", "تصميم CV", "مونتاج فيديو", "زين كاش", "أخرى"])
    u_details = st.text_area("📄 تفاصيل الطلب")
    
    submit = st.form_submit_button("إرسال الطلب وحجز رقم 🚀")

    if submit:
        if u_name and u_phone:
            order_id = f"AY-{random.randint(1000, 9999)}"
            st.success(f"تم استلام طلبك يا {u_name}!")
            st.info(f"رقم الطلب: {order_id}")
            
            wa_text = f"طلب جديد!%0aرقم الطلب: {order_id}%0aالأسم: {u_name}%0aالخدمة: {u_service}"
            wa_url = f"https://wa.me/{MY_WHATSAPP}?text={wa_text}"
            
            st.markdown(f'<a href="{wa_url}" target="_blank"><div style="background:#25d366; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold;">تأكيد عبر واتساب ✅</div></a>', unsafe_allow_html=True)
