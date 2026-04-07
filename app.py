import streamlit as st

# 1. إعدادات الصفحة الأساسية واللوغو
LOGO_URL = "https://raw.githubusercontent.com/ayubsmartiq-create/ayub-smart-app/main/Ayub-Logo.png"
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon=LOGO_URL, layout="wide")

# 2. هندسة الألوان والخطوط (CSS) - التركيز على اللون الأبيض
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل كل نصوص الموقع باللون الأبيض */
    html, body, [class*="css"], .stApp, p, h1, h2, h3, h4, span, label, div {{
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; 
        text-align: right !important;
        color: #ffffff !important;
    }}
    
    /* خلفية الموقع زرقاء غامقة جداً لتبرز الخط الأبيض */
    .stApp {{
        background-color: #0f172a !important;
    }}
    
    /* تصميم رأس الصفحة (الهيدر) */
    .header-box {{
        background: linear-gradient(135deg, #1e40af, #1e3a8a);
        padding: 30px; border-radius: 20px; border-bottom: 5px solid #facc15;
        text-align: center; margin-bottom: 25px;
    }}

    /* تعديل لون حقول الكتابة ليكون النص داخلها أسود (حتى يرى الزبون ما يكتب) */
    input, textarea, select {{
        color: #000000 !important;
        background-color: #ffffff !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة الرئيسي (الهيدر)
st.markdown('<div class="header-box"><h1>🦅 مكتبة أيوب الذكية </h1><p>خيارك الذكي للخدمات الإلكترونية والمونتاج</p></div>', unsafe_allow_html=True)

st.write("أهلاً بك يا بطل! هذا هو الهيكل الأساسي لموقعك باللون الأبيض.")
import random
import datetime

# --- إعدادات المبرمج أيوب ---
MY_WHATSAPP = "9647739778877"  # 👈 أيوب: لا تنسى تحط رقمك هنا بدون أصفار بالبداية
FORMSPREE_URL = "https://formspree.io/f/xvzvdjzq" # رابط الإيميل مالتك

# 1. تصميم الاستمارة داخل صندوق أنيق
st.markdown('<h3 style="color: #facc15; text-align: right;">📑 تقديم طلب خدمة جديد</h3>', unsafe_allow_html=True)

with st.form("ayub_order_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("الأسم الثلاثي")
    with col2:
        phone = st.text_input("رقم الهاتف (واتساب)")
        
    service = st.selectbox("نوع الخدمة المطلوبة", 
                          ["تقديم تعيينات/عقود", "مونتاج فيديو (CapCut)", "تصميم بوتات ذكاء اصطناعي", "خدمات مكتبية وتوصيل"])
    
    details = st.text_area("اشرح لنا طلبك أو الملاحظات")
    
    submit = st.form_submit_button("إرسال البيانات للمكتبة 🚀")

    if submit:
        if name and phone:
            # توليد رقم طلب مميز
            order_id = f"AY-{random.randint(1000, 9999)}"
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            # إرسال البيانات للإيميل (تلقائياً)
            payload = {
                "رقم الطلب": order_id,
                "اسم الزبون": name,
                "رقم الهاتف": phone,
                "نوع الخدمة": service,
                "التفاصيل": details,
                "وقت الطلب": now
            }
            requests.post(FORMSPREE_URL, data=payload)
            
            # إظهار رسالة النجاح
            st.success(f"عاشت إيدك يا {name}! استلمنا بياناتك برقم طلب: {order_id}")
            
            # تجهيز رابط الواتساب لتأكيد الطلب وإرسال الصور
            wa_msg = f"مرحباً أيوب، قدمت طلب جديد ورقم طلبي هو ({order_id}). هذي الصور والمستمسكات:"
            wa_url = f"https://wa.me/{MY_WHATSAPP}?text={wa_msg}"
            
            st.markdown(f"""
                <div style="background: #1e293b; padding: 20px; border-radius: 15px; border: 2px solid #25d366; margin-top: 15px; text-align: center;">
                    <h4 style="color: #facc15;">بقت خطوة وحدة يا بطل! 📸</h4>
                    <p style="color: white;">اضغط على الزر جوه حتى ترسل صور المستمسكات أو المرفقات على الواتساب مالتنا وتأكد الحجز:</p>
                    <a href="{wa_url}" target="_blank" style="display: block; background-color: #25d366; color: white !important; padding: 12px; border-radius: 10px; text-decoration: none; font-weight: bold; border: 1px solid white;">
                        تأكيد الطلب وإرسال المرفقات (WhatsApp) ✅
                    </a>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("عيني أيوب، ذكر الزبون يملأ الاسم والرقم ضروري!")
