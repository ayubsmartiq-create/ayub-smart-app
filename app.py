import streamlit as st
import pandas as pd
import os
import datetime
import random


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
                 # --- بداية الكود المصلح بدقة ---
        order_id = f"AY-{random.randint(1000, 9999)}"
        
        # تجهيز البيانات للحفظ (لاحظ مكان الفواصل في نهاية السطر)
        new_row = {
            "التاريخ": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")],
            "رقم الطلب": [order_id],
            "الاسم": [u_name],
            "الهاتف": [u_phone],
            "الخدمة": [u_service],
            "الحالة": ["قيد الانتظار"]
        }
        df_new = pd.DataFrame(new_row)

        # حفظ في ملف السجل
        file_db = "orders_database.csv"
        if not os.path.isfile(file_db):
            df_new.to_csv(file_db, index=False, encoding='utf-8-sig')
        else:
            df_new.to_csv(file_db, mode='a', header=False, index=False, encoding='utf-8-sig')

        # رسالة النجاح المنبثقة
        st.markdown(f"""
            <div style="background: #1e293b; padding: 20px; border-radius: 15px; border-right: 5px solid #c5a059; margin-bottom: 20px; text-align: right;">
                <h2 style="color: #25d366;">تم تسجيل طلبك! ✅</h2>
                <p style="color: #ffffff;">رقم التتبع: <span style="color: #facc15; font-weight: bold;">{order_id}</span></p>
                <p style="color: #cbd5e1; font-size: 14px;">اضغط على الزر أدناه لتأكيد الطلب</p>
            </div>
        """, unsafe_allow_html=True)

                # زر الواتساب (تأكد أن هذا الكود يوضع مرة واحدة فقط)
        wa_msg = f"هلا أيوب، أنا الزبون {u_name}، سجلت طلب بالموقع برقم: {order_id}"
        wa_url = f"https://wa.me/{MY_WHATSAPP}?text={wa_msg}"
        
        st.markdown(f"""
            <div style="text-align: center;">
                <a href="{wa_url}" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #25d366; color: white; padding: 15px 30px; border-radius: 10px; border: none; font-size: 18px; font-weight: bold; cursor: pointer; width: 100%;">
                        تأكيد الطلب عبر واتساب الآن
                    </button>
                </a>
            </div>
                """, unsafe_allow_html=True)
    
        else:
        st.error("يا طيب، لازم تملأ الاسم والرقم حتى نكدر نخدمك!")

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
    
# --- مساعد أيوب الذكي (نسخة الـ VIP الماركة) ---
st.write("---")
st.markdown('<h2 style="color: #c5a059; text-align: center;">🤖 مساعد أيوب الفهيم (خادمكم)</h2>', unsafe_allow_html=True)

# 1. تهيئة الذاكرة
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "يا هلا وكل الهلا بيك بمكتبة أخوك أيوب.. سولف عيوني، أنا هنا حتى أخدمك وأشيل عنك التعب. بشنو أگدر أفيدك اليوم؟"}]

# 2. عرض المحادثة
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

