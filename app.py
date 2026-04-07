import streamlit as st

# 1. إعدادات الصفحة الأساسية واللوغو الخاص بك
LOGO_URL = "https://raw.githubusercontent.com/ayubsmartiq-create/ayub-smart-app/main/Ayub-Logo.png"
st.set_page_config(page_title="مكتبة أيوب الذكية", page_icon=LOGO_URL, layout="wide")

# 2. هندسة الألوان (CSS) - لجعل الموقع فخم والكتابة واضحة
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* جعل كل النصوص العامة بيضاء تماماً */
    html, body, [class*="css"], .stApp, p, h1, h2, h3, h4, span, label, .stMarkdown {{
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important; 
        text-align: right !important;
        color: #ffffff !important; /* لون النص أبيض */
    }}
    
    /* خلفية الموقع زرقاء غامقة ملكية */
    .stApp {{
        background-color: #0f172a !important;
    }}
    
    /* تصميم المربعات (Input Boxes): خلفية غامقة وكتابة بيضاء واضحة */
    input, textarea, select, div[data-baseweb="select"] > div {{
        background-color: #1e293b !important; /* لون المربع غامق */
        color: #ffffff !important; /* الكتابة داخل المربع بيضاء */
        border: 2px solid #facc15 !important; /* إطار ذهبي مميز */
        border-radius: 10px !important;
    }}

    /* حل مشكلة اختفاء النص عند الكتابة داخل المربعات */
    input {{ color: white !important; -webkit-text-fill-color: white !important; }}
    textarea {{ color: white !important; -webkit-text-fill-color: white !important; }}

    /* تصميم رأس الصفحة (الهيدر) */
    .header-box {{
        background: linear-gradient(135deg, #1e40af, #1e3a8a);
        padding: 30px; border-radius: 20px; border-bottom: 5px solid #facc15;
        text-align: center; margin-bottom: 25px;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة الرئيسي (الهيدر)
st.markdown('<div class="header-box"><h1>🦅 مكتبة أيوب الذكية </h1><p>دقة، سرعة، واحترافية رقمية من قلب اليوسفية</p></div>', unsafe_allow_html=True)

st.write("---")
st.info("أهلاً بك يا أيوب! تم تأسيس الهيكل بنجاح. جرب الآن إذا كانت الألوان مريحة للعين.")
import random
import datetime
import requests

# --- إعدادات المبرمج أيوب ---
MY_WHATSAPP = "9647739778877"  # 👈 أيوب: حط رقمك الحقيقي هنا (بدون أصفار بالبداية)
FORMSPREE_URL = "https://formspree.io/f/xvzvdjzq" # رابط الإيميل مالتك

# 1. عنوان الاستمارة
st.markdown('<h3 style="color: #facc15; text-align: right;">📑 تقديم طلب خدمة جديد</h3>', unsafe_allow_html=True)

# 2. بناء الاستمارة
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
            
            # إرسال البيانات للإيميل (تلقائياً عبر Formspree)
            payload = {
                "رقم الطلب": order_id,
                "اسم الزبون": name,
                "رقم الهاتف": phone,
                "نوع الخدمة": service,
                "التفاصيل": details,
                "وقت الطلب": now
            }
            # محاولة إرسال البيانات
            try:
                requests.post(FORMSPREE_URL, data=payload)
                
                # إظهار رسالة النجاح للزبون
                st.success(f"عاشت إيدك يا {name}! استلمنا بياناتك برقم طلب: {order_id}")
                
                # تجهيز رابط الواتساب لتأكيد الطلب وإرسال الصور
                wa_msg = f"مرحباً أيوب، قدمت طلب جديد ورقم طلبي هو ({order_id}). هذي الصور والمستمسكات:"
                wa_url = f"https://wa.me/{MY_WHATSAPP}?text={wa_msg}"
                
                # تصميم زر الواتساب الأخضر
                st.markdown(f"""
                    <div style="background: #1e293b; padding: 20px; border-radius: 15px; border: 2px solid #25d366; margin-top: 15px; text-align: center;">
                        <h4 style="color: #facc15;">بقت خطوة وحدة يا بطل! 📸</h4>
                        <p style="color: white;">اضغط على الزر أدناه حتى ترسل صور المستمسكات أو المرفقات على الواتساب مالتنا وتأكد الحجز:</p>
                        <a href="{wa_url}" target="_blank" style="display: block; background-color: #25d366; color: white !important; padding: 12px; border-radius: 10px; text-decoration: none; font-weight: bold; border: 1px solid white;">
                            تأكيد الطلب وإرسال المرفقات (WhatsApp) ✅
                        </a>
                    </div>
                """, unsafe_allow_html=True)
            except:
                st.error("عذراً، حدث خطأ في الاتصال. تأكد من الإنترنت وحاول مجدداً.")
        else:
            st.warning("عيني أيوب، ذكر الزبون يملأ الاسم والرقم ضروري!")
# --- 1. فاصل جمالي ---
st.write("---")

# --- 2. لوحة الخدمات والأسعار (لزيادة الثقة) ---
st.markdown("""
    <div style="background: #1e293b; padding: 20px; border-radius: 15px; border: 1px dashed #facc15; margin-bottom: 30px;">
        <h3 style="color: #facc15; text-align: center; margin-bottom: 15px;">💰 قائمة الخدمات المتوفرة</h3>
        <table style="width: 100%; color: white; text-align: right; border-collapse: collapse;">
            <tr style="border-bottom: 1px solid #334155;">
                <td style="padding: 10px;">📄 التقديم على العقود والتعيينات</td>
                <td style="padding: 10px; color: #facc15;">تبدأ من 5,000 د.ع</td>
            </tr>
            <tr style="border-bottom: 1px solid #334155;">
                <td style="padding: 10px;">🎬 مونتاج فيديو احترافي (CapCut)</td>
                <td style="padding: 10px; color: #facc15;">تبدأ من 15,000 د.ع</td>
            </tr>
            <tr>
                <td style="padding: 10px;">🤖 تصميم وبرمجة بوتات ذكية</td>
                <td style="padding: 10px; color: #facc15;">حسب الاتفاق</td>
            </tr>
        </table>
    </div>
""", unsafe_allow_html=True)

# --- 3. قسم تتبع حالة المعاملة ---
st.markdown('<h3 style="color: #facc15; text-align: right;">🔍 تتبع حالة معاملتك</h3>', unsafe_allow_html=True)

with st.container():
    track_phone = st.text_input("أدخل رقم الهاتف الذي قدمت به الطلب:")
    if st.button("فحص حالة الطلب 🔎"):
        if track_phone:
            # رسالة طمأنة للزبون (تظهر دائماً بشكل مؤقت حتى نربطها بقاعدة بيانات مستقبلاً)
            st.info(f"الطلب المرتبط بالرقم ({track_phone}) قيد التدقيق حالياً. سيقوم أيوب بالتواصل معك فور إكمال المعاملة.")
        else:
            st.warning("يرجى إدخال رقم الهاتف أولاً.")

# --- 4. تذييل الصفحة (الفوتر) ---
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #334155;">
        <p style="color: #94a3b8;">جميع الحقوق محفوظة لمكتبة أيوب الذكية © {datetime.datetime.now().year}</p>
        <p style="color: #facc15; font-size: 12px;">اليوسفية - بغداد - العراق</p>
    </div>
""", unsafe_allow_html=True)
# --- إضافة مسافة جمالية كبيرة قبل المساعد ---
st.markdown("<br><br><br>", unsafe_allow_html=True)

# --- تصميم حاوية المساعد الذكي ---
st.markdown("""
    <div style="background: linear-gradient(135deg, #1e293b, #0f172a); padding: 25px; border-radius: 20px; border: 2px solid #facc15; box-shadow: 0px 10px 30px rgba(0,0,0,0.5);">
        <h2 style="color: #facc15; text-align: center; margin-bottom: 10px;">🤖 مستشارك الذكي (أبو الغيرة)</h2>
        <p style="color: #94a3b8; text-align: center; font-size: 14px;">خادمكم موجود 24 ساعة.. اسألني عن أي شيء ببالك!</p>
    </div>
    <br>
""", unsafe_allow_html=True)

# 1. تهيئة الذاكرة والترحيب الحار
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "يا مية هلا بجيتك! نورت مكتبة أخوك أيوب هاني. أنا مساعدك الذكي، اعتبرني أخوك الصغير وآمرني.. تريد تقديم، مونتاج، لو بس جاي تسلم؟ العين إلك والراس إلك! 🦅✨"}
    ]

# 2. عرض المحادثة بتنسيق أنيق
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f'<div style="text-align: right; font-size: 16px; line-height: 1.6;">{msg["content"]}</div>', unsafe_allow_html=True)

# 3. معالجة الأسئلة بذكاء "ابن ولاية"
if user_input := st.chat_input("اكتب سؤالك هنا.. (مثلاً: شوكت تخلص معاملتي؟)"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(f'<div style="text-align: right;">{user_input}</div>', unsafe_allow_html=True)

    # --- منطق الردود الواسعة والممتعة ---
    u = user_input.lower()
    response = ""

    if any(word in u for word in ["شلونك", "اخبارك", "يا هلا", "هلو", "مرحبا"]):
        response = "بخير ونعمة إذا أنت بخير! نورتنا يا طيب. أنا هنا حتى أسهل عليك أمورك، كولي بشنو أقدر أخدمك اليوم؟"
    
    elif any(word in u for word in ["عنوان", "مكان", "وين"]):
        response = "تدلل عيوني! إحنا موجودين بـ **بغداد - اليوسفية - القصر الأوسط**. بس تدري، إحنا شغلنا كله 'أونلاين' وبسرعة البرق، يعني وأنت كاعد ببيتك تشرب شاي، أيوب يخلص لك معاملتك ويدزها لك واتساب!"
    
    elif any(word in u for word in ["تقديم", "عقد", "تعيين", "استمارة"]):
        response = "التقديم عدنا 'غير شكل'! أيوب يشيك لك كل المعلومات حتى ما ترفضك الوزارة. نحتاج منك (الجنسية، بطاقة السكن، وصورة للشهادة). املأ الاستمارة اللي فوك، ووديك للواتساب حتى تدز الصور، والباقي علينا.. نام رغد!"
    
    elif any(word in u for word in ["مونتاج", "فيديو", "تيك توك", "كاب كات"]):
        response = "أوه! جيت على الاختصاص. أيوب ملك الـ CapCut بالمنطقة. يسوي لك مونتاج يخلي الفيديو مالتك 'طاير' ترند. انتقالات خرافية، تعديل ألوان، وكتابة سيناريو. تريد فيديو لمحلك لو شخصي؟"
    
    elif any(word in u for word in ["سعر", "فلوس", "بيش", "تكلفة"]):
        response = "لا تشيل هم الفلوس، إحنا ولد منطقة وحدة وما نختلف. التقديم يبدأ من 5 آلاف، والمونتاج حسب الشغل. أهم شي تطلع راضي وتدعي لنا بالخير!"
    
    elif any(word in u for word in ["وقت", "شوكت", "تأخير"]):
        response = "أيوب ما يحب التأخير، شعاره 'السرعة والدقة'. أغلب المعاملات تخلص بنفس اليوم، وإذا بيها زخم، فما تعبر الـ 24 ساعة. إنت بس انطينا رقم طلبك بالواتساب ونبشرك!"
    
    elif any(word in u for word in ["ذكاء", "بوت", "برمجة"]):
        response = "إي نعم! إحنا مو بس مكتبة، إحنا مركز تقني. نصمم لك بوتات ذكية مثل حلاتي تخدم شغلك وتجاوب زبائنك وأنت نايم. تريد نسوي لك واحد؟"

    elif any(word in u for word in ["صورة", "رفع", "مستمسك"]):
        response = "عيني، الصور ما ترفعهن هنا بالموقع للخصوصية. من تدوس 'إرسال' بالاستمارة فوك، راح يطلع لك زر أخضر يوديك للواتساب، هناك دز الصور لأيوب بأمان."

    elif any(word in u for word in ["شكرا", "ممنون", "خوش"]):
        response = "بخدمتك يا غالي! هذا واجبنا. إذا احتاجيت أي شي ثاني، أنا موجود.. لا تتردد!"

    else:
        response = "والله يا طيب، هذا السؤال يحتاج له 'صفنة' من أيوب نفسه. ياريت تضغط على زر الواتساب فوك وتسأله مباشرة، هو يجاوبك جواب شافي وكافي!"

    # عرض الرد مع لمسة ذهبية
    with st.chat_message("assistant"):
        st.markdown(f'<div style="text-align: right; color: #facc15; font-weight: bold; border-right: 3px solid #facc15; padding-right: 10px;">{response}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": response})

# --- الفوتر المحدث بالعنوان الدقيق ---
st.markdown(f"""
    <br><br>
    <div style="text-align: center; padding: 30px; background: #0f172a; border-top: 2px solid #1e40af;">
        <h4 style="color: #facc15;">📍 مكتبة أيوب الذكية</h4>
        <p style="color: white; font-size: 14px;">العراق - بغداد - اليوسفية - القصر الأوسط</p>
        <p style="color: #64748b; font-size: 12px;">© {datetime.datetime.now().year} | تطوير وإدارة: أيوب هاني</p>
        <div style="margin-top: 10px;">
            <span style="background: #1e3a8a; color: white; padding: 5px 15px; border-radius: 20px; font-size: 10px;">خدمة متاحة 24/7 أونلاين</span>
        </div>
    </div>
""", unsafe_allow_html=True)
