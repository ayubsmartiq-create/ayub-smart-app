import streamlit as st
import requests

# 1. إعدادات الهوية
LOGO_URL = "https://raw.githubusercontent.com/ayubsmartiq-create/ayub-smart-app/main/Ayub-Logo.png"
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon=LOGO_URL, layout="wide")

# 2. تصميم CSS (إضافة ستايل التتبع)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"], .stApp {{
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; text-align: right !important;
        background-color: #0f172a !important; color: white !important;
    }}
    .status-box {{
        background-color: #1e293b; padding: 20px; border-radius: 15px;
        border: 1px solid #facc15; text-align: center; margin-top: 10px;
    }}
    .header-box {{
        background: linear-gradient(135deg, #1e40af, #1e3a8a);
        padding: 30px; border-radius: 20px; border-bottom: 5px solid #facc15;
        text-align: center; margin-bottom: 25px;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر
st.markdown(f'<div class="header-box"><h1>🦅 مكتبة أيوب الذكية 🦅</h1><p>نظام الخدمات الإلكترونية المطور</p></div>', unsafe_allow_html=True)

# 4. التبويبات (Tabs) - لتنظيم الموقع
tab1, tab2 = st.tabs(["📑 طلب خدمة جديدة", "🔍 تتبع حالة طلبك"])

with tab1:
    st.subheader("📝 استمارة التقديم")
    with st.form("main_form"):
        name = st.text_input("الأسم الثلاثي")
        phone = st.text_input("رقم الهاتف")
        service = st.selectbox("نوع الخدمة", ["تقديم تعيينات", "ذكاء اصطناعي", "مونتاج", "قرطاسية"])
        details = st.text_area("التفاصيل")
        submit = st.form_submit_button("إرسال الطلب 🚀")
        if submit:
            if name and phone:
                requests.post("https://formspree.io/f/xvzvdjzq", data={"الاسم": name, "الهاتف": phone, "الخدمة": service, "التفاصيل": details})
                st.success("تم الإرسال! سيتم تزويدك برقم الطلب عبر الواتساب.")
            else:
                st.warning("يرجى ملء البيانات.")

with tab2:
    st.subheader("🔎 استعلم عن معاملتك")
    track_phone = st.text_input("أدخل رقم الموبايل المسجل به:")
    if st.button("فحص الحالة"):
        if track_phone:
            # هنا مستقبلاً نربطها بجدول بيانات، حالياً سنضع رسالة ترحيبية ذكية
            st.markdown(f"""
                <div class="status-box">
                    <h4 style="color: #facc15;">حالة الطلب للرقم: {track_phone}</h4>
                    <p>🟡 قيد المراجعة والتدقيق</p>
                    <small>سيتم تحديث الحالة فور إنجاز المعاملة من قبل أيوب</small>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("يرجى إدخال الرقم.")

# 5. المساعد الذكي (أسفل الصفحة)
st.divider()
with st.expander("🤖 اسأل مساعد أيوب (AI)"):
    if "msgs" not in st.session_state: st.session_state.msgs = []
    for m in st.session_state.msgs: st.chat_message(m["role"]).write(m["content"])
    prompt = st.chat_input("كيف أخدمك؟")
    if prompt:
        st.session_state.msgs.append({"role": "user", "content": prompt})
        st.session_state.msgs.append({"role": "assistant", "content": "أهلاً بك، أيوب سيقوم بالرد عليك بخصوص هذا الاستفسار قريباً."})
        st.rerun()
# أضف هذا الكود في نهاية ملف app.py المرة الجاية

st.markdown(f"""
    <a href="https://wa.me/9647739778877" class="whatsapp-btn" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="50">
    </a>
    <style>
    .whatsapp-btn {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 1000;
        filter: drop-shadow(2px 4px 6px black);
    }}
    </style>
""", unsafe_allow_html=True)
# أضف هذا داخل استمارة التقديم (Form)
uploaded_file = st.file_uploader("📎 ارفع المستمسكات أو الصور المطلوبة هنا (اختياري)", type=['png', 'jpg', 'pdf'])

# أضف هذا القسم في أسفل الصفحة للتواصل السريع
st.markdown("""
    <div style="text-align: center; padding: 20px; background: #1e293b; border-radius: 15px; margin-top: 30px;">
        <h3 style="color: #facc15;">📞 تواصل معنا مباشرة</h3>
        <p>للاستفسارات العاجلة، يمكنك مراسلتنا عبر:</p>
        <a href="https://wa.me/9647700000000" style="text-decoration: none; color: #25d366; font-weight: bold; font-size: 20px;">واتساب المكتبة ✅</a>
        <br><br>
        <p style="font-size: 12px; color: gray;">الموقع: بغداد - اليوسفية - مكتبة أيوب الذكية</p>
    </div>
""", unsafe_allow_html=True)
# 1. إضافة شريط العروض في أعلى الصفحة
st.markdown("""
    <div style="background-color: #ef4444; color: white; text-align: center; padding: 5px; font-weight: bold; border-radius: 5px;">
        🔥 عرض محدود: استشارة ذكاء اصطناعي مجانية عند طلب أي خدمة تقديم إلكتروني!
    </div>
""", unsafe_allow_html=True)

# 2. كود تحويل الموقع لتطبيق (يضاف في الـ Head)
st.markdown("""
    <script>
    // كود بسيط لإشعار المستخدم بإضافة الموقع للشاشة الرئيسية
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js');
      });
    }
    </script>
