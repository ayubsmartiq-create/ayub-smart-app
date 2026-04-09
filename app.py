import streamlit as st
import pandas as pd
import os
import datetime
import random
# إعداد الصفحة
st.set_page_config(page_title="مكتبة أيوب الذكية", layout="centered")

# تصميم الألوان (CSS)
st.markdown("""
    <style>
    /* 1. لون الخلفية الأساسية للموقع (كحلي ملكي) */
    .main { background-color: #0f172a; }
    .stApp { background-color: #0f172a; }

    /* 2. لون النص الرئيسي فوق المربعات (ذهبي) */
    .gold-title { 
        color: #c5a059 !important; 
        text-align: right; 
        font-family: 'Arial'; 
        font-weight: bold;
    }

    /* 3. تصميم المربعات (الحاويات) */
    .custom-box {
        background-color: #1e293b; /* لون المربع من الداخل */
        padding: 20px; 
        border-radius: 15px; 
        border-right: 5px solid #c5a059; /* خط ذهبي جانبي */
        margin-bottom: 20px;
        text-align: right;
    }

    /* 4. لون النص داخل المربعات (أبيض ناصع) */
    .box-text { 
        color: #ffffff !important; 
        font-size: 16px;
    }

    /* 5. تنسيق الحقول (Inputs) */
    input, textarea {
        background-color: #334155 !important;
        color: white !important; /* لون الكتابة داخل حقل الإدخال */
        border: 1px solid #c5a059 !important;
    }
    </style>
    """, unsafe_allow_html=True)
# نص فوق المربع (ذهبي)
st.markdown('<h1 class="gold-title">🦅 مكتبة أيوب هاني الذكية</h1>', unsafe_allow_html=True)

# المربع وبداخله نص (أبيض)
st.markdown("""
    <div class="custom-box">
        <p class="box-text">أهلاً بك يا بطل! هذا المربع مصمم لعرض المعلومات بوضوح وبألوان متناسقة مع هويتك البصرية.</p>
    </div>
    """, unsafe_allow_html=True)
# --- عنوان قسم الخدمات ---
st.markdown('<h2 class="gold-title">🛠️ خدماتنا الاحترافية</h2>', unsafe_allow_html=True)

# القسم الأول: المونتاج
st.markdown("""
    <div class="custom-box">
        <h3 style="color: #c5a059;">🎬 صناعة المحتوى والمونتاج</h3>
        <p class="box-text">
            • مونتاج فيديوهات تيك توك وريلز باحترافية عالي.<br>
            • إضافة انتقالات وترجمة تلقائية (Subtitles).<br>
            • تعديل الألوان وهندسة الصوت باستخدام CapCut Pro.
        </p>
    </div>
    """, unsafe_allow_html=True)

# القسم الثاني: الخدمات المكتبية والبحوث
st.markdown("""
    <div class="custom-box">
        <h3 style="color: #c5a059;">📄 الخدمات المكتبية والبحوث</h3>
        <p class="box-text">
            • طباعة وبحوث التخرج والتقارير المدرسية.<br>
            • تصميم السيرة الذاتية (CV) بنماذج عصرية.<br>
            • سحب وتصوير المستندات بدقة عالية.
        </p>
    </div>
    """, unsafe_allow_html=True)

# القسم الثالث: الهوية البصرية
st.markdown("""
    <div class="custom-box">
        <h3 style="color: #c5a059;">🎨 التصميم الجرافيكي</h3>
        <p class="box-text">
            • تصميم لوغو (Logo) خاص لمشروعك.<br>
            • تصميم كروت عمل (Business Cards).<br>
            • بوستات إعلانية احترافية للفيسبوك والانستغرام.
        </p>
    </div>
    """, unsafe_allow_html=True)
# عنوان الاستمارة بلون ذهبي
st.markdown('<h2 class="gold-title">📝 اطلب خدمتك الآن</h2>', unsafe_allow_html=True)

# المربع الكبير الذي يضم الاستمارة
with st.container():
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    
    # بداية النموذج
    with st.form("order_form"):
        u_name = st.text_input("الاسم الثلاثي")
        u_phone = st.text_input("رقم الهاتف (واتساب)")
        u_service = st.selectbox("اختار الخدمة", ["مونتاج فيديو", "تصميم شعار", "طباعة وبحوث", "خدمة أخرى"])
        u_details = st.text_area("تفاصيل إضافية (اختياري)")
        
        # زر الإرسال
        submit_btn = st.form_submit_button("إرسال الطلب وحفظه")
    
    st.markdown('</div>', unsafe_allow_html=True)
    if submit_btn:
        if u_name and u_phone: # التأكد أن الزبون لم يترك الاسم والرقم فارغين
            
            # 1. توليد رقم طلب مميز (حتى تميز زبائنك)
            order_id = f"AY-{random.randint(1000, 9999)}"
            
            # 2. تحديد الوقت الحالي (تاريخ وساعة الطلب)
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

            # 3. تجميع المعلومات في "سطر واحد" (الجدول)
            new_entry = {
                "الوقت": [current_time],
                "رقم الطلب": [order_id],
                "الاسم": [u_name],
                "الهاتف": [u_phone],
                "الخدمة": [u_service],
                "التفاصيل": [u_details],
                "الحالة": ["قيد الانتظار"]
            }

            # 4. تحويل المعلومات إلى شكل جدول (DataFrame)
            df_new = pd.DataFrame(new_entry)

            # 5. تحديد مكان الإرسال (ملف الإكسل CSV)
            file_name = "orders_database.csv"

            # 6. عملية الحفظ الذكية
            if not os.path.isfile(file_name):
                # إذا الملف مو موجود، أنشئه وحط العناوين
                df_new.to_csv(file_name, index=False, encoding='utf-8-sig')
            else:
                # إذا الملف موجود، ضيف السطر الجديد بالأخير بدون ما تمسح القديم
                df_new.to_csv(file_name, mode='a', header=False, index=False, encoding='utf-8-sig')

            # 7. إبلاغ الزبون بالنجاح
            st.success(f"تم إرسال طلبك بنجاح يا {u_name}! رقم طلبك هو: {order_id}")
            
        else:
            # إذا نسى يكتب اسمه أو رقمه
            st.warning("عذراً، يرجى كتابة الاسم ورقم الهاتف لإكمال الطلب.")
            # --- كود الواتساب المصلح ---
            MY_WHATSAPP = "9647739778877" # اكتب رقمك هنا بدون أصفار بالبداية
            
            wa_msg = f"هلا أيوب، أنا الزبون {u_name}، سجلت طلب رقم: {order_id}"
            # تحويل الرسالة لرابط يفهمه المتصفح
            wa_url = f"https://wa.me/{MY_WHATSAPP}?text={wa_msg.replace(' ', '%20')}"

            st.markdown(f"""
                <div style="text-align: center;">
                    <a href="{wa_url}" target="_blank" style="text-decoration: none;">
                        <button style="background-color: #25d366; color: white; padding: 15px; border-radius: 10px; border: none; width: 100%; font-weight: bold; cursor: pointer;">
                            تأكيد الطلب عبر واتساب الآن 🟢
                        </button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

            