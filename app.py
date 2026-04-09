import streamlit as st
import pandas as pd
import os
import datetime
import random
# إعدادات الصفحة
st.set_page_config(page_title="مكتبة أيوب الذكية", layout="centered")

# التصميم البرمجي (CSS)
st.markdown("""
    <style>
    /* لون الخلفية الأساسية */
    .stApp { background-color: #0f172a; }

    /* تنسيق العنوان الذهبي فوق المربعات */
    .gold-title { 
        color: #c5a059 !important; 
        text-align: right; 
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* تنسيق المربعات (الحاويات) */
    .custom-box {
        background-color: #1e293b; 
        padding: 20px; 
        border-radius: 15px; 
        border-right: 5px solid #c5a059;
        margin-bottom: 25px;
        text-align: right;
    }

    /* لون النص داخل المربعات */
    .box-text { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)
st.markdown('<h1 class="gold-title">🦅 مكتبة أيوب هاني الذكية</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="custom-box">
        <p class="box-text">أهلاً بك في منصتنا الإلكترونية. نحن هنا لنقدم لك أفضل خدمات المونتاج، التصميم، والخدمات المكتبية بأعلى جودة.</p>
    </div>
    """, unsafe_allow_html=True)
# --- قسم الخدمات ---
st.markdown('<h2 class="gold-title">🛠️ خدماتنا الاحترافية</h2>', unsafe_allow_html=True)

# سنقوم بتقسيم الشاشة لعمودين حتى تظهر الخدمات بشكل أرتب
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="custom-box">
            <h3 style="color: #c5a059;">🎬 المونتاج</h3>
            <p class="box-text">تعديل فيديوهات احترافي لصناع المحتوى (TikTok, Reels) مع إضافة ترجمة وانتقالات.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="custom-box">
            <h3 style="color: #c5a059;">📄 الطباعة والبحوث</h3>
            <p class="box-text">كتابة وتنسيق بحوث التخرج والتقارير المدرسية وتصميم السيرة الذاتية CV.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="custom-box">
        <h3 style="color: #c5a059;">🎨 التصميم الجرافيكي</h3>
        <p class="box-text">تصميم شعارات (Logos)، هويات بصرية، وبوستات إعلانية احترافية للسوشيال ميديا.</p>
    </div>