""", unsafe_allow_html=True)
# أضف هذا القسم قبل الاستمارة مباشرة
st.markdown("""
    <div style="background: #1e293b; padding: 20px; border-radius: 15px; border: 1px dashed #facc15; margin-bottom: 20px;">
        <h3 style="color: #facc15; text-align: center;">💰 قائمة الخدمات والأسعار</h3>
        <table style="width: 100%; color: white; text-align: right;">
            <tr><td>📄 التقديم الإلكتروني (عقود/تعيينات)</td><td>تبدأ من 5,000 د.ع</td></tr>
            <tr><td>🎬 مونتاج فيديو احترافي (CapCut)</td><td>تبدأ من 15,000 د.ع</td></tr>
            <tr><td>🤖 بناء بوت ذكاء اصطناعي خاص</td><td>حسب الاتفاق</td></tr>
        </table>
    </div>
""", unsafe_allow_html=True)

# أضف خانة كود الخصم داخل الاستمارة
promo_code = st.text_input("🎟️ هل لديك كود خصم؟")
# 1. إعداد نظام الذاكرة للمساعد الذكي
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "هلا بيك بمكتبة أيوب الذكية! 🦅 أنا مساعد أيوب التقني، شلون أقدر أساعدك بمعاملاتك اليوم؟"}
    ]

# 2. تصميم واجهة المساعد (UI)
st.markdown("""
    <div style="background: linear-gradient(90deg, #1e3a8a, #1e40af); padding: 15px; border-radius: 15px 15px 0 0; border-bottom: 3px solid #facc15;">
        <h3 style="color: white; margin: 0; text-align: center;">🤖 مساعد أيوب الذكي</h3>
    </div>
