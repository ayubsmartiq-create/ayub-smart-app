 # --- 2. تصميم الواجهة (CSS Custom Styling) المحدث للخط الأبيض ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل كل النصوص في الموقع باللون الأبيض */
    html, body, [class*="css"], .stApp, p, h1, h2, h3, h4, span, label {{
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; 
        text-align: right !important;
        color: #ffffff !important; /* اللون الأبيض الناصع */
    }}
    
    .stApp {{
        background-color: #0f172a !important; 
    }}
    
    .header-box {{
        background: linear-gradient(135deg, #1e40af, #1e3a8a);
        padding: 30px; border-radius: 20px; border-bottom: 5px solid #facc15;
        text-align: center; margin-bottom: 25px;
    }}
    
    /* لون الخط داخل حقول الإدخال يبقى واضحاً */
    input, textarea, select {{
        color: #000000 !important; /* النص داخل المربعات أسود لسهولة الكتابة */
        background-color: #ffffff !important;
    }}

    .price-card {{
        background: #1e293b; padding: 15px; border-radius: 15px;
        border: 1px dashed #facc15; margin-bottom: 20px;
    }}
    
    .wa-button {{
        display: block; text-align: center; background-color: #25d366; 
        color: white !important; padding: 15px; border-radius: 12px; 
        text-decoration: none; font-weight: bold; font-size: 18px;
        border: 2px solid white; margin-top: 10px;
    }}
    
    .stButton button {{ 
        background: #facc15 !important; 
        color: #1e3a8a !important; 
        font-weight: 900 !important; 
        width: 100%; 
        border-radius: 10px; 
    }}
    </style>
""", unsafe_allow_html=True)

import streamlit as st
import requests
import random
import datetime

# --- 1. إعدادات الهوية والصفحة ---
LOGO_URL = "https://raw.githubusercontent.com/ayubsmartiq-create/ayub-smart-app/main/Ayub-Logo.png"
MY_WHATSAPP = "9647700000000" # 👈 أيوب: حط رقمك الحقيقي هنا (بدون أصفار بالبداية)
FORMSPREE_URL = "https://formspree.io/f/xvzvdjzq"

st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon=LOGO_URL, layout="wide")

# --- 2. تصميم الواجهة (CSS Custom Styling) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"], .stApp {{
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; text-align: right !important;
        background-color: #0f172a !important; color: white !important;
    }}
    .header-box {{
        background: linear-gradient(135deg, #1e40af, #1e3a8a);
        padding: 30px; border-radius: 20px; border-bottom: 5px solid #facc15;
        text-align: center; margin-bottom: 25px;
    }}
    .price-card {{
        background: #1e293b; padding: 15px; border-radius: 15px;
        border: 1px dashed #facc15; margin-bottom: 20px;
    }}
    .wa-button {{
        display: block; text-align: center; background-color: #25d366; 
        color: white !important; padding: 15px; border-radius: 12px; 
        text-decoration: none; font-weight: bold; font-size: 18px;
        border: 2px solid white; margin-top: 10px;
    }}
    .stButton button {{ background: #facc15 !important; color: #1e3a8a !important; font-weight: 900 !important; width: 100%; border-radius: 10px; }}
    </style>
""", unsafe_allow_html=True)

# --- 3. شريط العروض المتحرك ---
st.markdown("""
    <div style="background-color: #ef4444; color: white; text-align: center; padding: 5px; font-weight: bold; border-radius: 5px; margin-bottom: 10px;">
        🔥 عرض خاص: استشارة ذكاء اصطناعي مجانية عند طلب أي خدمة تقديم إلكتروني اليوم!
    </div>
""", unsafe_allow_html=True)

# --- 4. الهيدر الرئيسي ---
st.markdown(f'<div class="header-box"><h1>🦅 مكتبة أيوب الذكية </h1><p>خيارك الذكي للخدمات الإلكترونية والمونتاج الاحترافي</p></div>', unsafe_allow_html=True)

# --- 5. نظام التبويبات (Tabs) ---
tab1, tab2, tab3 = st.tabs(["📑 تقديم طلب", "🔍 تتبع المعاملة", "🤖 مساعد أيوب الذكي"])

