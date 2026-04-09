import streamlit as st
import pandas as pd
import os
import datetime
import random

# 1. إعدادات الصفحة والتصميم (CSS)
st.set_page_config(page_title="مكتبة أيوب هاني الذكية", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .gold-title { 
        color: #c5a059 !important; 
        text-align: right; 
        font-weight: bold;
        margin-bottom: 20px;
    }
    .custom-box {
        background-color: #1e293b; 
        padding: 20px; 
        border-radius: 15px; 
        border-right: 5px solid #c5a059;
        margin-bottom: 25px;
        text-align: right;
        color: white;
    }
    .box-text { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. العناوين والترحيب
st.markdown('<h1 class="gold-title">🦅 مكتبة أيوب هاني الذكية</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="custom-box">
        <p class="box-text">أهلاً بك في منصتنا الإلكترونية. نحن هنا لنقدم لك أفضل خدمات المونتاج، التصميم، والخدمات المكتبية بأعلى جودة.</p>
    </div>
    """, unsafe_allow_html=True)

# 3. قسم الخدمات
st.markdown('<h2 class="gold-title">🛠️ خدماتنا الاحترافية</h2>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="custom-box"><h3 style="color:#c5a059;">🎬 المونتاج</h3><p>تعديل فيديوهات TikTok و Reels باحترافية عالية.</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="custom-box"><h3 style="color:#c5a059;">📄 البحوث</h3><p>كتابة وتنسيق بحوث التخرج والتقارير المدرسية.</p></div>', unsafe_allow_html=True)

# 4. المساعد الذكي المطوّر
st.markdown('<h2 class="gold-title">🤖 مساعد أيوب الذكي</h2>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    user_input = st.text_input("سولف وياي.. أي شي ببالك عن المكتبة؟")
    if user_input:
        text = user_input.lower()
        if any(word in text for word in ["هلا", "هلو", "مرحبا"]):
            st.info("يا هلا بيك بنورك! بشنو أقدر أخدمك اليوم؟")
        elif "سعر" in text or "بكم" in text:
            st.info("أسعارنا تنافسية جداً، اترك طلبك بالاستمارة تحت وأبشر بالخير.")
        elif "مونتاج" in text or "فيديو" in text:
            st.info("أيوب خبير بمونتاج CapCut، نطلع لك فيديو عالمي!")
        else:
            st.info("خوش سؤال! تكدر تسألني عن المونتاج، الأسعار، أو موقعنا باليوسفية.")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. استمارة الطلب وحفظ البيانات
st.markdown('<h2 class="gold-title">📝 سجل طلبك الآن</h2>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    with st.form("main_order_form"):
        u_name = st.text_input("الاسم الكامل")
        u_phone = st.text_input("رقم الهاتف (واتساب)")
        u_service = st.selectbox("نوع الخدمة", ["مونتاج فيديو", "تصميم شعار", "طباعة وبحوث", "خدمة أخرى"])
        u_details = st.text_area("تفاصيل إضافية")
        submit_btn = st.form_submit_button("إرسال الطلب ✅")

    if submit_btn:
        if u_name and u_phone:
            order_id = f"AY-{random.randint(1000, 9999)}"
            order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            # الحفظ في ملف CSV
            new_data = {"التاريخ": [order_date], "الرقم": [order_id], "الاسم": [u_name], "الهاتف": [u_phone], "الخدمة": [u_service]}
            df = pd.DataFrame(new_data)
            file_db = "orders_database.csv"
            
            if not os.path.isfile(file_db):
                df.to_csv(file_db, index=False, encoding='utf-8-sig')
            else:
                df.to_csv(file_db, mode='a', header=False, index=False, encoding='utf-8-sig')

            st.success(f"تم تسجيل طلبك! رقم الطلب: {order_id}")
            
            # رابط الواتساب (ضع رقمك هنا)
            MY_NUMBER = "9647739778877" 
            wa_text = f"أهلاً أيوب، سجلت طلب جديد برقم {order_id}. الاسم: {u_name}"
            wa_url = f"https://wa.me/{MY_NUMBER}?text={wa_text.replace(' ', '%20')}"
            
            st.markdown(f'<a href="{wa_url}" target="_blank"><div style="background-color:#25d366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">تأكيد عبر واتساب 🟢</div></a>', unsafe_allow_html=True)
        else:
            st.error("يرجى ملء الاسم والهاتف.")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. لوحة التحكم السرية (خاصة بأيوب)
st.write("---")
with st.expander("🔐 إدارة الطلبات (خاص بأيوب)"):
    admin_pass = st.text_input("كلمة السر الخاصة بك", type="password")
    if admin_pass == "57575656":
        if os.path.exists("orders_database.csv"):
            try:
                df_view = pd.read_csv("orders_database.csv")
                if not df_view.empty:
                    st.write("سجل الزبائن الحالي:")
                    st.dataframe(df_view)
                    with open("orders_database.csv", "rb") as f:
                        st.download_button("📥 تحميل الإكسل", f, file_name="ayub_orders.csv")
                else:
                    st.warning("الملف موجود لكنه فارغ.")
            except:
                st.error("حدث خطأ أثناء قراءة البيانات.")
        else:
            st.info("لا يوجد سجل طلبات بعد.")
