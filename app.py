import streamlit as st

# --- 1. الإعدادات الأساسية للمتصفح ---
st.set_page_config(page_title="مكتبة أيوب هاني الذكية", page_icon="🦅", layout="wide")

# --- 2. تصميم الألوان والهوية (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل الخط عربي والاتجاه من اليمين */
    html, body, [class*="css"], .stApp {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0f172a !important; /* كحلي ملكي عميق */
    }

    /* الكتابة العامة بيضاء صافية */
    p, h1, h2, h3, h4, span, label, li {
        color: #ffffff !important;
    }

    /* ميزة ذكية: الكتابة داخل المربعات (Input) لونها ذهبي لتتميز عن النص الأبيض */
    input, textarea, select, div[data-baseweb="select"] > div {
        background-color: #1e293b !important;
        color: #facc15 !important; /* ذهبي للمدخلات */
        border: 2px solid #c5a059 !important;
        border-radius: 12px !important;
    }

    /* تصميم مقدمة الموقع (الرأس) */
    .header-box {
        background: linear-gradient(135deg, #0b3d61 0%, #1e293b 100%);
        padding: 40px;
        border-radius: 25px;
        border-right: 10px solid #c5a059;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 40px;
    }

    /* تصميم كروت الخدمات */
    .service-card {
        background: #1e293b;
        padding: 25px;
        border-radius: 20px;
        border-bottom: 4px solid #c5a059;
        transition: 0.4s;
        text-align: center;
        height: 100%;
    }
    .service-card:hover {
        transform: translateY(-10px);
        border-bottom: 4px solid #facc15;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. عرض مقدمة الموقع ---
st.markdown("""
    <div class="header-box">
        <h1 style="color: #c5a059 !important; font-weight: 900; font-size: 42px;">🦅 مكتبة أيوب هاني الذكية</h1>
        <p style="font-size: 20px; color: #cbd5e1 !important;">بوابتك الرقمية للمونتاج والخدمات المكتبية في القصر الأوسط</p>
    </div>
""", unsafe_allow_html=True)

# --- 4. قسم عرض الخدمات ---
st.write("### 🛠️ خدماتنا المتميزة")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059;">📂 خدمات مكتبية</h3>
            <p>• استنساخ وطباعة ملونة<br>• تصميم CV احترافي<br>• تقديم على التعيينات<br>• تحويل ملفات PDF</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059;">🎬 مونتاج وإبداع</h3>
            <p>• مونتاج CapCut Pro<br>• تصميم لوغوهات وهويات<br>• تصميم منيو وكارتات<br>• تعديل صور بالذكاء الاصطناعي</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059;">💰 معاملات مالية</h3>
            <p>• سحب وإيداع زين كاش<br>• تحويل أموال للمحافظات<br>• شحن بطاقات ألعاب<br>• دفع فواتير وخدمات</p>
        </div>
    """, unsafe_allow_html=True)
import random # تأكد من وجود هذا السطر في أعلى الملف مع streamlit

# --- 5. إعدادات رقم الواتساب ورقم الطلب ---
# ضع رقمك هنا بالصيغة الدولية (بدون أصفار وبدون +)
MY_WHATSAPP = "9647739778877" 

st.write("---") # خط فاصل للتنظيم
st.markdown('<h2 style="color: #c5a059; text-align: center;">📝 قسم حجز الطلبات</h2>', unsafe_allow_html=True)

# بداية حاوية الاستمارة
with st.container():
    # تصميم إطار خارجي للاستمارة
    st.markdown('<div style="background: #1e293b; padding: 30px; border-radius: 20px; border: 1px solid #c5a059;">', unsafe_allow_html=True)
    
    with st.form("order_form", clear_on_submit=False):
        # تقسيم المدخلات لصفوف
        col_name, col_phone = st.columns(2)
        
        with col_name:
            u_name = st.text_input("👤 الاسم الثلاثي", placeholder="اكتب اسمك هنا...")
        
        with col_phone:
            u_phone = st.text_input("📞 رقم التواصل (واتساب)", placeholder="07XXXXXXXXX")
        
        # قائمة الخدمات مع خيار "أخرى"
        service_list = [
            "اختر الخدمة...", 
            "استنساخ وطباعة", 
            "تصميم CV احترافي", 
            "مونتاج فيديو (CapCut)", 
            "معاملات زين كاش", 
            "تصميم لوغو / هوية", 
            "أخرى (اذكرها في التفاصيل)"
        ]
        u_service = st.selectbox("🎯 نوع الخدمة المطلوبة", service_list)
        
        # مربع التفاصيل
        u_details = st.text_area("📄 تفاصيل إضافية عن طلبك", placeholder="اشرح لنا ما تحتاجه بالضبط...")
        
        # زر الإرسال
        submit_btn = st.form_submit_button("توليد رقم الطلب وإرسال 🚀")

        if submit_btn:
            if u_name and u_phone and u_service != "اختر الخدمة...":
                # توليد رقم طلب مميز يبدأ بـ AY (اختصار أيوب)
                order_number = f"AY-{random.randint(1000, 9999)}"
                
                # إظهار رسالة نجاح للزبون
                st.success(f"تم استلام بياناتك بنجاح يا {u_name}!")
                
                # عرض رقم الطلب بشكل بارز وفخم
                st.markdown(f"""
                    <div style="background: #0f172a; padding: 20px; border-radius: 15px; border: 2px dashed #c5a059; text-align: center; margin: 20px 0;">
                        <h3 style="color: #facc15; margin: 0;">رقم طلبك هو: {order_number}</h3>
                        <p style="color: white; font-size: 14px; margin-top: 10px;">يرجى تزويدنا بهذا الرقم عند المراجعة</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # تحضير رسالة الواتساب
                wa_text = f"طلب جديد من الموقع 🦅%0a%0a" \
                          f"🔢 رقم الطلب: {order_number}%0a" \
                          f"👤 الأسم: {u_name}%0a" \
                          f"🎯 الخدمة: {u_service}%0a" \
                          f"📄 التفاصيل: {u_details}%0a" \
                          f"📞 رقم التواصل: {u_phone}"
                
                wa_link = f"https://wa.me/{MY_WHATSAPP}?text={wa_text}"
                
                # زر الانتقال للواتساب لتأكيد الطلب
                st.markdown(f"""
                    <a href="{wa_link}" target="_blank" style="text-decoration: none;">
                        <div style="background-color: #25d366; color: white; padding: 15px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 18px;">
                            تأكيد الطلب عبر واتساب الآن ✅
                        </div>
                    </a>
                """, unsafe_allow_html=True)
            else:
                st.error("عذراً.. يرجى ملء الاسم، الرقم، واختيار نوع الخدمة.")

    st.markdown('</div>', unsafe_allow_html=True)