""", unsafe_allow_html=True)
st.write("---") # خط فاصل

# عنوان الاستمارة بتصميم ملكي
st.markdown('<h2 class="gold-title">📋 نموذج طلب خدمة احترافي</h2>', unsafe_allow_html=True)

# تباين الألوان: سنضع الاستمارة داخل صندوق المعزول (custom-box)
with st.container():
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    
    with st.form("professional_order_form"):
        # 1. معلومات التواصل (تباين عالٍ: نصوص ذهبية فوق حقول غامقة)
        st.markdown('<p style="color: #c5a059; font-weight: bold;">👤 معلومات العميل الأساسية</p>', unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            u_name = st.text_input("الاسم الكامل (الثلاثي)", placeholder="مثال: أيوب هاني جاسم")
        with col_b:
            u_phone = st.text_input("رقم الواتساب (للتواصل)", placeholder="9647XXXXXXXX")

        # 2. تفاصيل الخدمة
        st.markdown('<p style="color: #c5a059; font-weight: bold;">🛠️ تفاصيل الطلب والدقة</p>', unsafe_allow_html=True)
        u_service = st.selectbox("نوع الخدمة المطلوبة", 
                                ["مونتاج فيديو (TikTok/Reels)", "تصميم شعار (Logo)", "كتابة بحوث وتقارير", "تصميم سيرة ذاتية (CV)", "خدمات أخرى"])
        
        u_urgency = st.select_slider("مدى استعجال الطلب", options=["عادي", "مستعجل", "طارئ (خلال ساعات)"])
        
        u_details = st.text_area("اشرح لنا تفاصيل طلبك بدقة (كلما زادت التفاصيل زادت الجودة)", height=150)

        # 3. زر الإرسال (احترافي)
        submit_btn = st.form_submit_button("إرسال الطلب واعتماد البيانات ✅")

    if submit_btn:
        if u_name and u_phone and len(u_phone) >= 10:
            # --- أ. توليد رقم الطلب الفريد ---
            order_id = f"AY-{random.randint(1000, 9999)}"
            order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

            # --- ب. حفظ المعلومات في سجل الإكسل (CSV) بدقة ---
            new_order = {
                "التاريخ": [order_date],
                "رقم الطلب": [order_id],
                "العميل": [u_name],
                "الهاتف": [u_phone],
                "الخدمة": [u_service],
                "الأهمية": [u_urgency],
                "التفاصيل": [u_details]
            }
            df = pd.DataFrame(new_order)
            file_db = "orders_database.csv"
            
            # الحفظ بدون تكرار العناوين
            if not os.path.isfile(file_db):
                df.to_csv(file_db, index=False, encoding='utf-8-sig')
            else:
                df.to_csv(file_db, mode='a', header=False, index=False, encoding='utf-8-sig')

            # --- ج. رسالة النجاح (تباين ألوان عالي) ---
            st.markdown(f"""
                <div style="background-color: #1e293b; border: 2px solid #c5a059; padding: 20px; border-radius: 15px; text-align: center;">
                    <h3 style="color: #c5a059;">تم تسجيل طلبك بنجاح! 🎉</h3>
                    <p style="color: white; font-size: 20px;">رقم تتبع الطلب الخاص بك: <b style="color: #facc15;">{order_id}</b></p>
                </div>
            """, unsafe_allow_html=True)

            # --- د. إرسال معلومات الزبون للواتساب بدقة عالية ---
            MY_WHATSAPP = "9647739778877" # اكتب رقمك هنا
            
            # تنسيق الرسالة لتصلك بشكل "فاتورة" مرتبة
            wa_message = (
                f"🚨 *طلب جديد من الموقع* 🚨%0a%0a"
                f"🆔 *رقم الطلب:* {order_id}%0a"
                f"👤 *اسم العميل:* {u_name}%0a"
                f"📞 *رقم الهاتف:* {u_phone}%0a"
                f"💼 *الخدمة:* {u_service}%0a"
                f"⚡ *الأهمية:* {u_urgency}%0a"
                f"📝 *التفاصيل:* {u_details}%0a%0a"
                f"📅 *تاريخ الطلب:* {order_date}"
            )
            
            wa_url = f"https://wa.me/{MY_WHATSAPP}?text={wa_message}"

            # زر الواتساب الاحترافي (تباين أخضر وذهبي)
            st.markdown(f"""
                <div style="margin-top: 15px;">
                    <a href="{wa_url}" target="_blank" style="text-decoration: none;">
                        <div style="background: linear-gradient(90deg, #25d366, #128c7e); color: white; padding: 18px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 18px; box-shadow: 0px 4px 15px rgba(0,0,0,0.3);">
                            تأكيد الطلب عبر الواتساب (دقة عالية) 📱
                        </div>
                    </a>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ عذراً، يجب إدخال الاسم ورقم هاتف صحيح لإتمام العملية.")

    st.markdown('</div>', unsafe_allow_html=True)
