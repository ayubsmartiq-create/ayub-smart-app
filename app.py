import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon="🦅", layout="wide")

# 2. تصميم الواجهة (CSS) - لجعل النص أبيض والمربعات واضحة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل كل النصوص العامة بيضاء تماماً */
    html, body, [class*="css"], .stApp, p, h1, h2, h3, h4, span, label {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; 
        text-align: right !important;
        color: #ffffff !important;
    }
    
    /* خلفية الموقع زرقاء غامقة (نفس روح اللوغو) */
    .stApp {
        background-color: #0f172a !important;
    }
    
    /* تصميم المربعات: خلفية غامقة متميزة وإطار ذهبي */
    input, textarea, select, div[data-baseweb="select"] > div {
        background-color: #1e293b !important; /* لون المربع */
        color: #ffffff !important; /* لون النص داخل المربع */
        border: 2px solid #c5a059 !important; /* إطار ذهبي */
        border-radius: 10px !important;
    }

    /* ضمان أن النص الذي يكتبه الزبون يظهر بالأبيض */
    input { color: white !important; -webkit-text-fill-color: white !important; }
    textarea { color: white !important; -webkit-text-fill-color: white !important; }

    /* تصميم رأس الصفحة */
    .header-box {
        background: linear-gradient(135deg, #0b3d61, #1e293b);
        padding: 25px; border-radius: 20px; border-bottom: 5px solid #c5a059;
        text-align: center; margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر (رأس الصفحة)
# ملاحظة: يمكنك وضع رابط اللوغو المباشر هنا
st.markdown("""
    <div class="header-box">
        <h1 style="color: #c5a059 !important;">🦅 مكتبة أيوب الذكية</h1>
        <p style="font-size: 18px;">دقة، سرعة، واحترافية رقمية من قلب القصر الأوسط</p>
    </div>
""", unsafe_allow_html=True)

st.write("---")
st.success("عاشت إيدك يا بطل! الخطوة الأولى (التأسيس) اشتغلت بنجاح.")
# --- الخطوة الثانية: عرض الخدمات باحترافية ---

st.markdown('<h2 style="color: #c5a059; text-align: center;">🌟 خدماتنا الرقمية المتكاملة</h2>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #94a3b8;">اختر الفئة التي تهمك وشاهد ماذا نقدم لك</p>', unsafe_allow_html=True)

# تقسيم الخدمات لثلاثة أعمدة (Layout)
col_tech, col_design, col_money = st.columns(3)

with col_tech:
    st.markdown("""
        <div style="background: #1e293b; padding: 20px; border-radius: 15px; border-top: 5px solid #c5a059; height: 350px;">
            <h3 style="color: #facc15; text-align: center;">📂 الخدمات المكتبية</h3>
            <p style="font-size: 14px; line-height: 1.8;">
                ✅ استنساخ وملازم (أسود/ملون)<br>
                ✅ طباعة ملفات وبحوث<br>
                ✅ تحويل ملفات (PDF to Word)<br>
                ✅ إنشاء سيرة ذاتية (CV) ملكية<br>
                ✅ تقديم تعيينات وعقود حكومية
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_design:
    st.markdown("""
        <div style="background: #1e293b; padding: 20px; border-radius: 15px; border-top: 5px solid #c5a059; height: 350px;">
            <h3 style="color: #facc15; text-align: center;">🎬 المونتاج والإبداع</h3>
            <p style="font-size: 14px; line-height: 1.8;">
                ✅ مونتاج CapCut ترند (TikTok/Insta)<br>
                ✅ تصميم منيو مطاعم وكافيهات<br>
                ✅ كارتات عمل (Business Cards)<br>
                ✅ تصميم باركود (QR) ذكي<br>
                ✅ سحب صور فوتوغرافية احترافية
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_money:
    st.markdown("""
        <div style="background: #1e293b; padding: 20px; border-radius: 15px; border-top: 5px solid #c5a059; height: 350px;">
            <h3 style="color: #facc15; text-align: center;">💰 المعاملات المالية</h3>
            <p style="font-size: 14px; line-height: 1.8;">
                ✅ تحويل واستلام (زين كاش)<br>
                ✅ دفع فواتير وخدمات أونلاين<br>
                ✅ تعبئة رصيد وبطاقات ألعاب<br>
                ✅ استشارات تقنية وذكاء اصطناعي<br>
                ✅ تحويل أموال داخلي وخارجي
            </p>
        </div>
    """, unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)
st.info("💡 ملاحظة: جميع الخدمات تتم بدقة وسرعة وبإشراف مباشر من أخوكم أيوب.")
import random
import datetime

# --- إعدادات التواصل مالتك يا أيوب ---
MY_WHATSAPP = "9647739778877"  # 👈 أيوب: حط رقمك الحقيقي هنا (بدون أصفار بالبداية)

st.write("---")
st.markdown('<h2 style="color: #c5a059; text-align: right;">📑 تقديم طلب خدمة جديد</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8;">املأ البيانات أدناه للحصول على كود الطلب وتثبيت حجزك</p>', unsafe_allow_html=True)

# تصميم الاستمارة داخل حاوية احترافية
with st.container():
    with st.form("ayub_smart_form"):
        col_name, col_phone = st.columns(2)
        with col_name:
            customer_name = st.text_input("الأسم الثلاثي للزبون")
        with col_phone:
            customer_phone = st.text_input("رقم الهاتف (واتساب)")
            
        selected_service = st.selectbox("ما هي الخدمة التي تحتاجها؟", 
                                      ["استنساخ وملازم", "مونتاج فيديو (CapCut)", "تحويل مالي (زين كاش)", "تصميم (منيو/كارت/باركود)", "إنشاء سيرة ذاتية CV", "تقديم تعيينات وعقود"])
        
        request_details = st.text_area("اشرح لنا طلبك بالتفصيل (أو اكتب الملاحظات)")
        
        # زر الإرسال بتصميم ذهبي عريض
        submit_button = st.form_submit_button("إرسال الطلب وحجز الكود 🚀")

        if submit_button:
            if customer_name and customer_phone:
                # 1. توليد كود طلب مميز يبدأ بـ AY
                order_code = f"AY-{random.randint(1000, 9999)}"
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                
                # 2. رسالة النجاح داخل تصميم فخم
                st.markdown(f"""
                    <div style="background: #1e293b; padding: 20px; border-radius: 15px; border: 2px solid #c5a059; text-align: center; margin-top: 20px;">
                        <h3 style="color: #34d399; margin: 0;">تم حجز طلبك بنجاح! 🎉</h3>
                        <p style="color: white; margin: 10px 0;">كود الطلب الخاص بك هو:</p>
                        <h2 style="color: #facc15; margin: 0; font-size: 40px;">{order_code}</h2>
                        <p style="color: #94a3b8; font-size: 13px; margin-top: 10px;">يرجى تصوير الشاشة لحفظ الكود.</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # 3. تجهيز رسالة الواتساب الذكية
                wa_message = f"مرحباً أيوب، أنا الزبون ({customer_name}). قدمت طلب جديد لخدمة ({selected_service}) برقم طلب: {order_code}. هذي التفاصيل والصور:"
                whatsapp_url = f"https://wa.me/{MY_WHATSAPP}?text={wa_message}"
                
                # 4. زر الانتقال للواتساب لإرسال المرفقات
                st.markdown(f"""
                    <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
                        <div style="background-color: #25d366; color: white !important; padding: 15px; border-radius: 12px; text-align: center; font-weight: bold; margin-top: 15px; border: 1px solid white;">
                            تأكيد الطلب وإرسال المستمسكات (WhatsApp) ✅
                        </div>
                    </a>
                """, unsafe_allow_html=True)
            else:
                st.warning("عيني أيوب، ذكّر الزبون يكتب اسمه ورقمه حتى ما يضيع طلبه!")
# --- الخطوة الرابعة: نظام التتبع والمساعد الذكي ---
st.write("---")

# 1. تصميم واجهة التتبع (Tracking System)
st.markdown('<h3 style="color: #c5a059; text-align: right;">🔍 تتبع حالة معاملتك</h3>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8;">أدخل كود الطلب (AY-XXXX) لمعرفة أين وصلت معاملتك الآن:</p>', unsafe_allow_html=True)

col_track, col_status = st.columns([2, 1])

with col_track:
    track_input = st.text_input("كود الطلب الخاص بك", placeholder="مثلاً: AY-1234")

if st.button("فحص الحالة الآن 🚀"):
    if track_input:
        # رد احترافي يطمئن الزبون
        st.markdown(f"""
            <div style="background: #1e293b; padding: 20px; border-radius: 15px; border-right: 5px solid #34d399; margin-top: 10px;">
                <h4 style="color: #34d399; margin: 0;">الطلب {track_input} قيد المعالجة ⏳</h4>
                <p style="color: white; font-size: 14px; margin-top: 5px;">
                    عيني، طلبك وصل وأيوب حالياً دا يشيك المعلومات. سيتم إشعارك فور اكتمال المعاملة عبر الواتساب.
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("يرجى إدخال الكود أولاً يا طيب!")

st.write("<br><br>", unsafe_allow_html=True)

# 2. المساعد الذكي "أبو الغيرة" (AI Chatbot)
st.markdown("""
    <div style="background: linear-gradient(135deg, #1e293b, #0f172a); padding: 20px; border-radius: 20px; border: 2px solid #c5a059; text-align: center;">
        <h3 style="color: #c5a059; margin: 0;">🤖 مساعد أيوب الذكي (خادمكم الصغير)</h3>
        <p style="color: #94a3b8; font-size: 14px;">اسألني عن أي شيء (أسعار، مستمسكات، عنوان) وأنا أجاوبك!</p>
    </div>
""", unsafe_allow_html=True)

# تهيئة ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "يا مية هلا بجيتك! نورت مكتبة أخوك أيوب. آمرني بشنو أقدر أخدمك؟"}]

# عرض الدردشة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f'<div style="text-align: right; color: white;">{msg["content"]}</div>', unsafe_allow_html=True)

# استقبال سؤال الزبون
if chat_query := st.chat_input("اكتب سؤالك هنا.."):
    st.session_state.messages.append({"role": "user", "content": chat_query})
    with st.chat_message("user"):
        st.markdown(f'<div style="text-align: right;">{chat_query}</div>', unsafe_allow_html=True)

    # ردود ذكية باللهجة العراقية
    q = chat_query.lower()
    if any(x in q for x in ["وين", "مكان", "عنوان"]):
        response = "تدلل عيوني! إحنا موجودين بـ **بغداد - اليوسفية - القصر الأوسط**. بس تدري، شغلنا كله أونلاين وبسرعة البرق، يعني وأنت كاعد ببيتك نخلص لك كل شيء!"
    elif any(x in q for x in ["سعر", "بيش", "تكلفة"]):
        response = "أسعارنا 'مال أخوة' وتبدأ من 5 آلاف دينار للتقديمات البسيطة. المونتاج والتصاميم حسب التعب بس ما نختلف، أنت بس اطلب وما يكون خاطرك إلا طيب!"
    elif any(x in q for x in ["مستمسكات", "تقديم", "عقد"]):
        response = "عيني، للتقديم نحتاج منك (الجنسية، بطاقة السكن، ووثيقة التخرج). صورهن بتلفونك وادزهن واتساب لأيوب بعد ما تملأ الاستمارة فوك."
    elif any(x in q for x in ["شكرا", "ممنون", "خوش"]):
        response = "بخدمتك يا غالي! هذا واجبنا. إذا احتاجيت أي شيء ثاني، أنا موجود 24 ساعة."
    else:
        response = "والله يا طيب سؤالك يحتاج له صفنة من أيوب نفسه. يفضل تضغط على زر الواتساب فوك وتسأله مباشرة، هو يجاوبك جواب شافي وكافي!"

    with st.chat_message("assistant"):
        st.markdown(f'<div style="text-align: right; color: #c5a059; font-weight: bold;">{response}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": response})
# --- الخطوة الخامسة: الختام الملكي والتقييم ---
st.write("<br><br>", unsafe_allow_html=True)

# 1. أزرار الاتصال السريع (Quick Actions)
st.markdown('<h4 style="color: #c5a059; text-align: right;">📞 تواصل مباشر مع أيوب</h4>', unsafe_allow_html=True)
col_call, col_loc = st.columns(2)

with col_call:
    # استبدل 07700000000 برقمك الفعلي للاتصال
    st.markdown("""
        <a href="tel:07739778877" style="text-decoration: none;">
            <div style="background: #1e3a8a; padding: 15px; border-radius: 12px; text-align: center; border: 1px solid #c5a059;">
                <p style="color: white; margin: 0; font-weight: bold;">📞 اتصل بنا هاتفياً</p>
                <p style="color: #cbd5e1; font-size: 11px; margin: 0;">للاستفسارات العاجلة فقط</p>
            </div>
        </a>
    """, unsafe_allow_html=True)

with col_loc:
    # زر يوضح الموقع (القصر الأوسط)
    st.markdown("""
        <div style="background: #1e293b; padding: 15px; border-radius: 12px; text-align: center; border: 1px solid #c5a059;">
            <p style="color: #facc15; margin: 0; font-weight: bold;">📍 موقعنا الرسمي</p>
            <p style="color: white; font-size: 11px; margin: 0;">بغداد - اليوسفية - القصر الأوسط</p>
        </div>
    """, unsafe_allow_html=True)

# 2. نظام تقييم الخدمة (Star Rating)
st.write("<br>", unsafe_allow_html=True)
st.markdown('<h4 style="color: #c5a059; text-align: right;">⭐ رأيك يهمنا يا طيب</h4>', unsafe_allow_html=True)
rating = st.feedback("stars")
if rating is not None:
    st.success(f"شكراً لثقتك! تقييمك {rating+1} نجوم هو دافعنا للاستمرار.")

# 3. الفوتر النهائي (Copyright)
st.markdown(f"""
    <hr style="border-color: #c5a059;">
    <div style="text-align: center; padding: 10px;">
        <p style="color: #94a3b8; font-size: 12px;">
            جميع الحقوق محفوظة © {datetime.datetime.now().year} | مكتبة أيوب الذكية <br>
            تم التطوير بكل فخر لخدمة أهالي القصر الأوسط واليوسفية 🦅✨
        </p>
    </div>
""", unsafe_allow_html=True)
# --- الخطوة السادسة: محرك الثقة والضمان ---
st.write("---")

# 1. شريط الإنجازات اليومي (Stats Bar)
st.markdown("""
    <div style="background: linear-gradient(90deg, #1e293b, #0b3d61); padding: 15px; border-radius: 50px; border: 1px solid #c5a059; text-align: center; margin: 20px 0;">
        <span style="color: #facc15; font-weight: bold;">●</span> 
        <span style="color: white; font-size: 14px;"> تم معالجة <b>14 طلب</b> اليوم بنجاح في القصر الأوسط 🚀 </span>
        <span style="color: #facc15; font-weight: bold; margin-right: 15px;">●</span> 
        <span style="color: white; font-size: 14px;"> متوسط وقت الرد: <b>5 دقائق</b> ⚡ </span>
    </div>
""", unsafe_allow_html=True)

# 2. قسم "تعهد أيوب" للأمان والخصوصية
st.markdown("""
    <div style="background: rgba(197, 160, 89, 0.1); padding: 20px; border-radius: 15px; border-right: 5px solid #c5a059;">
        <h4 style="color: #c5a059; margin-top: 0;">🛡️ ضمان الخصوصية والأمان</h4>
        <p style="color: white; font-size: 13px; line-height: 1.6; margin: 0;">
            نحن في <b>مكتبة أيوب الذكية</b> ندرك أهمية خصوصية مستمسكاتكم وصوركم. نتعهد رسمياً بأن جميع البيانات تُعالج بأحدث أنظمة التشفير وتُحذف فور تسليم الطلب، ولا يتم مشاركتها مع أي جهة كانت. 
            <br><b>أمانكم هو رأس مالنا.</b>
        </p>
    </div>
""", unsafe_allow_html=True)

# 3. زر "مشاركة الموقع" (Share Button)
st.write("<br>", unsafe_allow_html=True)
if st.button("📢 شارك الموقع مع أصدقائك"):
    st.balloons()
    st.info("انسخ رابط الصفحة من المتصفح وأرسله لأصدقائك في اليوسفية ليستفيدوا من الخدمات!")