# 3. صندوق المحادثة الاحترافي
if prompt := st.chat_input("اكتب أي شي ببالك (شغل، سوالف، استفسار)..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # تنظيف النص لضمان الفهم الصحيح
    p_low = prompt.strip().lower()
    res = ""

    # --- القاموس الذكي للمساعد (أولوية الفحص) ---

    # أ. الترحيب والمجاملات
    if any(x in p_low for x in ["هلو", "شلونك", "يا هلا", "سلام", "صباح", "مساء", "شلون الصحة", "شكو ماكو"]):
        res = random.choice([
            "يا مية هلا بالطيب، نورت مكتبتنا بطلتك الغالية. أنا بخير ما طولك بخير!",
            "هلا بيك عيوني، نورتنا وتشرفنا بيك. اؤمرني بشنو أقدر أخدمك؟",
            "صافية دافية يا ذهب.. إحنا بخدمة الطيبين مثلك، شمحتاج وتدلل؟"
        ])

    # ب. يوميات العراق (الحر، الكهرباء، الحالة)
    elif any(x in p_low for x in ["حر", "صيف", "كهرباء", "طفت", "حارة", "تموع", "الوضع"]):
        res = "والله يا خوي الجو يموع الصخر والكهرباء تعبانة مثل ما تعرف.. بس إحنا صامدون والشغل يخلص بوقته لو تطفى الدنيا!"

    # ج. المونتاج والفيكات (لعبتك يا أيوب)
    elif any(x in p_low for x in ["مونتاج", "فيديو", "تكتك", "طاش", "ترند", "فيكة", "تصميم", "كاب كات", "capcut"]):
        res = "بالمونتاج لعبتنا! أيوب يسويلك فيديوهات 'فيكة' تصعدك ترند وتطشك طشة معدلة. نستخدم CapCut Pro وبلمسات عالمية، بس دز الفيديو وشوف الفرق!"

    # د. المكتبية والتعيينات (السي في)
    elif any(x in p_low for x in ["سي في", "cv", "شغل", "وظيفة", "تقديم", "تعيين", "استنساخ", "طباعة", "PDF"]):
        res = "تريد تتوظف وتخلص من الكعدة؟ إحنا نصمم لك 'سي في' ملكي يخلي المدير يقبلك فوراً. ونقدم لك على التعيينات بدون أي غلطة بالبيانات. اؤمر وتدلل!"

    # هـ. المالية وزين كاش (الفلوس)
    elif any(x in p_low for x in ["زين كاش", "فلوس", "سحب", "ايداع", "رصيد", "تحويل", "شحن"]):
        res = "خدماتنا المالية متوفرة بأي وقت. سحب وإيداع زين كاش، تحويل أموال، وشحن ألعاب ورصيد. مكتبتنا هي محفظتك الآمنة بالقصر الأوسط."

    # و. الأسعار والمكاسر (البيش)
    elif any(x in p_low for x in ["بيش", "سعر", "بكم", "خصم", "غالي", "رخيص", "ببلاش"]):
        res = "أسعارنا 'مال أخوة' وتناسب الكل. لا تشيل هم المادة، إحنا نراعي الطيبين والبركة بالقليل.. المهم تطلع راضي وممنون."

    # ز. المكان والجغرافيا (وينكم)
    elif any(x in p_low for x in ["وين", "مكان", "عنوان", "قصر", "يوسفية"]):
        res = "إحنا باليوسفية، منطقة القصر الأوسط. تعال وشرفنا، ومكاننا معروف وما يتيه، أهل المنطقة كلهم يدلونك علينا."

    # ح. الرياضة والطوبة (سوالف ونسة)
    elif any(x in p_low for x in ["طوبة", "ريال", "برشا", "مباراة", "لعبة", "كرة"]):
        res = "ها بدأت سوالف ريال وبرشا؟ المهم الونسة واللعب النظيف. بس لا تخلي الطوبة تنسيك شغلك، اطلب خدمتك هسة ونخلصها قبل المباراة!"

    # ط. الأكل والعزيمة (الكرم العراقي)
    elif any(x in p_low for x in ["جوعان", "أكل", "عزيمة", "شاي", "كهوة"]):
        res = "أبشر بالعزيمة! خلص شغلك ويانا وتدلل على أحلى استكان شاي مهيل يطير التعب. مكتبة أيوب هي بيت الكرم."

    # ي. الشكر والدعاء
    elif any(x in p_low for x in ["شكرا", "ممنون", "رحم الله", "عاشت ايدك", "تسلم"]):
        res = "بالخدمة يا طيب، هذا واجبنا اتجاه أهلنا. رحم الله والديك وممنون من ذوقك الراقي."

    # ك. شرح طريقة العمل (شنو نسوي)
    elif any(x in p_low for x in ["شسوي", "شلون اطلب", "شنو خدماتكم", "فهمتني"]):
        res = "بسيطة يا ذهب: 1. تختار الخدمة من القائمة فوك. 2. تملأ اسمك ورقمك وتفاصيل طلبك. 3. تضغط إرسال.. وراح يجيك رقم طلب، تضغط وراه على زر الواتساب حتى نتواصل وياك ونبلش بالشغل فوراً."

    # ل. كلمات عراقية متنوعة (ضوجة، ما بيه حيل، إلخ)
    elif any(x in p_low for x in ["ضوجة", "مختنك", "ما بيه حيل", "تعبان", "مالي خلك"]):
        res = "سلامتك من الـ 'ما بيه حيل'! إذا ضايج تعال نسولف، وإذا تعبان دز شغلك أونلاين وإحنا نخلصه وإنت كاعد بمكانك ومرتاح."

    # الرد النهائي (إذا ما لقى كلمة مطابقة)
    else:
        res = "على راسي كلامك، بس يا ريت توضح لي أكثر.. تريد مونتاج لو سي في لو زين كاش؟ أنا هنا حتى أساعدك بكل شي."

    # 4. حفظ الرد وعرضه
    st.session_state.chat_history.append({"role": "assistant", "content": res})
    with st.chat_message("assistant"):
        st.write(res)