st.write("---")
st.markdown('<h2 class="gold-title">🤖 مساعد أيوب الذكي (نسخة مطورة)</h2>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    
    # حقل الإدخال
    user_input = st.text_input("سولف وياي.. أي شي ببالك عن المكتبة أو الخدمات؟", placeholder="مثلاً: شلون أسوي مونتاج؟")

    if user_input:
        # تحويل النص لسهولة الفحص
        text = user_input.lower()
        
        # مصفوفة الذكاء والردود
        if any(word in text for word in ["هلا", "هلو", "السلام", "مرحبا"]):
            st.info("يا هلا بيك! نورت مكتبة أيوب هاني. تفضل عيوني، بشنو أقدر أخدمك اليوم؟")
            
        elif any(word in text for word in ["شلونك", "اخبارك"]):
            st.info("بخير إذا أنت بخير! أنا هنا مثل المساعد الآلي لأيوب، جاهز أسمع طلباتك وأرتبها إلك.")

        elif any(word in text for word in ["مونتاج", "فيديو", "تصميم", "تيك توك", "ريلز"]):
            st.info("أنت بالمكان الصح! أيوب مختص بمونتاج الـ CapCut Pro. نعدل الألوان، نضيف انتقالات خرافية، ونخلي الفيديو مالتك يصير ترند. بس املأ الاستمارة جوة حتى نبدأ.")

        elif any(word in text for word in ["سعر", "بكم", "تكلفة", "فلوس", "رخيص"]):
            st.info("أسعارنا مناسبة جداً وتنافسية. المونتاج يبدأ من سعر بسيط ويعتمد على مدة الفيديو. اترك طلبك وأيوب راح يحدد لك السعر النهائي اللي يرضيك.")

        elif any(word in text for word in ["وين", "عنوان", "مكان", "بغداد", "يوسفية"]):
            st.info("مكتبتنا موجودة في بغداد - منطقة اليوسفية (القصر الأوسط). نتشرف بزيارتك بأي وقت، بس الأفضل تسجل طلبك هنا أونلاين أولاً.")

        elif any(word in text for word in ["وكت", "وقت", "شوكت", "ساعة", "مفتوحين"]):
            st.info("نستلم الطلبات أونلاين 24 ساعة! أما المحل فيفتح من الصبح للمساء. سجل طلبك هسة وحجز دورك.")

        elif any(word in text for word in ["شكرا", "رحم الله والديك", "عاشت ايدك"]):
            st.info("ولو، تدلل! هذا واجبي. لا تنسى تسجل طلبك بالاستمارة حتى لا يضيع وقتك.")

        elif any(word in text for word in ["منو", "أيوب", "انت"]):
            st.info("أنا المساعد الذكي الخاص بـ 'أيوب هاني'. أيوب هو مبرمج وصانع محتوى وخبير مونتاج، وهذا الموقع هو بوابتك لكل خدماته.")

        else:
            # الرد الذكي في حال لم يفهم الكلمة
            st.info("خوش سؤال! بس ياريت توضح أكثر حتى أقدر أساعدك بدقة. تكدر تسألني عن (المونتاج، التصميم، الأسعار، أو الموقع).")

    st.markdown('</div>', unsafe_allow_html=True)
st.write("---")
# --- لوحة التحكم السرية الخاصة بأيوب هاني ---
st.write("---")
with st.expander("🔐 لوحة إدارة الطلبات (خاص بالمدير)"):
    # حقل إدخال كلمة المرور
    admin_pass = st.57575656("أدخل رمز الدخول لرؤية سجل الزبائن", type="password")
    
    if admin_pass == "57575656":
        # التأكد من وجود ملف قاعدة البيانات
        if os.path.exists("orders_database.csv"):
            try:
                # قراءة البيانات باستخدام pandas
                df_view = pd.read_csv("orders_database.csv")
                
                # فحص إذا كان الملف يحتوي على بيانات
                if not df_view.empty:
                    st.success("أهلاً بك يا أيوب. إليك قائمة الطلبات الحالية:")
                    st.dataframe(df_view) # عرض الجدول بشكل تفاعلي
                    
                    # زر لتحميل الملف بجهازك بصيغة CSV (Excel)
                    with open("orders_database.csv", "rb") as f:
                        st.download_button(
                            label="📥 تحميل سجل الطلبات كملف Excel",
                            data=f,
                            file_name="ayub_library_orders.csv",
                            mime="text/csv"
                        )
                else:
                    st.warning("السجل موجود ولكنه فارغ حالياً (بانتظار أول زبون).")
            except Exception as e:
                st.error("حدث خطأ أثناء محاولة قراءة السجل. تأكد من إرسال طلب تجريبي أولاً.")
        else:
            st.info("لا يوجد سجل طلبات حالياً. سيظهر السجل هنا فور إرسال أول طلب من الموقع.")
    elif admin_pass:
        st.error("رمز الدخول غير صحيح!")
