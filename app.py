import streamlit as st
import pandas as pd
import os
import datetime
import random

# --- 1. إعدادات الصفحة الأساسية ---
st.set_page_config(page_title="مكتبة أيوب هاني الذكية", page_icon="🏆", layout="centered")

# --- 2. روابط ثابتة (تأكد من رقم الواتساب) ---
MY_WHATSAPP = "9647739778877" 

# --- 3. عزل الألوان والتصميم (CSS) لمنع التداخل ---
st.markdown("""
    <style>
    .main { background-color: #0f172a; } /* خلفية كحلية عميقة */
    .stApp { background-color: #0f172a; }
    
    /* تنسيق النصوص */
    .gold-text { color: #c5a059 !important; text-align: right; font-weight: bold; }
    .white-text { color: #ffffff !important; text-align: right; }
    
    /* تنسيق الحاويات لعزل الأقسام */
    .section-container {
        background-color: #1e293b; 
        padding: 20px; 
        border-radius: 15px; 
        border-right: 5px solid #c5a059;
        margin-bottom: 25px;
    }
    
    /* تنسيق الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #c5a059, #9a7b41);
        color: white;
        font-weight: bold;
        border: none;
        height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. واجهة العرض الرئيسية ---
st.markdown('<h1 class="gold-text">🦅 مكتبة أيوب هاني الذكية</h1>', unsafe_allow_html=True)
st.markdown('<p class="white-text">خيارك الأول للمونتاج الاحترافي والخدمات الرقمية في اليوسفية</p>', unsafe_allow_html=True)

st.write("---")

# --- 5. تطوير المساعد الذكي (الذكاء الاصطناعي الخاص بأيوب) ---
st.markdown('<h3 class="gold-text">🤖 مساعد أيوب الذكي</h3>', unsafe_allow_html=True)

with st.container():
    user_q = st.text_input("اسألني عن أي شيء (مثلاً: شلون أسوي طلب؟ أو شنو خدماتكم؟)", key="ai_input")
    
    if user_q:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        q = user_q.lower()
        
        # منطق الردود الذكي
        if "مونتاج" in q or "فيديو" in q or "تيك توك" in q:
            st.markdown('<p class="white-text">أيوب ملك المونتاج! نستخدم CapCut Pro وبأحدث الانتقالات. تكدر تطلب فيديو للسوشيال ميديا أو توثيق مناسبات.</p>', unsafe_allow_html=True)
        elif "شلون" in q or "طريقة" in q or "طلب" in q:
            st.markdown('<p class="white-text">سهلة جداً! انزل جوة املأ الاستمارة باسمك ورقمك، والسيستم راح يعطيك رقم طلب، وبعدها تضغط زر الواتساب وتجيني للمحل.</p>', unsafe_allow_html=True)
        elif "وين" in q or "مكان" in q or "عنوان" in q:
            st.markdown('<p class="white-text">موقعنا: بغداد - اليوسفية - القصر الأوسط. نتشرف بزيارتك!</p>', unsafe_allow_html=True)
        elif "سعر" in q or "فلوس" in q or "بكم" in q:
            st.markdown('<p class="white-text">الأسعار تعتمد على نوع الشغل، بس لا تشيل هم، أيوب دائماً يقدم أفضل سعر لأهل منطقته. املأ الطلب ونحدد السعر.</p>', unsafe_allow_html=True)
        elif "وقت" in q or "ساعة" in q or "متى" in q:
            st.markdown('<p class="white-text">نشتغل يومياً من الصبح لليل. والطلبات الإلكترونية نستلمها 24 ساعة!</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="white-text">خوش سؤال! بس الأفضل تسألني عن (المونتاج، الخدمات، أو شلون تطلب). أو اترك رسالة بالاستمارة وأيوب يجاوبك بنفسه.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# --- 6. استمارة الطلب مع حفظ البيانات ---
st.markdown('<h3 class="gold-text">📝 سجل طلبك الجديد</h3>', unsafe_allow_html=True)

with st.form("main_form"):
    col1, col2 = st.columns(2)
    with col1:
        u_name = st.text_input("الاسم الكامل")
    with col2:
        u_phone = st.text_input("رقم الموبايل")
        
    u_service = st.selectbox("اختار الخدمة", ["مونتاج فيديو احترافي", "تصميم شعار (Logo)", "بحوث وطباعة", "تحويل رصيد/خدمات دفع", "أخرى"])
    u_details = st.text_area("توضيح بسيط لطلبك")
    
    submit_btn = st.form_submit_button("إرسال الطلب أونلاين")

    if submit_btn:
        if u_name and u_phone:
            # توليد رقم الطلب
            order_id = f"AY-{random.randint(1000, 9999)}"
            
            # حفظ في ملف CSV (قاعدة بيانات أيوب)
            new_data = {
                "Time": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")],
                "ID": [order_id],
                "Name": [u_name],
                "Phone": [u_phone],
                "Service": [u_service],
                "Status": ["Pending"]
            }
            df = pd.DataFrame(new_data)
            file_path = "orders_database.csv"
            
            if not os.path.isfile(file_path):
                df.to_csv(file_path, index=False, encoding='utf-8-sig')
            else:
                df.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8-sig')

            # إظهار رسالة النجاح بتصميم ملكي
            st.markdown(f"""
                <div style="background-color: #1e293b; padding: 20px; border-radius: 15px; border: 2px solid #25d366; text-align: center;">
                    <h2 style="color: #25d366;">عاش حلك! تم الحفظ ✅</h2>
                    <p style="color: white;">رقم طلبك هو: <b style="color: #facc15;">{order_id}</b></p>
                    <a href="https://wa.me/{MY_WHATSAPP}?text=هلا أيوب، سجلت طلب رقم {order_id}" target="_blank">
                        <button style="background-color: #25d366; color: white; padding: 10px 20px; border-radius: 8px; border: none; cursor: pointer;">
                            اضغط هنا لتأكيد الطلب بالواتساب
                        </button>
                    </a>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("يا طيب، املأ الاسم والرقم حتى نعرفك!")

# --- 7. حقوق الطبع ---
st.markdown('<br><p style="text-align: center; font-size: 12px; color: #64748b !important;">جميع الحقوق محفوظة © 2026 - مكتبة أيوب الذكية</p>', unsafe_allow_html=True)
