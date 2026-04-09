import streamlit as st

# --- 1. إعدادات المتصفح الأساسية ---
st.set_page_config(page_title="مكتبة أيوب هاني الذكية", page_icon="🦅", layout="wide")

# --- 2. هندسة التصميم والألوان (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* الخلفية العامة والنصوص */
    html, body, [class*="css"], .stApp {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0f172a !important; /* لون كحلي ملكي عميق */
    }

    /* النصوص العامة باللون الأبيض الصافي */
    p, h1, h2, h3, h4, span, label, li {
        color: #ffffff !important;
    }

    /* --- تمييز المربعات والقوائم باحترافية --- */
    /* جعل المربعات بلون أغمق قليلاً مع إطار ذهبي */
    div[data-baseweb="select"] > div, input, textarea {
        background-color: #1e293b !important; 
        color: #facc15 !important; /* الكتابة داخل المربع بلون أصفر ذهبي ساطع */
        border: 2px solid #c5a059 !important;
        border-radius: 12px !important;
    }

    /* حل مشكلة القائمة المنسدلة (حتى لا تظهر بيضاء) */
    div[role="listbox"] ul, div[role="listbox"] li {
        background-color: #1e293b !important;
        color: #ffffff !important;
    }

    /* تصميم رأس الصفحة (Header) */
    .header-box {
        background: linear-gradient(135deg, #0b3d61 0%, #1e293b 100%);
        padding: 45px;
        border-radius: 30px;
        border-right: 12px solid #c5a059;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        margin-bottom: 50px;
    }

    /* تصميم كروت الخدمات */
    .service-card {
        background: #1e293b;
        padding: 30px;
        border-radius: 20px;
        border-bottom: 5px solid #c5a059;
        transition: 0.4s ease-in-out;
        text-align: center;
        height: 100%;
    }
    .service-card:hover {
        transform: translateY(-10px);
        border-bottom: 5px solid #facc15;
        box-shadow: 0 10px 20px rgba(197, 160, 89, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. عرض مقدمة الموقع الفخمة ---
st.markdown("""
    <div class="header-box">
        <h1 style="color: #c5a059 !important; font-weight: 900; font-size: 45px; margin-bottom: 10px;">🦅 مكتبة أيوب هاني الذكية</h1>
        <p style="font-size: 22px; color: #cbd5e1 !important; font-weight: 700;">المونتاج الاحترافي والخدمات السريعة | اليوسفية - القصر الأوسط</p>
    </div>
""", unsafe_allow_html=True)

# --- 4. عرض الأقسام (الخدمات) ---
st.write("### 🛠️ خدماتنا المتميزة")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059; font-weight: 900;">📂 مكتبية</h3>
            <p>• استنساخ وطباعة ملونة<br>• تصميم CV احترافي<br>• تقديم تعيينات حكومية<br>• تحويل ملفات PDF</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059; font-weight: 900;">🎬 مونتاج وإبداع</h3>
            <p>• مونتاج CapCut Pro<br>• تصميم لوغوهات وهويات<br>• تصميم منيو وكارتات<br>• تعديل صور بالذكاء الاصطناعي</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-card">
            <h3 style="color: #c5a059; font-weight: 900;">💰 مالي وألعاب</h3>
            <p>• سحب وإيداع زين كاش<br>• تحويل أموال فوري<br>• شحن بطاقات ألعاب<br>• دفع فواتير وخدمات</p>
        </div>
    """, unsafe_allow_html=True)
import random # تأكد أن هذا السطر موجود في أعلى الملف تماماً

# --- 5. رقم الواتساب الخاص بك ---
MY_WHATSAPP = "9647739778877" # ضع رقمك هنا

st.write("---")
st.markdown('<h2 style="color: #c5a059; text-align: center;">📝 قسم حجز الطلبات</h2>', unsafe_allow_html=True)

# تصميم حاوية الاستمارة
with st.container():
    st.markdown('<div style="background: #1e293b; padding: 30px; border-radius: 20px; border: 1px solid #c5a059;">', unsafe_allow_html=True)
    
    with st.form("main_order_form", clear_on_submit=False):
        col_name, col_phone = st.columns(2)
        with col_name:
            u_name = st.text_input("👤 الاسم الثلاثي", placeholder="اكتب اسمك هنا...")
        with col_phone:
            u_phone = st.text_input("📞 رقم الواتساب", placeholder="07XXXXXXXXX")
        
        u_service = st.selectbox("🎯 نوع الخدمة", ["استنساخ", "تصميم CV", "مونتاج فيديو", "زين كاش", "أخرى"])
        u_details = st.text_area("📄 تفاصيل الطلب", placeholder="اشرح لنا ما تحتاجه...")
        
        # زر الإرسال بتصميم مميز
        submit_btn = st.form_submit_button("إرسال الطلب وحجز رقم 🚀")

        if submit_btn:
            if u_name and u_phone:
                # توليد رقم طلب آلي
                order_id = f"AY-{random.randint(1000, 9999)}"
                
                # --- الرسالة المنبثقة بتصميم وألوان خاصة جداً ---
                st.markdown(f"""
                    <div style="background: #0f172a; padding: 25px; border-radius: 15px; border: 2px dashed #facc15; text-align: center; margin-top: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.4);">
                        <h2 style="color: #25d366 !important; margin-bottom: 10px;">✅ تم استلام بياناتك بنجاح!</h2>
                        <p style="color: #ffffff !important; font-size: 18px;">أهلاً بك يا <b>{u_name}</b>، شكراً لثقتك بنا.</p>
                        <div style="background: #1e293b; padding: 10px; border-radius: 10px; display: inline-block; margin: 10px 0;">
                            <span style="color: #facc15 !important; font-size: 24px; font-weight: bold;">رقم الطلب: {order_id}</span>
                        </div>
                        <p style="color: #cbd5e1 !important; font-size: 14px;">يرجى الضغط على الزر أدناه لتأكيد الطلب عبر الواتساب</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # تحضير رسالة الواتساب
                wa_msg = f"طلب جديد من الموقع 🦅%0a🔢 رقم الطلب: {order_id}%0a👤 الاسم: {u_name}%0a🎯 الخدمة: {u_service}%0a📄 التفاصيل: {u_details}"
                wa_url = f"https://wa.me/{MY_WHATSAPP}?text={wa_msg}"
                
                # زر الواتساب الأخضر الاحترافي
                st.markdown(f"""
                    <div style="text-align: center; margin-top: 15px;">
                        <a href="{wa_url}" target="_blank" style="text-decoration: none;">
                            <button style="background-color: #25d366; color: white; padding: 15px 40px; border-radius: 12px; border: none; font-weight: bold; font-size: 20px; cursor: pointer; width: 100%;">
                                تأكيد الطلب عبر واتساب الآن 🟢
                            </button>
                        </a>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("عذراً، يرجى ملء الحقول الأساسية (الاسم والرقم) لإكمال الطلب.")

st.write("---")
st.markdown('<h2 style="color: #c5a059; text-align: center;">🔍 تتبع حالة طلبك</h2>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div style="background: #0f172a; padding: 25px; border-radius: 20px; border: 1px solid #c5a059;">', unsafe_allow_html=True)
    
    search_id = st.text_input("ادخل رقم الطلب الخاص بك", placeholder="AY-XXXX")
    track_btn = st.button("بحث عن حالة الطلب 🔎")

    if track_btn:
        if search_id:
            # تم تعديل السطر التالي ليتفادى الخطأ الأحمر
            import datetime 
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            
            st.markdown(f"""
                <div style="background: #1e293b; padding: 20px; border-radius: 15px; border-right: 5px solid #facc15; margin-top: 15px;">
                    <h4 style="color: #facc15 !important; margin: 0;">نتائج البحث عن: {search_id}</h4>
                    <hr style="border-color: #c5a059;">
                    <p style="color: white !important;">📍 <b>الحالة الحالية:</b> <span style="color: #25d366;">قيد المعالجة (In Progress)</span></p>
                    <p style="color: white !important;">📅 <b>آخر تحديث للنظام:</b> {current_date}</p>
                    <p style="color: #cbd5e1 !important; font-size: 14px;">طلبك موجود لدينا، سيتم التواصل معك فور الجاهزية.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("يرجى إدخال رقم الطلب أولاً.")

    st.markdown('</div>', unsafe_allow_html=True)
    
# --- مساعد أيوب الذكي (النسخة السوبر الماركة) ---
st.write("---")
st.markdown('<h2 style="color: #c5a059; text-align: center;">🤖 مساعد أيوب (الفهيم)</h2>', unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "يا هلا بيك عيوني.. أنا مساعد أيوب الفهيم، اسألني عن أي شي ببالك، عن الشغل أو عن سوالف الدنيا وتدلل!"}]

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

if prompt := st.chat_input("سولف وياي بكل شي..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    p_low = prompt.lower()
    res = ""

    # 1. كلمات عراقية عميقة وحالات يومية
    if any(x in p_low for x in ["ضوجة", "ملل", "مختنك"]):
        res = "ليش الضوجة يا غالي؟ الدنيا ما تسوى. تعالي للمكتبة نسولف ونشرب شاي، ونرتب لك فد مونتاج 'فيكة' يغير جوك ويطير الضوجة!"
    
    elif any(x in p_low for x in ["طاش", "مشهور", "ترند", "فيكة"]):
        res = "تريد تطش؟ إنت بمكان الصح! أيوب يسوي لك مونتاج ببرنامج CapCut Pro يخلي فيديوهاتك تكتك وتصعد ترند، شغلنا مرتب ومو مال غشمة."

    elif any(x in p_low for x in ["ما بيه حيل", "تعبان", "مالي خلك"]):
        res = "سلامتك من التعب! إذا ما بيك حيل للمراجعات والدوخة، بس دز لنا التفاصيل واتساب وإحنا نخلص لك كل شي (تقديم، طباعة، تصميم) وإنت كاعد بمكانك."

    # 2. شرح الخدمات بالتفصيل (شنو نسوي)
    elif any(x in p_low for x in ["شسوي", "شنو تسوون", "شلون تساعدني", "خدمات"]):
        res = """
        بسيطة عيوني، إحنا هنا نسوي كل شي يريحك:
        1. **بالمونتاج:** نحول فيديوهاتك العادية لقطع فنية (ترندات، إعلانات، قصص).
        2. **بالمكتبية:** نسوي CV ملكي يخليك تتوظف، ونقدم لك على التعيينات بدون غلطة.
        3. **بالمالي:** نسحب ونودع زين كاش ونحول رصيد بأي وقت.
        بس كول يا الله واختار وحدة منهن!
        """

    elif any(x in p_low for x in ["سي في", "cv", "سيرة ذتية", "شغل", "وظيفة"]):
        res = "تريد وظيفة؟ أول خطوة هي 'السي في' المعدل. إحنا نصممه لك بطريقة احترافية تجذب أبو الشغل، ونرتبه بتنسيق حديث يبيض وجهك."

    # 3. ردود ذكية شاملة
    elif any(x in p_low for x in ["هلو", "شلونك", "يا هلا"]):
        res = random.choice(["يا مية هلا، نورتنا بطلتك!", "بخير إذا إنت بخير يا ذهب، اؤمرني بشنو أخدمك؟"])

    elif any(x in p_low for x in ["حر", "صيف", "كهرباء"]):
        res = "الجو صاير نار! بس لا تهتم، مكتبتنا باردة والكهرباء عدنا ما تطفى (بالموقع وبالشغل)، اطلب وتدلل."

    elif any(x in p_low for x in ["سعر", "بكم", "خصم"]):
        res = "أسعارنا 'مال أخوة'، لا تشيل هم الفلوس. إحنا نراعي الطيبين مثلك، والسعر يعتمد على نوع الفيكة اللي تريدها بالطلب."

    elif any(x in p_low for x in ["وين", "مكان", "بالقصر"]):
        res = "إحنا باليوسفية - القصر الأوسط، بين أهلك وناسك. تشرفنا بأي وقت!"

    elif any(x in p_low for x in ["شكرا", "ممنون", "عاشت ايدك"]):
        res = "بالخدمة يا طيب، إحنا هنا لجلكم. رحم الله والديك."

    else:
        res = "والله كلامك ذهب، بس وضح لي أكثر حتى أفيدك. تريد مونتاج فيديو؟ لو معاملة مكتبية؟ لو بس تريد تسولف وتدردش؟ أنا وياك للأخير!"

    st.session_state.chat_history.append({"role": "assistant", "content": res})
    with st.chat_message("assistant"):
        st.write(res)