# --- التبويب الأول: استمارة الطلب ---
with tab1:
    st.markdown('<div class="price-card"><h4>💰 أسعار الخدمات تبدأ من 5,000 د.ع فقط!</h4></div>', unsafe_allow_html=True)
    
    with st.form("main_order_form"):
        name = st.text_input("الأسم الثلاثي")
        phone = st.text_input("رقم الهاتف (واتساب)")
        service = st.selectbox("نوع الخدمة المطلوبة", ["تقديم تعيينات/عقود", "مونتاج فيديو (CapCut)", "تصميم بوتات ذكاء اصطناعي", "خدمات مكتبية وتوصيل"])
        details = st.text_area("اشرح لنا طلبك بالتفصيل")
        
        submit = st.form_submit_button("إرسال الطلب الآن 🚀")
        
        if submit:
            if name and phone:
                order_id = f"AY-{random.randint(1000, 9999)}"
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                
                # إرسال البيانات للإيميل
                form_payload = {"ID": order_id, "Name": name, "Phone": phone, "Service": service, "Note": details, "Time": now}
                requests.post(FORMSPREE_URL, data=form_payload)
                
                # إظهار رسالة النجاح والواتساب
                st.success(f"عاشت إيدك! تم استلام طلبك برقم: {order_id}")
                wa_msg = f"مرحباً أيوب، قدمت طلب جديد باسم ({name}) ورقم الطلب: {order_id}. هذي الصور والمستمسكات:"
                wa_url = f"https://wa.me/{MY_WHATSAPP}?text={requests.utils.quote(wa_msg)}"
                
                st.markdown(f"""
                    <div style="background: #1e293b; padding: 20px; border-radius: 15px; border: 2px solid #25d366; margin-top: 20px;">
                        <h3 style="color: #facc15; text-align: center;">خطوة أخيرة مهمة! 📸</h3>
                        <p style="text-align: center;">يرجى الضغط على الزر أدناه لإرسال الصور أو المستمسكات عبر الواتساب لتثبيت الطلب:</p>
                        <a href="{wa_url}" target="_blank" class="wa-button">تأكيد الطلب وإرسال الصور ✅</a>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("يرجى إكمال الاسم ورقم الهاتف.")

# --- التبويب الثاني: تتبع الطلب ---
with tab2:
    st.subheader("🔎 تتبع حالة معاملتك")
    track_input = st.text_input("أدخل رقم الهاتف المسجل به:")
    if st.button("فحص الحالة"):
        if track_input:
            st.info(f"الطلب المرتبط بالرقم {track_input} حالياً **قيد المعالجة**. سيتم التواصل معك فور الإنجاز.")
        else:
            st.error("يرجى إدخال الرقم.")

# --- التبويب الثالث: مساعد أيوب AI ---
with tab3:
    st.subheader("🤖 دردشة مباشرة مع الذكاء الاصطناعي")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "أهلاً بك! أنا مساعد أيوب الذكي. كيف يمكنني خدمتك اليوم؟"}]
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if prompt := st.chat_input("اسألني عن الخدمات أو المستمسكات..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        
        # ردود ذكية بسيطة
        response = "شكراً لسؤالك! أيوب سيقوم بالرد عليك بالتفصيل بخصوص '" + prompt + "' فور تواجده، أو يمكنك مراسلته واتساب للسرعة."
        if "تعيين" in prompt: response = "للتعيينات نحتاج: صورة الجنسية، بطاقة السكن، ووثيقة التخرج. ارفعها بالاستمارة وراسلنا واتساب!"
        
        with st.chat_message("assistant"): st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- 6. الفوتر (Footer) ---
st.markdown(f"""
    <hr>
    <div style="text-align: center; color: gray; padding-bottom: 20px;">
        <p>بغداد - اليوسفية | مكتبة أيوب الذكية</p>
        <p>© {datetime.datetime.now().year} جميع الحقوق محفوظة لـ أيوب هاني</p>
    </div>
""", unsafe_allow_html=True)
