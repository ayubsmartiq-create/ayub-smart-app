import streamlit as st
import pandas as pd
import os
import datetime
import random

# --- 1. التصميم الملكي العالمي (تنسيق فائق الاحترافية) ---
st.set_page_config(page_title="مكتبة أيوب الذكية", layout="wide")

st.markdown("""
    <style>
    /* الألوان الأساسية */
    .stApp { background-color: #000000; direction: rtl; }
    h1, h2, h3, h4, p, label, span, div { color: #FFD700 !important; text-align: right !important; font-family: 'Cairo', sans-serif; }
    
    /* الحقول والمدخلات */
    .stTextInput input, .stSelectbox div, .stTextArea textarea {
        background-color: #111111 !important; color: #FFD700 !important;
        border: 2px solid #FFD700 !important; border-radius: 12px !important;
    }

    /* صناديق الخدمات */
    .service-card {
        background: linear-gradient(145deg, #0a0a0a, #1a1a1a); padding: 25px;
        border-radius: 20px; border: 1px solid #FFD700; text-align: right;
        transition: 0.3s; box-shadow: 0px 5px 15px rgba(255, 215, 0, 0.1);
    }
    .service-card:hover { transform: translateY(-5px); border-width: 2px; box-shadow: 0px 10px 25px rgba(255, 215, 0, 0.2); }

    /* الأمان والحقوق */
    .trust-badge {
        background-color: #0a2a0a; color: #00ff00 !important;
        padding: 10px; border-radius: 10px; border: 1px solid #00ff00;
        text-align: center !important; font-size: 14px; margin-top: 10px;
    }
    .footer-credits {
        text-align: center !important; color: #555 !important; font-size: 12px; margin-top: 50px; border-top: 1px solid #222; padding-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. الهوية البصرية ---
st.markdown('<h1 style="text-align:center; font-size: 50px; margin-bottom:0;">مكتبة أيوب الذكية</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size: 18px; color:#b8860b !important;">الابتكار.. السرعة.. الأمان</p>', unsafe_allow_html=True)

# --- 3. مساعد أيوب الذكي (الدردشة التفاعلية) ---
with st.sidebar:
    st.markdown('<h2 style="text-align:center;">🤖 مساعد أيوب الذكي</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:14px;">أهلاً بيك عيوني.. اسألني أي شي ببالك عن خدماتنا وباللهجة اللي تعجبك!</p>', unsafe_allow_html=True)
    user_msg = st.text_input("اكتب سؤالك هنا...")
    if user_msg:
        # نظام ردود ذكي يفهم اللهجة
        responses = {
            "شلون": "أهلاً بيك! إحنا بخير إذا أنت بخير. نكدر نساعدك بالمونتاج، البحوث، أو التحويل المالي.",
            "سعر": "تدلل، الأسعار عدنا تنافسية وتعتمد على نوع الخدمة. اطلب وراح نتواصل وياك وما نختلف.",
            "وقت": "إحنا نعتز بالسرعة، أغلب الطلبات تخلص بنفس اليوم أو خلال 24 ساعة.",
            "وين": "مكتبنا بالخدمة دائماً أونلاين، والتسليم يوصلك وين ما كنت.",
            "شكرا": "ولو تدلل، إحنا بخدمتكم دائماً!"
        }
        found = False
        for key in responses:
            if key in user_msg:
                st.info(responses[key])
                found = True
                break
        if not found:
            st.info("كلامك على راسي، بس ياريت توضح أكثر أو راسل أيوب مباشرة عالواتساب حتى يجاوبك بدقة.")

# --- 4. صناديق الخدمات ---
st.write("")
cols = st.columns(4)
services = [
    {"t": "الخدمات المكتبية", "d": "طباعة احترافية وعمل سير ذاتية عالمية."},
    {"t": "التحويل المالي", "d": "زين كاش، ماستر كارد، وتعبئة كافة الأرصدة."},
    {"t": "الذكاء الاصطناعي", "d": "برمجة مواقع وشعارات بلمسة ذكية."},
    {"t": "المونتاج والإبداع", "d": "تعديل فيديوهات تيك توك ويوتيوب باحترافية."}
]
for i, s in enumerate(services):
    with cols[i]:
        st.markdown(f'<div class="service-card"><h3>{s["t"]}</h3><p>{s["d"]}</p></div>', unsafe_allow_html=True)

# --- 5. استمارة الطلب وشهادة الأمان ---
st.write("---")
col_form, col_trust = st.columns([2, 1])

with col_form:
    st.markdown('<h3>📝 طلب خدمة جديدة</h3>', unsafe_allow_html=True)
    with st.form("main_form"):
        u_name = st.text_input("الأسم الكريم")
        u_phone = st.text_input("رقم الواتساب (للتواصل)")
        u_service = st.selectbox("نوع الخدمة", ["عمل CV", "تحويل مالي", "تصميم شعار", "موقع إلكتروني", "أخرى"])
        u_details = st.text_area("ملاحظات إضافية")
        submit = st.form_submit_button("إرسال الطلب الآن 🚀")

with col_trust:
    st.markdown('<br><br>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">🔒 اتصال مشفر وآمن 100%</div>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">✅ ضمان جودة العمل واسترداد المبلغ</div>', unsafe_allow_html=True)
    st.markdown('<div class="trust-badge">📞 دعم فني متواصل 24/7</div>', unsafe_allow_html=True)

if submit:
    if u_name and u_phone:
        order_id = f"AY-{random.randint(1000, 9999)}"
        # حفظ البيانات
        new_row = pd.DataFrame({"التاريخ": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M")], "الرقم": [order_id], "الاسم": [u_name], "الهاتف": [u_phone], "الخدمة": [u_service], "الحالة": ["قيد المراجعة"]})
        new_row.to_csv("orders_database.csv", mode='a', header=not os.path.exists("orders_database.csv"), index=False, encoding='utf-8-sig')
        
        st.success(f"عاشت إيدك يا {u_name}! طلبك سجلناه برقم: {order_id}")
        wa_url = f"https://wa.me/9647739778877?text=هلا أيوب، سجلت طلب جديد برقم {order_id}."
        st.markdown(f'<a href="{wa_url}" target="_blank"><div style="background-color:#25d366;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">تأكيد الطلب عبر واتساب أيوب 🟢</div></a>', unsafe_allow_html=True)
    else:
        st.error("لطفاً، املأ الاسم والرقم")

# --- 6. تتبع الطلب والحقوق ---
st.write("---")
with st.expander("🔍 تتبع حالة طلبك"):
    search = st.text_input("دخل رقم طلبك هنا")
    if search and os.path.exists("orders_database.csv"):
        df = pd.read_csv("orders_database.csv", on_bad_lines='skip')
        res = df[df['الرقم'].astype(str).str.contains(search)]
        if not res.empty:
            st.info(f"حالة طلبك الحالية هي: {res.iloc[-1]['الحالة']}")

st.markdown(f"""
    <div class="footer-credits">
        جميع الحقوق محفوظة © {datetime.datetime.now().year} - مكتبة أيوب الذكية<br>
        تم التطوير بواسطة نظام أيوب للذكاء الاصطناعي
    </div>
""", unsafe_allow_html=True)