""", unsafe_allow_html=True)

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 3. معالجة إدخال الزبون
if prompt := st.chat_input("اكتب استفسارك هنا (مثلاً: شنو المستمسكات المطلوبة للتعيين؟)"):
    # إضافة رسالة الزبون للذاكرة
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # رد المساعد (هنا نضع المنطق الذكي)
    with st.chat_message("assistant"):
        response = ""
        if "تعيين" in prompt or "عقد" in prompt:
            response = "تدلل! للتقديم على التعيينات نحتاج منك (الجنسية، بطاقة السكن، وشهادة التخرج). تقدر ترفعهن بالاستمارة جوه أو تراسلنا واتساب."
        elif "مونتاج" in prompt or "تصميم" in prompt:
            response = "أنت بالمكان الصح! أيوب خبير مونتاج ببرنامج CapCut، نكدر نسويلك فيديو احترافي (Transitions و Color Grading) يبيض الوجه. شنو نوع الفيديو اللي تريده؟"
        elif "ذكاء" in prompt or "بوت" in prompt:
            response = "هذا اختصاصنا! نصمم لك بوتات ذكية ونعلمك شلون تستخدم الـ AI بشغلك. تريد نبني لك بوت خاص؟"
        else:
            response = "رسالتك وصلت يا طيب. أيوب راح يشوف الطلب ويجاوبك بأسرع وقت، أو تقدر تضغط على زر الواتساب للتواصل المباشر."
        
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
import random
import datetime

# أضف هذا الجزء داخل كود الإرسال (Submit)
if submit:
    if name and phone:
        order_id = f"AY-{random.randint(1000, 9999)}" # توليد رقم طلب
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # البيانات اللي راح تروح للإيميل أو الجدول
        data = {
            "رقم الطلب": order_id,
            "الاسم": name,
            "الهاتف": phone,
            "الخدمة": service,
            "التفاصيل": details,
            "الوقت": now
        }
        
        requests.post("https://formspree.io/f/xvzvdjzq", data=data)
        
        st.success(f"عاشت إيدك يا {name}! طلبك وصل بنجاح.")
        st.info(f"🆔 رقم طلبك هو: **{order_id}** (يرجى حفظه لمتابعة الحالة)")
if submit:
    if name and phone:
        order_id = f"AY-{random.randint(1000, 9999)}" # توليد رقم الطلب
        
        # 1. إرسال البيانات للإيميل كالمعتاد
        data = {
            "رقم الطلب": order_id,
            "الاسم": name,
            "الهاتف": phone,
            "الخدمة": service,
            "التفاصيل": details
        }
        requests.post("https://formspree.io/f/xvzvdjzq", data=data)
        
        # 2. إنشاء رابط واتساب ذكي يحتوي على رقم الطلب
        # استبدل 96477XXXXXXXX برقمك الحقيقي
        wa_number = "96477XXXXXXXX" 
        wa_message = f"مرحباً مكتبة أيوب، قمت بإرسال طلب جديد باسم ({name}) ورقم الطلب هو: {order_id}"
        wa_link = f"https://wa.me/{wa_number}?text={requests.utils.quote(wa_message)}"
        
        # 3. إظهار النتيجة للزبون مع زر التأكيد
        st.success(f"عاشت إيدك! طلبك وصل للإيميل برقم: {order_id}")
        st.markdown(f"""
            <div style="text-align: center; background: #1e293b; padding: 15px; border-radius: 10px; border: 1px solid #25d366;">
                <p style="color: white;">لضمان سرعة التنفيذ، يرجى تأكيد الطلب عبر الواتساب:</p>
                <a href="{wa_link}" target="_blank" style="background-color: #25d366; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">
                     تأكيد الطلب عبر الواتساب ✅
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("يرجى ملء الاسم ورقم الهاتف.")
# تأكد من إضافة هذا التعديل في قسم الإرسال (Submit)
if submit:
    if name and phone:
        order_id = f"AY-{random.randint(1000, 9999)}"
        
        # تحضير البيانات للإرسال (بما فيها الملف المرفق)
        files = {}
        if uploaded_file is not None:
            files = {"upload": (uploaded_file.name, uploaded_file.getvalue())}
        
        payload = {
            "رقم الطلب": order_id,
            "الاسم": name,
            "الهاتف": phone,
            "الخدمة": service,
            "التفاصيل": details
        }
        
        # إرسال البيانات مع الملف إلى Formspree
        response = requests.post("https://formspree.io/f/xvzvdjzq", data=payload, files=files)
        
        if response.status_code == 200:
            st.success(f"✅ تم استلام طلبك بنجاح! رقم الطلب هو: {order_id}")
            st.balloons() # حركة احتفالية بسيطة
            
            # رابط الواتساب مع رقم الطلب
            wa_msg = f"مرحباً أيوب، قدمت طلب جديد ورقم الطلب هو: {order_id}"
            st.markdown(f'<a href="https://wa.me/96477XXXXXXXX?text={wa_msg}" target="_blank" style="display: block; text-align: center; background: #25d366; color: white; padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold;">تأكيد الطلب وإرسال المرفقات عبر الواتساب ✅</a>', unsafe_allow_html=True)
        else:
            st.error("فشل الإرسال، تأكد من اتصال الإنترنت.")
